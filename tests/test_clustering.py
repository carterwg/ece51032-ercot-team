"""Known-answer and end-to-end checks for the six-stage electrical analysis."""
from copy import deepcopy
from dataclasses import asdict, replace
import csv
import json
from pathlib import Path

import numpy as np
import pytest

from team_strategy.clustering.candidates import load_candidate_pool
from team_strategy.clustering.bottlenecks import HostingLP, analyze_candidates
from team_strategy.clustering.stress_scenarios import (
    BackgroundTeam, StressScenario, add_loads, run_stress_scenarios,
)
from team_strategy.clustering.groups import (
    build_groups, complete_link_groups, jaccard, ptdf_features, signature_features,
)
from team_strategy.clustering.interactions import (
    interaction_metrics, run_interactions, select_pairs, summarize_validation,
)
from team_strategy.clustering.report import render_report, write_tables, load_baseline
from team_strategy.context import file_fingerprint, scenario_fingerprint
from tools.hosting_capacity import prepared_artifact_period_provider, solve_hosting_capacity_at_bus


@pytest.fixture
def electrical_case(tmp_path):
    def write(name, headers, rows):
        with (tmp_path / name).open("w", newline="") as stream:
            writer = csv.writer(stream); writer.writerow(headers); writer.writerows(rows)
    (tmp_path / "manifest.json").write_text(json.dumps({
        "package_version": "activsg2000-scenarios-v1", "validation_status": "passed", "horizon": 2,
    }))
    write("bus.csv", ["bus_id", "type"], [["A", 3], ["B", 1]])
    write("demand_bus.csv", ["period", "A", "B"], [[0, 0, 10], [1, 0, 10]])
    write("generator_limits.csv", ["generator_id", "bus_id", "p_min_mw", "p_max_mw", "marginal_cost_c1_per_mwh", "status"],
          [["G", "A", 0, 100, 10, 1]])
    write("branch_limits.csv", ["branch_id", "from_bus_id", "to_bus_id", "reactance_pu", "thermal_limit_mva", "status"],
          [["L", "A", "B", .1, 40, 1]])
    write("dcline.csv", ["status", "from_bus_id", "to_bus_id", "Pt"], [])
    write("hc.csv", ["bus_id", "min_hosting_capacity_mw", "binding_period_index"], [["A", 90, 0], ["B", 30, 0]])
    write("screen.csv", ["bus_id", "overall_rank"], [["A", 2], ["B", 1]])
    pool = load_candidate_pool(hosting_capacity_file=tmp_path / "hc.csv", screening_file=tmp_path / "screen.csv",
                               bus_catalog_file=tmp_path / "bus.csv", top_hosting_count=2, top_screening_count=1)
    provider = prepared_artifact_period_provider(tmp_path)
    periods = tuple(provider(i) for i in range(2))
    baseline = analyze_candidates(pool, tmp_path, solver_backend="highs")
    scenarios = (StressScenario("baseline"), StressScenario("source_A_5", (BackgroundTeam("rival", (("A", 5.),)),)))
    stress = run_stress_scenarios(periods, pool, baseline, solver_backend="highs", scenarios=scenarios,
                                 requested_mw=5., near_limit_fraction=.25)
    return tmp_path, pool, periods, baseline, stress


def test_known_capacities_directions_and_all_ties(electrical_case):
    _, _, periods, baseline, _ = electrical_case
    by_bus = {b.bus_id: b for b in baseline}
    assert by_bus["A"].minimum_hosting_capacity_mw == pytest.approx(90)
    assert by_bus["B"].minimum_hosting_capacity_mw == pytest.approx(30)
    assert by_bus["B"].limiting_periods == (0, 1)
    diagnosis = by_bus["B"].diagnoses[0]
    assert diagnosis.tight_lines[0].direction == "upper"
    assert diagnosis.tight_lines[0].capacity_shadow_mw_per_mw == pytest.approx(1)
    official = solve_hosting_capacity_at_bus(periods[0], "B", solver_backend="highs")
    assert official.hosting_capacity_mw == pytest.approx(30)


def test_candidate_state_is_reset_and_infeasibility_is_explicit(electrical_case):
    _, _, periods, _, _ = electrical_case
    m = HostingLP(periods[0], solver_backend="highs"); m.set_period(periods[0])
    assert [m.maximize(b) for b in ("A", "B", "A")] == pytest.approx([90, 30, 90])
    with pytest.raises(RuntimeError, match="not solve optimally"):
        m.set_period(add_loads(periods[0], {"B": 31}))


@pytest.mark.parametrize("sites", [(("A", 501.),), (("A", -1.),), (("A", float("nan")),), (("A", 300.), ("B", 300.))])
def test_background_team_cap_and_values(sites):
    with pytest.raises(ValueError):
        BackgroundTeam("rival", sites)


def test_infeasible_background_is_not_a_zero_capacity_result(electrical_case):
    _, pool, periods, baseline, _ = electrical_case
    result = run_stress_scenarios(periods, pool, baseline, solver_backend="highs", requested_mw=5.,
        scenarios=(StressScenario("bad", (BackgroundTeam("rival", (("B", 31.),)),)),))
    assert result["scenarios"][0]["status"] == "infeasible_background"
    assert result["scenarios"][0]["candidates"] == {}


