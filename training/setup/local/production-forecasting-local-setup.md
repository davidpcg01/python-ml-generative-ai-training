# Production Forecasting Demo: Local Setup Guide

This guide shows how to run the BSEE offshore-completion production-forecasting notebook locally on `macOS` and `Windows`.

## Files You Need
Use these files from the training package:
- `training/demos/production-forecasting/production-forecasting-demo.ipynb`
- `training/data/production_forecasting/well_monthly_production.csv`
- `training/data/production_forecasting/well_master.csv`
- `training/data/production_forecasting/data_dictionary.md`
- `training/data/production_forecasting/source_notes.md`

## Recommended Local Stack
- `Python 3.10` or newer
- `Jupyter Notebook` or `JupyterLab`
- A lightweight virtual environment

Required packages:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy`
- `statsmodels`
- `jupyter`

## Option A: Run From The Repo Root
If you already have this repo on your machine:
1. Open a terminal in the repo root.
2. Create and activate a virtual environment.
3. Install the required packages.
4. Launch Jupyter.
5. Open `training/demos/production-forecasting/production-forecasting-demo.ipynb`.

## macOS Setup
### Step 1: Check Python
In Terminal, run:

```bash
python3 --version
```

If Python is missing, install it from [python.org](https://www.python.org/downloads/) or through your preferred package manager.

### Step 2: Create A Virtual Environment
From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Packages
If you want the exact notebook dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels jupyter
```

If you prefer the repo requirements:

```bash
pip install -r training/setup/requirements.txt
```

### Step 4: Launch Jupyter
Run:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

Then open:

`training/demos/production-forecasting/production-forecasting-demo.ipynb`

## Windows Setup
### Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/windows/).
2. During installation, check `Add Python to PATH`.

### Step 2: Open PowerShell
Navigate to the repo root.

### Step 3: Create And Activate A Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again.

### Step 4: Install Packages

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels jupyter
```

or

```powershell
pip install -r training\requirements.txt
```

### Step 5: Launch Jupyter

```powershell
jupyter notebook
```

Then open:

`training/demos/production-forecasting/production-forecasting-demo.ipynb`

## Expected Project Layout
If you run the notebook from the repo root, the notebook should automatically find:

- `training/data/production_forecasting/well_monthly_production.csv`
- `training/data/production_forecasting/well_master.csv`
- `training/data/production_forecasting/data_dictionary.md`

## Running The Notebook
Run cells in order:
1. Package install
2. Imports and data-location logic
3. Data loading and inspection
4. Data preparation
5. Arps fitting
6. Random forest forecasting
7. Exponential Smoothing and ARIMA
8. Metrics and plots
9. Export results

## Output Files
Results are written to:

`training/demos/production-forecasting/results/production_forecasting/`

Expected exports:
- `model_comparison_metrics.csv`
- `per_completion_metrics.csv`
- `per_well_metrics.csv`
- `holdout_forecasts.csv`
- `prediction_timeline.csv`
- `arps_parameters.csv`
- `rf_model_summary.csv`
- `time_series_model_summary.csv`

## Common Local Issues
### `ModuleNotFoundError`
Install the missing package inside the active virtual environment.

Example:

```bash
pip install scipy
```

### Notebook cannot find the sample data
- Make sure you launched Jupyter from the repo root.
- Confirm the `training/data/production_forecasting/` folder exists.
- Check that the filenames are unchanged.

### Matplotlib plots not showing
- Rerun the plotting cell.
- If using Jupyter Notebook, ensure the earlier cells completed successfully.

### Different results on another machine
- Small differences can happen because of package-version changes.
- The notebook sets `random_state=42` for the Random Forest to improve repeatability, while the statistical baselines may still differ slightly across package versions.

## Suggested Local Workflow
1. Open the notebook.
2. Review the source notes and data dictionary.
3. Run the data preparation cells.
4. Run `Arps hyperbolic` first.
5. Run the multivariate `RandomForestRegressor` plus `Exponential Smoothing` and `ARIMA`.
6. Compare the train/test/forecast charts and metrics across all models.
7. Review the exported CSV files.

Notes for this dataset:
- `oil_bbl`, `gas_mcf`, and `water_bbl` are monthly volumes.
- The notebook converts those volumes to `bbl/day on production` and related daily rates using `days_on_prod`.
