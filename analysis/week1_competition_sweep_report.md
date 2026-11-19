# Week 1 Full-Evaluator Competition Sweep

## Executive summary

The 67 Week 1, Submission 1 screening plans were each evaluated twice with the
full batch evaluator: once alone and once with seven copied plans. This is 134
completed full-evaluator runs over all 120 representative periods. Team 7's
original CSV was retained in each run; the seven copies changed only `team_id`
and `site_id`.

- All **67 solo runs** accepted one team and completed.
- All **67 eight-team runs** accepted eight distinct teams and completed; no
  submissions were rejected.
- The evaluator used a joint dispatch in 73 runs (67 solo and 6 crowded) and a
  `joint_projection` in the other 61 crowded runs. Those 61 cases first found
  the unscaled eight-team request physically infeasible, then recovered by
  applying the evaluator's allocation projection. This is not a failed run.
- Family A's mean eight-team service fraction rose with battery size, from
  71.48% at 0 MW to 89.15% at 200 MW, averaged across its five buses. This is
  full storage dispatch, unlike the experiment runner's idle-storage preview.
- Family C's best crowded generator candidate was 250 MW at bus 6062, at about
  **$17.760B**. The highest Team 7 score overall in the tested crowded cases
  was Family A's 200 MW battery at bus 6141: about **$17.983B**, with full
  service in this specific eight-copy scenario.

These are simulated, strategy-copying stress cases, not predictions of class
submissions or official classroom scores.

## Scope and reproducibility

The experiment set comes from the existing
[`week1_submission1_screening`](week1_submission1_screening) candidate files:

- 30 Family A single-bus battery candidates;
- 25 Family B diversified connection plans; and
- 12 Family C generator candidates.

For every candidate, the solo input directory contained only Team 7's
generated candidate CSV. The crowded input contained Team 7's same CSV and
seven copies with team IDs `mock-02` through `mock-08`. Copies preserved site
capacities, bus IDs, generator, and storage capacities; only their team and site
identifiers differed. The resulting crowded scenario had eight teams total,
not nine.

Evaluation used the finalized 500 MW scoring rules and release, Week 1,
Submission 1, the ACTIVSg2000 representative package, HiGHS, all 120 periods,
and `--output-mode full`. Week 1 grid energy cost was off. The output files
include per-period storage dispatch for battery plans.

Full input CSV paths and SHA-256 hashes, run IDs, output paths, acceptance and
feasibility statuses, Team 7 score components, service/allocation factors,
warnings, and per-period battery dispatch are recorded in
[`week1_competition_sweep_manifest.csv`](week1_competition_sweep_manifest.csv).
The full per-run evaluator artifacts are under
[`runs/week1_full_evaluator_sweep/`](../runs/week1_full_evaluator_sweep/),
including each run's `leaderboard.csv`, `submission_manifest.csv`,
`evaluation.json`, `diagnostics/`, and `dispatch/period_<n>.json`.

The full-evaluator results were **not** appended to
[`run_database.csv`](run_database.csv), which remains the experiment runner's
student-preview database.

## Results by candidate family

Scores below are Team 7's evaluator-reported USD scores. Family means are
descriptive averages across the candidate plans in that family; they do not
represent a single strategy or predict a final tournament.

| Family | Runs (solo / crowded) | Mean solo score | Mean crowded score | Mean crowded service fraction | Crowded projection runs |
|---|---:|---:|---:|---:|---:|
| A — Single-Bus Battery Sweep | 30 / 30 | $18.158B | $14.561B | 80.22% | 30 / 30 |
| B — Diversification Study | 25 / 25 | $18.263B | $13.724B | 75.15% | 25 / 25 |
| C — Generator Screening | 12 / 12 | $17.838B | $15.750B | 89.83% | 6 / 12 |

### Family A — battery size and location

All solo plans served 100% of the requested 500 MW. In the solo comparison,
increasing battery size reduced the score because the battery adds capital
cost, while it did not increase service beyond 100%. The full evaluator did
dispatch the batteries: across the 25 nonzero-battery plans, mean unweighted
charge and discharge were each about **2,311 MWh-equivalent per 120-period
representative block** in solo runs.

