"""Part 2 legality, carryover, integrity, and conditional decision tests."""
from dataclasses import replace
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from team_strategy.context import file_fingerprint
from team_strategy.contracts import GRADED_ROUNDS, NamedPlan, Plan, RoundKey, Scenario, SiteProposal
from team_strategy.evaluation.campaign import BatchEvaluator, run_campaign
from team_strategy.experiments.concentration import (load_experiment, make_comparison, verify_cell,
                                                      verify_experiment_inputs, write_report)
from team_strategy.context import scenario_fingerprint
from team_strategy.strategies.corridor_portfolio import CorridorPortfolio
from team_strategy.validation import validate_plan


def test_capacity_weights_and_resource_ratio(context):
    strategy = CorridorPortfolio(("1", "2", "3"), (.2, .3, .5), .5)
    p = strategy.propose(context)
    assert [s.connection_mw for s in p.sites] == pytest.approx([100, 150, 250])
    assert sum(s.generator_mw for s in p.sites) == 250
    assert validate_plan(p, context).valid
    assert p == strategy.propose(context)
    small = strategy.propose(replace(context, connection_budget_mw=100))
    assert sum(s.connection_mw for s in small.sites) == 100


@pytest.mark.parametrize("kwargs", [
    {"bus_ids": ("1", "1")}, {"bus_ids": ("1", "2"), "weights": (.4, .4)},
    {"bus_ids": ("1", "2"), "weights": (0., 1.)}, {"weights": (1.,)},
    {"generator_fraction": -1}, {"generator_fraction": 1.1},
    {"generator_fraction": float("nan")}, {"generator_fraction": True},
    {"bus_ids": ("1",), "weights": (True,)},
])
def test_invalid_portfolios(kwargs):
    with pytest.raises(ValueError): CorridorPortfolio(**kwargs)


def test_active_context_limits(context):
    with pytest.raises(ValueError, match="unknown bus"):
        CorridorPortfolio(("missing",)).propose(context)
    with pytest.raises(ValueError, match="active rules"):
        CorridorPortfolio(("1",), generator_fraction=1).propose(replace(context, max_generator_to_connection_ratio=.5))


def test_default_experiment_is_matched_and_part1_verified():
    root = Path(__file__).resolve().parents[1]
    config, evidence = load_experiment(root / "configs/experiments/corridor_part2.json", root)
    assert len(config["portfolios"]) == 9 and len(config["scenarios"]) == 5
    assert len(evidence) == 3
    assert {p["generator_fraction"] for p in config["portfolios"] if p["role"] == "primary"} == {0.}
    assert not next(s for s in config["scenarios"] if s["name"] == "solo")["include_in_risk"]


def test_joint_fallback_is_not_accepted_as_a_matched_score(tmp_path, context, monkeypatch):
    import team_strategy.evaluation.campaign as adapter
    bad = SimpleNamespace(rejected_submissions=(), competition_scope="individual_fallback",
                          team_scores=(SimpleNamespace(team_id=context.team_id, valid=True, feasible=True),))
    monkeypatch.setattr(adapter, "evaluate_csv_batch", lambda *args, **kwargs: bad)
    monkeypatch.setattr(adapter, "write_batch_outputs", lambda *args, **kwargs: None)
    with pytest.raises(RuntimeError, match="full joint evaluation failed"):
        BatchEvaluator(tmp_path).evaluate(context=context, our_plan=CorridorPortfolio().propose(context),
                                         scenario=Scenario("test", (), 17))


def test_duplicate_team_ids_rejected(tmp_path, context):
    plan = CorridorPortfolio().propose(context)
    with pytest.raises(ValueError, match="distinct"):
        BatchEvaluator(tmp_path).evaluate(context=context, our_plan=plan,
            scenario=Scenario("test", (NamedPlan(context.team_id, plan),), 17))


def test_full_campaign_carries_all_teams_and_resets_weeks(tmp_path):
    root = Path(__file__).resolve().parents[1]
    result = run_campaign(strategy=CorridorPortfolio(("1",), generator_fraction=1),
        opponent_strategies=(("rival", CorridorPortfolio(("2",), generator_fraction=1)),),
        scenario_name="toy", seed=17, output_dir=tmp_path / "campaign",
        release_file=root / "configs/rounds/finalized_release_500mw.json",
        scenario_dir=root / "ercot-connection-game/data/teaching/ieee14_demo_representative",
        rules_file=root / "ercot-connection-game/data/teaching/dispatch_scoring_rules_ieee14_demo_representative_v1.json")
    assert result["status"] == "complete"
    rounds = {r["round"]: r for r in result["rounds"]}
    assert set(rounds) == {r.key for r in GRADED_ROUNDS}
    assert rounds['week-2-submission-1']['scenario_sha256'] == rounds['week-3-submission-1']['scenario_sha256']
    assert all(c['team_ids'] == ['our-team', 'rival'] for c in result['carryovers'])
    assert not rounds['week-2-submission-2']['energy_cost_enabled']
    assert rounds['week-3-submission-1']['energy_cost_enabled']
    for week in [2, 3]:
        a, b = rounds[f'week-{week}-submission-1'], rounds[f'week-{week}-submission-2']
        assert a['scenario_sha256'] != b['scenario_sha256']
        assert {s['site_id'] for s in a['site_allocations']}.isdisjoint(s['site_id'] for s in b['site_allocations'])
        assert b['scenario_sha256'] == result['carryovers'][week - 2]['carried_scenario_sha256']
    assert result['campaign_score_usd'] == pytest.approx(sum(r['score_usd'] for r in rounds.values()))


