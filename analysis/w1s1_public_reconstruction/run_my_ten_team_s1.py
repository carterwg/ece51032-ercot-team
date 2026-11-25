"""Edit OUR_SUBMISSION_CSV, then run this file to rank ten W1S1 teams.

From the repository root:
    .venv/bin/python analysis/w1s1_public_reconstruction/run_my_ten_team_s1.py

The nine fixed rivals are the eight plans inferred from the public W1S1 CSV,
plus an exact copy of the inferred 25 x 20 MW, G1-per-site plan. Their original
private CSVs are unavailable, so this is the calibrated reconstruction.
Each run uses the unchanged 120-period course evaluator and saves its inputs,
ranking.json, and canonical diagnostics under runs/w1s1-my-ten-team-s1/.
"""

from __future__ import annotations

from dataclasses import asdict, replace
from datetime import datetime
import json
from pathlib import Path
import secrets
import sys


# ---------------------------------------------------------------------------
# EDIT ONLY THIS CSV BLOCK FOR YOUR TEAM. Add or remove site rows as needed.
# Keep the header exactly as shown. Use team07 in every row. The total requested
# connection capacity must be at most 500 MW. For a four-hour battery, enter
# storage_energy_mwh = 4 * storage_power_mw; use 0,0 for no battery.
# Site IDs must be unique within this submission. You may reuse a bus ID.
# ---------------------------------------------------------------------------
OUR_SUBMISSION_CSV = """\
team_id,site_id,bus_id,connection_capacity_mw,generator_capacity_mw,storage_power_mw,storage_energy_mwh
team07,w1-s1-0001,6141,100,1,0,0
team07,w1-s1-0002,5260,100,1,0,0
team07,w1-s1-0003,8126,100,1,0,0
team07,w1-s1-0004,3046,100,1,0,0
team07,w1-s1-0005,2011,100,1,0,0
"""


REPO = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(REPO / "src"), str(REPO / "ercot-connection-game" / "src"),
                str(REPO / "ercot-connection-game")]

from ercot_game.batch_evaluation import evaluate_csv_batch, load_scoring_rules, write_batch_outputs
from ercot_game.csv_submission import read_student_csv
from team_strategy.context import load_context
from team_strategy.contracts import RoundKey
from team_strategy.submissions.csv_export import export_plan

from week1_public_reconstruction import make_plans


RIVAL_LABELS = {
    "rival-20mw-x25": "25 x 20 MW, G1 each",
    "rival-20mw-x25-copy": "25 x 20 MW, G1 each (copy)",
    "rival-100mw-g20": "5 x 100 MW, G20 each",
    "rival-500mw-g350": "500 MW, G350",
    "rival-250mw-hybrid": "2 x 250 MW, hybrid",
    "rival-100mw-mixed": "5 x 100 MW, mixed generation",
    "rival-250mw-grid": "2 x 250 MW, grid only",
    "rival-100mw-grid": "5 x 100 MW, grid only",
    "rival-5mw-x100": "100 x 5 MW, grid only",
    "team07": "Our team",
}


def main() -> None:
    context = load_context(
        release_file=REPO / "configs/rounds/finalized_release_500mw.json",
        rules_file=REPO / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=REPO / "ercot-connection-game/data/processed/activsg2000_representative_v1",
        round=RoundKey(1, 1), team_id="team07", seed=20261123,
    )
    rules = load_scoring_rules(context.rules_file, artifact_dir=context.scenario_dir,
                               horizon=context.horizon)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = REPO / "runs/w1s1-my-ten-team-s1" / f"{stamp}-{secrets.token_hex(3)}"
    inputs = run_dir / "inputs"
    inputs.mkdir(parents=True)

    own_csv = inputs / "team-000.csv"
    own_csv.write_text(OUR_SUBMISSION_CSV.strip() + "\n", encoding="utf-8")
    try:
        own_submission = read_student_csv(
            own_csv, bus_ids=context.bus_ids, horizon=context.horizon,
            max_generator_to_connection_ratio=context.max_generator_to_connection_ratio,
            max_team_connection_capacity_mw=context.connection_budget_mw,
        )
    except ValueError as exc:
        raise SystemExit(f"Your CSV is invalid: {exc}") from None
    if own_submission.team_id != context.team_id:
        raise ValueError(f"CSV team_id must be {context.team_id}, got {own_submission.team_id}")

    _, inferred_rivals = make_plans(
        REPO / "analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv"
    )
    leader = next(rival for rival in inferred_rivals if rival.team_id == "rival-20mw-x25")
    rivals = (*inferred_rivals, replace(leader, team_id="rival-20mw-x25-copy"))
    for index, rival in enumerate(rivals, start=1):
        export_plan(rival.plan, replace(context, team_id=rival.team_id),
                    inputs / f"team-{index:03d}.csv")

    print(f"Evaluating {len(own_submission.plan.sites)} of your sites against nine fixed rivals...",
          flush=True)
    print(f"Run folder: {run_dir}", flush=True)
    evaluation = evaluate_csv_batch(
        inputs, artifact_dir=context.scenario_dir, horizon=context.horizon, rules=rules,
        dispatch_workers=2, storage_parallel_workers=2,
        storage_solver_backend="highs", storage_solver="monolithic",
        submission_number=1, energy_cost_enabled=context.energy_cost_enabled,
    )
    scores = sorted(evaluation.team_scores, key=lambda score: score.rank)
    if (len(scores) != 10 or evaluation.rejected_submissions
            or any(not score.valid or not score.feasible for score in scores)
            or evaluation.competition_scope not in {"joint", "joint_projection"}
            or evaluation.dispatch is None
            or len(evaluation.dispatch.periods) != context.horizon):
        write_batch_outputs(
            evaluation, run_dir / "canonical", scenario_version=context.scenario_fingerprint,
            evaluator_version="instructor-ercot-game-0.3",
            period_indices=tuple(range(context.horizon)), output_mode="compact",
        )
        raise RuntimeError(f"Full ten-team evaluation did not complete; inspect {run_dir / 'canonical'}")

    write_batch_outputs(
        evaluation, run_dir / "canonical", scenario_version=context.scenario_fingerprint,
        evaluator_version="instructor-ercot-game-0.3",
        period_indices=tuple(range(context.horizon)), output_mode="compact",
    )
    allocated = {owner.team_id: sum(site.connection_capacity_mw for site in owner.sites)
                 for owner in evaluation.evaluated_plans}
    rankings = [
        {"rank": score.rank, "team_id": score.team_id,
         "team_plan": RIVAL_LABELS[score.team_id],
         "allocated_mw": allocated[score.team_id],
         "score_usd": score.score}
        for score in scores
    ]
    result = {
        "description": "W1S1; eight reconstructed rivals plus a copy of the 25 x 20 MW rival",
        "all_teams_valid_feasible": True,
        "class_allocated_mw": sum(allocated.values()),
        "our_submission": [asdict(site) for site in own_submission.plan.sites],
        "rankings": rankings,
    }
    (run_dir / "ranking.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print("\nW1S1 ten-team result (all teams jointly reallocated)")
    print("| Rank | Team plan | Allocated MW | Score ($B) |")
    print("| ---: | --- | ---: | ---: |")
    for row in rankings:
        print(f"| {row['rank']} | {row['team_plan']} | {row['allocated_mw']:.3f} "
              f"| {row['score_usd'] / 1e9:.6f} |")
    print(f"\nClass allocated: {result['class_allocated_mw']:.3f} MW")
    print(f"Saved: {run_dir / 'ranking.json'}")


if __name__ == "__main__":
    main()
