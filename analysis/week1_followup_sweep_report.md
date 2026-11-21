# Week 1 Follow-up Storage and Hybrid Sweep

## Summary and status

- Candidate plans: 33 (Family D: 16, Family E: 11, Family F: 6).
- Planned full-evaluator runs: 72 (33 solo, 33 eight-team, and 6 sensitivity).
- Completed runs: 72 / 72; incomplete or non-completed: 0.
- Week 1, Submission 1, finalized 500 MW release, finalized scoring rules, HiGHS, all 120 representative periods, and full output were used.
- Team 7’s candidate file was copied byte-for-byte into every scenario. Synthetic copies changed only team_id and site_id.
- The repeated-plan cases are synthetic stress tests, not predictions of actual classroom submissions.
- Week 1 excludes grid-energy costs; results are Week 1 outcomes and do not establish Week 3 performance.

All run inputs and SHA-256 hashes, run outputs, dispatch summaries, warnings, and per-period storage time series are in the manifest. Full output folders are preserved under `../runs/week1_followup_sweep/`.

## Methods and checks

All candidate CSVs were checked with the project’s canonical CSV validator against the representative package, using the finalized release limits: 500 MW total connection capacity, generator capacity no greater than connection capacity, and storage energy equal to four times storage power. Validation details are in `../runs/week1_followup_sweep/validation_results.json`. The battery pilot had to accept exactly one/eight teams and produce 120 per-period dispatch JSONs with storage charge, discharge, and state-of-charge fields before the remaining cases were launched.

In the eight-team cases, Team 7 plus seven copies were evaluated together. Sensitivity cases use Team 7 plus one or three copies (two or four total teams). Allocation/projection status is taken from full evaluator outputs; a `joint_projection` run is a completed recovery through capacity allocation, not an evaluator failure.

For battery plans, charge/discharge totals sum MW across 120 one-hour representative periods, reported as unweighted MWh-equivalent. They are not annual, day-weighted, or ten-year energy. Per-period MW and SOC values remain in `battery_dispatch_by_period_json` and the raw dispatch files.

## Solo versus eight-team results

| Family | Plan | Solo score | 8-team score | Solo service | 8-team service | 8-team allocation fraction | 8-team scope |
|---|---|---:|---:|---:|---:|---:|---|
| D - Refine single-bus battery size | D_bus6141_battery_125mw | $18.088B | $18.088B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_150mw | $18.053B | $18.053B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_175mw | $18.018B | $18.018B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_225mw | $17.948B | $17.948B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_250mw | $17.913B | $17.913B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_300mw | $17.843B | $17.843B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_400mw | $17.703B | $17.703B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6141_battery_500mw | $17.563B | $17.563B | 100.00% | 100.00% | 100.00% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_125mw | $18.088B | $16.794B | 100.00% | 92.84% | 92.84% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_150mw | $18.053B | $17.178B | 100.00% | 95.15% | 95.15% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_175mw | $18.018B | $17.266B | 100.00% | 95.82% | 95.82% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_225mw | $17.948B | $17.295B | 100.00% | 96.36% | 96.36% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_250mw | $17.913B | $17.261B | 100.00% | 96.36% | 96.36% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_300mw | $17.843B | $17.193B | 100.00% | 96.36% | 96.36% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_400mw | $17.703B | $17.058B | 100.00% | 96.36% | 96.36% | joint_projection |
| D - Refine single-bus battery size | D_bus6062_battery_500mw | $17.563B | $16.924B | 100.00% | 96.36% | 96.36% | joint_projection |
| E - Batteries on diversified plans | E_2054-6062_equal_battery_50mw | $18.193B | $15.284B | 100.00% | 84.01% | 84.01% | joint_projection |
| E - Batteries on diversified plans | E_2054-6062_equal_battery_100mw | $18.123B | $17.128B | 100.00% | 94.51% | 94.51% | joint_projection |
| E - Batteries on diversified plans | E_2054-6062_equal_battery_200mw | $17.983B | $17.983B | 100.00% | 100.00% | 100.00% | joint_projection |
| E - Batteries on diversified plans | E_6298-7414_equal_battery_50mw | $18.193B | $14.713B | 100.00% | 80.87% | 80.87% | joint_projection |
| E - Batteries on diversified plans | E_6298-7414_equal_battery_100mw | $18.123B | $16.416B | 100.00% | 90.58% | 90.58% | joint_projection |
| E - Batteries on diversified plans | E_6298-7414_equal_battery_200mw | $17.983B | $17.983B | 100.00% | 100.00% | 100.00% | joint_projection |
| E - Batteries on diversified plans | E_four_bus_equal_battery_50mw | $18.193B | $15.284B | 100.00% | 84.01% | 84.01% | joint_projection |
| E - Batteries on diversified plans | E_four_bus_equal_battery_100mw | $18.123B | $17.128B | 100.00% | 94.51% | 94.51% | joint_projection |
| E - Batteries on diversified plans | E_four_bus_equal_battery_200mw | $17.983B | $17.983B | 100.00% | 100.00% | 100.00% | joint_projection |
| E - Batteries on diversified plans | E_2054-6062_concentrated_bus2054_battery_200mw | $17.983B | $17.983B | 100.00% | 100.00% | 100.00% | joint_projection |
| E - Batteries on diversified plans | E_2054-6062_concentrated_bus6062_battery_200mw | $17.983B | $17.983B | 100.00% | 100.00% | 100.00% | joint_projection |
| F - Generator plus battery | F_bus2054_gen250_battery_50mw | $17.693B | $17.361B | 100.00% | 100.00% | 100.00% | joint |
| F - Generator plus battery | F_bus2054_gen250_battery_100mw | $17.623B | $17.291B | 100.00% | 100.00% | 100.00% | joint |
| F - Generator plus battery | F_bus2054_gen250_battery_200mw | $17.483B | $17.151B | 100.00% | 100.00% | 100.00% | joint_projection |
| F - Generator plus battery | F_bus6062_gen250_battery_50mw | $17.693B | $17.693B | 100.00% | 100.00% | 100.00% | joint |
| F - Generator plus battery | F_bus6062_gen250_battery_100mw | $17.623B | $17.623B | 100.00% | 100.00% | 100.00% | joint |
| F - Generator plus battery | F_bus6062_gen250_battery_200mw | $17.483B | $17.483B | 100.00% | 100.00% | 100.00% | joint |

