from pathlib import Path

import pandas as pd
import pulp


def locate_data_dir() -> Path:
    here = Path(__file__).resolve().parent
    candidate_dirs = [
        here.parent.parent / "data" / "optimization_waterwise",
        Path.cwd() / "training" / "data" / "optimization_waterwise",
        Path.cwd() / "data" / "optimization_waterwise",
    ]
    for path in candidate_dirs:
        if path.exists():
            return path
    raise FileNotFoundError("Could not locate optimization_waterwise sample data directory.")


def load_inputs(data_dir: Path):
    sources = pd.read_csv(data_dir / "water_sources.csv")
    demands = pd.read_csv(data_dir / "demand_pads.csv")
    links = pd.read_csv(data_dir / "transport_links.csv")
    params = pd.read_csv(data_dir / "scenario_parameters.csv")
    param_map = dict(zip(params["parameter"], params["value"]))
    return sources, demands, links, param_map


def build_and_solve_model(sources, demands, links, param_map):
    source_map = sources.set_index("source").to_dict("index")
    demand_map = demands.set_index("pad").to_dict("index")
    link_map = {(row.source, row.pad): row for row in links.itertuples(index=False)}

    model = pulp.LpProblem("WaterWise_Training_Case", pulp.LpMinimize)

    flow = {
        (source, pad): pulp.LpVariable(f"flow__{source}__{pad}", lowBound=0)
        for source, pad in link_map
    }
    shortage = {
        pad: pulp.LpVariable(f"shortage__{pad}", lowBound=0)
        for pad in demand_map
    }

    model += (
        pulp.lpSum(
            flow[source, pad]
            * (
                source_map[source]["source_cost_per_bbl"]
                + link_map[source, pad].transport_cost_per_bbl
            )
            for source, pad in flow
        )
        + pulp.lpSum(
            shortage[pad] * demand_map[pad]["shortage_penalty_per_bbl"]
            for pad in shortage
        ),
        "total_cost",
    )

    for source in source_map:
        model += (
            pulp.lpSum(flow[s, p] for s, p in flow if s == source)
            <= source_map[source]["supply_bbl"],
            f"supply_limit__{source}",
        )

    for pad in demand_map:
        model += (
            pulp.lpSum(flow[s, p] for s, p in flow if p == pad) + shortage[pad]
            == demand_map[pad]["demand_bbl"],
            f"demand_balance__{pad}",
        )

    for (source, pad), link in link_map.items():
        model += (
            flow[source, pad] <= link.max_capacity_bbl,
            f"route_capacity__{source}__{pad}",
        )

    freshwater_sources = [
        source
        for source, row in source_map.items()
        if row["source_type"] == "freshwater"
    ]
    if freshwater_sources:
        model += (
            pulp.lpSum(
                flow[s, p]
                for s, p in flow
                if s in freshwater_sources
            )
            <= float(param_map["freshwater_cap_bbl"]),
            "freshwater_cap",
        )

    produced_sources = [
        source
        for source, row in source_map.items()
        if row["source_type"] == "produced_water"
    ]
    model += (
        pulp.lpSum(
            flow[s, p]
            for s, p in flow
            if s in produced_sources
        )
        >= float(param_map["min_produced_water_reuse_bbl"]),
        "produced_water_reuse_target",
    )

    solver = pulp.PULP_CBC_CMD(msg=False)
    model.solve(solver)
    return model, flow, shortage, source_map, demand_map, link_map


def build_outputs(flow, shortage, source_map, demand_map):
    allocation_rows = []
    for (source, pad), var in flow.items():
        value = float(var.value() or 0.0)
        if value > 1e-6:
            allocation_rows.append(
                {
                    "source": source,
                    "pad": pad,
                    "source_type": source_map[source]["source_type"],
                    "allocated_bbl": round(value, 2),
                }
            )
    allocation_df = pd.DataFrame(allocation_rows).sort_values(
        ["pad", "source", "allocated_bbl"], ascending=[True, True, False]
    )

    pad_rows = []
    for pad in demand_map:
        delivered = allocation_df.loc[allocation_df["pad"] == pad, "allocated_bbl"].sum()
        shortage_value = float(shortage[pad].value() or 0.0)
        pad_rows.append(
            {
                "pad": pad,
                "demand_bbl": demand_map[pad]["demand_bbl"],
                "delivered_bbl": round(delivered, 2),
                "shortage_bbl": round(shortage_value, 2),
                "fulfillment_pct": round(100.0 * delivered / demand_map[pad]["demand_bbl"], 2),
            }
        )
    pad_summary_df = pd.DataFrame(pad_rows)

    source_summary_df = (
        allocation_df.groupby(["source", "source_type"], as_index=False)["allocated_bbl"]
        .sum()
        .sort_values(["source_type", "allocated_bbl"], ascending=[True, False])
    )
    return allocation_df, pad_summary_df, source_summary_df


def main():
    data_dir = locate_data_dir()
    sources, demands, links, param_map = load_inputs(data_dir)
    model, flow, shortage, source_map, demand_map, link_map = build_and_solve_model(
        sources, demands, links, param_map
    )

    status = pulp.LpStatus[model.status]
    allocation_df, pad_summary_df, source_summary_df = build_outputs(
        flow, shortage, source_map, demand_map
    )

    total_cost = pulp.value(model.objective)
    freshwater_used = source_summary_df.loc[
        source_summary_df["source_type"] == "freshwater", "allocated_bbl"
    ].sum()
    produced_used = source_summary_df.loc[
        source_summary_df["source_type"] == "produced_water", "allocated_bbl"
    ].sum()
    total_allocated = source_summary_df["allocated_bbl"].sum()
    produced_reuse_pct = 100.0 * produced_used / total_allocated if total_allocated else 0.0

    print("=== WaterWise Training Case Study ===")
    print(f"Solver status: {status}")
    print(f"Objective value (total cost): ${total_cost:,.2f}")
    print(f"Total allocated water: {total_allocated:,.0f} bbl")
    print(f"Produced water reused: {produced_used:,.0f} bbl ({produced_reuse_pct:0.1f}%)")
    print(f"Freshwater used: {freshwater_used:,.0f} bbl")
    print()
    print("Pad summary")
    print(pad_summary_df.to_string(index=False))
    print()
    print("Top route allocations")
    print(allocation_df.sort_values("allocated_bbl", ascending=False).head(10).to_string(index=False))

    results_dir = Path(__file__).resolve().parent / "results" / "optimization_waterwise"
    results_dir.mkdir(parents=True, exist_ok=True)
    allocation_df.to_csv(results_dir / "route_allocations.csv", index=False)
    pad_summary_df.to_csv(results_dir / "pad_summary.csv", index=False)
    source_summary_df.to_csv(results_dir / "source_summary.csv", index=False)
    print()
    print(f"Results written to: {results_dir}")


if __name__ == "__main__":
    main()
