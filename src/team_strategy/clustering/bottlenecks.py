"""Stage 2: recompute standalone hosting capacities and signed bottlenecks.

Maximize extra grid-only load at ONE candidate at a time, keeping the base
demands and generator/line limits supplied by the instructor's period loader.
This is a capacity diagnostic, not economic dispatch or a 500 MW submission.
"""

from dataclasses import asdict, dataclass
import csv
import json
import math
from pathlib import Path
import sys

import numpy as np

from ercot_game.scenario_package import require_validated_block
from tools.activsg2000.dcopf import (
    GurobiReusableDCOPFModel, ReusableDCOPFModel, _run_highs, resolve_solver_backend,
)
from tools.hosting_capacity import HostingCapacityPeriod, prepared_artifact_period_provider, validate_period

from ..context import file_fingerprint, scenario_fingerprint
from .candidates import CandidatePool, load_candidate_pool


@dataclass(frozen=True)
class Tolerances:
    tight_mw: float = 1e-4
    shadow: float = 1e-7
    period_tie_mw: float = 1e-4

    def __post_init__(self) -> None:
        for value in (self.tight_mw, self.shadow, self.period_tie_mw):
            if not math.isfinite(value) or value <= 0:
                raise ValueError("tolerances must be finite and positive")


@dataclass(frozen=True)
class LineConstraint:
    branch_id: str
    from_bus_id: str
    to_bus_id: str
    direction: str
    flow_mw: float
    limit_mw: float
    capacity_shadow_mw_per_mw: float
    # Classification from this optimal dual solution, not a proof of unique
    # causality. Degenerate LPs can have nonunique duals; later stages validate interactions.
    materially_limiting: bool


@dataclass(frozen=True)
class PeriodDiagnosis:
    period_index: int
    hosting_capacity_mw: float
    generation_headroom_mw: float
    limiting_resource: str
    tight_lines: tuple[LineConstraint, ...]
    generator_pmax_ids: tuple[str, ...]
    generator_pmin_ids: tuple[str, ...]
    # (generator ID, bound, extra hosting MW per MW of bound relaxation).
    # Fixed-output units are omitted here: their two coincident bounds make
    # individual lower/upper shadow attribution ambiguous. Both ID lists retain them.
    generator_bound_marginals: tuple[tuple[str, str, float], ...]
    max_balance_error_mw: float
    max_limit_violation_mw: float
    duality_gap_mw: float


@dataclass(frozen=True)
class BusBottlenecks:
    bus_id: str
    minimum_hosting_capacity_mw: float
    screening_capacity_difference_mw: float
    capacity_by_period_mw: tuple[float, ...]
    limiting_periods: tuple[int, ...]
    diagnoses: tuple[PeriodDiagnosis, ...]


