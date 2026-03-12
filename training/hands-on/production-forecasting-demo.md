# Production Forecasting Demo

## Purpose
This exercise shows how a petroleum-engineering forecasting workflow can combine:
- a classical engineering method
- a machine-learning benchmark
- an AI copilot for code, interpretation, and workflow packaging

The forecasting engine in this demo is not the LLM. The forecasting engines are:
- `Arps hyperbolic decline`
- `RandomForestRegressor`
- `Exponential Smoothing`
- `ARIMA`

## Learning Objective
This exercise highlights the difference between:
- `ML as the forecasting engine`
- `GenAI as the engineering copilot around that engine`

## Scenario
Use a small official `BSEE OGOR-A` subset with `3` offshore producing completions:
- `G21245 PN002`
- `G21245 PS001`
- `G21245 PS002`

For each completion, the demo uses:
- a selected `48-month` analysis window
- `30 months` for model fitting
- `6 months` for internal test comparison
- `12 months` for forecast evaluation

The business question is:

`If I only had a longer training history for each completion, how well would Arps, a multivariate Random Forest, Exponential Smoothing, and ARIMA track the next 6 months of known data and then forecast the following 12 months of oil production?`

## Why This Case Works
- It uses real monthly well histories rather than a synthetic example.
- It uses official offshore regulator data rather than an unofficial sample export.
- It compares a familiar petroleum-engineering method against both ML and pure time-series baselines.
- It keeps the data small enough to run and review quickly.
- It creates a clean bridge into AI-assisted code generation, interpretation, and dashboarding.

## Files Used In This Demo
- `training/hands-on/production-forecasting-demo.ipynb`
- `training/hands-on/production-forecasting-colab-guide.md`
- `training/hands-on/production-forecasting-local-setup.md`
- `training/hands-on/cursor-setup-and-ai-workflow.md`
- `training/hands-on/cursor-prompts/`
- `training/sample-data/production_forecasting/well_monthly_production.csv`
- `training/sample-data/production_forecasting/well_master.csv`
- `training/sample-data/production_forecasting/data_dictionary.md`
- `training/sample-data/production_forecasting/source_notes.md`

## Suggested Workflow
1. Read the problem statement in petroleum-engineering terms.
2. Review the source notes and dataset provenance.
3. Review the monthly production table and the well master file.
4. Review the split:
   - `30 months` train
   - `6 months` test
   - `12 months` forecast
5. Fit `Arps hyperbolic decline`.
6. Train the multivariate `RandomForestRegressor` and fit `Exponential Smoothing` plus `ARIMA`.
7. Compare metrics and the train/test/forecast plots across all model families.
8. Use the LLM to explain results, improve presentation, or package the workflow.

## Analytical Structure
### Classical engineering baseline
- Convert monthly oil volume into average oil rate.
- Fit `Arps hyperbolic decline` separately for each completion.
- Forecast the test and forecast windows from the end of the training period.

### ML benchmark
- Build multivariate production-state features separately for each completion.
- Train a separate `RandomForestRegressor` per completion.
- Forecast the test and forecast months recursively.

### Pure time-series baselines
- Fit `Exponential Smoothing` on each completion's ordered oil-rate history.
- Fit `ARIMA` on each completion's ordered oil-rate history.
- Compare those baselines against the engineering and ML approaches.

### Evaluation
Compare all model families using:
- `MAE`
- `RMSE`
- `MAPE`
- per-well actual-vs-predicted plots

## Suggested Discussion Questions
- When does a decline-curve forecast still outperform a more flexible ML model?
- What kinds of well behavior are hard for Arps to capture?
- What kinds of state variables improve the Random Forest forecast?
- When do the pure time-series baselines behave more like Arps than like the multivariate RF?
- When would this workflow be good enough for screening, but not for budgeting?
- What would have to change before using this on internal field data?

## Bridge To Cursor And GenAI
After the notebook run, use `Cursor` to explore how AI can help:
- generate a standalone Python script for Arps forecasting
- build a static HTML dashboard from the CSV outputs
- analyze the forecast results and draft engineering recommendations

Use the prompt files in:

`training/hands-on/cursor-prompts/`

## Practical Notes
- This is a compact learning subset, not a full field database.
- The selected window is structured so both methods can be compared on a short internal test period and a separate 12-month forecast period.
- `oil_bbl` is stored as monthly volume, while the notebook plots `bbl/day on production` using `days_on_prod`.
- The notebook is designed for `Colab`, `Jupyter`, or local use.
- The core message is: `the models do the forecasting; the LLM helps build and operationalize the workflow.`