## Family summaries

- **D - Refine single-bus battery size:** mean solo-to-eight-team score change -$0.385B (difference, not a score); mean service-fraction change -2.15 percentage points.
- **E - Batteries on diversified plans:** mean solo-to-eight-team score change -$1.182B (difference, not a score); mean service-fraction change -6.50 percentage points.
- **F - Generator plus battery:** mean solo-to-eight-team score change -$0.166B (difference, not a score); mean service-fraction change +0.00 percentage points.

In Family D, bus 6141 served the full 500 MW request at every tested battery size; the highest score was the smallest tested size, 125 MW, because additional storage capital cost did not improve service in this scenario. At bus 6062, service rose from 92.84% at 125 MW to 96.36% at 225 MW, then remained at 96.36% through 500 MW while scores declined with added storage cost. These location-specific results are not a general battery-sizing rule.

### Battery-size trends: buses 6141 and 6062

| Bus | Battery MW | Solo score | 8-team score | 8-team service | 8-team dispatch charge / discharge (unweighted MWh-eq) |
|---:|---:|---:|---:|---:|---:|
| 6141 | 125 | $18.088B | $18.088B | 100.00% | 3712.1697098731 / 3712.1697098732 |
| 6141 | 150 | $18.053B | $18.053B | 100.00% | 4633.7627058471 / 4633.7627058471 |
| 6141 | 175 | $18.018B | $18.018B | 100.00% | 4826.9737574662 / 4826.9737574661 |
| 6141 | 225 | $17.948B | $17.948B | 100.00% | 6830.8992616943 / 6830.8992616942 |
| 6141 | 250 | $17.913B | $17.913B | 100.00% | 7833.9263008069 / 7833.9263008069 |
| 6141 | 300 | $17.843B | $17.843B | 100.00% | 9625.1778501267 / 9625.1778501267 |
| 6141 | 400 | $17.703B | $17.703B | 100.00% | 12745.8688264113 / 12745.8688264114 |
| 6141 | 500 | $17.563B | $17.563B | 100.00% | 18625.1693715642 / 18625.1693715643 |
| 6062 | 125 | $18.088B | $16.794B | 92.84% | 4494.4775049915 / 4494.4775049917 |
| 6062 | 150 | $18.053B | $17.178B | 95.15% | 5503.253653024901 / 5503.253653025001 |
| 6062 | 175 | $18.018B | $17.266B | 95.82% | 6554.2721340824 / 6554.2721340826 |
| 6062 | 225 | $17.948B | $17.295B | 96.36% | 8378.3362217913 / 8378.3362217912 |
| 6062 | 250 | $17.913B | $17.261B | 96.36% | 9492.9569270389 / 9492.956927039 |
| 6062 | 300 | $17.843B | $17.193B | 96.36% | 11261.0937496191 / 11261.0937496193 |
| 6062 | 400 | $17.703B | $17.058B | 96.36% | 15226.6590104446 / 15226.6590104449 |
| 6062 | 500 | $17.563B | $16.924B | 96.36% | 18885.5254292331 / 18885.5254292329 |

### Diversified storage portfolios

