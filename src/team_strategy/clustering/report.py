"""Run and preserve all six stages of Part 1.

Example, from the repository root:
PYTHONPATH=src:ercot-connection-game:ercot-connection-game/src .venv/bin/python \
    -m team_strategy.clustering.report --solver-backend highs --output-dir runs/part1-complete

Use --baseline for a current, fingerprint-matching Stage 2 bottlenecks.json.
Existing output directories are never overwritten. A manifest is marked
complete only after all stages and verification checks have succeeded.
"""
from dataclasses import asdict
import csv
import html
import json
from pathlib import Path
import sys

from tools.activsg2000.dcopf import resolve_solver_backend
from tools.hosting_capacity import prepared_artifact_period_provider
from ercot_game.scenario_package import require_validated_block
from ..context import file_fingerprint, scenario_fingerprint
from .bottlenecks import (BusBottlenecks, LineConstraint, PeriodDiagnosis, analyze_candidates)
from .candidates import CandidateBus, CandidatePool, load_candidate_pool
from .stress_scenarios import (run_stress_scenarios, compact_diagnosis, default_scenarios,
                               BackgroundTeam, StressScenario, critical_operating_periods)
from .groups import build_groups
from .interactions import run_interactions, summarize_validation, select_pairs


def _save(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def load_baseline(path, pool, scenario_dir, backend):
    """Accept a cache only when scenario, candidate pool, source, and solver match."""
    data = json.loads(path.read_text())
    if data["scenario_sha256"] != scenario_fingerprint(scenario_dir) or data["solver"] != backend:
        raise ValueError("baseline scenario/solver mismatch; rerun Stage 2 or omit --baseline")
    if data["candidate_pool"] != json.loads(json.dumps(asdict(pool))):
        raise ValueError("baseline candidate selection differs")
    for name in ("candidates.py", "bottlenecks.py"):
        if data["source_sha256"][name] != file_fingerprint(Path(__file__).with_name(name)):
            raise ValueError(f"baseline source {name} changed; rerun Stage 2")
    results = []
    for row in data["results"]:
        diagnoses = []
        for raw in row["diagnoses"]:
            d = dict(raw)
            d["tight_lines"] = tuple(LineConstraint(**line) for line in d["tight_lines"])
            for key in ("generator_pmax_ids", "generator_pmin_ids"):
                d[key] = tuple(d[key])
            d["generator_bound_marginals"] = tuple(tuple(m) for m in d["generator_bound_marginals"])
            diagnoses.append(PeriodDiagnosis(**d))
        results.append(BusBottlenecks(row["bus_id"], row["minimum_hosting_capacity_mw"],
                                      row["screening_capacity_difference_mw"], tuple(row["capacity_by_period_mw"]),
                                      tuple(row["limiting_periods"]), tuple(diagnoses)))
    return tuple(results)


def load_reuse_run(directory, root, pool, scenario_dir, backend):
    """Reuse physical measurements only with identical network/model/settings.

    Driver/grouping changes may relabel a measurement, but cannot change its
    raw capacity. Physics source hashes, scenario, pool, solver, and horizon
    must match. Every reused artifact receives a new content fingerprint.
    """
    metadata = json.loads((directory / "manifest.json").read_text())
    if (metadata["status"] != "complete" or metadata["solver"] != backend
            or metadata["scenario_sha256"] != scenario_fingerprint(scenario_dir)
            or metadata["candidate_pool"] != json.loads(json.dumps(asdict(pool)))):
        raise ValueError("reused run is incomplete or has different inputs/solver")
    required = ("src/team_strategy/clustering/candidates.py", "src/team_strategy/clustering/bottlenecks.py",
                "src/team_strategy/clustering/stress_scenarios.py", "ercot-connection-game/tools/hosting_capacity.py",
                "ercot-connection-game/tools/activsg2000/dcopf.py")
    if any(metadata["source_sha256"].get(name) != file_fingerprint(root / name) for name in required):
        raise ValueError("physical-model source changed; cached measurements cannot be reused")
    raw = json.loads((directory / "baseline.json").read_text())
    # The compact cache retains diagnoses verbatim in the output. The driver
    # needs only capacities/ties to plan new nonzero-background experiments.
    baseline = tuple(BusBottlenecks(b["bus_id"], b["minimum_hosting_capacity_mw"],
                                   b["screening_capacity_difference_mw"], tuple(b["capacity_by_period_mw"]),
                                   tuple(b["limiting_periods"]), ()) for b in raw)
    stress = json.loads((directory / "stress.json").read_text())
    interactions = json.loads((directory / "interactions.json").read_text())
    if (stress["requested_mw"] != 500 or stress["near_limit_fraction"] != .95
            or interactions["horizon"] != metadata["horizon"]
            or interactions["loads_mw"] != [250., 500.]):
        raise ValueError("cached experiment settings differ")
    fingerprints = {name: file_fingerprint(directory / name) for name in
                    ("manifest.json", "baseline.json", "stress.json", "interactions.json")}
    return baseline, raw, stress, interactions["records"], fingerprints


def write_tables(output, baseline, stress, groups, validation):
    cohort = {bus: c["cohort_id"] for c in groups["refined_cohorts"] for bus in c["members"]}
    memberships = {bus: [g["group_id"] for g in groups["overlapping_groups"] if bus in g["members"]]
                   for bus in cohort}
    valid = [s for s in stress["scenarios"] if s["status"] == "valid"]
    with (output / "bus_groups.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("bus_id", "baseline_hosting_capacity_mw", "overlapping_signed_groups",
                         "ptdf_refined_cohort", "worst_tested_residual_capacity_mw",
                         "scenarios_supporting_full_500mw", "valid_scenario_count", "interaction_test_count"))
        for bus in baseline:
            writer.writerow((bus.bus_id, bus.minimum_hosting_capacity_mw, ";".join(memberships[bus.bus_id]),
                             cohort[bus.bus_id], min(s["candidates"][bus.bus_id]["minimum_hosting_capacity_mw"] for s in valid),
                             sum(s["candidates"][bus.bus_id]["full_request_feasible"] for s in valid),
                             len(valid), validation["candidate_test_counts"][bus.bus_id]))
    with (output / "group_validation.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("group_id", "member_count", "status", "within_pairs", "across_pairs",
                         "within_mean_excess_per_added_mw", "across_mean_excess_per_added_mw"))
        for g in validation["overlapping_group_validation"]:
            writer.writerow((g["group_id"], g["member_count"], g["status"],
                             g["within"]["unordered_pair_count"], g["across"]["unordered_pair_count"],
                             g["within"]["mean_excess_per_added_mw"], g["across"]["mean_excess_per_added_mw"]))
    with (output / "ptdf_distances.csv").open("w", newline="") as stream:
        writer = csv.writer(stream); ids = groups["ptdf"]["bus_ids"]
        writer.writerow(["bus_id", *ids])
        for bus, distances in zip(ids, groups["normalized_ptdf_distances"], strict=True):
            writer.writerow([bus, *distances])


