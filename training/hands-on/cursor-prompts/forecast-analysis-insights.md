# Prompt: Analyze Forecast Results And Produce Engineering Insights

Use this prompt inside `Cursor` after the forecast output files already exist.

```text
You are acting as a petroleum-engineering analysis assistant inside a Cursor project.

I need a detailed engineering interpretation of the forecast results from the production-forecasting workflow.

Available files:
- results/production_forecasting/holdout_forecasts.csv
- results/production_forecasting/prediction_timeline.csv
- results/production_forecasting/arps_parameters.csv
- results/production_forecasting/model_comparison_metrics.csv
- results/production_forecasting/per_completion_metrics.csv
- optionally:
  - results/production_forecasting/per_well_metrics.csv
  - results/production_forecasting/rf_model_summary.csv
  - results/production_forecasting/time_series_model_summary.csv
  - results/production_forecasting/arps_holdout_forecast.csv
  - results/production_forecasting/arps_model_metrics.csv
- supporting context:
  - well_monthly_production.csv
  - well_master.csv
  - data_dictionary.md
  - source_notes.md

Your task:
1. Read the forecast outputs.
2. Compare model quality completion by completion and phase by phase.
3. Identify which completions were forecast more accurately by `Arps`, `Random forest (multivariate)`, `Exponential smoothing`, and `ARIMA`.
4. Explain the results in practical petroleum-engineering language.
5. Produce actionable recommendations.

Required output format:
1. Brief context
2. Overall forecast-quality summary
3. Well-by-well findings
4. Engineering interpretation
5. Recommendations
6. Risks and cautions

Detailed requirements:
- Use the actual data in the CSV files
- Do not invent wells, metrics, or conclusions
- Treat `oil_bbl` as a monthly volume and `oil_rate_bbl_per_day` as the rate-based forecast target
- Quote or summarize the important metric values
- Identify:
  - completions with the lowest forecast error
  - completions with the highest forecast error
  - whether the models perform differently on the 6-month test segment versus the 12-month forecast segment
  - which model family is strongest overall and which is strongest on specific completions
  - completions showing smooth decline behavior
  - completions showing behavior that may violate simple decline assumptions
- If Arps fit parameters look unusual, call that out explicitly
- If a well looks noisy or has abrupt changes, mention that as a possible reason for forecast error
- If the files contain enough information, discuss whether the forecast errors look systematic or random

Petroleum-engineering interpretation requirements:
- Use practical terms such as decline trend, well behavior, production stability, shut-in-like behavior, anomalous response, forecast uncertainty, and screening value
- Keep the explanation accessible to production engineers, not academic only
- Avoid vague statements like “the model did okay”
- Explain why an engineer might still prefer Arps for some screening tasks even if a data-driven model sometimes performs better
- Use the train/test/forecast split correctly:
  - `30` months for training
  - `6` months for internal test comparison
  - `12` months for forward forecast evaluation

Recommendation requirements:
- Give at least 5 concrete recommendations
- Recommendations should include:
  - how to use the forecast operationally
  - where to apply engineering review before action
  - what additional data would improve the forecast
  - whether to trust the results for ranking, budgeting, or surveillance
  - what to test next

Output-file requirement:
- Create a markdown report named forecast_analysis_report.md

Report quality requirements:
- Use clear headings
- Use tables if useful
- Use bullet points where they improve readability
- Keep the tone professional and technically grounded
- Do not include speaker notes
- Do not include generic AI disclaimers

Validation requirements:
- If a required file is missing, say exactly which file is missing
- If the available data is insufficient to support a conclusion, say that explicitly rather than guessing

At the end:
- summarize the top 3 takeaways in one short section titled Final Takeaways
```