def synthetic_cells(tmp_path):
    portfolios = [{"name": name, "role": role, "bus_ids": ["1"], "weights": [1.],
                   "generator_fraction": 1. if role == "benchmark" else 0., "description": "<example>"}
                  for name, role in [("a", "primary"), ("b", "primary"), ("benchmark", "benchmark")]]
    scenarios = [{"name": name, "include_in_risk": name != "solo", "rival_bus_ids": [], "rival_generator_fraction": 0.}
                 for name in ["stress1", "stress2", "solo"]]
    scores = {"a": [60., 40., 1000.], "b": [50., 49., 0.], "benchmark": [100., 100., 2000.]}
    cells = {}
    for p in portfolios:
        for i, s in enumerate(scenarios):
            folder = tmp_path / p['name'] / s['name']; folder.mkdir(parents=True)
            rounds = [{"round": r.key, "score_usd": scores[p['name']][i] * 1e9 / 4,
                       "service_fraction": 1., "score_breakdown": {"grid_energy_cost_usd": 0., "generator_operating_cost_usd": 0.}}
                      for r in GRADED_ROUNDS]
            result = {"status": "complete", "portfolio": p['name'], "role": p['role'], "scenario": s['name'],
                      "rounds": rounds, "include_in_risk": s['include_in_risk'], "campaign_score_usd": scores[p['name']][i] * 1e9}
            path = folder / "campaign.json"; path.write_text(json.dumps(result))
            cells[p['name'] + '/' + s['name']] = {"status": "complete", "output": str(folder), "result": result,
                                                 "artifact_sha256": {"campaign.json": file_fingerprint(path)}}
    return {"portfolios": portfolios, "scenarios": scenarios}, cells


def test_maximin_mean_and_regret_are_separate_and_benchmark_excluded(tmp_path):
    config, cells = synthetic_cells(tmp_path)
    comparison = make_comparison(config, cells)
    assert comparison['maximin_primary'] == 'b'
    assert comparison['best_mean_primary'] == 'a'
    assert comparison['minimax_regret_primary'] == 'a'
    assert comparison['primary_pareto_frontier'] == ['a', 'b']
    assert comparison['risk_scenarios'] == ['stress1', 'stress2']
    assert next(r for r in comparison['summary'] if r['name'] == 'a')['scenario_count'] == 2


def test_missing_campaign_never_becomes_zero(tmp_path):
    config, cells = synthetic_cells(tmp_path)
    del cells['b/stress2']
    with pytest.raises(ValueError, match="missing matched scenarios"):
        make_comparison(config, cells)


def test_cached_results_must_match_their_evidence(tmp_path):
    _, cells = synthetic_cells(tmp_path)
    cell = next(iter(cells.values()))
    assert verify_cell(cell)
    cell['result']['campaign_score_usd'] += 1
    with pytest.raises(ValueError, match="scores differ"):
        verify_cell(cell)


def test_artifact_tampering_is_detected(tmp_path):
    _, cells = synthetic_cells(tmp_path)
    cell = next(iter(cells.values()))
    (Path(cell['output']) / 'campaign.json').write_text('{}')
    with pytest.raises(ValueError, match="evidence changed"):
        verify_cell(cell)


def test_report_and_recommendation_export(tmp_path):
    config, cells = synthetic_cells(tmp_path)
    comparison = make_comparison(config, cells)
    write_report(tmp_path, config, comparison, cells)
    assert '&lt;example&gt;' in (tmp_path / 'report.html').read_text()
    spec = json.loads((tmp_path / 'recommended_strategy.json').read_text())
    assert spec['strategy'] == 'corridor_portfolio'
    assert (tmp_path / 'comparison.csv').exists() and (tmp_path / 'rounds.csv').exists()


def test_all_input_fingerprints_are_rechecked(tmp_path):
    root = tmp_path
    (root/'network').mkdir();(root/'network/data').write_text('network')
    (root/'part1').mkdir()
    for name in ['manifest','groups','interactions']:(root/f'part1/{name}.json').write_text('{}')
    for name in ['config.json','rules.json','release.json','source.py']:(root/name).write_text('{}')
    config={'scenario_directory':'network','rules_file':'rules.json','release_file':'release.json','part1_directory':'part1'}
    identity={'config_sha256':file_fingerprint(root/'config.json'),'scenario_sha256':scenario_fingerprint(root/'network'),
              'rules_sha256':file_fingerprint(root/'rules.json'),'release_sha256':file_fingerprint(root/'release.json'),
              'source_sha256':{'source.py':file_fingerprint(root/'source.py')},
              'part1_sha256':{n:file_fingerprint(root/f'part1/{n}.json') for n in ['manifest','groups','interactions']}}
    verify_experiment_inputs(root,root/'config.json',config,identity)
    (root/'rules.json').write_text('{"changed":true}')
    with pytest.raises(ValueError,match='economic inputs changed'):
        verify_experiment_inputs(root,root/'config.json',config,identity)
