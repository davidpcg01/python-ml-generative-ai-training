# Session 1 Slides

## Session Goal
Session 1 should leave participants with two strong takeaways:
- classical ML is useful for prediction and optimization in energy workflows
- GenAI can go well beyond summarization and act as an analysis and workflow-building copilot

## Slide 1: Title
`From ML To GenAI In Energy`

Key message:
- Today is about understanding where AI fits across prediction, optimization, and engineering decision support.

Visual idea:
- A simple flow from `data` to `prediction` to `decision` to `workflow assistant`

## Slide 2: About The Presenter
Title:
`Why I Am Teaching This`

Suggested bullets:
- `David Nnamdi`
- Staff Data Scientist at `Intuit`
- Former `Reservoir Engineer` and `Petroleum Engineering Software Developer` in upstream oil and gas
- Built optimization products including `WaterWise`, `SandWise`, `FracGenie`, and `Sequestrix`
- Experience in `production forecasting`, `decline curve analysis`, `reservoir modeling`, `optimization`, and internal technical software
- Dual master's degrees in `Petroleum Engineering` and `Data Science and Analytics` from the `University of Oklahoma`
- SPE Journal author on `CO2 transportation network optimization`

Suggested links:
- [LinkedIn](https://www.linkedin.com/in/david-nnamdi/)
- [GitHub](https://github.com/davidpcg01)
- [Google Scholar](https://scholar.google.com/citations?user=Qfo5LYcAAAAJ)

Key message:
- This session is coming from someone who has worked across reservoir engineering, production forecasting, optimization, and modern AI-enabled workflow building.

Visual idea:
- Simple professional bio layout with your name, role, and a two-column split:
  - `Energy domain experience`
  - `AI/ML and analytics experience`

## Slide 3: Why This Matters Now
Talking points:
- Technical teams are drowning in data, reports, spreadsheets, and repeated analyses.
- Engineering workflows often combine numerical prediction and document-heavy reasoning.
- AI is valuable when it saves time, improves consistency, and supports better decisions.

Anchor examples:
- production forecasting
- drilling report review
- well-log interpretation support
- carbon storage screening

## Slide 4: Three Levels Of Analytics
Structure:
- `Descriptive`: what happened?
- `Predictive`: what is likely to happen?
- `Prescriptive`: what should we do?

Energy examples:
- descriptive: production dashboard
- predictive: next-month oil rate forecast
- prescriptive: choose the next surveillance action or operating setting

## Slide 5: Where ML Fits
Core message:
- ML is strongest when you have historical patterns and want to predict numbers, classes, trends, anomalies, or actions under constraints.

Examples by role:
- reservoir and production: forecast production, classify underperforming wells
- drilling: predict risk or performance
- geoscience: classify facies or lithology
- carbon storage: rank sites or estimate capacity

## Slide 6: ML Workflow Without The Jargon
Sequence:
1. define the problem
2. collect and clean data
3. choose features and target
4. train and test
5. evaluate
6. decide how to use the result

Key caution:
- a good model on bad data is still a bad decision aid

## Slide 7: Core ML Methods For This Audience
Simple map:
- regression: predict a number
- classification: predict a category
- clustering: group similar wells or intervals
- anomaly detection: flag unusual behavior
- time-series or lagged models: forecast over time
- optimization: recommend an action under constraints

## Slide 8: Role-Specific ML Examples
Layout:
- `Production`: forecast oil rate, identify underperformers, review lift performance
- `Drilling`: predict NPT risk, compare offsets, flag dysfunction patterns
- `Geoscience`: classify facies, support log interpretation, compare notes across wells
- `Carbon`: screen formations, rank candidates, estimate storage support metrics

## Slide 9: Prescriptive Analytics
Key message:
- Prediction tells you what may happen. Prescriptive analytics helps answer what to do next.

Examples:
- optimize choke or surveillance priority
- rank wells for intervention
- choose candidate storage sites under constraints

## Slide 10: Optimization In Energy
Headline:
`Optimization Is Bigger Than Many Engineers Realize`

Key message:
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
Simple roadmap:
1. learn the building blocks: `decision variables`, `objective`, `constraints`
2. start with small allocation or routing problems
3. translate one engineering workflow into an optimization model
4. solve it with a tool such as `Excel Solver`, `PuLP`, `Pyomo`, `OR-Tools`, or `Gurobi`
5. validate outputs against engineering common sense and field constraints

Use cases to mention:
- which wells to prioritize
- how to allocate water, sand, or transport capacity
- where to tie in pipelines or place infrastructure
- how to schedule operations under time and cost limits

## Slide 12: Optimization Demo Step By Step
Title:
`Hands-On Demo: WaterWise-Style Optimization`

Step-by-step flow:
1. define the business problem:
   - supply water to frac pads at lowest feasible cost
2. show the input tables:
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

Key teaching message:
- this is what prescriptive analytics looks like in practice

## Slide 13: Transition To GenAI
Headline:
`So where does GenAI fit?`

Key message:
- Use ML when you need to predict or optimize.
- Use GenAI when you need to work with language, documents, reasoning steps, code generation, and workflow assembly.

Short contrast:
- ML predicts the number
- GenAI helps the engineer use the number

## Slide 14: GenAI In Energy Is More Than Summarization
Examples:
- search across reports and technical notes
- extract structured facts from unstructured text
- compare wells, reports, or scenarios
- explain model outputs in plain English
- write Python or SQL for analysis
- assemble repeatable internal workflow tools

## Slide 15: Featured Scenario
Title:
`Production Forecasting Copilot`

Scenario bullets:
- 18 wells across 3 pads
- need a 6-month forecast
- identify likely underperformers
- flag possible drivers such as water cut and uptime
- produce visuals and an engineering summary

## Slide 16: What ML Does In This Scenario
Points:
- uses historical well and operating data
- learns patterns linked to future oil rate
- supports well-level forecasting
- can help rank wells by expected underperformance

## Slide 17: What GenAI Does In This Scenario
Points:
- frames the business problem
- writes or improves Python analysis code
- suggests plots
- interprets the outputs in engineering language
- drafts a summary memo
- helps package the workflow as a notebook or internal mini-tool

## Slide 18: Predictive Demo Step By Step
Title:
`Hands-On Demo: Production Forecasting Copilot`

Step-by-step flow:
1. show the dataset
2. frame the predictive question:
   - what will next-month or next-period production look like?
3. run the simple notebook model
4. inspect forecast accuracy and sample well plots
5. identify likely underperformers or surveillance candidates
6. prompt the LLM with the scenario
7. generate a first-pass analysis workflow
8. improve plots and interpretation
9. package as a reusable notebook or app concept

Presenter note:
- keep repeating the distinction between `forecasting model` and `GenAI copilot`

## Slide 19: Practical Limits And Risks
Key cautions:
- poor data quality
- changing operating conditions
- workovers and interventions
- hallucinated explanations or code
- overtrust in recommendations without engineering review

## Slide 20: Suggested Paper Reading
Title:
`Suggested Reading: Oil And Gas ML And Optimization`

Suggested papers:
- Production forecasting with ML:
  - [Production Forecasting in Conventional Oil Reservoirs Using Deep Learning](https://doi.org/10.2118/209277-MS)
  - [A Data-Driven Approach to Forecasting Production with Applications to Multiple Shale Plays](https://doi.org/10.2118/200365-MS)
- Well logs and subsurface ML:
  - [Automated Well-Log Processing and Lithology Classification by Identifying Optimal Features Through Unsupervised and Supervised Machine-Learning Algorithms](https://doi.org/10.2118/202477-PA)
  - [Machine Learning for Well Log Normalization](https://doi.org/10.2118/196178-MS)
- Drilling and development optimization:
  - [Large-Scale Deployment of a Closed-Loop Drilling Optimization System: Implementation and Field Results](https://doi.org/10.2118/199601-MS)
  - [Joint Optimization of Well Locations, Types, Drilling Order, and Controls Given a Set of Potential Drilling Paths](https://doi.org/10.2118/193885-PA)
- Carbon and infrastructure optimization:
  - [Embedding Existing Pipelines in Design of CO2 Transportation Networks for Optimal Sequestration Economics](https://doi.org/10.2118/214917-PA)

Presenter note:
- Keep this slide selective. The goal is to give participants a credible starting point, not an exhaustive literature review.

## Slide 21: Session 1 Wrap-Up
Closing points:
- ML helps predict and optimize
- GenAI helps interpret, accelerate, and operationalize the work
- together, they are more useful than either alone

Bridge to Session 2:
- next time we go fully into LLMs, RAG, chatbots, agents, coding copilots, and MCP-style tool connectivity