class HostingLP:
    """Small diagnostic adapter around the unchanged instructor formulation.

    The public hosting-capacity API returns capacity but not LP sensitivities.
    Only this adapter accesses private model handles: solver, generator/angle/
    candidate columns, and balance rows. HiGHS uses one row per branch;
    Gurobi uses named upper/lower rows. Check these layouts before use. Never infer these shadow
    values from a subsequent economic-dispatch solve.
    """

    def __init__(self, template: HostingCapacityPeriod, tolerances: Tolerances = Tolerances(),
                 *, solver_backend: str = "auto"):
        self.template = validate_period(template)
        self.tolerances = tolerances
        # Auto checks both the package and a full-size license before solving.
        # A numerical/infeasible solve never silently switches solver.
        self.backend = resolve_solver_backend(solver_backend)
        model_class = GurobiReusableDCOPFModel if self.backend == "gurobi" else ReusableDCOPFModel
        self.model = model_class(
            buses=tuple(self.template.buses), generators=tuple(self.template.generators),
            branches=tuple(self.template.branches), enable_candidate_demand_probes=True,
            solver_threads=1,
        )
        if self.backend == "gurobi":
            self.solver = self.model._model
            self.infinity = self.model._gp.GRB.INFINITY
            self.solver.Params.FeasibilityTol = 1e-9
            self.solver.Params.OptimalityTol = 1e-9
            self.solver.Params.Method = 1  # Dual simplex provides basis duals.
            self.line_rows = tuple((self.solver.getConstrByName(f"line-upper:{b.branch_id}"),
                                    self.solver.getConstrByName(f"line-lower:{b.branch_id}"))
                                   for b in self.template.branches)
            if (self.solver.NumConstrs != len(self.template.buses) + 2 * len(self.template.branches)
                    or any(row is None for pair in self.line_rows for row in pair)):
                raise RuntimeError("instructor Gurobi row layout changed; review diagnostic adapter")
            for column in self.model._generator_columns.values():
                column.Obj = 0.0
        else:
            import highspy

            self.highspy = highspy
            self.solver = self.model._highs
            self.infinity = highspy.kHighsInf
            # Keep the engine's process-global thread-pool convention.
            self.solver.setOptionValue("primal_feasibility_tolerance", 1e-9)
            self.solver.setOptionValue("dual_feasibility_tolerance", 1e-9)
            if self.solver.getNumRow() != len(self.template.buses) + len(self.template.branches):
                raise RuntimeError("instructor HiGHS row layout changed; review diagnostic adapter")
            for column in self.model._generator_columns.values():
                self.solver.changeColCost(int(column.index), 0.0)
        self.previous_candidate = None
        self.period = None

    def _set_candidate(self, column, upper: float, cost: float) -> None:
        if self.backend == "gurobi":
            column.LB, column.UB, column.Obj = 0.0, upper, cost
        else:
            self.solver.changeColBounds(int(column.index), 0.0, upper)
            self.solver.changeColCost(int(column.index), cost)

    def _run(self) -> None:
        if self.backend == "gurobi":
            self.solver.optimize()
            optimal = self.solver.Status == self.model._gp.GRB.OPTIMAL
            status = f"Gurobi status {self.solver.Status}"
            errors = ((self.solver.ConstrVio, self.solver.BoundVio, self.solver.DualVio)
                      if optimal else ())
        else:
            _run_highs(self.solver)
            optimal = self.solver.getModelStatus() == self.highspy.HighsModelStatus.kOptimal
            status = self.solver.modelStatusToString(self.solver.getModelStatus())
            info = self.solver.getInfo()
            errors = (info.max_primal_infeasibility, info.max_dual_infeasibility)
        if not optimal:
            raise RuntimeError(f"period {self.period.period_index}: LP did not solve optimally ({status})")
        if any(not math.isfinite(error) or error > self.tolerances.tight_mw for error in errors):
            raise RuntimeError(f"solver feasibility checks failed: {errors}")

    def set_period(self, period: HostingCapacityPeriod) -> None:
        """Update only demands/fixed injections; reject changing network limits."""
        period = validate_period(period)
        if (period.generators != self.template.generators
                or period.branches != self.template.branches
                or tuple((b.bus_id, b.reference) for b in period.buses)
                != tuple((b.bus_id, b.reference) for b in self.template.buses)):
            raise ValueError("this adapter requires fixed topology and generator limits across periods")
        if self.previous_candidate is not None:
            self._set_candidate(self.previous_candidate, 0.0, 0.0)
            self.previous_candidate = None
        self.period = period
        for bus in period.buses:
            demand = bus.demand_mw - period.fixed_injection_mw_by_bus.get(bus.bus_id, 0.0)
            if self.backend == "gurobi":
                self.model._balance_rows[bus.bus_id].RHS = demand
            else:
                self.solver.changeRowBounds(self.model._balance_row_indices[bus.bus_id], demand, demand)
        # Check the original base case with ALL added-load columns fixed to zero.
        self._run()

    def maximize(self, bus_id: str) -> float:
        """Maximize one added-load column; every other candidate stays at zero."""
        if self.period is None:
            raise ValueError("call set_period before maximizing candidate load")
        if bus_id not in self.model._candidate_demand_columns:
            raise ValueError(f"unknown candidate bus: {bus_id}")
        if self.previous_candidate is not None:
            self._set_candidate(self.previous_candidate, 0.0, 0.0)
        column = self.model._candidate_demand_columns[bus_id]
        self._set_candidate(column, self.infinity, -1.0)  # Minimize -load = maximize load.
        self.previous_candidate = column
        self._run()
        capacity = float(column.X if self.backend == "gurobi"
                         else self.solver.getSolution().col_value[int(column.index)])
        if not math.isfinite(capacity) or capacity < -self.tolerances.tight_mw:
            raise RuntimeError(f"invalid hosting capacity: {capacity}")
        return max(0.0, capacity)

    def _snapshot(self):
        """Normalize solver values, signed line marginals, and the dual objective."""
        if self.backend == "gurobi":
            variables, rows = self.solver.getVars(), self.solver.getConstrs()
            values = self.solver.getAttr("X", variables)
            reduced_costs = self.solver.getAttr("RC", variables)
            row_duals = self.solver.getAttr("Pi", rows)
            dual_objective = math.fsum(d * r.RHS for d, r in zip(row_duals, rows, strict=True))
            lowers = self.solver.getAttr("LB", variables)
            uppers = self.solver.getAttr("UB", variables)
            line_shadows = tuple((-upper.Pi, lower.Pi) for upper, lower in self.line_rows)
        else:
            solution, lp = self.solver.getSolution(), self.solver.getLp()
            values, reduced_costs = list(solution.col_value), list(solution.col_dual)
            row_duals = list(solution.row_dual)
            dual_objective = math.fsum(
                d * (lo if d >= 0 else hi)
                for d, lo, hi in zip(row_duals, lp.row_lower_, lp.row_upper_, strict=True)
            )
            lowers, uppers = lp.col_lower_, lp.col_upper_
            line_shadows = tuple((-d, d) for d in row_duals[len(self.template.buses):])
        for dual, lower, upper in zip(reduced_costs, lowers, uppers, strict=True):
            bound = lower if dual >= 0 else upper
            if -self.infinity < bound < self.infinity:
                dual_objective += dual * bound
            elif abs(dual) > self.tolerances.shadow:
                raise RuntimeError("nonzero dual on an infinite bound")
        return values, reduced_costs, line_shadows, dual_objective

    def diagnose(self, bus_id: str) -> PeriodDiagnosis:
        """Solve and capture tight constraints, marginals, and physical residuals."""
        capacity = self.maximize(bus_id)
        period, tol = self.period, self.tolerances
        values, reduced_costs, line_shadows, dual_objective = self._snapshot()
        balance = {b.bus_id: period.fixed_injection_mw_by_bus.get(b.bus_id, 0.0) - b.demand_mw
                   for b in period.buses}
        balance[bus_id] -= capacity
        angles = {bus: (0.0 if column is None else values[int(column.index)] / self.model._angle_scale)
                  for bus, column in self.model._angle_columns.items()}
        pmax, pmin, marginals, tight_lines = [], [], [], []
        violations = [0.0]
        for generator in period.generators:
            column = int(self.model._generator_columns[generator.generator_id].index)
            output, reduced_cost = values[column], reduced_costs[column]
            balance[generator.bus_id] += output
            violations.extend((generator.p_min_mw - output, output - generator.p_max_mw))
            at_min = abs(output - generator.p_min_mw) <= tol.tight_mw
            at_max = abs(output - generator.p_max_mw) <= tol.tight_mw
            if at_min:
                pmin.append(generator.generator_id)
            if at_max:
                pmax.append(generator.generator_id)
            if generator.p_max_mw == generator.p_min_mw:
                continue
            if at_max and -reduced_cost > tol.shadow:
                marginals.append((generator.generator_id, "upper", -reduced_cost))
            if at_min and reduced_cost > tol.shadow:
                marginals.append((generator.generator_id, "lower", reduced_cost))
        for index, branch in enumerate(period.branches):
            flow = branch.susceptance_pu * (angles[branch.from_bus_id] - angles[branch.to_bus_id])
            balance[branch.from_bus_id] -= flow
            balance[branch.to_bus_id] += flow
            violations.append(abs(flow) - branch.thermal_limit_mw)
            upper_shadow, lower_shadow = line_shadows[index]
            for direction, signed_limit, shadow in (
                ("upper", branch.thermal_limit_mw, upper_shadow),
                ("lower", -branch.thermal_limit_mw, lower_shadow),
            ):
                if abs(flow - signed_limit) <= tol.tight_mw:
                    tight_lines.append(LineConstraint(
                        branch.branch_id, branch.from_bus_id, branch.to_bus_id, direction,
                        flow, branch.thermal_limit_mw, max(0.0, shadow), shadow > tol.shadow,
                    ))
        # Independently check nodal balances, limits, and primal/dual objective agreement.
        balance_error = max(abs(value) for value in balance.values())
        limit_error = max(violations)
        gap = abs(-capacity - dual_objective)
        if max(balance_error, limit_error, gap) > tol.tight_mw:
            raise RuntimeError(f"independent solution checks failed: {balance_error}, {limit_error}, {gap}")
        headroom = (math.fsum(g.p_max_mw for g in period.generators)
                    + math.fsum(period.fixed_injection_mw_by_bus.values())
                    - math.fsum(b.demand_mw for b in period.buses))
        transmission = any(line.materially_limiting for line in tight_lines)
        generation = abs(capacity - headroom) <= tol.tight_mw
        resource = ("mixed" if transmission and generation else "transmission" if transmission
                    else "system_generation" if generation else "other_or_degenerate")
        return PeriodDiagnosis(period.period_index, capacity, headroom, resource, tuple(tight_lines),
                               tuple(pmax), tuple(pmin), tuple(marginals), balance_error, limit_error, gap)


