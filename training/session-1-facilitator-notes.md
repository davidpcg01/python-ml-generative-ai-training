# Session 1 Facilitator Notes

## Session Theme
`ML foundations plus a strong GenAI bridge`

This session should feel practical from the first few minutes. The audience should leave believing two things:
- classical ML is useful and understandable
- GenAI is not only for text generation, but can help with real analytical and workflow tasks in energy

## Timing Plan
- `0 to 5 min`: opening and context
- `5 to 20 min`: ML foundations without jargon
- `20 to 35 min`: energy-specific ML use cases and prescriptive modeling
- `35 to 50 min`: GenAI bridge and featured production forecasting copilot
- `50 to 60 min`: demo wrap-up, risks, and bridge to Session 2

## Speaker Posture
- Speak like a technical peer, not like a software evangelist.
- Avoid heavy math unless someone asks.
- Keep reminding the room that engineering judgment remains central.
- Use phrases like `decision support`, `technical copilot`, and `workflow acceleration`.

## Slide-By-Slide Notes

### Slide 1: Title
Opening script:
“This first session is about building a usable mental model. I want you to leave knowing where machine learning fits, where generative AI fits, and how both can support engineering and geoscience workflows.”

Audience check-in question:
- “How many of you have already tried ChatGPT, Claude, Copilot, or something similar?”

### Slide 2: Why This Matters Now
Suggested phrasing:
“Most technical teams in energy do not have a shortage of data. They have a shortage of time, attention, and repeatable ways to turn that data into decisions.”

Tie back to audience roles:
- production engineers live in surveillance data, spreadsheets, and performance review loops
- drilling teams live in reports, offsets, lessons learned, and real-time decisions
- geoscientists live in interpretations, logs, technical notes, and uncertainty
- carbon teams live in screening studies, criteria, and documentation

### Slide 3: Three Levels Of Analytics
Use a simple ladder:
- descriptive tells us what happened
- predictive tells us what is likely to happen
- prescriptive suggests what to do

Helpful line:
“Many teams already do descriptive analytics. The step change comes when you move into prediction and then into action support.”

### Slide 4: Where ML Fits
Teaching emphasis:
- ML is pattern recognition applied to historical data
- It is useful when the output is numerical or categorical

Examples to stress:
- next-month or next-quarter production
- whether a well is likely to underperform
- whether a drilling event looks risky
- whether a site looks more or less attractive for storage screening

Likely question:
- “Do I need huge data for ML?”

Suggested answer:
- “Not always. Bigger is often better, but even moderate datasets can be useful if the problem is scoped well and the data quality is decent.”

### Slide 5: ML Workflow Without The Jargon
Talk track:
“Before we talk algorithms, we need to ask four practical questions: what do we want to predict, what data do we trust, what features matter, and how will we know if the model is useful?”

Whiteboard option:
- draw a simple pipeline from `raw data` to `clean data` to `model` to `decision`

Common pitfall to mention:
- leakage from using future information in training

### Slide 6: Core ML Methods For This Audience
Suggested explanation:
- regression is for predicting a value such as oil rate
- classification is for sorting into classes such as likely underperformer or not
- anomaly detection is useful for unusual wells or behavior
- optimization helps when you need to recommend an action, not just make a forecast

Do not spend time on algorithm names unless asked. Focus on problem types first.

### Slide 7: Role-Specific ML Examples
Delivery tip:
pause briefly on each role so nobody feels left out

Suggested phrasing:
- “If you are in production, think forecasting and surveillance.”
- “If you are in drilling, think risk, performance, and lessons from offsets.”
- “If you are in geoscience, think classification, interpretation support, and cross-well comparison.”
- “If you are in carbon storage, think screening, ranking, and technical documentation.”

### Slide 8: Prescriptive Analytics
Key line:
“Prediction is not the end of the workflow. Technical teams want to know what to do next.”

Use simple examples:
- which wells deserve immediate surveillance
- which drilling settings deserve review
- which storage candidates should move to the next stage

If time is tight:
- mention reinforcement learning only as advanced context

### Slide 9: Transition To GenAI
This is a key transition. Slow down here.

Suggested phrasing:
“ML answers questions like: what number or class do I expect? GenAI answers questions like: how do I work through this problem, find the right documents, generate the analysis code, and explain the answer?”

Important contrast:
- ML is often the prediction engine
- GenAI is often the copilot around the workflow

