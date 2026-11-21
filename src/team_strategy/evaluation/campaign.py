"""Full instructor evaluation, with explicit all-team S1 withdrawal carryover.

No replacement dispatch, allocation, or scoring is implemented. Every graded
submission is evaluated over the entire horizon. S1 sites become fixed net
withdrawal in S2 and are neither rebuilt nor scored again. Weeks reset.
"""
from dataclasses import asdict, dataclass, replace
import json
import math
from pathlib import Path

from ercot_game.batch_evaluation import evaluate_csv_batch, load_scoring_rules, write_batch_outputs
from ercot_game.base_load import (materialize_base_load_artifact, net_withdrawal_by_bus,
                                  site_net_withdrawal_rows, write_site_net_withdrawal)

from ..context import assert_inputs_current, file_fingerprint, load_context, scenario_fingerprint
from ..contracts import (EvaluationResult, EvaluationStatus, NamedPlan, RoundKey, Scenario,
                         ScoreBreakdown, SiteAllocation)
from ..submissions.csv_export import export_plan, site_ids


def save_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


@dataclass
class RoundOutcome:
    result: EvaluationResult
    evaluation: object
    summary: dict
    input_files: dict[str, Path]


class BatchEvaluator:
    """Evaluator protocol adapter; output folders are immutable per round."""
    def __init__(self, output_dir: Path, *, workers=1, solver_backend="highs", storage_solver="benders"):
        self.output_dir = Path(output_dir)
        self.workers, self.solver_backend = workers, solver_backend
        self.storage_solver = storage_solver

    def evaluate(self, *, context, our_plan, scenario):
        return self.evaluate_round(context=context, our_plan=our_plan, scenario=scenario).result

    def evaluate_round(self, *, context, our_plan, scenario, reserved_by_team=None):
        assert_inputs_current(context)
        reserved = {} if reserved_by_team is None else reserved_by_team
        plans = (NamedPlan(context.team_id, our_plan), *scenario.opponents)
        ids = [p.team_id for p in plans]
        if len(ids) != len(set(ids)):
            raise ValueError("team IDs must be distinct, including our team")
        destination = self.output_dir / context.round.key
        destination.mkdir(parents=True, exist_ok=False)
        inputs = destination / "inputs"; inputs.mkdir()
        files = {}
        for number, named in enumerate(plans):
            team_context = replace(context, team_id=named.team_id,
                                   prior_site_ids=frozenset(reserved.get(named.team_id, ())))
            path = inputs / f"team-{number:03d}.csv"
            export_plan(named.plan, team_context, path)
            files[named.team_id] = path
        rules = load_scoring_rules(context.rules_file, artifact_dir=context.scenario_dir, horizon=context.horizon)
        evaluation = evaluate_csv_batch(
            inputs, artifact_dir=context.scenario_dir, horizon=context.horizon, rules=rules,
            dispatch_workers=self.workers, storage_parallel_workers=self.workers,
            storage_solver_backend=self.solver_backend, storage_solver=self.storage_solver,
            submission_number=context.round.submission,
            energy_cost_enabled=context.energy_cost_enabled, reserved_site_ids_by_team=reserved,
        )
        canonical = destination / "canonical"
        write_batch_outputs(evaluation, canonical, scenario_version=context.scenario_fingerprint,
                            evaluator_version="instructor-ercot-game-0.3", period_indices=tuple(range(context.horizon)),
                            output_mode="compact")
        if (evaluation.rejected_submissions or set(s.team_id for s in evaluation.team_scores) != set(ids)
                or any(not s.valid or not s.feasible for s in evaluation.team_scores)
                or evaluation.competition_scope not in {"joint", "joint_projection"}):
            raise RuntimeError("full joint evaluation failed; inspect canonical diagnostics; no synthetic score substituted")
        if evaluation.dispatch is None or len(evaluation.dispatch.periods) != context.horizon:
            raise RuntimeError("full-horizon joint dispatch missing")
        score = next(s for s in evaluation.team_scores if s.team_id == context.team_id)
        breakdown = ScoreBreakdown(score.it_value, score.energy_cost, score.generator_operating_cost,
                                    score.generator_capital_cost, score.storage_capital_cost, score.site_cost)
        if abs(breakdown.total_usd - score.score) > max(1., abs(score.score) * 1e-10):
            raise RuntimeError("score does not match instructor economic components")
        requested = {s: site.connection_mw for s, site in zip(site_ids(our_plan, context), our_plan.sites, strict=True)}
        ours = next(p for p in evaluation.evaluated_plans if p.team_id == context.team_id)
        allocated = ({c.connection_id: c.capacity_mw for c in ours.connections} if ours.connections
                     else {s.site_id: s.connection_capacity_mw for s in ours.sites})
        allocations = tuple(SiteAllocation(s, allocated.get(s, 0.) / mw, mw, allocated.get(s, 0.))
                            for s, mw in requested.items())
        fraction = math.fsum(a.allocated_connection_mw for a in allocations) / math.fsum(requested.values())
        result = EvaluationResult(EvaluationStatus.VALID, score.score, fraction, destination,
                                  score_breakdown=breakdown, site_allocations=allocations)
        weighted_hours = math.fsum(rules.weight_for(i) for i in range(context.horizon)) / rules.present_value_factor
        if abs(score.served_load_mwh - fraction * math.fsum(requested.values()) * weighted_hours) > 1.:
            raise RuntimeError("served energy and site allocation disagree")
        summary = {"round": context.round.key, "status": "valid", "score_usd": score.score,
                   "service_fraction": fraction, "score_breakdown": asdict(breakdown),
                   "site_allocations": [asdict(a) for a in allocations],
                   "team_scores": [asdict(s) for s in evaluation.team_scores],
                   "competition_scope": evaluation.competition_scope,
                   "scenario_sha256": context.scenario_fingerprint, "rules_sha256": context.rules_fingerprint,
                   "input_sha256_by_team": {team: file_fingerprint(path) for team, path in files.items()},
                   "energy_cost_enabled": context.energy_cost_enabled, "horizon": context.horizon}
        save_json(destination / "round.json", summary)
        assert_inputs_current(context)
        return RoundOutcome(result, evaluation, summary, files)


