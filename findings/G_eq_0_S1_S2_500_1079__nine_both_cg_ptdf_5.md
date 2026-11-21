<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_S2_500_1079","policy":"G_eq_0_S1_S2","portfolio":"hosting_1_grid","buses":["1079"],"weights":[1.0],"scenario":"nine_both_cg_ptdf_5","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign","campaign_sha256":"bfffb2f00a16618ce3ed3c1006772df9367288f3cb9cbf8f13708fe1fa5b33ce","score_usd":35949219194.35954,"it_value_usd":61526574299.18591,"grid_mwh":8760000.000087256,"generation_mwh":0.0,"modeled_generator_hours":0.0,"annual_generator_hours":0.0,"required_annual_hours":0.0,"minimum_admission":1.0173330278771633e-11,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/bfffb2f00a16618ce3ed3c1006772df9367288f3cb9cbf8f13708fe1fa5b33ce-3eea05334a1d.json"} -->
# G_eq_0_S1_S2_500_1079 — nine_both_cg_ptdf_5

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 500.000000 | 500.000000 | 30.763287 | 18.263287 |
| week-2-submission-2 | 500.000 | 0.000 | 0.000000 | 500.000000 | 0.000000 | 0.000000 |
| week-3-submission-1 | 500.000 | 0.000 | 500.000000 | 500.000000 | 30.763287 | 17.685932 |
| week-3-submission-2 | 500.000 | 0.000 | 0.000000 | 500.000000 | 0.000000 | 0.000000 |
| Campaign total | — | — | — | — | 61.526574 | 35.949219 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,380,000.000 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 0.000 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 0.000 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| week-3-submission-1 | 0.577355 | 0.000000 | 0.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_S2`.
- Layout: 1079: 500 MW per submission.
- Opponents: 9. Each uses 6141 (100 MW), 5395 (100 MW), 6342 (100 MW), 5451 (100 MW), 6004 (100 MW) per submission. G/C is 1 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 0 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 9, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 68, 69, 70, 71, 73 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.000000 MW** (0.000000%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 12 modeled periods; the largest own backup lower bound is 500.000000 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 (day 5, h10) | 1.000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 2, 3, 23 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 101, 102, 103, 115, 116, 117 | none | False |

### Snapshot counterfactuals for this round

- Period 106: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4e-09 MW. Generation-only capacity ceiling = 0.000000 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/8212270d6d285b53db8a4e3c0fa649d394860658c827511642e0a37c3445d002.json>).
- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.36e-08 MW. Generation-only capacity ceiling = 0.000000 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/e7cdae43232372af2de45eb5242498651c0d1931c63231f771c0021c3ef2fd22.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 115.159491 | 0.000000 | 0.000000 | 9.982339 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 109 (day 5, h13) | 1.000 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.526769 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 9, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 68, 69, 70, 71, 73 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.000000 MW** (0.000000%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 12 modeled periods; the largest own backup lower bound is 500.000000 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 2, 3, 23 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 101, 102, 103, 115, 116, 117 | none | False |

### Snapshot counterfactuals for this round

- Period 106: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4e-09 MW. Generation-only capacity ceiling = 0.000000 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/8212270d6d285b53db8a4e3c0fa649d394860658c827511642e0a37c3445d002.json>).
- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.36e-08 MW. Generation-only capacity ceiling = 0.000000 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/e7cdae43232372af2de45eb5242498651c0d1931c63231f771c0021c3ef2fd22.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `bfffb2f00a16618ce3ed3c1006772df9367288f3cb9cbf8f13708fe1fa5b33ce`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_grid/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