The congested results show the storage dispatch can matter when a team's
requested capacity is projected. Mean service and score across the five buses
by battery power were:

| Storage power | Mean crowded score | Mean crowded service fraction |
|---:|---:|---:|
| 0 MW | $13.055B | 71.48% |
| 25 MW | $13.705B | 75.18% |
| 50 MW | $14.365B | 78.96% |
| 75 MW | $14.894B | 82.02% |
| 100 MW | $15.317B | 84.51% |
| 200 MW | $16.031B | 89.15% |

Best Family A crowded result: **bus 6141, 200 MW / 800 MWh**. Team 7's score
was about $17.983B with a 1.0 service fraction; the storage capital charge was
about $280M. Its unweighted 120-period Team 7 dispatch summed to 6,200 MWh of
charge and 6,200 MWh of discharge. This is evidence for this tested case only;
it is not a general guarantee that the same battery or bus will rank best with
different competitors.

### Family B — diversified sites

All 25 solo diversification plans served 100% and had the same score, about
$18.263B. In the eight-team identical-copy scenario, mean service was 75.15%,
with a relatively narrow range from **73.11% to 75.61%**. The highest-service
plan was the 2054/6062 two-bus combination at 75.61%; the lowest was the
6298/7414 two-bus combination at 73.11%. The approximately 2.5 percentage
point range suggests location mix has some effect in this particular crowding
test, but every plan still required the allocation projection.

### Family C — generator screening

All solo candidates served 100%. In the crowded scenarios, six of twelve
remained feasible in joint dispatch without allocation; the other six required
projection. All three 250 MW generator candidates and all three 500 MW
candidates served 100% in the eight-team runs. The highest Family C score was
bus 6062 with a 250 MW generator: about **$17.760B**, with about $500M generator
capital cost and $3.11M generator operating cost. The 500 MW generator cases
also served fully but scored less because the additional generator capital
charge outweighed the operating-cost difference in these Week 1 conditions.

## How to interpret battery dispatch totals

`team7_battery_dispatch_by_period_json` in the manifest preserves Team 7's
per-period charge (MW), discharge (MW), and state of charge (MWh), by storage
asset. The compact battery summary columns sum charge and discharge over the
120 one-hour representative periods, so the totals are **unweighted
MWh-equivalent across the representative block**. They are not annual totals,
ten-year totals, day-weighted energy, or present-value quantities. State-of-
charge min/mean/max are unweighted summaries of the period-level SOC entries.
The evaluator's score columns, by contrast, use the configured game scoring
weights and capital charges.

The full output for the pilot's 25 MW / 100 MWh battery shows the dispatch
fields are populated: solo charge and discharge each totaled 700 MWh-equivalent;
the eight-team run totaled about 437.73 MWh-equivalent each. Those are distinct
from the much larger per-period score weights used for the ten-year value.

## Projection, warnings, and limitations

Every input set had the intended number of accepted teams: one in solo runs
and eight in crowded runs, with zero rejected teams. All 134 Team 7 submissions
were valid and feasible after evaluator processing, and all 134 produced 120
period dispatch files.

For the 61 projected runs, `evaluation.json` records
`DCOPF physically infeasible: HighsModelStatus.kInfeasible` as the original
full-request dispatch failure. The evaluator recovered by running its
continuous allocation projection; `competition_scope` is `joint_projection`.
Therefore this text is a recovery diagnostic, not an unsuccessful final
evaluation. The six remaining crowded scenarios completed as `joint` without
projection. A projection does not always mean curtailment: a few projected
cases still report a service fraction of 1.0.

Other cautions:

- Seven copied opponents are an artificial deterministic assumption. A
  different mix, number, siting, generation, or storage can change every team's
  score and allocation.
- Exact copies test the system's response to repeated identical plans; they
  do not estimate strategy diversity or actual classmates' behavior.
- Week 1 is practice/feedback and excludes grid-energy costs. Week 3 can have
  different outcomes because grid energy is charged at the joint-dispatch LMP.
- The run is not an official instructor outcome. Actual class submissions and
  the official evaluator determine classroom results.
- Full per-period JSON files are large. Use the manifest for comparisons and
  inspect the per-run dispatch artifacts for detailed operating behavior.