def test_actual_operating_point_differs_from_maximum_hosting(electrical_case):
    _, _, _, _, stress = electrical_case
    baseline = stress["scenarios"][0]["candidates"]["B"]
    assert baseline["observed_request_mw"] == 5
    assert baseline["minimum_hosting_capacity_mw"] == pytest.approx(30)
    assert baseline["near_lines"]["L:upper"]["max_utilization"] == pytest.approx(15 / 40)
    assert baseline["near_lines"]["L:upper"]["max_aligned_impact_mw"] == pytest.approx(5)


def test_baseline_reuse_does_not_depend_on_candidate_order(electrical_case):
    _, pool, periods, baseline, _ = electrical_case
    result = run_stress_scenarios(periods, pool, tuple(reversed(baseline)), solver_backend="highs", requested_mw=5.,
                                  scenarios=(StressScenario("baseline"),))
    assert result["scenarios"][0]["candidates"]["A"]["minimum_hosting_capacity_mw"] == pytest.approx(90)


def test_unknown_load_bus_and_negative_load_rejected(electrical_case):
    period = electrical_case[2][0]
    for loads in ({"missing": 5}, {"A": -1}):
        with pytest.raises(ValueError): add_loads(period, loads)


def test_tied_hours_do_not_inflate_signature_weights(electrical_case):
    stress = electrical_case[4]
    before, _ = signature_features(stress)
    repeated = deepcopy(stress)
    for scenario in repeated["scenarios"]:
        for candidate in scenario["candidates"].values(): candidate["diagnoses"] *= 3
    after, _ = signature_features(repeated)
    for bus in before:
        assert before[bus] == pytest.approx(after[bus])


def test_empty_signatures_do_not_imply_similarity():
    assert jaccard([], []) == 0
    assert jaccard(["L:upper"], ["L:lower"]) == 0
    assert jaccard(["L:upper"], ["L:upper", "M:upper"]) == .5


def test_complete_link_does_not_chain_similarity():
    allowed = lambda a, b: {a, b} in ({"A", "B"}, {"B", "C"})
    result = complete_link_groups(["C", "B", "A"], allowed)
    assert result == [("A", "B"), ("C",)]


def test_ptdf_known_answer_and_slack_invariant_differences(electrical_case):
    period = electrical_case[2][0]
    a = ptdf_features(period, ["A", "B"], ["L:upper"], reference_bus="A")
    b = ptdf_features(period, ["A", "B"], ["L:upper"], reference_bus="B")
    va, vb = np.array(a["rating_normalized_load_ptdf"]), np.array(b["rating_normalized_load_ptdf"])
    assert va[:, 0] == pytest.approx([0., 1 / 40])
    assert va[0] - va[1] == pytest.approx(vb[0] - vb[1])
    assert a["max_nodal_residual"] < 1e-10


def test_group_coverage_and_sensitivity(electrical_case):
    groups = build_groups(electrical_case[4], electrical_case[2][0])
    assert groups["system_generation_shared_by"] == ["A", "B"]
    assert sorted(b for c in groups["refined_cohorts"] for b in c["members"]) == ["A", "B"]
    assert len(groups["threshold_sensitivity"]) == 3
    assert select_pairs(groups, pair_count=1) == (("A", "B"),)
    with pytest.raises(ValueError): select_pairs(groups, pair_count=0)


def test_supply_floor_excess_and_counterflow():
    pure = interaction_metrics(3000., 2500., 500., 3000.)
    assert pure["capacity_loss_mw"] == 500
    assert pure["transmission_excess_loss_mw"] == 0
    extra = interaction_metrics(2800., 2100., 500., 3024.)
    assert extra["generation_forced_loss_floor_mw"] == 276
    assert extra["transmission_excess_loss_mw"] == 424
    beneficial = interaction_metrics(2800., 2810., 500., 4000.)
    assert beneficial["interaction_fraction"] < 0


def test_all_interaction_directions_and_load_sizes(electrical_case):
    _, _, periods, baseline, stress = electrical_case
    groups = build_groups(stress, periods[0])
    result = run_interactions(periods, baseline, groups, stress, pair_count=1, loads_mw=(5., 10.))
    assert len(result["records"]) == 4
    assert result["candidate_coverage"] == ["A", "B"]
    for row in result["records"]:
        assert row["transmission_excess_loss_mw"] == pytest.approx(0)
        expected = row["added_load_mw"] if row["target_bus"] == "A" else 0
        assert row["capacity_loss_mw"] == pytest.approx(expected)
    summary = summarize_validation(result, groups)
    assert all(n == 4 for n in summary["candidate_test_counts"].values())
    assert all(g["status"] == "limited_evidence" for g in summary["overlapping_group_validation"])