### Slide 10: GenAI In Energy Is More Than Summarization
Say this explicitly:
“Summarization is the easiest example to show, but it is far from the whole story.”

Examples to emphasize:
- extract facts from drilling reports
- compare two field cases
- generate SQL or Python
- explain model outputs to a wider audience
- build repeatable analysis helpers

### Slide 11: Featured Scenario
Use the production forecasting storyline with confidence.

Suggested script:
“Imagine a production engineer responsible for 18 wells across 3 pads. They need a six-month forecast, need to flag likely underperformers, and need a clean summary of what deserves attention. That is exactly the kind of workflow where ML and GenAI work well together.”

### Slide 12: What ML Does In This Scenario
Emphasize boundaries:
- ML forecasts likely oil rate or underperformance
- ML does not explain the organizational context by itself
- ML does not automatically package the result into a reusable tool

Good line:
“The model gives us the analytical engine. It does not give us the full working system.”

### Slide 13: What GenAI Does In This Scenario
Suggested framing:
“GenAI can help before, during, and after the model.”

Before:
- frame the problem
- suggest features
- write first-pass code

During:
- improve plots
- inspect odd outputs
- suggest checks

After:
- draft engineering notes
- create a reusable notebook structure
- help turn the workflow into a small internal tool

### Slide 14: Live Demo Setup
Keep the demo narrow and controlled. Do not try to impress with too many moving pieces.

Recommended demo steps:
1. explain the scenario in one minute
2. show the dataset columns
3. paste the master prompt
4. ask the model to propose a workflow and code
5. ask for better visuals and an engineering interpretation
6. ask how the notebook could be packaged into a small internal app

Presenter cue:
- if the model output is messy, say “this is exactly why prompt structure and human review matter”

### Slide 15: Practical Limits And Risks
Important tone:
- not fear
- not hype
- practical realism

Suggested phrasing:
“These systems are valuable, but they can absolutely mislead you if the data is poor, the scope is unclear, or the output is accepted without review.”

Mention specifically:
- interventions and workovers can break simple historical assumptions
- production history alone may not capture operational intent
- generated code should be reviewed before trust

### Slide 16: Session 1 Wrap-Up
Closing script:
“If you remember one line from today, let it be this: ML helps us predict. GenAI helps us think through, communicate, and operationalize the work around those predictions.”

Bridge to Session 2:
“In the next session we go all the way into GenAI itself: LLMs, RAG, chatbots, agents, AI coding copilots, and MCP-style tool connectivity.”

## Demo Notes: Production Forecasting Copilot

### Scenario Summary
A production engineer needs a fast, repeatable way to forecast the next six months of oil production for 18 wells across 3 pads and produce a short engineering review.

### Demo Objective
Show that GenAI can support:
- problem framing
- analysis code generation
- plot improvement
- output interpretation
- workflow packaging

### Master Prompt Summary
The master prompt should ask the LLM to:
- frame the business problem
- propose a practical analytical approach
- write Python code
- suggest plots
- interpret results in engineering language
- identify underperforming wells
- propose a notebook or Streamlit packaging approach

### Demo Guardrails
- do not promise that the first model is production-ready
- explain that generated code must be reviewed
- keep the distinction clear between the statistical model and the LLM assistant

## Likely Audience Questions

### “Is this replacing engineers?”
Suggested response:
“No. It is best seen as accelerating repetitive parts of technical work and helping teams reason faster with better structure.”

### “Can GenAI do the forecast itself?”
Suggested response:
“It can help create the forecasting workflow, but the forecast quality still depends on the underlying data and model. The LLM is not automatically the forecasting engine.”

### “Can this work with our internal data?”
Suggested response:
“Yes, if governance, confidentiality, and connectivity are handled properly. That is where enterprise tools, approval workflows, and tool connectivity become important.”

### “How much coding is required?”
Suggested response:
“Very little for this training. The point is to show what is possible and give you enough confidence to begin experimenting.”

## Optional Whiteboard Diagram
Use this if discussion gets abstract:

`Historical data -> ML model -> forecast -> GenAI interpretation -> engineering action`

Then add a second lane:

`Documents and notes -> retrieval -> GenAI -> cited summary or recommendation`

## Session 1 Success Check
At the end, participants should be able to answer:
- When would I use ML?
- When would I use GenAI?
- How can the two work together in a production forecasting workflow?
