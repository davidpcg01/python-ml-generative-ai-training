# Session 2 Slides

## Session Goal
Session 2 focuses on GenAI, LLMs, chatbots, agents, and tools for technical energy workflows.

## Slide 1: Title
`GenAI, LLMs, Chatbots, Agents, And Tools For Energy`

- The focus is on turning AI from an interesting concept into a practical technical workflow assistant.

## Slide 2: Instructor Background
`Why I Am Teaching This`

- `David Nnamdi`
- Staff Data Scientist at `Intuit`
- Former `Reservoir Engineer` with hands-on work in `production forecasting`, reserves evaluation, reservoir studies, and field optimization
- Built internal tools and optimization products including `WaterWise`, `SandWise`, `FracGenie`, and `Sequestrix`
- Experience across `petroleum engineering`, `analytics`, `optimization`, `ML`, and `GenAI-enabled` workflow building
- SPE Journal author on `CO2 transportation network optimization`

Links:
- [LinkedIn](https://www.linkedin.com/in/david-nnamdi/)
- [GitHub](https://github.com/davidpcg01)
- [Google Scholar](https://scholar.google.com/citations?user=Qfo5LYcAAAAJ)

## Slide 3: Quick Recap From Session 1
- ML predicts and optimizes
- GenAI works with language, context, code, and workflow support
- the combination is often where real value appears

This session focuses on the GenAI side of that combination.

## Slide 4: What An LLM Actually Is
- an LLM predicts likely next tokens based on patterns learned from large text corpora
- it is strong at language, pattern completion, restructuring information, and generating code or explanations
- it is not a reservoir simulator, historian, or source of truth by itself

## Slide 5: Important Concepts In Plain English
Terms to know:
- tokens
- context window
- hallucination
- embeddings
- retrieval
- function calling or tool use

## Slide 6: High-Value GenAI Use Cases In Energy
- search and Q&A over technical reports
- structured extraction from drilling reports and lessons learned
- comparison across offset wells or field cases
- engineering summary drafting
- well-log interpretation support
- carbon storage screening memo support
- analysis copilot for notebooks, SQL, and internal tools

## Slide 7: Why Raw Chat Is Not Enough
- basic chat can be useful, but it often lacks grounding, citations, and access to enterprise data

Important additions:
- retrieval
- tools
- workflow structure
- human review

## Slide 8: RAG In One Picture
1. user asks a question
2. system retrieves relevant documents
3. model answers using retrieved context
4. answer cites sources

Energy examples:
- drilling procedures
- reservoir review notes
- well-log interpretation memos
- carbon storage screening documents

## Slide 9: Chatbots For Technical Teams
A good technical chatbot should:
- search the right documents
- answer with traceable evidence
- stay within scope
- expose uncertainty
- escalate when the answer requires human judgment

## Slide 10: Agents And Tool Use
- agents are useful when the work involves multiple steps, decisions, or tools

Example workflow:
- retrieve documents
- query a table
- run a simple calculation
- generate a recommendation draft
- ask for human approval

## Slide 11: MCP-Style Connectivity
- MCP-style connectivity is a way for LLM systems to connect to tools, files, databases, APIs, and internal services in a more structured way

Why it matters:
- the LLM becomes more than a chatbot
- it can act on real enterprise context
- it supports tool-based workflows instead of isolated answers

## Slide 12: Modern Tooling Landscape
Main categories:
- chat assistants
- AI coding copilots
- RAG applications
- domain copilots
- tool-using agents

Examples:
- `Cursor`
- `Claude Code`
- `Codex`

## Slide 13: Why These Tools Matter For Engineers And Geoscientists
- write quick Python for analysis
- generate SQL for data pulls
- clean messy tables
- create notebooks faster
- build internal helpers and dashboards
- prototype technical workflow tools without waiting for a full software project

## Slide 14: Revisit The Production Forecasting Copilot
- In Session 1, GenAI was used around one forecasting workflow.
- The same concept can expand into a reusable app, chatbot, or tool-using agent.

## Slide 15: Example Agentic Energy Workflow
Scenario:
- a user asks which wells are most likely to miss plan next quarter
- the system retrieves production data and surveillance notes
- the model runs analysis or calls a tool
- the model drafts a ranked summary with evidence and cautions

Lesson:
- useful agents combine retrieval, calculation, and explanation

## Slide 16: Hands-On Lab
Options:
- prompt engineering on technical document excerpts
- simple RAG over a small document set
- AI copilot walkthrough that builds a small internal helper

## Slide 17: Guardrails And Governance
Critical points:
- confidentiality and IP
- citations and evidence
- auditability
- approval workflows
- data quality and scope control
- human accountability

## Slide 18: Practical Adoption Roadmap
1. start with low-risk copilots
2. move to grounded search and extraction
3. introduce tool-connected workflows
4. pilot agents in narrow, reviewable processes

## Slide 19: Close
- GenAI is not only for writing text
- it can support technical reasoning, analysis, tool use, and workflow creation
- the strongest outcomes happen when domain expertise stays in the loop