def test_report_artifacts_and_html_escaping(electrical_case):
    root, _, periods, baseline, stress = electrical_case
    groups = build_groups(stress, periods[0])
    interaction = run_interactions(periods, baseline, groups, stress, pair_count=1, loads_mw=(5., 10.))
    validation = summarize_validation(interaction, groups)
    write_tables(root, baseline, stress, groups, validation)
    render_report(root, {"horizon": 2, "solver": "<unsafe>"}, baseline, stress, groups, interaction, validation)
    document = (root / "report.html").read_text()
    assert "&lt;unsafe&gt;" in document and "<unsafe>" not in document
    assert len(list(csv.DictReader((root / "bus_groups.csv").open()))) == 2
    assert (root / "group_validation.csv").exists() and (root / "ptdf_distances.csv").exists()


def test_cache_fingerprints_prevent_stale_baseline(electrical_case):
    root, pool, _, baseline, _ = electrical_case
    module = Path(__file__).resolve().parents[1] / "src/team_strategy/clustering"
    payload = {"scenario_sha256": scenario_fingerprint(root), "solver": "highs",
               "candidate_pool": json.loads(json.dumps(asdict(pool))),
               "source_sha256": {n: file_fingerprint(module / n) for n in ("candidates.py", "bottlenecks.py")},
               "results": [asdict(b) for b in baseline]}
    path = root / "cached.json"
    # Keep cache outside the scenario directory: its contents affect scenario fingerprints.
    external = root.parent / f"{root.name}-cached.json"
    try:
        external.write_text(json.dumps(payload))
        assert load_baseline(external, pool, root, "highs") == baseline
        payload["source_sha256"]["bottlenecks.py"] = "stale"
        external.write_text(json.dumps(payload))
        with pytest.raises(ValueError, match="changed"): load_baseline(external, pool, root, "highs")
    finally:
        external.unlink(missing_ok=True)


@pytest.mark.parametrize("backend", ["highs", "gurobi"])
def test_backend_directions_and_sensitivities(electrical_case, backend):
    if backend == "gurobi":
        from tools.activsg2000.dcopf import gurobi_is_available
        if not gurobi_is_available():
            pytest.skip("full-size Gurobi license unavailable")
    period = electrical_case[2][0]
    reverse = replace(period,
        buses=tuple(replace(b, demand_mw=10. if b.bus_id == "A" else 0.) for b in period.buses),
        generators=tuple(replace(g, bus_id="B") for g in period.generators))
    model = HostingLP(reverse, solver_backend=backend); model.set_period(reverse)
    diagnosis = model.diagnose("A")
    assert diagnosis.hosting_capacity_mw == pytest.approx(30)
    assert diagnosis.tight_lines[0].direction == "lower"
    assert diagnosis.tight_lines[0].capacity_shadow_mw_per_mw == pytest.approx(1)
    assert diagnosis.duality_gap_mw < 1e-7


def test_pair_sample_covers_all_101_candidates_and_is_reproducible():
    buses = [f"{i:04d}" for i in range(101)]
    groups = {"ptdf": {"bus_ids": buses},
              "signatures": {b: [f"L{i % 5}:upper"] for i, b in enumerate(buses)},
              "normalized_ptdf_distances": [[abs(i - j) / 100 for j in range(101)] for i in range(101)]}
    pairs = select_pairs(groups, pair_count=96, seed=17)
    assert len(pairs) == len(set(pairs)) == 96
    assert {b for pair in pairs for b in pair} == set(buses)
    assert pairs == select_pairs(groups, pair_count=96, seed=17)
    assert pairs != select_pairs(groups, pair_count=96, seed=18)


def test_reused_measurements_are_relabelled_for_new_groups(electrical_case, monkeypatch):
    _, _, periods, baseline, stress = electrical_case
    groups = build_groups(stress, periods[0])
    original = run_interactions(periods, baseline, groups, stress, pair_count=1, loads_mw=(5., 10.))
    changed = deepcopy(groups)
    changed["refined_cohorts"] = [{"cohort_id": "merged", "members": ["A", "B"]}]
    def fail_if_recomputed(*args, **kwargs):
        raise AssertionError("a complete physical cache must avoid repeated LP solves")
    monkeypatch.setattr(HostingLP, "maximize", fail_if_recomputed)
    result = run_interactions(periods, baseline, changed, stress, pair_count=1, loads_mw=(5., 10.),
                              validation_pairs=original["pairs"], cached_records=original["records"])
    assert all(r["same_refined_cohort"] for r in result["records"])
    assert [r["residual_hosting_capacity_mw"] for r in result["records"]] == pytest.approx(
        [r["residual_hosting_capacity_mw"] for r in original["records"]])
    assert all(r["reused_measurement"] or r["reused_stress_scan"] for r in result["records"])


def test_reused_measurements_reject_changed_baseline(electrical_case):
    _, _, periods, baseline, stress = electrical_case
    groups = build_groups(stress, periods[0])
    original = run_interactions(periods, baseline, groups, stress, pair_count=1, loads_mw=(5., 10.))
    original["records"][0]["baseline_hosting_capacity_mw"] += 1
    with pytest.raises(ValueError, match="baseline/candidates differ"):
        run_interactions(periods, baseline, groups, stress, pair_count=1, loads_mw=(5., 10.),
                         cached_records=original["records"])
