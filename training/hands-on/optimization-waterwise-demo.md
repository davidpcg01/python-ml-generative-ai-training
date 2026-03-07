# Optimization WaterWise Demo

## Purpose
This is a simple, workshop-friendly optimization case study inspired by completions water management in upstream oil and gas. It is designed for a longer session where participants can see optimization framed as a practical engineering tool rather than abstract mathematics.

## Why This Case Works
- It is easy to explain in operational language.
- It maps cleanly to linear optimization.
- The outputs are intuitive: where should water come from, where should it go, and how much should be allocated?
- It opens the door to broader discussions around `WaterWise`, `SandWise`, logistics, routing, scheduling, and CCS network design.

## Scenario
A completions team must supply water to three frac pads:
- `Pad_A`
- `Pad_B`
- `Pad_C`

Water can come from:
- produced water sources
- a brackish source
- a limited freshwater backup source

Each source has:
- a finite supply
- a source cost
- route-specific transport capacities and costs to each pad

Business constraints:
- total freshwater use must stay below a cap
- produced water reuse must exceed a minimum target
- each pad's demand should be satisfied if feasible
- unmet demand is allowed only through a very high shortage penalty

## Optimization Question
What is the lowest-cost feasible water-allocation plan that:
- meets pad demand
- respects source supply limits
- respects route capacities
- limits freshwater use
- encourages produced-water reuse

## Files
- `training/sample-data/optimization_waterwise/water_sources.csv`
- `training/sample-data/optimization_waterwise/demand_pads.csv`
- `training/sample-data/optimization_waterwise/transport_links.csv`
- `training/sample-data/optimization_waterwise/scenario_parameters.csv`
- `training/hands-on/optimization-waterwise-demo.py`
- `training/hands-on/notebook-optimization-waterwise.ipynb`

## Teaching Objectives
Participants should leave understanding:
- what `decision variables`, `objective`, and `constraints` mean
- how a real engineering problem becomes a linear optimization model
- why optimization is valuable in water, sand, logistics, scheduling, and carbon workflows

## Suggested Live Demo Flow
1. Explain the scenario in business language.
2. Show the four CSVs and talk through the data structure.
3. Define the optimization problem:
   - decision variables
   - objective function
   - constraints
4. Run the Python script or notebook.
5. Review the optimal allocations and engineering interpretation.
6. Ask what would change if:
   - freshwater cap became tighter
   - produced water reuse target increased
   - one route lost capacity
   - pad demand changed

## Engineering Translation
Frame the model like this:

- `Decision variables`: how many barrels to send from each source to each pad
- `Objective`: minimize total water supply and transport cost, plus any shortage penalty
- `Constraints`: supply limits, route limits, pad demand, freshwater cap, produced-water reuse target

## How To Run

From the repo root:

```bash
python3 "training/hands-on/optimization-waterwise-demo.py"
```

The script:
- solves the linear program with `PuLP`
- prints the optimal cost and allocation summaries
- writes result CSVs to:
  - `training/hands-on/results/optimization_waterwise/`

## Discussion Questions
- Why is this a better fit for optimization than for ML?
- Which variables are decisions, and which are inputs?
- What trade-offs are being enforced by the constraints?
- How would this model grow in a real field setting?
- Where else in the energy value chain does this same pattern appear?

## Natural Extensions
- Add storage tanks or intermediate hubs
- Add trucking versus pipeline options
- Add water quality compatibility constraints
- Add multiple time periods
- Add integer decisions such as whether a route or facility is used

## Good Bridge To Your Real Examples
After the toy demo, say:

“This is the simplified form of a much broader class of optimization problems. The same modeling language shows up in water logistics, sand supply, stage scheduling, and CO2 transport network design. The toy example is intentionally small so the structure is easy to see.”
