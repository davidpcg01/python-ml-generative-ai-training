# Production Forecasting Data Dictionary

## Dataset Overview
This subset uses official monthly production records for `3` offshore Gulf of Mexico completions from `BSEE OGOR-A`.

Selected completions:
- `G21245 PN002`
- `G21245 PS001`
- `G21245 PS002`

Shared context:
- operator: `UNION OIL COMPANY OF CALIFORNIA`
- area / block: `WR 678`
- basin: `Gulf of Mexico`
- reporting source: `BSEE OGOR-A` well-completion production

Each completion includes `48` monthly records:
- `30` months for model fitting
- `6` months for internal test comparison
- `12` months reserved as the forward forecast window

This supports a clean comparison between:
- `Arps hyperbolic decline`
- `RandomForestRegressor` trained separately for each completion with multivariate production-state features
- `Exponential Smoothing`
- `ARIMA`

## File: `well_monthly_production.csv`
One row per `well_id` per month.

### Columns
- `well_id`: completion label used in the demo
- `api_uwi`: offshore API / UWI identifier from the BSEE source
- `operator`: operator name
- `county`: broad location label used for the subset
- `reservoir`: field code used as the reservoir-style label in the repo files
- `state`: `OCS` for Outer Continental Shelf
- `basin`: basin name
- `area_block`: offshore area and block code from BSEE
- `date`: month-start date for the production record
- `oil_bbl`: monthly oil volume in `bbl/month`
- `gas_mcf`: monthly gas volume in `mcf/month`
- `water_bbl`: monthly water volume in `bbl/month`
- `days_on_prod`: number of days the completion was reported on production in that month
- `days_in_month`: calendar days in the month

### Recommended derived columns in the notebook
- `oil_rate_bbl_per_day`: `oil_bbl / days_on_prod`
- `gas_rate_mcf_per_day`: `gas_mcf / days_on_prod`
- `water_rate_bbl_per_day`: `water_bbl / days_on_prod`
- `water_cut_pct`: `100 * water_bbl / (oil_bbl + water_bbl)` when total liquid is positive
- `gor_mcf_per_bbl`: `gas_mcf / oil_bbl` when oil volume is positive

## File: `well_master.csv`
One row per demo completion.

### Columns
- `well_id`: completion label used in the notebook
- `api_uwi`: offshore API / UWI identifier
- `operator`: operator name
- `county`: broad location label
- `reservoir`: field code used as a compact label
- `state`: `OCS`
- `basin`: basin name
- `area_block`: offshore area and block code
- `subset_start_date`: first month kept for the classroom subset
- `subset_end_date`: last month kept for the classroom subset
- `total_months`: total records per completion in the subset
- `holdout_months`: number of months reserved for the forward forecast evaluation window
- `training_months`: number of months retained as the pre-forecast modeling window
- `source_dataset`: short provenance label

## Usage Notes
- This is a compact subset, not the full upstream BSEE database.
- The notebook uses a `36-month` modeling window per completion, split into `30` training months and `6` internal test months.
- The `12-month forecast` is evaluated against known future months in the selected analysis window.
- The notebook compares `Arps`, a multivariate `RandomForestRegressor`, `Exponential Smoothing`, and `ARIMA`.
- The notebook trains each model separately for each completion rather than pooling the completions together.
- `oil_bbl`, `gas_mcf`, and `water_bbl` are monthly volumes. The plots in the notebook show daily rates derived from `days_on_prod`.
