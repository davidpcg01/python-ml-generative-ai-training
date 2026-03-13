# Training Package Guide

## Start Here
This folder is organized so students can move through the course in session order while still finding shared demos, setup instructions, and data in predictable places.

## Session 1
- Start with `sessions/session-1/session-1-slides.md`
- Use `sessions/session-1/From-ML-To-GenAI-In-Energy-Session-1-Final.pdf` if you prefer the exported deck
- Run `sessions/session-1/notebook-ml-basics.ipynb`
- Follow the optimization case in `demos/optimization-waterwise/README.md`
- Use the production forecasting case in `demos/production-forecasting/README.md` as the main predictive workflow example

## Session 2
- Start with `sessions/session-2/session-2-slides.md`
- Use `sessions/session-2/From-ML-To-GenAI-In-Energy-Session-2-Final.pdf` if you prefer the exported deck
- Run `sessions/session-2/notebook-genai-rag.ipynb`
- Continue with `demos/production-forecasting/README.md` for the forecasting copilot storyline
- Use `setup/colab/production-forecasting-colab-guide.md` or `setup/local/production-forecasting-local-setup.md` to run the forecasting demo

## Folder Guide
- `sessions/`: session decks, facilitator notes, PDFs, and session-specific notebooks
- `demos/`: the two main case studies, grouped by workflow instead of file type
- `data/`: all shared datasets, data dictionaries, and technical documents
- `setup/`: local and Colab instructions plus shared Python requirements
- `resources/`: optional reading and supporting materials

## Recommended Student Flow
1. Read the slide deck for the session you are in.
2. Run the session notebook.
3. Open the matching demo folder and read its `README.md`.
4. Review the relevant files in `data/`.
5. Use the setup guides only when you need to run a notebook locally or in Colab.
