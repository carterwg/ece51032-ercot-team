# Site-size and competition sensitivity study

## Scope and assumptions

The five candidate buses were evaluated on the ACTIVSg2000 representative
package. The student preview checked all 120 periods at a one-hour stride.
Plans have no private generation or storage; storage is not dispatched by the
preview. Week 2 was selected, so grid-energy charges were off.

The game limits each team's total connection capacity to 1,000 MW per
submission. Therefore, 500 MW and 1,000 MW candidate plans were previewed;
the 1,500 MW and 2,000 MW plans were created as CSVs but rejected by the
submission validator and have no score or dispatch metrics. The CSV checker
confirmed that a 1,500 MW request is invalid under the 1,000 MW team cap.

For competition, each candidate was separately evaluated as a 1,000 MW
submission against either five or ten rival teams, each requesting 1,000 MW.
Rival buses were selected from `hosting_capacity_all_buses.csv` by descending
minimum hosting capacity; bus ID was the tie-breaker for exact ties:

- Five rivals: 6349, 5045, 5120, 5131, 5236
- Ten rivals: 6349, 5045, 5120, 5131, 5236, 5279, 5018, 6045, 6056, 6197

The reported limiting period is zero-based and maximizes the larger of system
generation utilization and maximum branch utilization; ties select the latest
period index.
Binding branches are those that reached their thermal limit in at least one
period. These stress indicators do not mean a fully served standalone plan
was curtailed. Generator utilization is total system generation divided by
the 81,201.89 MW of active generator Pmax.

The experiments used `ercot_game.student_preview.preview_plans`, the same
preview implementation used by the `ercot-game-preview` command. One 1,000 MW
input was also checked through the CLI; its score matched the API result. The
preview is conservative and non-authoritative, and its competition fallback
allocates capacity when the full requests are infeasible.

## Standalone site-size sweep, ranked by score

All scored cases served their full request with zero curtailment. Scores are
identical across buses at a given size; 1,000 MW sites rank above 500 MW sites.
The branch list covers any period in the horizon.

| Rank | Bus | Site size (MW) | Score (billion units) | Served | Curtailment (MW) | Stress period | Generator utilization | Binding branches |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1079 | 1,000 | 36.5266 | 100% | 0 | 119 | 88.3% | b02355, b02579 |
| 1 | 2054 | 1,000 | 36.5266 | 100% | 0 | 119 | 88.3% | b02355, b02579 |
| 1 | 6062 | 1,000 | 36.5266 | 100% | 0 | 109 | 97.5% | None |
| 1 | 6298 | 1,000 | 36.5266 | 100% | 0 | 116 | 91.3% | b02355, b02579 |
| 1 | 7414 | 1,000 | 36.5266 | 100% | 0 | 47 | 73.5% | b02355 |
| 6 | 1079 | 500 | 18.2633 | 100% | 0 | 119 | 87.6% | b02355, b02579 |
| 6 | 2054 | 500 | 18.2633 | 100% | 0 | 119 | 87.6% | b02355, b02579 |
| 6 | 6062 | 500 | 18.2633 | 100% | 0 | 26 | 72.4% | b02260 |
| 6 | 6298 | 500 | 18.2633 | 100% | 0 | 115 | 91.9% | b02355, b02579 |
| 6 | 7414 | 500 | 18.2633 | 100% | 0 | 115 | 91.9% | b02355, b02579 |

| Bus | 1,500 MW result | 2,000 MW result |
|---:|---|---|
| 1079 | Rejected: exceeds 1,000 MW team cap | Rejected: exceeds 1,000 MW team cap |
| 2054 | Rejected: exceeds 1,000 MW team cap | Rejected: exceeds 1,000 MW team cap |
| 6062 | Rejected: exceeds 1,000 MW team cap | Rejected: exceeds 1,000 MW team cap |
| 6298 | Rejected: exceeds 1,000 MW team cap | Rejected: exceeds 1,000 MW team cap |
| 7414 | Rejected: exceeds 1,000 MW team cap | Rejected: exceeds 1,000 MW team cap |

The preview warning for each valid standalone case was that it is a preview
only, checks all 120 periods, and does not dispatch storage. No allocation
projection was needed. Branches b02355 (7058–7095, 2,295 MVA),
b02579 (8004–7150, 647 MVA), and b02260 (7030–7029, 126.6 MVA) are the
thermal limits reached in at least one standalone dispatch; their presence
did not prevent full service at the requested size.

## Competition scenarios

Each candidate's change is relative to that bus's standalone 1,000 MW result.
Percent changes in served fraction are percentage-point changes.