| Portfolio / configuration | Storage MW | Solo score | 8-team score | 8-team service | Charge / discharge (unweighted MWh-eq) |
|---|---:|---:|---:|---:|---:|
| E_2054-6062_equal_battery_50mw | 50 | $18.193B | $15.284B | 84.01% | 1018.0375629374 / 1018.0375629374 |
| E_2054-6062_equal_battery_100mw | 100 | $18.123B | $17.128B | 94.51% | 2130.8230964584 / 2130.8230964584 |
| E_2054-6062_equal_battery_200mw | 200 | $17.983B | $17.983B | 100.00% | 4524.5735700003 / 4524.5735700003 |
| E_6298-7414_equal_battery_50mw | 50 | $18.193B | $14.713B | 80.87% | 1144.918092104 / 1144.9180921038999 |
| E_6298-7414_equal_battery_100mw | 100 | $18.123B | $16.416B | 90.58% | 2467.1399830738 / 2467.1399830738 |
| E_6298-7414_equal_battery_200mw | 200 | $17.983B | $17.983B | 100.00% | 6095.0138227397 / 6095.0138227398 |
| E_four_bus_equal_battery_50mw | 50 | $18.193B | $15.284B | 84.01% | 1029.3659784072 / 1029.3659784072 |
| E_four_bus_equal_battery_100mw | 100 | $18.123B | $17.128B | 94.51% | 2086.3860261013 / 2086.3860261013 |
| E_four_bus_equal_battery_200mw | 200 | $17.983B | $17.983B | 100.00% | 4362.2032239885 / 4362.2032239885 |
| E_2054-6062_concentrated_bus2054_battery_200mw | 200 | $17.983B | $17.983B | 100.00% | 4299.5763380446 / 4299.5763380446 |
| E_2054-6062_concentrated_bus6062_battery_200mw | 200 | $17.983B | $17.983B | 100.00% | 4508.7684144128 / 4508.7684144129 |

At 200 MW total storage, each diversified portfolio—both evenly distributed and concentrated—served 100% in the eight-team identical-copy scenario and had the same rounded score. Dispatch totals varied by bus placement. At 50 and 100 MW, the 6298/7414 portfolio served less than the 2054/6062 and four-bus portfolios, showing that diversification alone did not remove the location-specific congestion effect in these tests.

### Generator plus battery versus generator-only baseline

| Bus | Battery MW | Scenario | Prior 250 MW generator-only score | New 250 MW generator + battery score | Difference | Prior service | New service |
|---:|---:|---|---:|---:|---:|---:|---:|
| 2054 | 50 | solo | $17.763B | $17.693B | -$0.070B | 100.00% | 100.00% |
| 2054 | 50 | eight_team_copies | $17.429B | $17.361B | -$0.069B | 100.00% | 100.00% |
| 2054 | 100 | solo | $17.763B | $17.623B | -$0.140B | 100.00% | 100.00% |
| 2054 | 100 | eight_team_copies | $17.429B | $17.291B | -$0.139B | 100.00% | 100.00% |
| 2054 | 200 | solo | $17.763B | $17.483B | -$0.280B | 100.00% | 100.00% |
| 2054 | 200 | eight_team_copies | $17.429B | $17.151B | -$0.279B | 100.00% | 100.00% |
| 6062 | 50 | solo | $17.763B | $17.693B | -$0.070B | 100.00% | 100.00% |
| 6062 | 50 | eight_team_copies | $17.760B | $17.693B | -$0.067B | 100.00% | 100.00% |
| 6062 | 100 | solo | $17.763B | $17.623B | -$0.140B | 100.00% | 100.00% |
| 6062 | 100 | eight_team_copies | $17.760B | $17.623B | -$0.137B | 100.00% | 100.00% |
| 6062 | 200 | solo | $17.763B | $17.483B | -$0.280B | 100.00% | 100.00% |
| 6062 | 200 | eight_team_copies | $17.760B | $17.483B | -$0.277B | 100.00% | 100.00% |

The 250 MW generator-only baselines already served 100% in these matched cases. Adding storage did not raise service, and the hybrid score was lower by approximately the storage capital charge (about $70M, $140M, or $280M for 50, 100, or 200 MW, respectively). In these Week 1 cases, the battery dispatch did not offset its capital cost in the score.

### Crowd-size sensitivity for selected family winners

| Family | Selected plan (highest 8-team score) | 2-team score / service | 4-team score / service | 8-team score / service |
|---|---|---:|---:|---:|
| D - Refine single-bus battery size | D_bus6141_battery_125mw | $18.088B / 100.00% | $18.088B / 100.00% | $18.088B / 100.00% |
| E - Batteries on diversified plans | E_2054-6062_equal_battery_200mw | $17.983B / 100.00% | $17.983B / 100.00% | $17.983B / 100.00% |
| F - Generator plus battery | F_bus6062_gen250_battery_50mw | $17.693B / 100.00% | $17.693B / 100.00% | $17.693B / 100.00% |

## Incomplete runs and limitations

- No incomplete or non-completed runs.

Scores and dispatch reflect the finalized Week 1 evaluator and its fixed representative-period dispatch/weighting rules. Repeated identical submissions are deliberately synthetic; they do not model mixed strategy choices, classroom roster behavior, or future rule changes. Battery dispatch aggregates are simple unweighted sums over the 120 one-hour periods; they should not be read as annualized energy.
