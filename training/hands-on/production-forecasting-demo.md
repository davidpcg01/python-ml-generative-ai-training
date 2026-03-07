# Production Forecasting Demo

## Purpose
This is the featured Session 1 GenAI demo. It is designed to show that GenAI can do more than summarize documents. In this exercise, the LLM helps frame a production-engineering problem, write analysis code, suggest visualizations, interpret outputs, and package the result into a reusable workflow.

## Teaching Objective
Participants should see the difference between:
- `ML as the forecasting engine`
- `GenAI as the engineering copilot around that engine`

## Scenario
A production engineer manages `18 wells` across `3 pads` and needs a reusable workflow to:
- forecast the next `6 months` of oil production
- identify wells likely to underperform
- flag likely operational drivers such as high water cut or poor uptime
- generate a short engineering summary
- turn the workflow into something repeatable, such as a notebook or lightweight app

Available data:
- monthly well production
- well attributes
- monthly operating variables
- event history such as workovers, pump changes, and shut-ins

## Files Used In This Demo
- `training/sample-data/production_forecasting/well_monthly_production.csv`
- `training/sample-data/production_forecasting/well_events.csv`
- `training/sample-data/production_forecasting/data_dictionary.md`

## Recommended Live Demo Flow
1. Set up the problem in business language.
2. Show the dataset columns and explain what is available.
3. Paste the master prompt into your LLM tool of choice.
4. Ask for a first-pass forecasting workflow and code.
5. Ask for improved visualizations and a better engineering interpretation.
6. Ask how to package the result into a reusable notebook or mini-app.
7. Close by separating the contribution of the ML model from the contribution of the LLM.

## Master Prompt
Use this prompt directly or adapt it to your preferred LLM tool.

```text
You are an AI copilot helping a production engineering team build a production forecasting workflow for oil wells.

I will give you a dataset with monthly well production and operating data. Your job is to help me:
1. understand the forecasting problem,
2. propose a sensible modeling approach,
3. write Python code for analysis,
4. inspect outputs and diagnose issues,
5. generate useful plots,
6. explain results in petroleum-engineering language,
7. package the work into a reusable notebook or lightweight internal tool.

Context:
- Audience: beginner/intermediate petroleum engineers and geoscientists
- Goal: forecast the next 6 months of oil production at the well level
- Secondary goal: identify underperforming wells and likely operational drivers
- Data may include:
  - well_id
  - date
  - oil_rate_bopd
  - gas_rate_mscfd
  - water_cut_pct
  - choke_size_64in
  - tubing_pressure_psi
  - casing_pressure_psi
  - uptime_pct
  - gor_scf_bbl
  - artificial_lift_type
  - reservoir_zone
  - well_age_months
  - lateral_length_ft
  - completion_stage_count
  - event_flag
  - event_type

Instructions:
- Start by briefly framing the business problem in plain English.
- Recommend a practical workflow using simple methods first, then suggest more advanced options.
- Prefer an approach that is teachable in a 1-hour training.
- Include data cleaning, feature engineering, train/test split, evaluation metrics, and forecasting logic.
- Write clear Python code using pandas, numpy, matplotlib, seaborn, and scikit-learn.
- If time series handling is needed, explain whether to use lag features, decline-curve-style features, or grouped well-level modeling.
- Suggest at least 3 useful visualizations.
- After the code, explain the forecast results and operational insights in simple engineering language.
- If appropriate, suggest wells for further surveillance and explain why.
- Finally, show how this can be turned into:
  1. a reusable notebook workflow, and
  2. a simple internal app such as Streamlit.

Output format:
1. Problem framing
2. Recommended analytical approach
3. Step-by-step code
4. Plot suggestions
5. Example interpretation of results
6. How to package into a reusable workflow or app
7. Limitations and engineering cautions

Important:
- Do not assume perfect data quality.
- Call out missing-data risks, noisy wells, workovers, and operational changes.
- Keep the explanation practical, not academic.
- Use petroleum-engineering terminology where appropriate, but keep it beginner-friendly.

I will provide the dataset next.
```

## Useful Follow-Up Prompts

### Compare approaches
```text
Modify the workflow so it compares a simple decline-curve-style baseline against a machine learning model.
```

### Feature explanation
```text
Which features are most likely to matter for underperformance, and how would you explain that to a production engineer?
```

### Management summary
```text
Create a short engineering summary for management highlighting 5 wells that need attention.
```

### Packaging prompt
```text
Turn this notebook into a simple Streamlit app with:
- file upload
- well selector
- forecast plot
- top underperforming wells table
- downloadable summary
```

### Safety prompt
```text
Add guardrails so the tool warns users when the model is extrapolating beyond the historical operating range.
```

## What To Say During The Demo

### When introducing the scenario
“The important thing here is that the LLM is not magically replacing the forecasting model. It is helping the engineer build and use the workflow around the model much faster.”

### When the model generates code
“This is where GenAI starts behaving like a technical copilot. It can help draft the analysis, but we still review and refine it.”

### When showing the output
“Notice that the value is not only the forecast. The value is also the explanation, the visualization, and the repeatable workflow we can now reuse.”

## Expected Takeaways
By the end of this demo, participants should understand that GenAI can:
- frame technical business problems
- generate first-pass analysis code
- improve visualizations
- explain results in domain language
- help turn one-off analysis into reusable internal tools

## Practical Notes
- Use the synthetic dataset provided in this package for a clean live demo.
- If live prompting fails, keep screenshots or a saved transcript of expected outputs.
- If time is limited, focus on one path: `problem framing -> code generation -> interpretation`.
