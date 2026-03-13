# Optimization WaterWise Data Dictionary

## Purpose
This dataset supports a simple, end-to-end optimization case study inspired by completions water management in upstream oil and gas. The objective is to decide how much water to move from different sources to different pads while minimizing total cost and respecting operational constraints.

## File: `water_sources.csv`
One row per water source.

Columns:
- `source`: source name
- `source_type`: simplified source category such as `produced_water`, `brackish`, or `freshwater`
- `supply_bbl`: maximum available volume in barrels
- `source_cost_per_bbl`: cost of obtaining water from that source before transport

## File: `demand_pads.csv`
One row per completion pad or demand location.

Columns:
- `pad`: pad name
- `demand_bbl`: required water demand in barrels
- `shortage_penalty_per_bbl`: penalty cost if demand is not met

## File: `transport_links.csv`
One row per allowed source-to-pad connection.

Columns:
- `source`: source name
- `pad`: demand pad
- `max_capacity_bbl`: maximum transport capacity on that route
- `transport_cost_per_bbl`: route-specific transport cost in dollars per barrel

## File: `scenario_parameters.csv`
Simple scenario-level business rules.

Columns:
- `parameter`: parameter name
- `value`: parameter value
- `description`: meaning of the parameter

Included parameters:
- `freshwater_cap_bbl`: global cap on freshwater usage
- `min_produced_water_reuse_bbl`: minimum produced water reuse target

## Notes
- This is a simplified linear programming case study.
- It is intentionally small enough to solve quickly.
- The structure is realistic even though the numbers are synthetic.
- It is a good bridge into larger optimization problems such as `WaterWise`, `SandWise`, routing, scheduling, or CCS network design.
