"""Submission-dependent resources, equal geometry budgets, and actual CSV checks."""
from dataclasses import replace
import csv
import json
from pathlib import Path

import pytest

from team_strategy.contracts import RoundKey
from team_strategy.evaluation.campaign import run_campaign
from team_strategy.experiments.submission_schedule import check_requested_resources, render_report
from team_strategy.strategies import build_strategy
from team_strategy.strategies.corridor_portfolio import CorridorPortfolio
from team_strategy.strategies.submission_generation import SubmissionGenerationPortfolio
from team_strategy.validation import validate_plan


@pytest.mark.parametrize("week,submission", [(2, 1), (2, 2), (3, 1), (3, 2)])
def test_resource_totals_are_matched_across_layouts(context, week, submission):
    ctx = replace(context, round=RoundKey(week, submission))
    plans = [SubmissionGenerationPortfolio(("1",)).propose(ctx),
             SubmissionGenerationPortfolio(("1", "2"), (.5, .5)).propose(ctx)]
    for plan in plans:
        assert validate_plan(plan, ctx).valid
        assert sum(s.connection_mw for s in plan.sites) == 500
        assert sum(s.generator_mw for s in plan.sites) == (500 if submission == 2 else 0)
    assert build_strategy("submission_generation", {"bus_ids": ["1"]}).propose(ctx) == plans[0]


def test_submission_2_still_respects_the_active_generation_cap(context):
    ctx = replace(context, max_generator_to_connection_ratio=.5)
    strategy = SubmissionGenerationPortfolio(("1",))
    assert validate_plan(strategy.propose(ctx), ctx).valid
    with pytest.raises(ValueError, match="active rules"):
        strategy.propose(replace(ctx, round=RoundKey(2, 2)))


def test_ten_team_experiment_crosses_primary_layouts_and_schedules():
    from team_strategy.experiments.ten_teams import ROOT, define_experiment, PRIMARY_POLICIES

    config = define_experiment(ROOT)
    assert config['team_count'] == 10 and config['capacity_per_submission_mw'] == 500
    assert all(s['rival_count'] == 9 for s in config['scenarios'])
    assert {len(s['rival_plan']['bus_ids']) for s in config['scenarios']} == {1, 2, 5}
    for layout, spec in config['layouts'].items():
        policies = [p for p in config['portfolios'] if p['layout'] == layout and p['role'] == 'primary']
        assert len(policies) == 3
        assert {tuple(p['generation_schedule'].values()) for p in policies} == set(PRIMARY_POLICIES.values())
        assert all(p['bus_ids'] == spec['bus_ids'] and p['weights'] == spec['weights'] for p in policies)


def test_actual_csv_verification_rejects_wrong_round_resources():
    p = {"bus_ids": ["1", "2"], "weights": [.5, .5]}
    rows = [{"team_id": "our-team", "bus_id": b, "connection_capacity_mw": "250", "generator_capacity_mw": "250",
             "storage_power_mw": "0", "storage_energy_mwh": "0"} for b in p["bus_ids"]]
    check_requested_resources(rows, p, 2)
    with pytest.raises(ValueError, match="submission schedule"):
        check_requested_resources(rows, p, 1)
    for row in rows: row["generator_capacity_mw"] = "0"
    check_requested_resources(rows, p, 1)
    with pytest.raises(ValueError, match="submission schedule"):
        check_requested_resources(rows, p, 2)


def test_full_scheduled_campaign_keeps_s1_grid_only_and_adds_new_s2_generators(tmp_path):
    root = Path(__file__).resolve().parents[1]
    output = tmp_path/"campaign"
    result = run_campaign(strategy=SubmissionGenerationPortfolio(("1", "2"), (.5, .5)),
        opponent_strategies=(("rival", CorridorPortfolio(("3",))),), scenario_name="scheduled", seed=17,
        output_dir=output, release_file=root/"configs/rounds/finalized_release_500mw.json",
        scenario_dir=root/"ercot-connection-game/data/teaching/ieee14_demo_representative",
        rules_file=root/"ercot-connection-game/data/teaching/dispatch_scoring_rules_ieee14_demo_representative_v1.json")
    for r in result["rounds"]:
        submission = int(r["round"][-1])
        with (output/r["round"]/"inputs/team-000.csv").open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        check_requested_resources(rows, {"bus_ids": ["1", "2"], "weights": [.5, .5]}, submission)
        if submission == 2: assert r["service_fraction"] == pytest.approx(1., abs=1e-6)
    assert all(c["team_ids"] == ["our-team", "rival"] for c in result["carryovers"])
    assert result["rounds"][0]["scenario_sha256"] == result["rounds"][2]["scenario_sha256"]


def test_report_exports_the_scheduled_strategy_and_uses_millions_for_siting_gains(tmp_path):
    portfolios = [{"name": "concentrate_6141", "bus_ids": ["1"], "weights": [1.]},
                  {"name": "split", "bus_ids": ["1", "2"], "weights": [.5, .5]}]
    scenarios = [{"name": name, "rival_bus_ids": [], "rival_generator_fraction": 0., "include_in_risk": name != "solo"}
                 for name in ["solo", "a", "b"]]
    scores = {"concentrate_6141": {"solo": 70e9, "a": 69e9, "b": 69e9},
              "split": {"solo": 70e9, "a": 69.01e9, "b": 69.03e9}}
    comparison = {"maximin_primary": "split", "risk_scenarios": ["a", "b"],
                  "campaign_scores_usd": scores, "summary": [{"name": p["name"]} for p in portfolios]}
    reference = {p+"/"+s: {"result": {"campaign_score_usd": 67e9}}
                 for p in ["concentrate_6141", "carter_cg_benchmark"] for s in ["a", "b"]}
    render_report(tmp_path, {"portfolios": portfolios, "scenarios": scenarios}, comparison,
                  {}, [{"service_fraction": 1.}], reference)
    config = json.loads((tmp_path/"recommended_strategy.json").read_text())
    assert config["strategy"] == "submission_generation"
    assert config["params"] == {"bus_ids": ["1", "2"], "weights": [.5, .5]}
    insights = json.loads((tmp_path/"interpretation.json").read_text())
    assert insights["best_split_minus_best_concentrated_mean_million_usd"] == pytest.approx(20.)
    assert "zero generation in S1" in (tmp_path/"report.html").read_text()
