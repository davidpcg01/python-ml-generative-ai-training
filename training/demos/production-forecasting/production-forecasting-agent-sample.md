# Production Forecasting Agent Walkthrough

## What This Is
This is a student-friendly example of a small `AI agent` in Python for a petroleum-engineering workflow.

The most important idea is:
- the `LLM` does not do the forecasting math
- the `Arps decline model` does the forecasting math
- the agent uses tools to inspect data, run the forecast, and explain the result

This is the Session 2 takeaway:
`the agent orchestrates the workflow, but the engineering model still does the numerical work`

## Learning Goal
After reading this example, you should be able to explain:
- what an `AI agent` is in practical terms
- why agents use `tools`
- how a production dataset can be connected to an agent safely
- how `Arps hyperbolic decline` can live inside a tool instead of inside the model

## The Scenario
We use the same offshore `BSEE OGOR-A` subset used elsewhere in this training.

Available completions:
- `G21245 PN002`
- `G21245 PS001`
- `G21245 PS002`

The question we want the agent to handle is:

`Can an agent load one completion, fit an Arps decline curve, forecast the next 12 months, and explain the result in plain English?`

## What Makes This An Agent
This example is more than a chatbot because it has:
- a `user request`
- a `model` that decides what to do next
- `tools` the model can call
- a short `system prompt` that sets the rules
- a loop that lets the model call tools before answering

## The Three Tools
This agent uses `3` tools:

1. `list_completions`
   Returns the available demo completions.

2. `load_completion_history`
   Loads one completion's monthly history and calculates daily oil rate.

3. `fit_arps_forecast`
   Fits `Arps hyperbolic decline` on the training window and forecasts the next months.

These are good teaching tools because:
- one tool helps the agent find the right well
- one tool helps the agent inspect the data
- one tool performs the engineering forecast

## Files Used
- `training/data/production_forecasting/well_monthly_production.csv`
- `training/data/production_forecasting/well_master.csv`

## Before You Run Anything
Install the required packages:

```bash
pip install openai pandas numpy scipy
```

Set your API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## How To Read The Code
Read the code in this order:

1. `locate_data_dir()`
   Finds the production-forecasting dataset.

2. `list_completions()`
   Lets the agent discover which completions exist.

3. `load_completion_history()`
   Lets the agent inspect one completion's recent history.

4. `fit_arps_forecast()`
   This is the engineering tool that does the decline-curve fit and forecast.

5. `TOOLS`
   This is the schema the model sees.

6. `run_agent()`
   This is the loop where the model decides whether to call a tool or answer directly.

## Full Python Example

