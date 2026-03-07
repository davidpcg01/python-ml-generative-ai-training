# Production Forecasting Data Dictionary

## File: `well_monthly_production.csv`
One row per `well_id` per month.

### Columns
- `well_id`: unique well identifier
- `pad`: operating pad or well group
- `date`: month start date for the observation
- `oil_rate_bopd`: average monthly oil rate in barrels of oil per day
- `gas_rate_mscfd`: average monthly gas rate in thousand standard cubic feet per day
- `water_cut_pct`: produced water percentage
- `uptime_pct`: estimated percentage of the month that the well was online
- `choke_size_64in`: choke size in sixty-fourths of an inch
- `tubing_pressure_psi`: tubing pressure proxy
- `casing_pressure_psi`: casing pressure proxy
- `gor_scf_bbl`: gas-oil ratio proxy
- `bhp_proxy_psi`: bottomhole pressure proxy used for demo purposes
- `artificial_lift_type`: simplified artificial lift category
- `reservoir_zone`: simplified reservoir zone label
- `well_age_months`: producing age of the well in months
- `lateral_length_ft`: lateral length in feet
- `completion_stage_count`: stage count for the completion design
- `event_flag`: indicates whether a reportable event occurred in that month
- `event_type`: simplified event label if present
- `forecast_target_next_month_bopd`: next month's oil rate for supervised learning examples

## File: `well_events.csv`
One row per operational event.

### Columns
- `well_id`: unique well identifier
- `event_date`: date of the event
- `event_type`: event classification such as `workover` or `pump_change`
- `event_cost_usd`: simplified cost estimate for the event
- `event_notes`: short text description for prompting or retrieval demos

## Usage Notes
- This dataset is synthetic and designed for training.
- Some missing values are intentionally included to create realistic data quality issues.
- The data should not be treated as a validated reservoir or production model.
- The target column is intended for simple forecasting exercises rather than rigorous time-series benchmarking.
