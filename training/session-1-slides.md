# Session 1 Slides

## Session Goal
Session 1 focuses on two core ideas:
- classical ML is useful for prediction and optimization in energy workflows
- GenAI can go beyond summarization and act as an analysis and workflow-building copilot

## Slide 1: Title
`From ML To GenAI In Energy`

- AI in technical energy work sits across prediction, optimization, and engineering decision support.
- A useful mental model is `data -> prediction -> decision -> workflow assistant`.

## Slide 2: Instructor Background
`Why I Am Teaching This`

- `David Nnamdi`
- Staff Data Scientist at `Intuit`
- Former `Reservoir Engineer` and `Petroleum Engineering Software Developer`
- Built optimization products including `WaterWise`, `SandWise`, `FracGenie`, and `Sequestrix`
- Experience in `production forecasting`, `decline curve analysis`, `reservoir modeling`, `optimization`, and technical workflow software
- Dual master's degrees in `Petroleum Engineering` and `Data Science and Analytics` from the `University of Oklahoma`
- SPE Journal author on `CO2 transportation network optimization`

Links:
- [LinkedIn](https://www.linkedin.com/in/david-nnamdi/)
- [GitHub](https://github.com/davidpcg01)
- [Google Scholar](https://scholar.google.com/citations?user=Qfo5LYcAAAAJ)

## Slide 3: Why This Matters Now
- Technical teams work with large volumes of data, reports, spreadsheets, and repeated analyses.
- Engineering workflows often combine numerical prediction and document-heavy reasoning.
- AI is valuable when it saves time, improves consistency, and supports better decisions.

Anchor examples:
- production forecasting
- drilling report review
- well-log interpretation support
- carbon storage screening

## Slide 4: Three Levels Of Analytics
- `Descriptive`: what happened?
- `Predictive`: what is likely to happen?
- `Prescriptive`: what should we do?

Energy examples:
- descriptive: production dashboard
- predictive: next-month oil rate forecast
- prescriptive: choose the next surveillance action or operating setting

## Slide 5: Where ML Fits
- ML is strongest when you have historical patterns and want to predict numbers, classes, trends, anomalies, or actions under constraints.

Examples by role:
- reservoir and production: forecast production, classify underperforming wells
- drilling: predict risk or performance
- geoscience: classify facies or lithology
- carbon storage: rank sites or estimate capacity

## Slide 6: ML Workflow Without The Jargon
1. define the problem
2. collect and clean data
3. choose features and target
4. train and test
5. evaluate
6. decide how to use the result

Caution:
- a good model on bad data is still a bad decision aid

## Slide 7: Core ML Methods For This Audience
- regression: predict a number
- classification: predict a category
- clustering: group similar wells or intervals
- anomaly detection: flag unusual behavior
- time-series or lagged models: forecast over time
- optimization: recommend an action under constraints

## Slide 8: Role-Specific ML Examples
- `Production`: forecast oil rate, identify underperformers, review lift performance
- `Drilling`: predict NPT risk, compare offsets, flag dysfunction patterns
- `Geoscience`: classify facies, support log interpretation, compare notes across wells
- `Carbon`: screen formations, rank candidates, estimate storage support metrics

## Slide 9: Prescriptive Analytics
- Prediction tells you what may happen.
- Prescriptive analytics helps answer what to do next.

Examples:
- optimize choke or surveillance priority
- rank wells for intervention
- choose candidate storage sites under constraints

## Slide 10: Optimization In Energy
`Optimization Is Bigger Than Many Engineers Realize`

- Optimization is about finding the best feasible decision under real technical, operational, and economic constraints.

Examples from practice:
- `WaterWise`: optimize completions water sourcing, storage, routing, and reuse across constrained networks
- `SandWise`: optimize proppant logistics and supply-chain decisions under cost and capacity limits
- `FracGenie`: optimize stage sequencing and completions scheduling
- `Sequestrix`: optimize CO2 transport networks, source-sink matching, and pipeline reuse for sequestration economics

Broader energy use cases:
- production network routing and allocation
- artificial lift and surveillance prioritization
- drilling and completions scheduling
- emissions, carbon transport, and sequestration planning
- portfolio, capital, and infrastructure decisions

## Slide 11: Practical Path To Learning Linear Optimization
1. learn the building blocks: `decision variables`, `objective`, `constraints`
2. start with small allocation or routing problems
3. translate one engineering workflow into an optimization model
4. solve it with a tool such as `Excel Solver`, `PuLP`, `Pyomo`, `OR-Tools`, or `Gurobi`
5. validate outputs against engineering common sense and field constraints

Example questions:
- which wells should be prioritized?
- how should water, sand, or transport capacity be allocated?
- where should pipelines tie in or infrastructure be placed?
- how should operations be scheduled under time and cost limits?

## Slide 12: Optimization Demo Step By Step
`Hands-On Demo: WaterWise-Style Optimization`

1. define the business problem:
   - supply water to frac pads at lowest feasible cost
2. review the input tables:
   - sources, pads, transport links, scenario parameters
3. define the optimization model:
   - decision variables
   - objective
   - constraints
4. solve the model in Python using `PuLP`
5. inspect the optimal allocation:
   - source-to-pad volumes
   - total cost
   - freshwater use
   - produced-water reuse
6. test a scenario change:
   - tighten freshwater cap
   - reduce route capacity
   - increase produced-water target

- This is what prescriptive analytics looks like in practice.

## Slide 13: Transition To GenAI
`So where does GenAI fit?`

- Use ML when you need to predict or optimize.
- Use GenAI when you need to work with language, documents, reasoning steps, code generation, and workflow assembly.

Short contrast:
- ML predicts the number
- GenAI helps the engineer use the number

## Slide 14: GenAI In Energy Is More Than Summarization
- search across reports and technical notes
- extract structured facts from unstructured text
- compare wells, reports, or scenarios
- explain model outputs in plain English
- write Python or SQL for analysis
- assemble repeatable internal workflow tools

## Slide 15: Featured Scenario
`Production Forecasting Copilot`

- official BSEE offshore completion subset
- 3 producing completions from the same operator and offshore block context
- 30 months train, 6 months test, and 12 months forecast
- compare `Arps hyperbolic decline` against multivariate `RandomForestRegressor`, `Exponential Smoothing`, and `ARIMA`
- produce visuals and an engineering summary

## Slide 16: What ML Does In This Scenario
- uses historical monthly production data from the selected BSEE completions
- fits `Arps hyperbolic decline` as the classical baseline
- trains a separate `RandomForestRegressor` on multivariate production-state features for each completion
- fits `Exponential Smoothing` and `ARIMA` as pure time-series baselines
- compares all four approaches on a 6-month internal test and a 12-month forecast window

## Slide 17: What GenAI Does In This Scenario
- frames the business problem
- writes or improves Python analysis code
- suggests plots
- interprets the outputs in engineering language
- drafts a summary memo
- helps package the workflow as a notebook or internal mini-tool

## Slide 18: Predictive Demo Step By Step
`Hands-On Demo: Production Forecasting Copilot`

1. review the dataset
2. frame the predictive question:
   - how well can the next 12 months be forecast after a 30-month training history and a 6-month test check?
3. fit `Arps hyperbolic decline`
4. train the multivariate `RandomForestRegressor`
5. fit `Exponential Smoothing` and `ARIMA`
6. inspect forecast accuracy and per-completion comparison plots
7. use an LLM with the scenario
8. generate a first-pass analysis workflow
9. improve plots and interpretation
10. package the workflow as a reusable notebook or app concept

## Slide 19: Practical Limits And Risks
- poor data quality
- changing operating conditions
- workovers and interventions
- hallucinated explanations or code
- overtrust in recommendations without engineering review

## Slide 20: Suggested Paper Reading
`Suggested Reading: Oil And Gas ML And Optimization`

Production forecasting with ML:
- [Production Forecasting in Conventional Oil Reservoirs Using Deep Learning](https://doi.org/10.2118/209277-MS)
- [A Data-Driven Approach to Forecasting Production with Applications to Multiple Shale Plays](https://doi.org/10.2118/200365-MS)

Well logs and subsurface ML:
- [Automated Well-Log Processing and Lithology Classification by Identifying Optimal Features Through Unsupervised and Supervised Machine-Learning Algorithms](https://doi.org/10.2118/202477-PA)
- [Machine Learning for Well Log Normalization](https://doi.org/10.2118/196178-MS)

Drilling and development optimization:
- [Large-Scale Deployment of a Closed-Loop Drilling Optimization System: Implementation and Field Results](https://doi.org/10.2118/199601-MS)
- [Joint Optimization of Well Locations, Types, Drilling Order, and Controls Given a Set of Potential Drilling Paths](https://doi.org/10.2118/193885-PA)

Carbon and infrastructure optimization:
- [Embedding Existing Pipelines in Design of CO2 Transportation Networks for Optimal Sequestration Economics](https://doi.org/10.2118/214917-PA)

## Slide 21: Session 1 Wrap-Up
- ML helps predict and optimize
- GenAI helps interpret, accelerate, and operationalize the work
- together, they are more useful than either alone

Next topic:
- LLMs, RAG, chatbots, agents, coding copilots, and MCP-style tool connectivity