def analyze_candidates(
    pool: CandidatePool, scenario_dir: Path, tolerances: Tolerances = Tolerances(),
    *, solver_backend: str = "auto",
) -> tuple[BusBottlenecks, ...]:
    """Scan the complete horizon, then diagnose EVERY period tied at each minimum."""
    if not pool.candidates or len({b.bus_id for b in pool.candidates}) != len(pool.candidates):
        raise ValueError("candidate pool must contain distinct buses")
    manifest = require_validated_block(scenario_dir)
    horizon = int(manifest["horizon"])
    if horizon <= 0:
        raise ValueError("scenario horizon must be positive")
    fingerprint = scenario_fingerprint(scenario_dir)
    if dict(pool.input_sha256).get("bus_catalog") != file_fingerprint(scenario_dir / "bus.csv"):
        raise ValueError("candidate pool bus catalog differs from the scenario")
    provider = prepared_artifact_period_provider(scenario_dir)
    model = HostingLP(provider(0), tolerances, solver_backend=solver_backend)
    capacities = np.empty((len(pool.candidates), horizon))
    for period_index in range(horizon):
        model.set_period(provider(period_index))
        for row, bus in enumerate(pool.candidates):
            capacities[row, period_index] = model.maximize(bus.bus_id)
        if (period_index + 1) % 12 == 0:
            print(f"Capacity scan: {period_index + 1}/{horizon} periods", file=sys.stderr)
    minimum = capacities.min(axis=1)
    ties = [tuple(int(i) for i in np.flatnonzero(values <= low + tolerances.period_tie_mw))
            for values, low in zip(capacities, minimum, strict=True)]
    diagnoses = [[] for _ in pool.candidates]
    for period_index in sorted(set().union(*ties)):
        model.set_period(provider(period_index))
        for row, bus in enumerate(pool.candidates):
            if period_index in ties[row]:
                diagnosis = model.diagnose(bus.bus_id)
                if abs(diagnosis.hosting_capacity_mw - capacities[row, period_index]) > tolerances.tight_mw:
                    raise RuntimeError("capacity changed between scan and diagnosis")
                diagnoses[row].append(diagnosis)
    if scenario_fingerprint(scenario_dir) != fingerprint:
        raise RuntimeError("scenario inputs changed during analysis; discard these results")
    return tuple(BusBottlenecks(
        bus.bus_id, float(minimum[row]), float(minimum[row] - bus.hosting_capacity_mw),
        tuple(float(value) for value in capacities[row]), ties[row], tuple(diagnoses[row]),
    ) for row, bus in enumerate(pool.candidates))