| Rivals | Candidate bus | Score (billion units) | Served fraction | Curtailed (MW) | Score change (billion units) | Served-fraction change | Stress period | Generator utilization | Binding branches |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 5 | 1079 | 18.4112 | 50.4050% | 495.95 | -18.1153 | -49.5950 pp | 119 | 90.75% | b02579 |
| 5 | 2054 | 18.4112 | 50.4050% | 495.95 | -18.1153 | -49.5950 pp | 119 | 90.75% | b02579 |
| 5 | 6062 | 18.4112 | 50.4050% | 495.95 | -18.1153 | -49.5950 pp | 119 | 90.75% | b02579 |
| 5 | 6298 | 18.4112 | 50.4050% | 495.95 | -18.1153 | -49.5950 pp | 119 | 90.75% | b02579 |
| 5 | 7414 | 18.4112 | 50.4050% | 495.95 | -18.1153 | -49.5950 pp | 119 | 90.75% | b02355, b02579 |
| 10 | 1079 | 10.0425 | 27.4937% | 725.06 | -26.4841 | -72.5063 pp | 119 | 90.75% | b02579 |
| 10 | 2054 | 10.0425 | 27.4937% | 725.06 | -26.4841 | -72.5063 pp | 119 | 90.75% | b02579 |
| 10 | 6062 | 10.0425 | 27.4937% | 725.06 | -26.4841 | -72.5063 pp | 119 | 90.75% | b02579 |
| 10 | 6298 | 10.0425 | 27.4937% | 725.06 | -26.4841 | -72.5063 pp | 119 | 90.75% | b02355, b02579 |
| 10 | 7414 | 10.0425 | 27.4937% | 725.06 | -26.4841 | -72.5063 pp | 119 | 90.75% | b02355, b02579 |

Both scenarios triggered the preview's allocation projection because the
unscaled aggregate requests were infeasible. Under five rivals, the
candidate's request was reduced to about 504.05 MW; under ten, to about
274.94 MW. The preview warning is that the full-request dispatch was
infeasible and allocation was applied. Branch b02579 was binding in both
scenarios; b02355 also bound for some candidate locations. Generation stayed
below Pmax, so these observed competition cases were primarily
transmission-limited.

## Robustness ranking and conclusions

The service fractions under competition are effectively equal across all five
candidates. Their tiny numerical differences (less than 0.000000002
percentage points) are not meaningful, so the robustness ranking treats them
as tied:

| Rank | Bus | Served with 5 rivals | Served with 10 rivals | Mean served fraction |
|---:|---:|---:|---:|---:|
| 1 (tie) | 1079 | 50.4050% | 27.4937% | 38.9493% |
| 1 (tie) | 2054 | 50.4050% | 27.4937% | 38.9493% |
| 1 (tie) | 6062 | 50.4050% | 27.4937% | 38.9493% |
| 1 (tie) | 6298 | 50.4050% | 27.4937% | 38.9493% |
| 1 (tie) | 7414 | 50.4050% | 27.4937% | 38.9493% |

- **No competition:** all five buses perform equally at both valid sizes; each
  serves 100% and earns the same score. There is no score-based reason to
  prefer one candidate in this preview.
- **Under competition:** no bus is meaningfully better. The common binding
  corridor b02579, plus b02355 in some cases, dominates the allocation.
- **Limiting mechanism:** the standalone 1,000 MW dispatch at bus 6062 is
  closest to the system generation ceiling (97.5% at its stress period), but
  the multi-team cases bind transmission at about 90.75% aggregate generator
  utilization. Thus the competition results are transmission-limited, not
  generation-limited.
- **Crowding resilience:** all candidates are effectively tied. Bus 1079 has
  the largest value in the raw mean-service ranking by a numerically
  negligible amount; it should not be treated as a distinct resilience
  advantage.

## Intermediate outputs

The [`site_size_sweep`](../analysis/site_size_sweep) directory contains the per-case
plan CSVs, aggregate metrics, raw preview summary, assumptions, and rankings:

- [`site_size_and_competition_results.csv`](../analysis/site_size_sweep/site_size_and_competition_results.csv)
- [`site_size_score_ranking.csv`](../analysis/site_size_sweep/site_size_score_ranking.csv)
- [`competition_robustness_ranking.csv`](../analysis/site_size_sweep/competition_robustness_ranking.csv)
- [`experiment_assumptions.json`](../analysis/site_size_sweep/experiment_assumptions.json)
- [`preview_raw_summary.json`](../analysis/site_size_sweep/preview_raw_summary.json)
- [`cli_validation.json`](../analysis/site_size_sweep/cli_validation.json)
