"""Reject unfair or incomplete combinations of separately evaluated matrices."""
from copy import deepcopy
import json

import pytest

from team_strategy.context import file_fingerprint
from team_strategy.contracts import GRADED_ROUNDS
from team_strategy.experiments.pool_comparisons import (combine_specifications, pool_runs,
                                                       verify_matrix, verify_site_permutation,
                                                       write_interpretation)


def specifications():
    base = {"seed": 17, "capacity_per_submission_mw": 500,
            "portfolios": [{"name": "a", "role": "primary", "generator_fraction": 0.},
                           {"name": "b", "role": "primary", "generator_fraction": 0.}],
            "scenarios": [{"name": "s1", "rival_bus_ids": ["1"], "include_in_risk": True}],
            "assumptions": "test"}
    other = deepcopy(base); other["scenarios"][0]["name"] = "s2"
    identity = {"config_sha256": "config1", "scenario_sha256": "network", "rules_sha256": "rules",
                "source_sha256": {"model.py": "source"}, "solver": "highs"}
    second = {**identity, "config_sha256": "config2"}
    return [base, other], [identity, second]


def test_disjoint_scenarios_keep_same_resource_menu():
    configs, identities = specifications()
    merged = combine_specifications(configs, identities)
    assert [s["name"] for s in merged["scenarios"]] == ["s1", "s2"]
    assert merged["portfolios"] == configs[0]["portfolios"]


def test_retry_may_permute_rows_without_changing_bus_capacity():
    original = {"name": "split", "bus_ids": ["1", "2"], "weights": [.25, .75], "generator_fraction": 0.}
    verify_site_permutation(original, {**original, "bus_ids": ["2", "1"], "weights": [.75, .25]})


@pytest.mark.parametrize("changes", [{"bus_ids": ["2", "1"]}, {"generator_fraction": 1.},
                                      {"bus_ids": ["1", "1"]}])
def test_retry_cannot_hide_a_changed_resource_plan(changes):
    original = {"name": "split", "bus_ids": ["1", "2"], "weights": [.25, .75], "generator_fraction": 0.}
    with pytest.raises(ValueError, match="physical portfolio"):
        verify_site_permutation(original, {**original, **changes})


@pytest.mark.parametrize("status", ["running", "failed"])
def test_unfinished_runs_cannot_issue_a_report(tmp_path, status):
    run = tmp_path / "run"; run.mkdir()
    (run / "manifest.json").write_text(json.dumps({"status": status}))
    output = tmp_path / "summary"
    with pytest.raises(ValueError, match="only completed"):
        pool_runs(tmp_path, [run], output)
    assert not output.exists()


@pytest.mark.parametrize("change", ["source", "network", "resource", "duplicate", "seed"])
def test_incompatible_matrices_rejected(change):
    configs, identities = specifications()
    if change == "source": identities[1]["source_sha256"] = {"model.py": "changed"}
    if change == "network": identities[1]["scenario_sha256"] = "other"
    if change == "resource": configs[1]["portfolios"][0]["generator_fraction"] = 1.
    if change == "duplicate": configs[1]["scenarios"][0]["name"] = "s1"
    if change == "seed": configs[1]["seed"] = 18
    with pytest.raises(ValueError): combine_specifications(configs, identities)


def matrix(tmp_path):
    configs, identities = specifications(); config, identity = configs[0], identities[0]
    cells = {}
    for p in config["portfolios"]:
        rounds = []
        for key in GRADED_ROUNDS:
            rounds.append({"round": key.key, "score_usd": 80., "status": "valid", "horizon": 120,
                "competition_scope": "joint", "rules_sha256": "rules", "energy_cost_enabled": key.week == 3,
                "scenario_sha256": "network" if key.submission == 1 else f"carry-{key.week}",
                "input_sha256_by_team": {"our-team": p["name"], "rival-01": "matched"},
                "score_breakdown": {"it_value_usd": 100., "grid_energy_cost_usd": 20.},
                "site_allocations": [{"site_id": key.key}]})
        result = {"status": "complete", "portfolio": p["name"], "role": p["role"], "generator_fraction": 0.,
                  "scenario": "s1", "seed": 17, "include_in_risk": True, "campaign_score_usd": 320., "rounds": rounds,
                  "carryovers": [{"week": w, "source_scenario_sha256": "network", "carried_scenario_sha256": f"carry-{w}",
                                  "team_ids": ["our-team", "rival-01"], "validation": {"passed_period_count": 120}} for w in (2, 3)]}
        output = tmp_path / p["name"]; output.mkdir(); path = output / "campaign.json"; path.write_text(json.dumps(result))
        cells[p["name"] + "/s1"] = {"status": "complete", "result": result, "output": str(output),
                                    "artifact_sha256": {"campaign.json": file_fingerprint(path)}}
    return config, cells, identity


def test_evidence_checks_cover_opponents_reset_and_arithmetic(tmp_path):
    config, cells, identity = matrix(tmp_path)
    checks = verify_matrix(config, cells, identity)
    assert checks["campaign_count"] == 2 and checks["evaluation_count"] == 8
    assert checks["matched_opponent_round_count"] == 4


def test_export_keeps_the_successful_retry_order(tmp_path):
    config, cells, _ = matrix(tmp_path)
    config["portfolios"][0].update(bus_ids=["1", "2"], weights=[.25, .75])
    cells["a/s1"]["execution_override"] = {"executed_bus_ids": ["2", "1"], "weights": [.75, .25]}
    for cell in cells.values():
        for r in cell["result"]["rounds"]:
            r["service_fraction"] = .01 if r["round"].endswith("submission-2") else 1.
    comparison = {"maximin_primary": "a", "risk_scenarios": ["s1"],
                  "campaign_scores_usd": {"a": {"s1": 320.}, "b": {"s1": 320.}}}
    (tmp_path / "report.html").write_text('<h2>Candidate plans</h2>')
    write_interpretation(tmp_path, config, comparison, cells)
    params = json.loads((tmp_path / "recommended_strategy.json").read_text())["params"]
    assert params["bus_ids"] == ["2", "1"] and params["weights"] == [.75, .25]


@pytest.mark.parametrize("change", ["missing", "opponent", "sum", "reset", "carry", "fallback"])
def test_evidence_discrepancies_rejected(tmp_path, change):
    config, cells, identity = matrix(tmp_path)
    if change == "missing":
        del cells["b/s1"]
    else:
        cell = cells["b/s1"]; r = cell["result"]; first = r["rounds"][0]
        if change == "opponent": first["input_sha256_by_team"]["rival-01"] = "unmatched"
        if change == "sum": r["campaign_score_usd"] += 1
        if change == "reset": first["scenario_sha256"] = "carry-previous-week"
        if change == "carry": r["carryovers"][0]["team_ids"] = ["our-team"]
        if change == "fallback": first["competition_scope"] = "individual_fallback"
        from pathlib import Path
        path = Path(cell["output"]) / "campaign.json"; path.write_text(json.dumps(r))
        cell["artifact_sha256"]["campaign.json"] = file_fingerprint(path)
    with pytest.raises(ValueError): verify_matrix(config, cells, identity)
