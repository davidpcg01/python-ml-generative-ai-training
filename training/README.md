# Energy Industry AI Training

## Overview
This package is a two-session, beginner-to-intermediate introduction to AI for petroleum engineers, geoscientists, and other technical energy professionals. It moves from core machine learning concepts into practical generative AI applications that are relevant to upstream oil and gas, subsurface workflows, and carbon storage.

The material is practical and role-aware. The goal is to help you understand what modern AI can do, where it fits in technical work, how to use it responsibly, and how to start experimenting on your own.

## Audience
Primary audience:
- Petroleum engineers with production, reservoir, and drilling backgrounds
- Geoscientists working in interpretation, well logs, and subsurface evaluation
- Technical professionals interested in carbon capture and sequestration workflows

Assumed starting point:
- Comfortable with engineering decision-making and domain terminology
- Limited or mixed exposure to ML and GenAI
- Some learners may code lightly in Python, but many will not

## Learning Arc
The material follows this progression:
1. Session 1 introduces predictive ML and prescriptive thinking, then pivots into practical GenAI use cases.
2. The hands-on notebooks and prompts let you try the ideas directly.
3. Session 2 focuses on GenAI, LLMs, RAG, agents, AI coding copilots, and tool connectivity.

## Session Timing
Each session now runs for `120 minutes`.

### Session 1
Theme: `ML foundations plus a strong GenAI bridge`

Outcomes:
- Distinguish descriptive, predictive, and prescriptive analytics.
- Understand core ML workflow ideas such as targets, features, validation, and overfitting.
- Map ML techniques to reservoir, production, drilling, geoscience, and carbon storage problems.
- Understand when to use ML versus GenAI.
- See GenAI used for more than summarization, including analysis support and workflow building.

### Session 2
Theme: `All GenAI for energy workflows`

Outcomes:
- Explain what LLMs are in plain English.
- Understand RAG, chatbots, agents, tool use, and MCP-style connectivity.
- See how modern tools such as `Cursor`, `Claude Code`, and `Codex` support technical work.
- Understand how GenAI can support document-heavy and analysis-heavy workflows in energy.
- Learn practical guardrails around hallucination, governance, and human review.

## Core Energy Use Cases
The training will repeatedly anchor back to these examples:

### Reservoir And Production
- Production forecasting
- Underperforming well identification
- Artificial lift optimization support
- Water cut and surveillance review

### Drilling
- Nonproductive time screening
- ROP prediction support
- Stuck-pipe risk framing
- Lessons-learned extraction from drilling reports

### Geoscience And Well Logs
- Facies or lithology classification
- Well-log interpretation support
- Cross-well note comparison
- Subsurface document search and Q&A

### Carbon Capture And Storage
- Site screening
- Storage capacity estimation support
- Candidate ranking
- Documentation and screening summary assistants

## Featured Demo Storyline
The primary running example is a `production forecasting copilot`.

Why this works well:
- It is familiar to petroleum engineers.
- It now uses a compact official BSEE offshore completion subset with regulator-backed monthly production rather than a synthetic field example.
- It shows where `Arps hyperbolic decline`, a multivariate `RandomForestRegressor`, `Exponential Smoothing`, and `ARIMA` act as the numerical engines.
- It also shows how GenAI can help frame the problem, write analysis code, inspect outputs, generate visuals, explain results, and package the workflow into something reusable.

This storyline appears in both sessions:
- Session 1: GenAI-assisted production forecasting workflow
- Session 2: how the same workflow can evolve into a chatbot, tool-using agent, or internal app

## Additional Hands-On Optimization Demo
Because the sessions are now longer, the package also includes a simple optimization case study inspired by completions water management.

Why this matters:
- it gives petroleum engineers a concrete prescriptive-analytics example
- it shows how linear optimization differs from ML
- it provides a practical bridge into larger optimization products such as `WaterWise`, `SandWise`, `FracGenie`, and `Sequestrix`

## Materials In This Package
- `training/session-1-slides.md`
- `training/session-2-slides.md`
- `training/hands-on/notebook-ml-basics.ipynb`
- `training/hands-on/production-forecasting-demo.ipynb`
- `training/hands-on/notebook-genai-rag.ipynb`
- `training/hands-on/production-forecasting-demo.md`
- `training/hands-on/production-forecasting-colab-guide.md`
- `training/hands-on/production-forecasting-local-setup.md`
- `training/hands-on/notebook-optimization-waterwise.ipynb`
- `training/hands-on/optimization-waterwise-demo.py`
- `training/hands-on/optimization-waterwise-demo.md`
- `training/sample-data/production_forecasting/`
- `training/sample-data/optimization_waterwise/`
- `training/reading-list.md`

## How To Use This Package
- Read the session slide files for the conceptual overview.
- Use the notebooks and setup guides for hands-on practice.
- Review the sample-data folders and data dictionaries before running the exercises.
- Use the standalone `Cursor` exercise repo if you want the AI-assisted coding workflow: `https://github.com/davidpcg01/hands-on-ml-cursor`
- Use the reading list for optional follow-up study.

## Practical Setup
- No coding is required to read the materials.
- Optional access to `Colab` or `Jupyter` is helpful for the notebook exercises.
- Optional access to the free version of `Cursor` is helpful if you also want to complete the separate `hands-on-ml-cursor` exercise.
- If you want to run everything locally, install the Python packages listed in `training/requirements.txt`.

## What You Should Be Able To Do
After working through the package, you should be able to:
- name several high-value AI use cases in your discipline
- explain the difference between ML, optimization, and GenAI
- complete at least one small ML exercise and one GenAI exercise
- describe where chatbots or agents would fit into a technical energy workflow
- identify one workflow in your own job that is ready for experimentation
