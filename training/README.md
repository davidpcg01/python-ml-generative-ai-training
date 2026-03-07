# Energy Industry AI Training

## Overview
This training is a two-session, beginner-to-intermediate program for petroleum engineers and geoscientists. It is designed to move participants from core machine learning concepts into practical generative AI applications that are directly relevant to upstream oil and gas, subsurface workflows, and carbon storage.

The tone of the training should be practical, role-aware, and confidence-building. The goal is not to make participants into data scientists in two hours. The goal is to help them understand what modern AI can do, where it fits in their work, how to use it responsibly, and how to begin experimenting on their own.

## Audience
Primary audience:
- Petroleum engineers with production, reservoir, and drilling backgrounds
- Geoscientists working in interpretation, well logs, and subsurface evaluation
- Technical professionals interested in carbon capture and sequestration workflows

Assumed starting point:
- Comfortable with engineering decision-making and domain terminology
- Limited or mixed exposure to ML and GenAI
- Some participants may code lightly in Python, but many will not

## Training Design Principles
- Start with intuition before technical detail.
- Use energy-specific examples, not generic retail or finance examples.
- Explain each concept at three levels: `what it is`, `where it works`, `how to try it`.
- Keep coding optional and lightweight.
- Show both `what AI can do well` and `what needs engineering judgment`.
- Make Session 1 useful on its own, while building momentum into Session 2.

## Learning Arc
The training follows a deliberate progression:

1. Session 1 introduces predictive ML and prescriptive thinking, then quickly pivots into richer GenAI use cases.
2. Between sessions, participants try lightweight prompts and optional notebooks.
3. Session 2 focuses fully on GenAI, LLMs, RAG, agents, AI coding copilots, and MCP-style tool connectivity.

## Session Timing
Each session runs for `60 minutes`.

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
- It shows where ML is the numerical engine.
- It also shows how GenAI can help frame the problem, write analysis code, inspect outputs, generate visuals, explain results, and package the workflow into something reusable.

This storyline should be referenced in both sessions:
- Session 1: GenAI-assisted production forecasting workflow
- Session 2: how the same workflow can evolve into a chatbot, tool-using agent, or internal app

## Delivery Stack
Recommended live delivery stack:
- Slides in Markdown or converted to PowerPoint/Google Slides
- Jupyter or Colab notebooks for ML and GenAI demos
- One LLM tool for prompting and workflow generation
- Optional AI coding copilot demo in `Cursor`, `Claude Code`, or `Codex`

## Materials In This Package
- `training/session-1-slides.md`
- `training/session-1-facilitator-notes.md`
- `training/session-2-slides.md`
- `training/session-2-facilitator-notes.md`
- `training/hands-on/notebook-ml-basics.ipynb`
- `training/hands-on/notebook-genai-rag.ipynb`
- `training/hands-on/production-forecasting-demo.md`
- `training/sample-data/production_forecasting/`
- `training/participant-workbook.md`
- `training/reading-list.md`

## Suggested Delivery Style
- Use analogies and role-specific examples.
- Ask short reflection questions during transitions.
- Keep formulas optional and secondary.
- Treat the LLM as a practical technical copilot, not as magic.
- Clearly separate:
  - what the model predicts
  - what the engineer decides
  - what GenAI can automate or accelerate

## Practical Setup
Minimum setup for the facilitator:
- Python environment with `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn`
- Internet access for live LLM demos, if allowed
- Backup screenshots in case live prompting is unreliable

Minimum setup for participants:
- No coding required for core participation
- Optional access to Colab or Jupyter for self-study
- Optional access to an LLM interface for prompting exercises

## Success Criteria
The training is successful if participants can:
- name several high-value AI use cases in their discipline
- explain the difference between ML, optimization, and GenAI
- complete at least one small ML exercise and one GenAI exercise
- describe where chatbots or agents would fit into a technical energy workflow
- identify one workflow in their own job that is ready for experimentation