def render_report(output, manifest, baseline, stress, groups, interactions, validation):
    """Standalone HTML with searchable bus membership and explicit evidence limits."""
    escape = lambda value: html.escape(str(value))
    def table(headers, rows, identifier=""):
        return (f'<table id="{identifier}"><thead><tr>' + ''.join(f'<th>{escape(x)}</th>' for x in headers)
                + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{escape(x)}</td>' for x in row) + '</tr>' for row in rows)
                + '</tbody></table>')
    valid = [s for s in stress["scenarios"] if s["status"] == "valid"]
    status_by_group = {g["group_id"]: g for g in validation["overlapping_group_validation"]}
    scenario_rows = []
    for s in stress["scenarios"]:
        residuals = [c["minimum_hosting_capacity_mw"] for c in s["candidates"].values()]
        scenario_rows.append((s["scenario"]["name"], sum(s["background_loads_mw"].values()), s["status"],
                              f'{min(residuals):.2f}–{max(residuals):.2f}' if residuals else 'not evaluated',
                              sum(c["full_request_feasible"] for c in s["candidates"].values())))
    overlap_rows = [(g["group_id"], len(g["members"]), ', '.join(g["members"]),
                     status_by_group[g["group_id"]]["status"]) for g in groups["overlapping_groups"]]
    cohort = {bus: c["cohort_id"] for c in groups["refined_cohorts"] for bus in c["members"]}
    bus_rows = [(b.bus_id, f'{b.minimum_hosting_capacity_mw:.3f}', ', '.join(groups["signatures"][b.bus_id]) or 'no retained transmission signature',
                 cohort[b.bus_id], f'{min(s["candidates"][b.bus_id]["minimum_hosting_capacity_mw"] for s in valid):.3f}',
                 validation["candidate_test_counts"][b.bus_id]) for b in baseline]
    comparison_rows = []
    for q, comparisons in validation["comparisons_by_added_load_mw"].items():
        for label in ("shared_signed_bottleneck", "same_initial_cohort", "same_refined_cohort"):
            c = comparisons[label]
            fmt = lambda x: 'unavailable' if x is None else f'{x:.3f}'
            comparison_rows.append((q, label, c["within"]["unordered_pair_count"], c["across"]["unordered_pair_count"],
                                    fmt(c["within"]["mean_excess_per_added_mw"]), fmt(c["across"]["mean_excess_per_added_mw"]), c["status"]))
    content = f'''<!doctype html><html><head><meta charset="utf-8"><title>Part 1 — Electrical bus groups</title>
<style>body{{font:16px/1.55 system-ui;margin:40px auto;max-width:1280px;padding:0 24px;color:#172233}}h1,h2{{line-height:1.2}}table{{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0}}th,td{{border:1px solid #d7dee7;padding:9px;text-align:left;vertical-align:top}}th{{background:#edf2f8}}td{{overflow-wrap:anywhere}}.note{{padding:16px;background:#edf5ff;border-left:4px solid #3262a8}}input{{padding:12px;width:320px}}code{{background:#eef1f4;padding:2px 5px}}</style></head><body>
<h1>Part 1: electrical bus groups and measured interactions</h1>
<p>{len(baseline)} candidates, {manifest['horizon']} periods, {len(valid)} valid background scenarios,
{len(interactions['pairs'])} sampled unordered pairs, {len(interactions['records'])} directional load tests.
Solver: {escape(manifest['solver'])}. All candidates participate in interaction tests.</p>
<div class="note">Transmission groups may overlap. Every bus also shares the system generation ceiling.
PTDF cohorts are a refinement hypothesis; use the validation status, not the cohort ID alone, when selecting Part 2 experiments.
An unshared line signature does not imply independent capacity.</div>
<h2>What was tested</h2><p>Each rival requests at most 500 MW; 2,000 MW backgrounds represent four teams.
Five-team backgrounds total 2,500 MW. Background withdrawals are fixed and uncurtailed, with no onsite generators or storage. Capacity limits are checked over every period.
Actual 500 MW economic-dispatch observations use periods {escape(stress['operating_periods'])}; near-limit means at least {stress['near_limit_fraction']:.0%} loading with a positive aligned flow increment.
These are electrical diagnostics, not official allocation or scores.</p>
{table(('Background','Added MW','Status','Residual HC range (MW)','Candidates supporting 500 MW'),scenario_rows)}
<h2>Interaction validation</h2><p>For a target j, I=(HC_j−HC_j after q at i)/HC_j. We separately remove the unavoidable loss imposed by
the shared generation ceiling: max(0, HC_j−(system headroom−q)). Excess/q measures additional transmission interaction.
The pair sample is fixed using the original seven backgrounds before adding the two five-rival cases.
Means are descriptive for this deterministic, coverage-balanced sample; directions and load sizes are dependent.</p>
{table(('Added MW','Grouping','Within pairs','Across pairs','Within excess/q','Across excess/q','Evidence status'),comparison_rows)}
<p>{escape(validation['support_rule'])} A group marked limited_evidence has insufficient measured pairs; not_separated_in_sample means the expected within/across contrast was not observed.</p>
<h2>Overlapping signed-constraint groups</h2>{table(('Constraint','Members','Bus IDs','Validation'),overlap_rows)}
<h2>PTDF refinement and sensitivity</h2><p>DC injection sensitivities use common reference bus {escape(groups['ptdf']['reference_bus'])}.
Candidate differences are slack invariant. Critical-line features are divided by thermal ratings and weighted by stress frequency.
Complete-link merges require all cross-pairs to pass the signed-signature/PTDF cutoffs, preventing similarity chaining.
The default PTDF distance cutoff is {groups['settings']['ptdf_cutoff_fraction']} times the median positive pair distance.</p>
{table(('Cutoff / median distance','Cohorts','Singletons'),[(s['ptdf_cutoff_fraction'],s['cohort_count'],s['singleton_count']) for s in groups['threshold_sensitivity']])}
<h2>Candidate lookup</h2><input id="search" placeholder="Search bus, constraint, or cohort" oninput="filterRows()">
{table(('Bus','Baseline HC (MW)','Retained signed signatures','PTDF cohort','Worst tested residual HC (MW)','Directional test involvement'),bus_rows,'buses')}
<h2>Use in Part 2</h2><p>Use measured interactions and group evidence to choose matched concentrated and diversified plans.
Keep the total request, generation/storage mix, opponent scenarios, and S1-to-S2 history matched.
Validate with the full game evaluator: the present groups do not establish competitor choice probabilities, allocation resilience, or economic superiority.</p>
<p>Evidence: <a href="bus_groups.csv">bus memberships</a> · <a href="group_validation.csv">group validation</a> ·
<a href="interactions.json">directional experiments</a> · <a href="stress.json">stress observations</a> ·
<a href="groups.json">PTDF and grouping data</a> · <a href="manifest.json">inputs, settings and source fingerprints</a>.</p>
<script>function filterRows(){{const q=document.getElementById('search').value.toLowerCase();for(const r of document.querySelectorAll('#buses tbody tr'))r.hidden=!r.textContent.toLowerCase().includes(q);}}</script></body></html>'''
    (output / "report.html").write_text(content)


