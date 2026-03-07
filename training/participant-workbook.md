# Participant Workbook

## How To Use This Workbook
This workbook supports both sessions of the training. It is designed for participants who want to follow the sessions live, reflect on their own workflows, and try a few practical exercises between sessions.

You do not need to code to benefit from the training. If you do have access to Python or a notebook environment, optional exercises are included.

## Session 1 Worksheet

### Part A: AI In Your Workflow
Write down one example from your current work for each category:

- `Descriptive`: what happened?
- `Predictive`: what is likely to happen?
- `Prescriptive`: what should we do next?

### Part B: ML Or GenAI?
For each task below, decide whether it is mostly an `ML` problem, a `GenAI` problem, or a `combined` problem.

- Forecast next-month oil rate for a well
- Compare two drilling reports and summarize key lessons learned
- Rank storage candidates based on tabular screening variables
- Explain why a forecasted well may underperform
- Draft a technical summary after a production review
- Build a repeatable notebook that forecasts wells and explains the results

### Part C: Production Forecasting Copilot Reflection
After the Session 1 demo, answer:

1. What part of the workflow was handled by the ML model?
2. What part of the workflow was accelerated by GenAI?
3. Which parts would still need engineering review before action?
4. If you were to adapt this to your team, what data would you need?

## Optional Session 1 Practice

### Option 1: No-Code Prompt Exercise
Use the production forecasting scenario and ask an LLM to:
- frame the problem
- propose a simple analytical approach
- list the data-quality checks it would perform
- suggest three useful plots

Reflection:
- Was the output practical?
- What did the model miss?
- How would you improve the prompt?

### Option 2: Notebook Exercise
Open `training/hands-on/notebook-ml-basics.ipynb` and work through:
- loading the synthetic data
- training the simple model
- reviewing the plots
- identifying wells that deserve surveillance

## Between-Session Practice
Suggested total time: `20 to 40 minutes`

### Required Reflection
Write a short answer to this question:

`Which part of your current workflow is repetitive, document-heavy, and suitable for AI assistance?`

### Practice Task
Choose one of the following:

- `Reservoir/production`: compare a production-prediction task with an LLM-based summary or extraction task
- `Drilling`: extract action items and lessons learned from a drilling report excerpt
- `Geoscience`: compare two interpretation notes and identify key differences
- `Carbon`: draft a site-screening summary from a structured note

### Bring To Session 2
Bring one of the following:
- a domain workflow you want to improve
- a technical question you want to ask a chatbot
- a sample document type you think would benefit from retrieval or extraction

## Session 2 Worksheet

### Part A: LLM Vocabulary Check
Write a one-sentence explanation of each term:
- token
- context window
- hallucination
- retrieval
- tool use
- agent

### Part B: Prompt Improvement
Below is a weak prompt:

`Summarize this drilling report and tell me what to do.`

Improve it by making it:
- more specific
- grounded in a role
- structured in output
- safer and more reviewable

### Part C: Architecture Choice
For each task below, choose the best starting pattern:
- `chat`
- `RAG`
- `tool-connected workflow`
- `agent`

Tasks:
- answer questions over internal drilling procedures
- compare surveillance notes across wells
- generate SQL to pull production data
- run a small calculation and draft a recommendation
- build a reusable internal helper for monthly forecast review

## Optional Session 2 Practice

### RAG Exercise
Open `training/hands-on/notebook-genai-rag.ipynb` and:
- run a query against the sample technical docs
- inspect the retrieved sources
- build a grounded prompt
- paste the prompt into your preferred LLM

### Copilot Exercise
Ask an AI coding copilot to help you create one of these:
- a simple data-cleaning script
- a small plotting helper
- a notebook template for technical review
- a mock internal app layout for an engineering workflow

## Personal Action Plan
Before leaving the training, complete these sentences:

1. `One workflow I want to test with AI is...`
2. `The first low-risk use case I would try is...`
3. `The main guardrail I need to respect is...`
4. `The tool or approach I want to explore next is...`

## Recommended Working Style After The Training
- Start with narrow, low-risk use cases.
- Prefer workflows where outputs can be reviewed.
- Keep one subject-matter expert in the loop.
- Save prompts, templates, and notebook structures that work.
- Treat early experiments as learning exercises, not final systems.