```python
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from openai import OpenAI
from scipy.optimize import curve_fit


PROJECT_ROOT = Path.cwd()
DATA_DIR_CANDIDATES = [
    PROJECT_ROOT / "training" / "data" / "production_forecasting",
    PROJECT_ROOT / "data" / "production_forecasting",
    Path(__file__).resolve().parents[2] / "data" / "production_forecasting",
]


def locate_data_dir() -> Path:
    for path in DATA_DIR_CANDIDATES:
        if (path / "well_monthly_production.csv").exists() and (path / "well_master.csv").exists():
            return path
    raise FileNotFoundError("Could not locate training/data/production_forecasting")


DATA_DIR = locate_data_dir()
MONTHLY_DF = pd.read_csv(DATA_DIR / "well_monthly_production.csv", parse_dates=["date"])
MASTER_DF = pd.read_csv(
    DATA_DIR / "well_master.csv",
    parse_dates=["subset_start_date", "subset_end_date"],
)

MONTHLY_DF["days_on_prod"] = MONTHLY_DF["days_on_prod"].replace(0, np.nan)
MONTHLY_DF["oil_rate_bbl_per_day"] = MONTHLY_DF["oil_bbl"] / MONTHLY_DF["days_on_prod"]
MONTHLY_DF = MONTHLY_DF.sort_values(["well_id", "date"]).reset_index(drop=True)


def arps_rate(t_months: np.ndarray, qi: float, b: float, di: float) -> np.ndarray:
    t_months = np.asarray(t_months, dtype=float)
    if abs(b) < 1e-8:
        return qi * np.exp(-di * t_months)
    return qi / np.power(1.0 + b * di * t_months, 1.0 / b)


def completion_frame(completion_id: str) -> pd.DataFrame:
    frame = MONTHLY_DF.loc[MONTHLY_DF["well_id"] == completion_id].copy()
    if frame.empty:
        raise ValueError(f"Unknown completion_id: {completion_id}")
    return frame.sort_values("date").reset_index(drop=True)


def list_completions() -> dict[str, Any]:
    cols = [
        "well_id",
        "operator",
        "area_block",
        "reservoir",
        "subset_start_date",
        "subset_end_date",
        "total_months",
    ]
    records = MASTER_DF[cols].copy()
    for col in ["subset_start_date", "subset_end_date"]:
        records[col] = records[col].dt.strftime("%Y-%m-%d")
    return {"completions": records.to_dict(orient="records")}


def load_completion_history(completion_id: str, months: int = 12) -> dict[str, Any]:
    frame = completion_frame(completion_id)
    window = frame.tail(months).copy()
    preview = window[
        ["date", "oil_bbl", "days_on_prod", "oil_rate_bbl_per_day", "gas_mcf", "water_bbl"]
    ].copy()
    preview["date"] = preview["date"].dt.strftime("%Y-%m-%d")

    return {
        "completion_id": completion_id,
        "months_loaded": int(len(window)),
        "date_start": window["date"].min().strftime("%Y-%m-%d"),
        "date_end": window["date"].max().strftime("%Y-%m-%d"),
        "avg_oil_rate_bopd": round(float(window["oil_rate_bbl_per_day"].mean()), 2),
        "last_oil_rate_bopd": round(float(window["oil_rate_bbl_per_day"].iloc[-1]), 2),
        "history_preview": preview.to_dict(orient="records"),
    }


def fit_arps_forecast(
    completion_id: str,
    train_months: int = 30,
    forecast_months: int = 12,
) -> dict[str, Any]:
    frame = completion_frame(completion_id)
    required_months = train_months + forecast_months
    if len(frame) < required_months:
        raise ValueError(
            f"{completion_id} only has {len(frame)} rows; need at least {required_months}."
        )

    window = frame.tail(required_months).reset_index(drop=True)
    train = window.iloc[:train_months].copy()
    actual_future = window.iloc[train_months : train_months + forecast_months].copy()

    y_train = train["oil_rate_bbl_per_day"].astype(float).to_numpy()
    t_train = np.arange(len(train), dtype=float)

    qi0 = max(float(y_train[0]), 1.0)
    p0 = [qi0, 0.7, 0.05]
    bounds = ([0.1, 0.0, 1e-6], [1e6, 2.0, 5.0])

    params, _ = curve_fit(
        arps_rate,
        t_train,
        y_train,
        p0=p0,
        bounds=bounds,
        maxfev=20000,
    )
    qi, b, di = [float(x) for x in params]

    t_forecast = np.arange(train_months, train_months + forecast_months, dtype=float)
    forecast_values = arps_rate(t_forecast, qi, b, di)

    comparison = actual_future[["date", "oil_rate_bbl_per_day"]].copy()
    comparison["arps_forecast_bbl_per_day"] = forecast_values[: len(comparison)]
    comparison["abs_error_bopd"] = (
        comparison["oil_rate_bbl_per_day"] - comparison["arps_forecast_bbl_per_day"]
    ).abs()

    mae = float(comparison["abs_error_bopd"].mean())
    denom = comparison["oil_rate_bbl_per_day"].replace(0, np.nan)
    mape = float((comparison["abs_error_bopd"] / denom).dropna().mean() * 100.0)

    comparison["date"] = comparison["date"].dt.strftime("%Y-%m-%d")

    return {
        "completion_id": completion_id,
        "train_months": train_months,
        "forecast_months": forecast_months,
        "arps_parameters": {
            "qi_bopd": round(qi, 3),
            "b_factor": round(b, 4),
            "di_per_month": round(di, 6),
        },
        "fit_window": {
            "train_start": train["date"].min().strftime("%Y-%m-%d"),
            "train_end": train["date"].max().strftime("%Y-%m-%d"),
            "forecast_start": actual_future["date"].min().strftime("%Y-%m-%d"),
            "forecast_end": actual_future["date"].max().strftime("%Y-%m-%d"),
        },
        "metrics": {
            "mae_bopd": round(mae, 2),
            "mape_pct": round(mape, 2),
        },
        "forecast_table": comparison.round(2).to_dict(orient="records"),
    }


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_completions",
            "description": "List the available production-forecasting demo completions.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "load_completion_history",
            "description": "Load monthly production history for one completion and compute daily oil rate.",
            "parameters": {
                "type": "object",
                "properties": {
                    "completion_id": {"type": "string"},
                    "months": {"type": "integer", "default": 12},
                },
                "required": ["completion_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fit_arps_forecast",
            "description": "Fit an Arps hyperbolic decline curve and forecast the next months.",
            "parameters": {
                "type": "object",
                "properties": {
                    "completion_id": {"type": "string"},
                    "train_months": {"type": "integer", "default": 30},
                    "forecast_months": {"type": "integer", "default": 12},
                },
                "required": ["completion_id"],
            },
        },
    },
]


TOOL_FUNCTIONS = {
    "list_completions": list_completions,
    "load_completion_history": load_completion_history,
    "fit_arps_forecast": fit_arps_forecast,
}


SYSTEM_PROMPT = """
You are a production forecasting agent for petroleum-engineering workflows.

Rules:
- Use tools before making numerical claims.
- If the user asks about a completion but does not name one, call list_completions first.
- If the user asks for a forecast, call load_completion_history and then fit_arps_forecast.
- Keep the answer engineering-focused and concise.
- Say clearly that Arps is a screening model, not a full reservoir simulation or reserves booking workflow.
"""


def run_agent(user_request: str, model: str = "gpt-4o-mini") -> str:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_request},
    ]

    while True:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
        )
        message = response.choices[0].message

        assistant_message: dict[str, Any] = {
            "role": "assistant",
            "content": message.content or "",
        }
        if message.tool_calls:
            assistant_message["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": tool_call.type,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in message.tool_calls
            ]
        messages.append(assistant_message)

        if not message.tool_calls:
            return message.content or ""

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments or "{}")
            result = TOOL_FUNCTIONS[tool_name](**tool_args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": json.dumps(result),
                }
            )


if __name__ == "__main__":
    prompt = (
        "Forecast the next 12 months for G21245 PN002 using Arps decline. "
        "Summarize the fitted qi, b, and di values, report forecast accuracy "
        "over the known holdout period, and give me a short engineering interpretation."
    )
    answer = run_agent(prompt)
    print(answer)
```