def main() -> None:
    """Run Stage 1 selection followed by Stage 2; preserve results in a fresh directory."""
    import argparse

    root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", type=Path, default=root / "ercot-connection-game/data/processed/activsg2000_representative_v1")
    parser.add_argument("--hosting-capacity", type=Path, default=root / "analysis/hosting_capacity_all_buses.csv")
    parser.add_argument("--screening", type=Path, default=root / "analysis/bus_screening_metrics.csv")
    parser.add_argument("--top-hosting", type=int, default=100)
    parser.add_argument("--top-screening", type=int, default=20)
    parser.add_argument("--include", action="append", default=[])
    parser.add_argument("--solver-backend", choices=("auto", "gurobi", "highs"), default="auto",
                        help="auto prefers usable Gurobi; otherwise uses HiGHS")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.output_dir.exists():
        parser.error("output directory already exists; choose a fresh run directory")
    tolerances = Tolerances()
    pool = load_candidate_pool(
        hosting_capacity_file=args.hosting_capacity, screening_file=args.screening,
        bus_catalog_file=args.scenario / "bus.csv", top_hosting_count=args.top_hosting,
        top_screening_count=args.top_screening, required_bus_ids=tuple(args.include),
    )
    fingerprint = scenario_fingerprint(args.scenario)
    backend = resolve_solver_backend(args.solver_backend)
    print(f"Selected solver: {backend}" + (" (Gurobi unavailable)" if args.solver_backend == "auto" and backend == "highs" else ""), file=sys.stderr)
    results = analyze_candidates(pool, args.scenario, tolerances, solver_backend=backend)
    if scenario_fingerprint(args.scenario) != fingerprint:
        raise RuntimeError("scenario changed; results were not saved")
    if backend == "gurobi":
        import gurobipy as gp
        version = ".".join(map(str, gp.gurobi.version()))
    else:
        import highspy
        version = highspy.Highs().version()
    report = {"schema_version": 1, "scenario_sha256": fingerprint,
              "solver_requested": args.solver_backend, "solver": backend, "solver_version": version,
              "solver_parallel": "off", "solver_primal_dual_tolerance": 1e-9,
              "tolerances": asdict(tolerances), "candidate_pool": asdict(pool),
              "source_sha256": {name: file_fingerprint(Path(__file__).with_name(name))
                                for name in ("bottlenecks.py", "candidates.py")},
              "results": [asdict(result) for result in results]}
    args.output_dir.mkdir(parents=True, exist_ok=False)
    (args.output_dir / "bottlenecks.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    with (args.output_dir / "summary.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("bus_id", "minimum_hosting_capacity_mw", "screening_capacity_difference_mw",
                         "limiting_periods", "limiting_resources", "material_line_signatures"))
        for result in results:
            resources = sorted({d.limiting_resource for d in result.diagnoses})
            signatures = sorted({f"{line.branch_id}:{line.direction}" for d in result.diagnoses
                                 for line in d.tight_lines if line.materially_limiting})
            writer.writerow((result.bus_id, result.minimum_hosting_capacity_mw,
                             result.screening_capacity_difference_mw,
                             ";".join(map(str, result.limiting_periods)),
                             ";".join(resources), ";".join(signatures)))
    print(f"Saved {len(results)} bus analyses to {args.output_dir}")


if __name__ == "__main__":
    main()
