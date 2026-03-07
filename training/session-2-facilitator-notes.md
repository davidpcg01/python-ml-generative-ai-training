# Session 2 Facilitator Notes

## Session Theme
`All GenAI for energy workflows`

This session should feel like the exciting payoff. Participants should leave with a practical understanding of LLMs, RAG, chatbots, agents, AI coding copilots, and MCP-style tool connectivity, along with a clear sense of where these tools fit in technical energy workflows.

## Timing Plan
- `0 to 5 min`: recap and reset
- `5 to 20 min`: LLM concepts in plain English
- `20 to 35 min`: RAG, chatbots, and grounded answers
- `35 to 50 min`: agents, tools, coding copilots, MCP-style connectivity
- `50 to 60 min`: hands-on prompt lab, guardrails, and close

## Speaker Posture
- Keep the energy high, but avoid hype.
- Translate software terms into engineering value.
- Always connect architecture back to a real technical workflow.
- Stress that grounded, tool-connected systems are more useful than generic chat alone.

## Slide-By-Slide Notes

### Slide 1: Title
Opening line:
“Today we go fully into generative AI: how these systems work, what they can do in technical energy settings, and what modern tools make possible.”

### Slide 2: Quick Recap From Session 1
Use this as a mental reset:
- ML predicts and optimizes
- GenAI works with language, context, code, and workflow assembly
- the strongest results often combine the two

Suggested bridge:
“Session 1 showed a production forecasting copilot. Session 2 shows the broader ecosystem around that idea.”

### Slide 3: What An LLM Actually Is
Keep the explanation simple and calm.

Suggested phrasing:
“At a basic level, an LLM is a very strong pattern model for language. It predicts likely next tokens and can therefore rewrite, explain, compare, structure, and generate language or code.”

Important clarification:
- it does not inherently know your field data
- it is not automatically grounded in your internal documents
- it should not be treated as a source of truth

### Slide 4: Important Concepts In Plain English
Define each term with one sentence:
- tokens: small chunks of text the model processes
- context window: how much information it can hold in working memory
- hallucination: confident output that is unsupported or wrong
- embeddings: numerical representations used to compare meaning
- retrieval: bringing relevant source material into the model context
- tool use: calling external systems to fetch or compute something

Tip:
- avoid going deep into transformer mechanics unless asked

### Slide 5: High-Value GenAI Use Cases In Energy
Keep this role-specific.

Examples to mention:
- drilling: extract lessons learned from daily reports
- production: draft surveillance summaries and compare wells
- geoscience: search interpretation notes and compare formations
- carbon storage: draft screening summaries and compare candidate sites
- technical analysis: generate Python or SQL and package workflows

### Slide 6: Why Raw Chat Is Not Enough
Strong line:
“A generic chatbot can help you think, but it is usually not enough for technical work that needs evidence, access to specific data, or repeatable steps.”

Explain what is missing:
- grounding
- citations
- enterprise context
- reproducibility

### Slide 7: RAG In One Picture
Teach this as a workflow, not a buzzword.

Suggested phrasing:
“RAG means the system does not rely only on model memory. It retrieves relevant documents first, then answers based on that evidence.”

Use the phrase:
- `better than raw chat`
- `still requires source quality and human review`

### Slide 8: Chatbots For Technical Teams
Frame chatbots as interfaces, not magic.

What a useful technical chatbot should do:
- answer within a known domain
- cite source material
- admit uncertainty
- avoid pretending to know what it cannot verify

Ask the room:
- “If you had one internal technical chatbot tomorrow, what would you want it to know?”

### Slide 9: Agents And Tool Use
Suggested explanation:
“An agent is useful when a task needs multiple steps. It might retrieve a document, pull a table, run a calculation, and then draft a result.”

Important nuance:
- not every workflow needs an agent
- simple workflows are often better than complex autonomous ones

### Slide 10: MCP-Style Connectivity
Keep it plain:
“Think of MCP-style connectivity as structured plumbing between the model and useful tools.”

Translate into business value:
- safer tool access
- cleaner integrations
- more repeatable workflows
- less isolated chatting

Energy examples:
- connect to a document store
- connect to a production table
- connect to a calculation service
- connect to a plotting or reporting tool

### Slide 11: Modern Tooling Landscape
Make the categories feel concrete.

