# Cursor Free Setup Guide

This guide shows how to install the free version of `Cursor`, open the training files, and complete a small exercise using the prompt files in `training/hands-on/cursor-prompts/`.

## What You Need
- A computer with internet access
- A free `Cursor` account
- The training folder or repo on your machine

## Step 1: Install Cursor Free
1. Go to [https://www.cursor.com](https://www.cursor.com).
2. Download `Cursor` for your operating system.
3. Install it the same way you would install `VS Code`.
4. Open `Cursor`.
5. Sign in and choose the free plan if prompted.

## Step 2: Open The Training Folder
1. In `Cursor`, click `Open Project`.
2. Select the training folder or the repo root.
3. Wait for the files to load in the sidebar.

If you are only using the production-forecasting exercise, make sure this content is available in the folder you open:
- `training/hands-on/production-forecasting-demo.ipynb`
- `training/hands-on/cursor-prompts/`
- `training/sample-data/production_forecasting/well_monthly_production.csv`
- `training/sample-data/production_forecasting/well_master.csv`
- `training/sample-data/production_forecasting/data_dictionary.md`
- `training/sample-data/production_forecasting/source_notes.md`

## Step 3: Open The Key Files
Open these files in `Cursor` before you start prompting:
- `training/hands-on/production-forecasting-demo.ipynb`
- `training/sample-data/production_forecasting/well_monthly_production.csv`
- `training/sample-data/production_forecasting/well_master.csv`
- `training/sample-data/production_forecasting/data_dictionary.md`
- `training/sample-data/production_forecasting/source_notes.md`

This gives `Cursor` the project context it needs.

## Step 4: Optional Python Setup
If you want to run Python code directly inside `Cursor`:
1. Open the integrated terminal.
2. Create a virtual environment.
3. Install the required packages.
4. Select the Python interpreter if `Cursor` asks.

Example install command:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels jupyter
```

## Step 5: Find The Prompt Library
The prompt files for this exercise are in:

`training/hands-on/cursor-prompts/`

Use these files:
- `arps-forecast-per-well.md`
- `forecast-dashboard-html.md`
- `forecast-analysis-insights.md`

## Minimum Exercise
Complete this small exercise in `Cursor`:

1. Open the training folder in `Cursor`.
2. Open the files listed in the earlier steps.
3. Open `training/hands-on/cursor-prompts/arps-forecast-per-well.md`.
4. Copy the prompt text into the `Cursor` chat.
5. Ask `Cursor` to create the forecast script and output files.
6. Review the generated code before running it.
7. Then repeat the process with:
   - `training/hands-on/cursor-prompts/forecast-dashboard-html.md`
   - `training/hands-on/cursor-prompts/forecast-analysis-insights.md`

## Good Practice
- Read the prompt fully before sending it.
- Keep the relevant data files open in the editor.
- Check that generated code matches the file names and columns in the dataset.
- Review charts, metrics, and written conclusions before trusting them.
- Remember that `oil_bbl` is monthly volume and plotted oil rate is `bbl/day on production`.

## If Cursor Does Not Respond Well
- Open more of the relevant files before asking again.
- Use the exact prompt text from the prompt library.
- Be specific about the file you want created.
- Ask `Cursor` to explain what it changed.

## Expected Outcome
By the end of this exercise, you should be able to use `Cursor` to:
- generate a forecasting script
- generate a simple dashboard
- generate a written analysis report

The goal is to use `Cursor` as a coding and workflow assistant while you still review the technical output yourself.