def run_campaign(*, strategy, opponent_strategies, scenario_name, seed, output_dir, release_file,
                 scenario_dir, rules_file, workers=1, solver_backend="highs", team_id="our-team",
                 storage_solver="benders"):
    """Evaluate W2S1,W2S2,W3S1,W3S2; each candidate has its own carried package."""
    output_dir = Path(output_dir); output_dir.mkdir(parents=True, exist_ok=False)
    evaluator = BatchEvaluator(output_dir, workers=workers, solver_backend=solver_backend, storage_solver=storage_solver)
    rounds, carryovers = [], []
    for week in (2, 3):
        # Always start each week from the original scenario.
        reserved, active_scenario = {}, Path(scenario_dir)
        for submission in (1, 2):
            context = load_context(release_file=release_file, rules_file=rules_file,
                                   scenario_dir=active_scenario, round=RoundKey(week, submission),
                                   team_id=team_id, seed=seed, prior_site_ids=frozenset(reserved.get(team_id, ())))
            our_plan = strategy.propose(context)
            opponents = tuple(NamedPlan(owner, rival.propose(replace(context, team_id=owner,
                              prior_site_ids=frozenset(reserved.get(owner, ())))))
                              for owner, rival in opponent_strategies)
            scenario = Scenario(scenario_name, opponents, seed)
            outcome = evaluator.evaluate_round(context=context, our_plan=our_plan, scenario=scenario,
                                                reserved_by_team=reserved)
            rounds.append(outcome.summary)
            if submission == 1:
                all_plans = (NamedPlan(team_id, our_plan), *opponents)
                reserved = {p.team_id: frozenset(site_ids(p.plan, context)) for p in all_plans}
                rows = site_net_withdrawal_rows(outcome.evaluation)
                owners = {r["team_id"] for r in rows}
                if owners != {p.team_id for p in all_plans}:
                    raise RuntimeError("Submission 1 withdrawal is missing teams")
                withdrawal_file = output_dir / f"week-{week}-s1-withdrawal.csv"
                write_site_net_withdrawal(rows, withdrawal_file)
                withdrawals = net_withdrawal_by_bus(rows, context.horizon)
                active_scenario = output_dir / f"week-{week}-s2-base"
                carried = materialize_base_load_artifact(
                    scenario_dir, withdrawals, active_scenario, validate=True, workers=workers,
                    provenance={"scenario": scenario_name, "source_round": context.round.key,
                                "withdrawal_sha256": file_fingerprint(withdrawal_file)},
                )
                carryovers.append({"week": week, "source_scenario_sha256": scenario_fingerprint(Path(scenario_dir)),
                                   "withdrawal_sha256": file_fingerprint(withdrawal_file),
                                   "team_ids": sorted(owners), "carried_scenario_sha256": scenario_fingerprint(active_scenario),
                                   "validation": carried["validation"]})
    result = {"status": "complete", "scenario": scenario_name, "seed": seed,
              "rounds": rounds, "carryovers": carryovers,
              "campaign_score_usd": math.fsum(r["score_usd"] for r in rounds)}
    save_json(output_dir / "campaign.json", result)
    return result
