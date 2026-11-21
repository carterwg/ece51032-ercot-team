# Week 1, Submission 1 Screening Experiment

## Purpose and status

This screening campaign creates 67 candidate plans for Team 7, Week 1,
Submission 1. Each plan is generated as a canonical submission CSV, validated,
previewed, and recorded in
[`analysis/run_database.csv`](../analysis/run_database.csv). The per-candidate
inventory and result links are in
[`analysis/week1_experiment_manifest.csv`](../analysis/week1_experiment_manifest.csv).

The three machine-readable candidate lists are:

- [Family A: Single-Bus Battery Sweep](../analysis/week1_submission1_screening/family_a_single_bus_battery_sweep.json)
- [Family B: Diversification Study](../analysis/week1_submission1_screening/family_b_diversification_study.json)
- [Family C: Generator Screening](../analysis/week1_submission1_screening/family_c_generator_screening.json)

The shared experiment ID is `week1_submission1_screening`. Plans are submitted
to the runner in three family batches, sequentially, with the same team, week,
submission, scenario, rules, release, and preview stride.

All three batches completed. The runner appended **67 result rows**: 67 plans
were valid and all 67 previews completed successfully. These statuses describe
the student-preview workflow only; they do not mean that plans were evaluated
with opponents or that battery operation was dispatched. The manifest has been
reconciled to the run database and includes each run's status, metrics, and
artifact paths.

## Candidate count and design

| Family | Design | Count |
|---|---|---:|
| A | Five buses (`2054`, `6062`, `6141`, `6298`, `7414`) × six storage power settings (`0`, `25`, `50`, `75`, `100`, `200` MW); each plan has one 500 MW site and `storage_energy_mwh = 4 × storage_power_mw`. | 30 |
| B | For the same five buses, all unique 2-bus, 3-bus, and 4-bus combinations: `C(5,2)=10`, `C(5,3)=10`, and `C(5,4)=5`. Each plan has exactly 500 MW total connection capacity, split evenly across its sites, and no generator or storage. | 25 |
| C | Buses `2054`, `6062`, and `6298` × generator capacities `0`, `100`, `250`, and `500` MW; each plan has one 500 MW site and no storage. | 12 |
| **Total** | **30 + 25 + 12** | **67** |

Team ID is the string `7`, week is `1`, and submission is `1`. The selected
team release and scoring rules are the finalized 500 MW configuration. Each
candidate individually requests exactly 500 MW of connection capacity, the
per-team submission maximum. In Family C, the 500 MW generator case has
`G = C`, within the release limit. In Family B, the equal shares are represented
as decimal MW values whose sum is 500 MW.

## Evaluation procedure

Every candidate is a separate, solo run. The runner receives one family's
candidate list at a time and, for each candidate:

1. Writes its normalized plan and canonical site CSV under
   `runs/experiments/week1_submission1_screening/<run-id>/`.
2. Validates the CSV against the selected scenario and release rules.
3. Runs the student preview at stride 1 (all 120 representative periods).
4. Saves validation and preview outputs in the run folder.
5. Appends a result row to `analysis/run_database.csv` and lifecycle events to
   `analysis/experiment_log.csv`.

The run database is a row-per-plan result table. The experiment manifest is an
easy-to-filter index of the 67 planned candidates and, when populated, their
run IDs, statuses, metrics, and artifact paths. The detailed raw preview JSON
is authoritative for interpreting the preview result.

## Interpretation limits

- Week 1 is practice/feedback only; these results are not part of the final
  campaign score.
- These are **student-preview** results, not official evaluator results.
- Every candidate is evaluated by itself. The plans do not compete against one
  another or against mock opponents. These results do not estimate shared
  multi-team congestion or allocation.
- The student preview validates and capital-costs storage but leaves battery
  dispatch idle. Family A can screen validity and document candidate sizes,
  but its preview score does **not** measure battery charging/discharging
  benefit. Use the full `ercot-game-batch run` evaluator to assess actual
  battery dispatch and plan value, under both solo and explicit multi-team
  scenarios.
- Family B's split site capacities sum to the same 500 MW request in every
  candidate. The runner preview can compare these location combinations only
  as separate solo requests; it does not prove that the capacities are
  additive under competition.
- Each candidate has the same total connection capacity, but equipment differs
  within Families A and C. Interpret score differences alongside score
  components, service fraction, allocation, and costs, not as a pure bus
  ranking.

## Re-running

From the team repository root, the family batches can be run with:

```powershell
python .\src\experiment_runner.py `
  --plans .\analysis\week1_submission1_screening\family_a_single_bus_battery_sweep.json `
  --experiment-id week1_submission1_screening --team-id 7 --week 1 --submission 1 `
  --preview-stride 1

python .\src\experiment_runner.py `
  --plans .\analysis\week1_submission1_screening\family_b_diversification_study.json `
  --experiment-id week1_submission1_screening --team-id 7 --week 1 --submission 1 `
  --preview-stride 1

python .\src\experiment_runner.py `
  --plans .\analysis\week1_submission1_screening\family_c_generator_screening.json `
  --experiment-id week1_submission1_screening --team-id 7 --week 1 --submission 1 `
  --preview-stride 1
```

By default, the runner appends rather than replacing database and event-log
rows. Running these commands again creates additional run records with the
same experiment ID; it does not deduplicate prior runs.
