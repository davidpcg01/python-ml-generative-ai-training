# Reading List

## How To Use This List
This list is intentionally practical. It is grouped into short, useful readings and resources that support the training themes: core ML, optimization, GenAI, RAG, agents, tooling, and energy-specific applications.

Use the list in three ways:
- read `before or between sessions` for orientation
- use `during preparation` for demos and examples
- use `after the training` for deeper self-study

## Core ML Foundations

### For beginners
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
  A practical reference for regression, classification, preprocessing, and evaluation.

- [Google Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)
  Useful for simple definitions without heavy math.

- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
  Helpful for participants who want to strengthen `pandas`, plotting, and workflow basics.

### Energy-relevant ML ideas
- [Machine Learning of the Equinor Volve Production Data Set](https://sgk2004.github.io/Volve-Dataset/)
  A useful reference point for production-related modeling ideas using an industry-known dataset.

- [Production Data of Tight and Unconventional Reservoirs](https://data.mendeley.com/datasets/5pzzgngw72/1)
  A public dataset source that can support decline-curve and forecasting exercises.

## Optimization Foundations

### Beginner-friendly optimization resources
- [Google OR-Tools Linear Optimization Guide](https://developers.google.com/optimization/lp/lp_example)
  A good starting point for seeing decision variables, objectives, and constraints in code.

- [PuLP Documentation](https://coin-or.github.io/pulp/)
  A lightweight way to start building linear optimization models in Python.

- [Pyomo Documentation](https://pyomo.readthedocs.io/en/stable/)
  Useful once participants want a more structured modeling framework.

- [Gurobi Modeling Examples](https://gurobi.github.io/modeling-examples/)
  Helpful for understanding realistic linear and mixed-integer optimization patterns.

### How to learn linear optimization practically
- Start with a small resource-allocation problem.
- Move next to a routing or scheduling problem.
- Write down:
  - the `decision variables`
  - the `objective function`
  - the `constraints`
- Solve the toy problem first.
- Then add real engineering constraints one at a time.

### Optimization use cases in energy
- `Reservoir and production`: surveillance prioritization, lift allocation, network allocation, intervention ranking
- `Drilling and completions`: rig scheduling, stage sequencing, logistics planning, cost-constrained planning
- `Facilities and operations`: flow routing, storage utilization, transport and supply-chain decisions
- `Carbon and CCS`: source-sink matching, pipeline routing, tie-in decisions, sequestration network economics

### Presenter-linked examples
- `WaterWise`: completions water network optimization
- `SandWise`: proppant logistics optimization
- `FracGenie`: stage-sequence optimization
- `Sequestrix`: CO2 transportation network optimization

### Relevant publication
- [Embedding Existing Pipelines in Design of CO2 Transportation Networks for Optimal Sequestration Economics](https://doi.org/10.2118/214917-PA)
  An SPE Journal paper showing how optimization and graph-based network design can be used in carbon sequestration planning.

## GenAI And LLM Foundations

### Beginner-friendly
- [Generative AI With Large Language Models](https://learn.deeplearning.ai/courses/generative-ai-with-llms/lesson/rs5m7/course-introduction)
  Good conceptual foundation for how LLMs work and where they fit.

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
  Useful for prompt structure, task framing, and output control.

- [Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
  Practical guidance on structured prompting and safer prompt design.

## RAG, Chatbots, And Agents

- [LangChain RAG Concepts](https://python.langchain.com/docs/concepts/rag/)
  A simple reference for retrieval-augmented generation patterns.

- [LangChain Agents Concepts](https://python.langchain.com/docs/concepts/agents/)
  Useful for understanding when and why to use agents.

- [Streamlit Documentation](https://docs.streamlit.io/)
  Helpful for turning notebooks or analysis scripts into lightweight internal tools.

## Tooling And Technical Copilots

- [Cursor](https://www.cursor.com/)
  Reference for AI-assisted coding and workflow prototyping.

- [Anthropic Claude Code Docs](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
  Helpful for understanding AI coding workflows and tool use.

- [OpenAI Codex Overview](https://openai.com/index/introducing-codex/)
  Useful as background on code generation and AI-assisted development.

## Energy-Industry Application Reading

- [Texas Railroad Commission Production Data](https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/production-data/)
  Public source for production data exploration and demo inspiration.

- [Colorado Oil And Gas Well Analytical Data](https://ecmc.colorado.gov/data-maps/downloadable-data-documents/prod-well-download)
  Another public source for field and well-level data exploration.

- [Machine learning provides reconnaissance-type estimates of carbon dioxide storage resources in oil and gas reservoirs](https://pubs.usgs.gov/publication/70266138)
  Useful for showing carbon storage as a meaningful AI/ML application area.

- [Embedding Existing Pipelines in Design of CO2 Transportation Networks for Optimal Sequestration Economics](https://doi.org/10.2118/214917-PA)
  Useful for showing how optimization becomes a practical engineering tool in the carbon and infrastructure planning space.

## Suggested Oil And Gas Papers For Session 1

### Production forecasting and ML
- [Production Forecasting in Conventional Oil Reservoirs Using Deep Learning](https://doi.org/10.2118/209277-MS)
  Useful for showing a modern deep-learning forecasting approach in a conventional reservoir setting.

- [A Data-Driven Approach to Forecasting Production with Applications to Multiple Shale Plays](https://doi.org/10.2118/200365-MS)
  A practical production-forecasting paper with shale-play relevance.

### Well logs and subsurface ML
- [Automated Well-Log Processing and Lithology Classification by Identifying Optimal Features Through Unsupervised and Supervised Machine-Learning Algorithms](https://doi.org/10.2118/202477-PA)
  Good for geoscience and log-interpretation audiences.

- [Machine Learning for Well Log Normalization](https://doi.org/10.2118/196178-MS)
  A useful paper for explaining practical ML in petrophysical data workflows.

### Optimization in oil and gas
- [Large-Scale Deployment of a Closed-Loop Drilling Optimization System: Implementation and Field Results](https://doi.org/10.2118/199601-MS)
  Shows optimization in a drilling workflow with field implementation.

- [Joint Optimization of Well Locations, Types, Drilling Order, and Controls Given a Set of Potential Drilling Paths](https://doi.org/10.2118/193885-PA)
  Strong example of optimization applied to integrated development decisions.

### Carbon and infrastructure optimization
- [Embedding Existing Pipelines in Design of CO2 Transportation Networks for Optimal Sequestration Economics](https://doi.org/10.2118/214917-PA)
  Useful for participants interested in carbon, infrastructure reuse, and source-sink optimization.

## Suggested Practice Reading Between Sessions

### Short list for all participants
- one beginner-friendly ML overview
- one beginner-friendly optimization overview
- one prompt engineering guide
- one energy-use-case example that feels close to your role

### Short list by role
- `Production`: Volve dataset overview plus one optimization example around allocation or surveillance prioritization
- `Drilling`: prompt engineering guide plus the drilling report demo notes
- `Geoscience`: RAG concepts plus the well-log interpretation sample document
- `Carbon`: the SPE sequestration optimization paper plus the carbon screening sample note

## Recommended Internal Reading Prompts
If participants want to learn by doing, ask them to read any technical note and answer:
- What questions could an LLM answer from this document?
- What structured data could be extracted from it?
- Would this use case need plain chat, RAG, or tool connectivity?
- What human review would still be necessary?

## Reading Strategy For The Facilitator
- Do not overwhelm the audience with too much external reading.
- Assign short, high-value pieces between sessions.
- Prefer resources that help participants experiment quickly.
- Use public datasets and examples whenever possible.
