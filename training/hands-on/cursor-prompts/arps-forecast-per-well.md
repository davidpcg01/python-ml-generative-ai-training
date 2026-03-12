# Prompt: Generate Arps Forecast Script Per Completion

Use this prompt inside `Cursor` when the project already contains the production-forecasting dataset.

```text
You are acting as a petroleum-engineering coding assistant inside a Cursor project.

I need you to create a production-forecasting Python script that runs an Arps hyperbolic decline forecast for each completion in the dataset and saves the results to CSV files.

Project assumptions:
- The project contains a folder with these files:
  - well_monthly_production.csv
  - well_master.csv
  - data_dictionary.md
  - source_notes.md
- The main production file contains these columns:
  - well_id
  - api_uwi
  - operator
  - county
  - reservoir
  - state
  - basin
  - area_block
  - date
  - oil_bbl
  - gas_mcf
  - water_bbl
  - days_on_prod
  - days_in_month

Task:
1. Create a Python script named arps_forecast_per_completion.py.
2. The script must:
   - load the monthly production data
   - parse the date column as a proper datetime
   - sort the data by well_id and date
   - treat oil_bbl, gas_mcf, and water_bbl as monthly volumes
   - compute oil_rate_bbl_per_day as oil_bbl / days_on_prod
   - keep the most recent 48 months of each completion as the working window
   - split that window into 30 training months, 6 test months, and 12 forecast months
   - fit the model on the 30 training months
   - fit an Arps hyperbolic decline curve separately for each completion
   - generate predictions for the 6 test months and the 12 forecast months for each completion
   - compare predicted oil rate against actual oil rate for both the test and forecast segments
   - keep the output schema compatible with the notebook's `results/production_forecasting/` exports where practical
   - save outputs to CSV

Arps requirements:
- Use the standard hyperbolic decline equation:
  q(t) = qi / (1 + b * Di * t)^(1 / b)
- Fit qi, Di, and b for each completion
- Use scipy.optimize.curve_fit
- Apply bounds that keep the parameters physically reasonable
- Ignore or carefully handle months where oil_rate_bbl_per_day <= 0 during curve fitting
- If fitting fails for a completion, do not crash the script
- Instead, log the failure and continue with the remaining completions

Required outputs:
1. results/production_forecasting/arps_parameters.csv
   - one row per completion
   - columns:
     - well_id
     - api_uwi
     - qi
     - di
     - b
     - training_months
     - test_months
     - forecast_months
     - fit_status
2. results/production_forecasting/arps_holdout_forecast.csv
   - one row per completion per forecast month
   - columns:
     - well_id
     - api_uwi
     - date
     - actual_oil_rate_bbl_per_day
     - arps_pred_oil_rate_bbl_per_day
     - actual_oil_bbl
     - arps_pred_oil_bbl
     - abs_error_rate
     - pct_error_rate
3. results/production_forecasting/arps_prediction_timeline.csv
   - one row per completion per month in the 48-month window
   - columns:
     - well_id
     - api_uwi
     - date
     - phase
     - actual_oil_rate_bbl_per_day
     - arps_pred_oil_rate_bbl_per_day
     - actual_oil_bbl
     - arps_pred_oil_bbl
4. results/production_forecasting/arps_model_metrics.csv
   - overall metrics plus per-well metrics
   - separate the metrics by phase for test and forecast
   - include MAE, RMSE, and MAPE

Implementation requirements:
- Use only standard Python plus pandas, numpy, scipy, and pathlib
- Do not use placeholders
- Do not hardcode a single well
- The code must work for any number of completions present in the input
- Keep the phase labels exactly `train`, `test`, and `forecast`
- Keep units explicit so `oil_bbl` remains `bbl/month` and `oil_rate_bbl_per_day` remains `bbl/day on production`
- Use clear function boundaries such as:
  - load_data()
  - prepare_rates()
  - split_train_holdout()
  - fit_arps()
  - forecast_holdout()
  - calculate_metrics()
  - save_outputs()
- Add concise comments only where they improve clarity
- Print a short terminal summary when finished

Validation requirements:
- Before fitting, verify the required columns exist
- If required columns are missing, raise a clear error
- If a completion has fewer than 12 non-zero production months in training, skip fitting and mark that completion as insufficient_history
- If the completion does not have the full 30/6/12 split available, raise a clear warning

At the end:
- explain what files were created
- explain how to run the script from the terminal
- do not create notebooks
- do not create dashboards
- do not create speaker notes
```
