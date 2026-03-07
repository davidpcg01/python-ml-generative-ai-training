# Session 1 Facilitator Notes

## Session Theme
`ML foundations plus a strong GenAI bridge`

This session should feel practical from the first few minutes. The audience should leave believing two things:
- classical ML is useful and understandable
- GenAI is not only for text generation, but can help with real analytical and workflow tasks in energy

## Timing Plan
- `0 to 10 min`: opening and speaker context
- `10 to 35 min`: ML foundations without jargon
- `35 to 65 min`: energy-specific ML use cases, prescriptive modeling, and optimization
- `65 to 85 min`: optimization hands-on demo
- `85 to 110 min`: GenAI bridge and predictive production-forecasting demo
- `110 to 120 min`: risks, reading slide, and wrap-up

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

### Slide 2: About The Presenter
This slide should sound concise, credible, and grounded in real work.

Suggested phrasing:
“I come to this topic from both sides. I have worked as a reservoir engineer and petroleum engineering software developer, and I now work as a staff data scientist building ML, optimization, and GenAI-enabled systems. A lot of what I want to share today comes from problems I have actually seen in production forecasting, reservoir studies, field optimization, and technical tool building.”

Points to highlight:
- current role in data science and AI
- upstream petroleum engineering and reservoir background
- hands-on forecasting and optimization work
- internal software and workflow-building experience
- published work in carbon sequestration optimization

If you want to mention named examples, use:
- `WaterWise`
- `SandWise`
- `FracGenie`
- `Sequestrix`

### Slide 3: Why This Matters Now
Suggested phrasing:
“Most technical teams in energy do not have a shortage of data. They have a shortage of time, attention, and repeatable ways to turn that data into decisions.”

Tie back to audience roles:
- production engineers live in surveillance data, spreadsheets, and performance review loops
- drilling teams live in reports, offsets, lessons learned, and real-time decisions
- geoscientists live in interpretations, logs, technical notes, and uncertainty
- carbon teams live in screening studies, criteria, and documentation

### Slide 4: Three Levels Of Analytics
Use a simple ladder:
- descriptive tells us what happened
- predictive tells us what is likely to happen
- prescriptive suggests what to do

Helpful line:
“Many teams already do descriptive analytics. The step change comes when you move into prediction and then into action support.”

### Slide 5: Where ML Fits
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

### Slide 6: ML Workflow Without The Jargon
Talk track:
“Before we talk algorithms, we need to ask four practical questions: what do we want to predict, what data do we trust, what features matter, and how will we know if the model is useful?”

Whiteboard option:
- draw a simple pipeline from `raw data` to `clean data` to `model` to `decision`

Common pitfall to mention:
- leakage from using future information in training

### Slide 7: Core ML Methods For This Audience
Suggested explanation:
- regression is for predicting a value such as oil rate
- classification is for sorting into classes such as likely underperformer or not
- anomaly detection is useful for unusual wells or behavior
- optimization helps when you need to recommend an action, not just make a forecast

Do not spend time on algorithm names unless asked. Focus on problem types first.

### Slide 8: Role-Specific ML Examples
Delivery tip:
pause briefly on each role so nobody feels left out

Suggested phrasing:
- “If you are in production, think forecasting and surveillance.”
- “If you are in drilling, think risk, performance, and lessons from offsets.”
- “If you are in geoscience, think classification, interpretation support, and cross-well comparison.”
- “If you are in carbon storage, think screening, ranking, and technical documentation.”

### Slide 9: Prescriptive Analytics
Key line:
“Prediction is not the end of the workflow. Technical teams want to know what to do next.”

Use simple examples:
- which wells deserve immediate surveillance
- which drilling settings deserve review
- which storage candidates should move to the next stage

If time is tight:
- mention reinforcement learning only as advanced context

### Slide 10: Optimization In Energy
This is where you should make optimization feel concrete and valuable.

Suggested framing:
“Optimization is one of the most underappreciated tools in petroleum and energy workflows. If ML tells us what is likely to happen, optimization helps us decide what we should do, where we should route, how we should allocate, and how we should schedule under real constraints.”

Use your own examples:
- `WaterWise`: water sourcing, routing, storage, reuse, and capacity constraints across completions operations
- `SandWise`: proppant supply-chain optimization under cost and logistics constraints
- `FracGenie`: stage-sequence and scheduling optimization for completions
- `Sequestrix`: CO2 transport network optimization, source-sink matching, and pipeline reuse in sequestration planning

Good line:
“A lot of engineers think optimization is abstract math. In practice, it often becomes a very operational question: what is the best feasible plan given the constraints we actually face?”

Useful energy examples to mention:
- production routing and allocation
- well prioritization for surveillance or intervention
- artificial lift or operating setting selection
- infrastructure siting and transport routing
- carbon capture and sequestration network design
- scheduling problems in drilling and completions

### Slide 11: Practical Path To Learning Linear Optimization
Keep this encouraging and accessible.

