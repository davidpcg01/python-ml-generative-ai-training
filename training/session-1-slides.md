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

## Slide 2: Why This Matters Now
Talking points:
- Technical teams are drowning in data, reports, spreadsheets, and repeated analyses.
- Engineering workflows often combine numerical prediction and document-heavy reasoning.
- AI is valuable when it saves time, improves consistency, and supports better decisions.

Anchor examples:
- production forecasting
- drilling report review
- well-log interpretation support
- carbon storage screening

## Slide 3: Three Levels Of Analytics
Structure:
- `Descriptive`: what happened?
- `Predictive`: what is likely to happen?
- `Prescriptive`: what should we do?

Energy examples:
- descriptive: production dashboard
- predictive: next-month oil rate forecast
- prescriptive: choose the next surveillance action or operating setting

## Slide 4: Where ML Fits
Core message:
- ML is strongest when you have historical patterns and want to predict numbers, classes, trends, anomalies, or actions under constraints.

Examples by role:
- reservoir and production: forecast production, classify underperforming wells
- drilling: predict risk or performance
- geoscience: classify facies or lithology
- carbon storage: rank sites or estimate capacity

## Slide 5: ML Workflow Without The Jargon
Sequence:
1. define the problem
2. collect and clean data
3. choose features and target
4. train and test
5. evaluate
6. decide how to use the result

Key caution:
- a good model on bad data is still a bad decision aid

## Slide 6: Core ML Methods For This Audience
Simple map:
- regression: predict a number
- classification: predict a category
- clustering: group similar wells or intervals
- anomaly detection: flag unusual behavior
- time-series or lagged models: forecast over time
- optimization: recommend an action under constraints

## Slide 7: Role-Specific ML Examples
Layout:
- `Production`: forecast oil rate, identify underperformers, review lift performance
- `Drilling`: predict NPT risk, compare offsets, flag dysfunction patterns
- `Geoscience`: classify facies, support log interpretation, compare notes across wells
- `Carbon`: screen formations, rank candidates, estimate storage support metrics

## Slide 8: Prescriptive Analytics
Key message:
- Prediction tells you what may happen. Prescriptive analytics helps answer what to do next.

Examples:
- optimize choke or surveillance priority
- rank wells for intervention
- choose candidate storage sites under constraints

## Slide 9: Transition To GenAI
Headline:
`So where does GenAI fit?`

Key message:
- Use ML when you need to predict or optimize.
- Use GenAI when you need to work with language, documents, reasoning steps, code generation, and workflow assembly.

Short contrast:
- ML predicts the number
- GenAI helps the engineer use the number

## Slide 10: GenAI In Energy Is More Than Summarization
Examples:
- search across reports and technical notes
- extract structured facts from unstructured text
- compare wells, reports, or scenarios
- explain model outputs in plain English
- write Python or SQL for analysis
- assemble repeatable internal workflow tools

## Slide 11: Featured Scenario
Title:
`Production Forecasting Copilot`

Scenario bullets:
- 18 wells across 3 pads
- need a 6-month forecast
- identify likely underperformers
- flag possible drivers such as water cut and uptime
- produce visuals and an engineering summary

## Slide 12: What ML Does In This Scenario
Points:
- uses historical well and operating data
- learns patterns linked to future oil rate
- supports well-level forecasting
- can help rank wells by expected underperformance

## Slide 13: What GenAI Does In This Scenario
Points:
- frames the business problem
- writes or improves Python analysis code
- suggests plots
- interprets the outputs in engineering language
- drafts a summary memo
- helps package the workflow as a notebook or internal mini-tool

## Slide 14: Live Demo Setup
Demo flow:
1. show the dataset
2. prompt the LLM with the scenario
3. generate a first-pass analysis workflow
4. improve plots and interpretation
5. package as a reusable notebook or app concept

Presenter note:
- keep repeating the distinction between `forecasting model` and `GenAI copilot`

## Slide 15: Practical Limits And Risks
Key cautions:
- poor data quality
- changing operating conditions
- workovers and interventions
- hallucinated explanations or code
- overtrust in recommendations without engineering review

## Slide 16: Session 1 Wrap-Up
Closing points:
- ML helps predict and optimize
- GenAI helps interpret, accelerate, and operationalize the work
- together, they are more useful than either alone

Bridge to Session 2:
- next time we go fully into LLMs, RAG, chatbots, agents, coding copilots, and MCP-style tool connectivity