def main():
    import argparse
    root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", type=Path, default=root / "ercot-connection-game/data/processed/activsg2000_representative_v1")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--reuse-run", type=Path, help="Complete run with matching physical measurements")
    parser.add_argument("--extra-stress-cache", type=Path, help="Additional scenario evidence with matching model fingerprints")
    parser.add_argument("--solver-backend", choices=("auto", "gurobi", "highs"), default="auto")
    parser.add_argument("--pair-count", type=int, default=96)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    if args.output_dir.exists():
        parser.error("output directory already exists; choose a fresh directory")
    if args.baseline and args.reuse_run:
        parser.error("choose --baseline or --reuse-run")
    if args.extra_stress_cache and not args.reuse_run:
        parser.error("--extra-stress-cache requires --reuse-run")
    backend = resolve_solver_backend(args.solver_backend)
    pool = load_candidate_pool(hosting_capacity_file=root / "analysis/hosting_capacity_all_buses.csv",
                               screening_file=root / "analysis/bus_screening_metrics.csv",
                               bus_catalog_file=args.scenario / "bus.csv", required_bus_ids=("6141",))
    source_files = sorted(Path(__file__).parent.glob("*.py"))
    # Include the instructor implementation used by the diagnostic adapter.
    import tools.activsg2000.dcopf as dcopf
    import tools.hosting_capacity as hosting
    source_files += [Path(dcopf.__file__), Path(hosting.__file__)]
    sources = {str(path.relative_to(root)): file_fingerprint(path) for path in source_files}
    fingerprint = scenario_fingerprint(args.scenario)
    manifest = {"schema_version": 1, "status": "running", "solver": backend,
                "scenario_sha256": fingerprint, "source_sha256": sources, "seed": args.seed,
                "pair_count_requested": args.pair_count, "candidate_pool": asdict(pool),
                "horizon": int(require_validated_block(args.scenario)["horizon"]),
                "operating_request_mw": 500., "interaction_loads_mw": [250., 500.],
                "scope": "Fixed grid-only withdrawals; no game allocation, score, generator/storage sweep, or S2 carryover."}
    import numpy as np
    if backend == "gurobi":
        import gurobipy as gp
        solver_version = ".".join(map(str, gp.gurobi.version()))
    else:
        import highspy
        solver_version = highspy.Highs().version()
    manifest.update(python_version=sys.version, numpy_version=np.__version__, solver_version=solver_version)
    args.output_dir.mkdir(parents=True)
    _save(args.output_dir / "manifest.json", manifest)
    try:
        cached_stress, cached_records, raw_baseline = None, (), None
        if args.reuse_run:
            baseline, raw_baseline, cached_stress, cached_records, reused = load_reuse_run(
                args.reuse_run, root, pool, args.scenario, backend)
            manifest["reused_evidence_sha256"] = reused
        else:
            baseline = (load_baseline(args.baseline, pool, args.scenario, backend) if args.baseline
                        else analyze_candidates(pool, args.scenario, solver_backend=backend))
        if len(baseline) != len(pool.candidates) or any(len(b.capacity_by_period_mw) != manifest["horizon"] for b in baseline):
            raise RuntimeError("baseline coverage is incomplete")
        if raw_baseline is None:
            raw_baseline = [dict(bus_id=b.bus_id, minimum_hosting_capacity_mw=b.minimum_hosting_capacity_mw,
              screening_capacity_difference_mw=b.screening_capacity_difference_mw,
              limiting_periods=b.limiting_periods, capacity_by_period_mw=b.capacity_by_period_mw,
              diagnoses=[compact_diagnosis(d) for d in b.diagnoses]) for b in baseline]
        _save(args.output_dir / "baseline.json", raw_baseline)
        provider = prepared_artifact_period_provider(args.scenario)
        periods = tuple(provider(i) for i in range(manifest["horizon"]))
        core_scenarios = default_scenarios()
        extended = tuple(StressScenario(name, tuple(BackgroundTeam(f"rival-{i}", ((bus, 500.),)) for i in range(5)))
                         for name, bus in (("hub_2500", "6141"), ("shared_line_2500", "5413")))
        scenarios = core_scenarios + extended
        cached_cases = {} if cached_stress is None else {s["scenario"]["name"]: s for s in cached_stress["scenarios"]}
        if args.extra_stress_cache:
            extra_metadata = json.loads((args.extra_stress_cache / "manifest.json").read_text())
            if (extra_metadata["status"] != "complete" or extra_metadata["solver"] != backend
                    or extra_metadata["scenario_sha256"] != fingerprint
                    or extra_metadata["candidate_pool"] != json.loads(json.dumps(asdict(pool)))):
                raise ValueError("extra scenario cache inputs differ")
            for name, digest in extra_metadata["source_sha256"].items():
                if digest != file_fingerprint(Path(__file__).with_name(name)):
                    raise ValueError("extra scenario model source changed")
            extra = json.loads((args.extra_stress_cache / "stress.json").read_text())
            if extra["requested_mw"] != 500 or extra["near_limit_fraction"] != .95:
                raise ValueError("extra scenario settings differ")
            cached_cases.update({s["scenario"]["name"]: s for s in extra["scenarios"]})
            manifest["extra_stress_evidence_sha256"] = {name: file_fingerprint(args.extra_stress_cache / name)
                                                      for name in ("manifest.json", "stress.json")}
        for scenario in scenarios:
            cached = cached_cases.get(scenario.name)
            if cached and cached["scenario"] != json.loads(json.dumps(asdict(scenario))):
                raise ValueError("cached background-team definitions differ")
        missing = tuple(s for s in scenarios if s.name not in cached_cases)
        if cached_stress is not None and "baseline" not in cached_cases:
            raise ValueError("reused run is missing its baseline scenario")
        if missing:
            computed = run_stress_scenarios(periods, pool, baseline, solver_backend=backend, scenarios=missing)
            cached_cases.update({s["scenario"]["name"]: s for s in computed["scenarios"]})
        operating = critical_operating_periods(periods, baseline)
        if any(tuple(s["operating_periods"]) != operating for s in cached_cases.values()):
            raise ValueError("cached operating-period selection differs")
        stress = {"solver": backend, "requested_mw": 500., "near_limit_fraction": .95,
                  "operating_periods": operating, "scenarios": [cached_cases[s.name] for s in scenarios]}
        _save(args.output_dir / "stress.json", stress)
        groups = build_groups(stress, periods[0])
        _save(args.output_dir / "groups.json", groups)
        # Freeze the validation design BEFORE the two heavier backgrounds.
        design = dict(stress, scenarios=[cached_cases[s.name] for s in core_scenarios])
        design_groups = build_groups(design, periods[0])
        pairs = select_pairs(design_groups, pair_count=args.pair_count, seed=args.seed)
        manifest["validation_sampling_scenarios"] = [s.name for s in core_scenarios]
        interactions = run_interactions(periods, baseline, groups, stress, pair_count=args.pair_count, seed=args.seed,
                                        validation_pairs=pairs, cached_records=cached_records)
        _save(args.output_dir / "interactions.json", interactions)
        validation = summarize_validation(interactions, groups)
        _save(args.output_dir / "validation.json", validation)
        if set(interactions["candidate_coverage"]) != {b.bus_id for b in pool.candidates}:
            raise RuntimeError("interaction validation missed candidates")
        if len(interactions["records"]) != len(interactions["pairs"]) * 4:
            raise RuntimeError("missing interaction directions or load sizes")
        if scenario_fingerprint(args.scenario) != fingerprint or any(file_fingerprint(root / name) != digest for name, digest in sources.items()):
            raise RuntimeError("source or input files changed during analysis")
        write_tables(args.output_dir, baseline, stress, groups, validation)
        render_report(args.output_dir, manifest, baseline, stress, groups, interactions, validation)
        manifest.update(status="complete", valid_scenario_count=sum(s["status"] == "valid" for s in stress["scenarios"]),
                        overlapping_group_count=len(groups["overlapping_groups"]), refined_cohort_count=len(groups["refined_cohorts"]),
                        interaction_pair_count=len(interactions["pairs"]), directional_test_count=len(interactions["records"]))
        _save(args.output_dir / "manifest.json", manifest)
        print(f"Part 1 complete: {args.output_dir / 'report.html'}")
    except Exception as error:
        manifest.update(status="failed", error=f"{type(error).__name__}: {error}")
        _save(args.output_dir / "manifest.json", manifest)
        raise
    from ..experiments.findings import export_part1, write_strategy_indexes
    export_part1(root, args.output_dir, root / "findings")
    write_strategy_indexes(root, root / "findings")


if __name__ == "__main__":
    main()