Suggested script:
“You do not need to start with advanced operations research. Start by learning to translate a problem into decision variables, an objective, and constraints.”

Practical learning sequence:
1. identify the decision you control
2. define the objective you want to maximize or minimize
3. write down the constraints that must be respected
4. build a tiny example in `Excel Solver` or Python
5. expand from linear optimization to integer or mixed-integer versions when choices become discrete

Suggested tools to mention:
- `Excel Solver` for first exposure
- `PuLP` or `Pyomo` for Python modeling
- `OR-Tools` for practical open-source workflows
- `Gurobi` for more advanced MILP problems

Key message:
- linear optimization is often the easiest useful entry point because many engineering allocation, routing, and scheduling problems can be approximated that way

### Slide 12: Optimization Demo Step By Step
This is the moment to make optimization feel operational and concrete.

Suggested framing:
“Now let me show you what this looks like in practice. We are going to solve a small water-allocation problem that mirrors the structure of real completions water management.”

Walk them through:
1. the business problem
2. the input CSVs
3. the decision variables
4. the objective function
5. the constraints
6. the solver output
7. one scenario sensitivity change

Important point:
- keep the language operational
- do not overemphasize the algebra

Demo artifact to use:
- `training/hands-on/optimization-waterwise-demo.py`
- or `training/hands-on/notebook-optimization-waterwise.ipynb`

Suggested scenario tweaks live:
- reduce one route capacity
- tighten the freshwater cap
- increase the produced-water reuse target

### Slide 13: Transition To GenAI
This is a key transition. Slow down here.

Suggested phrasing:
“ML answers questions like: what number or class do I expect? GenAI answers questions like: how do I work through this problem, find the right documents, generate the analysis code, and explain the answer?”

Important contrast:
- ML is often the prediction engine
- GenAI is often the copilot around the workflow

### Slide 14: GenAI In Energy Is More Than Summarization
Say this explicitly:
“Summarization is the easiest example to show, but it is far from the whole story.”

Examples to emphasize:
- extract facts from drilling reports
- compare two field cases
- generate SQL or Python
- explain model outputs to a wider audience
- build repeatable analysis helpers

### Slide 15: Featured Scenario
Use the production forecasting storyline with confidence.

Suggested script:
“Imagine a production engineer responsible for 18 wells across 3 pads. They need a six-month forecast, need to flag likely underperformers, and need a clean summary of what deserves attention. That is exactly the kind of workflow where ML and GenAI work well together.”

### Slide 16: What ML Does In This Scenario
Emphasize boundaries:
- ML forecasts likely oil rate or underperformance
- ML does not explain the organizational context by itself
- ML does not automatically package the result into a reusable tool

Good line:
“The model gives us the analytical engine. It does not give us the full working system.”

### Slide 17: What GenAI Does In This Scenario
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

### Slide 18: Predictive Demo Step By Step
Now the audience has seen optimization. This demo should show the predictive side plus the GenAI copilot layer.

Recommended flow:
1. explain the production-forecasting scenario
2. show the dataset columns
3. run the simple notebook model
4. show forecast metrics and sample well plots
5. discuss which wells deserve surveillance
6. paste the master prompt
7. ask the LLM to propose or improve the workflow
8. ask for better visuals and engineering interpretation
9. ask how the workflow could be packaged into a small internal app

Demo assets to use:
- `training/hands-on/notebook-ml-basics.ipynb`
- `training/hands-on/production-forecasting-demo.md`

Presenter cue:
- if the model output is messy, say “this is exactly why prompt structure and human review matter”
- keep reinforcing what the statistical model did versus what the LLM added

### Slide 19: Practical Limits And Risks
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

### Slide 20: Suggested Paper Reading
This slide should be presented as a curated starting point.

Suggested phrasing:
“Some of you will want to go deeper after this session. These papers are a good starting set because they connect directly to real oil and gas use cases across forecasting, well logs, drilling optimization, and carbon-related infrastructure planning.”

How to position the list:
- do not read every title in detail
- highlight one or two that best match the audience in the room
- point participants to the full reading list in the training package

Suggested emphasis by topic:
- `Production forecasting`: deep learning and shale-play forecasting papers
- `Subsurface ML`: lithology classification and well-log normalization
- `Optimization`: drilling optimization and joint field development optimization
- `Carbon optimization`: your SPE Journal paper as an example of optimization applied to transport-network economics

### Slide 21: Session 1 Wrap-Up
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

### “What kinds of optimization problems should petroleum engineers learn first?”
Suggested response:
“Start with allocation, routing, and scheduling problems. Those are usually the clearest. For example: which wells to prioritize, how to route water or CO2, how to allocate scarce capacity, or how to schedule operations under limits.”

### “Do I need advanced math to use optimization?”
Suggested response:
“You need structured thinking more than advanced math at the start. If you can define a decision, an objective, and a set of constraints, you can already begin modeling useful optimization problems.”

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
