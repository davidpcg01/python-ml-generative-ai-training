# Production Forecasting Demo: Google Colab Guide

This guide explains how to run the BSEE offshore-completion production-forecasting notebook in `Google Colab`.

## Files You Need
Upload these files from the training package:
- `training/hands-on/production-forecasting-demo.ipynb`
- `training/sample-data/production_forecasting/well_monthly_production.csv`
- `training/sample-data/production_forecasting/well_master.csv`
- `training/sample-data/production_forecasting/data_dictionary.md`
- `training/sample-data/production_forecasting/source_notes.md`

## Step 1: Open Google Colab
1. Go to [https://colab.research.google.com](https://colab.research.google.com).
2. Sign in with your Google account if needed.
3. Click `File` -> `Upload notebook`.
4. Select `production-forecasting-demo.ipynb`.

## Step 2: Review The Notebook
After the notebook opens:
1. Read the title and overview cell.
2. Confirm the notebook is the `Production Forecasting Demo: BSEE Gulf Of Mexico Completions`.
3. Do not worry if you see no data yet. The notebook can prompt for uploads.

## Step 3: Install Packages
1. Run the first code cell with `%pip install`.
2. Wait for package installation to finish.
3. If Colab asks to restart the runtime, allow it and then rerun the notebook from the top.

Required packages:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy`
- `statsmodels`

## Step 4: Upload The Dataset Files
The notebook checks whether the sample data is already present.

If the files are not found:
1. Run the data-loading cell.
2. Colab will open a file picker.
3. Upload:
   - `well_monthly_production.csv`
   - `well_master.csv`
   - `data_dictionary.md`
   - `source_notes.md`
4. Wait until the upload finishes.

Tip:
- Keep all four files together in one local folder before you start. That makes upload easier.

## Step 5: Run The Notebook Top To Bottom
Recommended order:
1. Intro and install cell
2. Imports and file-location cell
3. Data loading and data dictionary cell
4. Modeling approach markdown
5. Data preparation and split summary cell
6. Arps hyperbolic fitting cell
7. Random forest training and recursive forecast cell
8. Exponential Smoothing and ARIMA cell
9. Metrics and plotting cell
10. Interpretation markdown
11. Export-results cell

Fastest option:
1. Click `Runtime` -> `Run all`.
2. Watch for any upload prompt during the data-loading step.

## Step 6: Review The Outputs
You should see:
- a dataset summary
- a phase summary showing `30` train months, `6` test months, and `12` forecast months per completion inside the selected `48-month` window
- fitted `Arps` parameters for each completion
- multivariate `RandomForestRegressor` forecast results
- `Exponential Smoothing` and `ARIMA` forecast results
- phase-based forecast metrics
- per-completion comparison metrics
- charts showing actual vs predicted oil rates across train, test, and forecast periods

## Step 7: Download The Results
The notebook writes output files to:

`results/production_forecasting/`

Expected files:
- `model_comparison_metrics.csv`
- `per_completion_metrics.csv`
- `per_well_metrics.csv`
- `holdout_forecasts.csv`
- `prediction_timeline.csv`
- `arps_parameters.csv`
- `rf_model_summary.csv`
- `time_series_model_summary.csv`

To download from Colab:
1. Click the folder icon in the left sidebar.
2. Open `results`, then `production_forecasting`.
3. Use the three-dot menu beside each file to download it.

## What The Notebook Is Doing
The workflow is:
1. Convert monthly production volumes into daily average production rates using `days_on_prod`.
2. Keep the most recent `48` months per completion for the analysis window.
3. Split that window into `30` training months, `6` internal test months, and a `12` month forecast window.
4. Fit `Arps hyperbolic decline` to each completion individually on the training segment.
5. Train one multivariate `RandomForestRegressor` workflow per completion using oil, gas, and water production-state features.
6. Fit `Exponential Smoothing` and `ARIMA` on each completion's oil-rate history only.
7. Compare all four methods against known actuals in the test and forecast periods.

## Troubleshooting
### If package install fails
- Rerun the install cell.
- If needed, restart the runtime and run the notebook again from the top.

### If the notebook says files are missing
- Make sure the uploaded filenames are exact.
- Reupload `well_monthly_production.csv`, `well_master.csv`, and `data_dictionary.md`.

### If plots do not show
- Rerun the plotting cell.
- Confirm earlier model cells completed without errors.

### If forecasts look strange
- Check whether the selected test or forecast months include an abrupt change that is not well represented in the earlier history.
- Review the rows in `holdout_forecasts.csv` and `prediction_timeline.csv`.
- Remember that `Arps`, multivariate `Random Forest`, `Exponential Smoothing`, and `ARIMA` are being compared on a compact analysis window, not a full field-history matching exercise.
- Remember that `oil_bbl` is monthly volume while the plots show daily rates based on `days_on_prod`.

## Suggested Workflow
1. Review the data dictionary first.
2. Review the `30 month train -> 6 month test -> 12 month forecast` structure.
3. Run the `Arps` fit.
4. Run the multivariate `Random Forest`, `Exponential Smoothing`, and `ARIMA` cells.
5. Compare metrics and the train/test/forecast plots.
6. Discuss when an engineer would still trust decline curves more than ML or statistical time-series baselines.
