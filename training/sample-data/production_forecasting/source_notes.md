# BSEE Source Notes

## Primary Source
This classroom dataset is derived from the official `BSEE OGOR-A` monthly well-completion production files.

Key source pages:
- Raw data index: [https://www.data.bsee.gov/Main/RawData.aspx](https://www.data.bsee.gov/Main/RawData.aspx)
- OGOR-A yearly files: [https://www.data.bsee.gov/Main/OGOR-A.aspx](https://www.data.bsee.gov/Main/OGOR-A.aspx)
- OGOR-A field definitions: [https://www.data.bsee.gov/Main/HtmlPage.aspx?page=ogorA](https://www.data.bsee.gov/Main/HtmlPage.aspx?page=ogorA)

Direct raw files used for screening:
- `https://www.data.bsee.gov/Production/Files/ogora2021delimit.zip`
- `https://www.data.bsee.gov/Production/Files/ogora2022delimit.zip`
- `https://www.data.bsee.gov/Production/Files/ogora2023delimit.zip`
- `https://www.data.bsee.gov/Production/Files/ogora2024delimit.zip`

## Why This Source Was Chosen
This source works well for the training because it is:
- official regulator data rather than an unofficial classroom sample
- reported monthly at the completion level
- consistent enough to screen for continuous histories
- suitable for deriving daily production rates using `days_on_prod`

## Training Subset Definition
This repo includes a small, classroom-friendly subset rather than the full BSEE raw files.

Selected completions:
- `G21245 PN002`
- `G21245 PS001`
- `G21245 PS002`

Shared characteristics:
- operator: `UNION OIL COMPANY OF CALIFORNIA`
- area / block: `WR 678`
- basin: `Gulf of Mexico`
- state label in the training subset: `OCS`

Selected time window:
- `2021-01-01` through `2024-12-01`

Reason for selection:
- each completion has `48` continuous monthly records
- the completions share the same operator and offshore block context
- the histories support the intended `30 month train + 6 month test + 12 month forecast` workflow
- the selected completions behave more cleanly under the notebook workflow than the earlier Texas sample

## Important Units Note
In the raw BSEE records:
- `oil_bbl`, `gas_mcf`, and `water_bbl` are monthly volumes
- `days_on_prod` is the number of producing days reported for that month

In the notebook:
- the forecast target is `oil_rate_bbl_per_day = oil_bbl / days_on_prod`
- the plots therefore show `bbl/day on production`, not monthly barrels

## Supporting References
These references still anchor the modeling approach used in the notebook:
- Oil and Gas Production Forecasting Using Decision Trees, Random Forest, and XGBoost: [https://jqcsm.qu.edu.iq/index.php/journalcm/article/view/1431](https://jqcsm.qu.edu.iq/index.php/journalcm/article/view/1431)
- Application of machine learning in predicting oil rate decline for Bakken shale oil wells: [https://www.nature.com/articles/s41598-022-20401-6](https://www.nature.com/articles/s41598-022-20401-6)
- Machine learning based decline curve analysis for short-term oil production forecast: [https://journals.sagepub.com/doi/10.1177/01445987211011784](https://journals.sagepub.com/doi/10.1177/01445987211011784)
- Forecasting: Principles and Practice, Exponential Smoothing chapter: [https://otexts.com/fpp3/expsmooth.html](https://otexts.com/fpp3/expsmooth.html)
- Forecasting: Principles and Practice, ARIMA chapter: [https://otexts.com/fpp3/arima.html](https://otexts.com/fpp3/arima.html)

## Notes For Training Use
- The repo stores a cleaned monthly CSV subset so participants do not need to parse the raw regulator ZIP files during class.
- The notebook compares `Arps`, a multivariate `RandomForestRegressor`, `Exponential Smoothing`, and `ARIMA` on the same `30/6/12` completion-level split.
- The ML and time-series models are fit one completion at a time rather than pooling all completions into a single model.