Suggested grouping:
- chat tools for ideation and drafting
- coding copilots for scripts, notebooks, and internal helpers
- RAG apps for grounded answers over documents
- agents for multi-step tool-connected workflows

### Slide 12: Why These Tools Matter For Engineers And Geoscientists
This slide is where you normalize tool use for non-software teams.

Suggested phrasing:
“You do not need to be a software engineer to benefit from tools like Cursor, Claude Code, or Codex. These tools can help you create the glue code and reusable artifacts that technical teams often never quite have time to build.”

Examples:
- a data-cleaning script
- a forecast review notebook
- a well-ranking dashboard
- a document comparison helper

### Slide 13: Revisit The Production Forecasting Copilot
Bring the audience back to a familiar anchor.

Message:
- the same workflow can evolve from a one-off analysis into:
  - a notebook template
  - a Streamlit app
  - a retrieval-based assistant
  - a tool-connected agent with approvals

### Slide 14: Example Agentic Energy Workflow
Use a realistic example:
- the user asks which wells may miss plan next quarter
- the system retrieves production data and notes
- the system runs a calculation or calls a model
- the system drafts a ranked summary with reasons and cautions

Important teaching line:
“The agent is not valuable because it is autonomous. It is valuable because it can connect useful steps in a traceable way.”

### Slide 15: Hands-On Lab
Recommended live structure:
1. show a weak prompt
2. show a structured prompt
3. compare results
4. optionally show a tiny RAG or copilot workflow

If time is short:
- focus on one good prompt engineering example plus one architecture sketch

### Slide 16: Guardrails And Governance
Be direct here. Technical audiences usually appreciate candor.

Key points:
- do not paste confidential data into tools without approval
- require citations where possible
- review outputs before action
- keep a human accountable for decisions
- use narrow pilots before wider deployment

### Slide 17: Practical Adoption Roadmap
Suggested phrasing:
“Do not start with the most autonomous, complex idea. Start where the value is obvious and the risk is manageable.”

Recommended path:
1. prompting and copilots
2. grounded search and extraction
3. reusable internal helpers
4. tool-connected agents in narrow workflows

### Slide 18: Close
Closing script:
“GenAI is not just a writing tool. In the right setup, it becomes a technical copilot, a workflow builder, and a front end to useful tools and data. The domain expertise in this room is what makes it valuable.”

## Demo Notes

### Demo Option A: Prompt Engineering
Use a short drilling, reservoir, or carbon document excerpt.

Show:
- a vague prompt
- a structured extraction prompt
- a comparison prompt
- a recommendation-drafting prompt

### Demo Option B: Small RAG Walkthrough
Use a handful of small technical documents.

Show:
- a plain question
- retrieval of relevant excerpts
- answer with citations

### Demo Option C: AI Coding Copilot Walkthrough
Use `Cursor`, `Claude Code`, or `Codex` to show how a small internal helper might be generated.

Good example:
- turn a notebook idea into a small app skeleton for production forecasting review

Key message:
- these tools matter because they reduce the time needed to build useful internal workflow support

## Likely Audience Questions

### “Is RAG just search?”
Suggested response:
“It includes search, but the point is to retrieve relevant context and then let the model answer with that context in mind.”

### “Do we need agents for everything?”
Suggested response:
“No. Many good solutions are just structured prompts, retrieval, and a small amount of tool use. Agents are best when the workflow truly has multiple connected steps.”

### “What is the difference between Cursor, Claude Code, and Codex?”
Suggested response:
“Think of them as AI coding copilots that help create and refine technical artifacts such as scripts, notebooks, and small tools. The important point for this training is what they enable, not which brand wins.”

### “How should we start in our organization?”
Suggested response:
“Start with low-risk, document-heavy, repetitive workflows where the outputs can be reviewed. That gives you a fast path to learning and a safer path to value.”

## Optional Whiteboard Diagram
Draw three levels:

`Chat -> RAG -> Tool-connected agent`

Then underneath each, write:
- chat: useful for ideation
- RAG: useful for grounded answers
- agent: useful for multi-step workflows

## Session 2 Success Check
At the end, participants should be able to answer:
- what an LLM is in plain English
- why grounded systems beat raw chat for technical work
- where tools like `Cursor`, `Claude Code`, `Codex`, and MCP-style integrations fit
- how to start safely in their own workflows