## What The Agent Is Doing
When you run the sample, the flow is:

1. The user asks a forecasting question.
2. The model decides whether it needs a tool.
3. The model calls `load_completion_history` or `fit_arps_forecast`.
4. Python executes the tool.
5. The tool result is sent back to the model.
6. The model writes a final answer using real computed values.

That is the key point:
the model is not inventing the forecast; it is using tools to get the forecast.

## Example Questions To Try
- `List the available completions in this demo.`
- `Load the last 12 months for G21245 PS001 and summarize the recent oil-rate trend.`
- `Forecast the next 12 months for G21245 PN002 using Arps decline.`
- `Write a short engineering note for G21245 PS002 based on the Arps fit.`

## What Students Should Notice
- The `LLM` is useful because it can decide which tool to call next.
- The tool outputs are structured and reviewable.
- The forecasting result comes from deterministic Python code.
- This is safer than asking the model to invent decline parameters on its own.

## Good Next Steps
Once students understand this version, useful extensions are:
- add a plotting tool that saves an actual-vs-forecast chart
- add a comparison tool for `RandomForestRegressor`, `Exponential Smoothing`, or `ARIMA`
- add a reporting tool that writes a markdown summary

## Important Guardrail
This sample is a teaching example for workflow design.

It is useful for screening and explanation, but it should not be treated as a reserves, budgeting, or field-development decision engine without stronger validation, uncertainty handling, broader history, and engineering review.
