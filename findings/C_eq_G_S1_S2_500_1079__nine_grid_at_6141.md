<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_1079","policy":"C_eq_G_S1_S2","portfolio":"hosting_1_both_cg","buses":["1079"],"weights":[1.0],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign","campaign_sha256":"e71650eb2b6d8c8e2d9e0a380c5fa8540a286df9b0e09be9510a5df5d7a8a8d6","score_usd":67930061799.622505,"it_value_usd":123053148597.11996,"grid_mwh":17512871.083208367,"generation_mwh":7128.916787931606,"modeled_generator_hours":16.0,"annual_generator_hours":16.00000000015263,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/e71650eb2b6d8c8e2d9e0a380c5fa8540a286df9b0e09be9510a5df5d7a8a8d6-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_1079 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262137 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.260732 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.704884 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.702309 |
| Campaign total | — | — | — | — | 123.053149 | 67.930062 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,815.811 | 1,184.189 | 99.972964% | 3.000 | 3.000 | 3.000 | 0.000 | 499.410962 |
| week-2-submission-2 | 4,377,619.731 | 2,380.269 | 99.945656% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,815.811 | 1,184.189 | 99.972964% | 3.000 | 3.000 | 3.000 | 0.000 | 499.410962 |
| week-3-submission-2 | 4,377,619.731 | 2,380.269 | 99.945656% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001151 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.002555 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.557253 | 0.001151 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.558422 | 0.002555 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 1079: 500 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,184.189 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 342.389013 | 157.610987 | -0.000000 | 342.389013 | 342.389013 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.410962 | 0.589038 | 19.820496 | 479.590466 | 499.410962 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 342.389013 | 157.610987 | -0.000000 | 342.389013 | 342.389013 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 109 | 109 | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 99, 119 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 100, 118 | none | True |

### Snapshot counterfactuals for this round

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.410962 MW**; maximum nodal residual 3.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6277e6636b22cb64685ef23fc3a6cd5d919b841e2086c8dc053a3c30a6b2777e.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.410962 | 479.590466 | 19.820496 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,380.269 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 440.134703 | 59.865297 | -0.000000 | 440.134703 | 440.134703 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 19.820496 | 480.179504 | 500.000000 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 440.134703 | 59.865297 | -0.000000 | 440.134703 | 440.134703 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 109 | 109 | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 9, 17, 24, 25, 26, 27, 28, 29, 30, 44, 45, 46, 47, 56, 57, 65, 66, 77, 78, 92, 93, 99, 119 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 57, 65, 78, 92, 96, 97, 98, 99, 100, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.3e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b1714502076af1ed48adf4d537bdc9e81fee8df8ed45b024f826ba2a1cc2c2c2.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 480.179504 | 19.820496 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,184.189 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 2,150.420720 | 0.000000 | 0.000000 | 6.717357 | none |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,748.166398 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,610.964966 | 0.000000 | 0.000000 | 6.717357 | none |
| 108 (day 5, h12) | 1.000 | 342.389013 | 157.610987 | -0.000000 | 342.389013 | 342.389013 | 0.166049 | none |
| 109 (day 5, h13) | 1.000 | 499.410962 | 0.589038 | 19.820496 | 479.590466 | 499.410962 | 0.001034 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 342.389013 | 157.610987 | -0.000000 | 342.389013 | 342.389013 | 0.166049 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 109 | 109 | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 99, 119 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 100, 118 | none | True |

### Snapshot counterfactuals for this round

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.410962 MW**; maximum nodal residual 3.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6277e6636b22cb64685ef23fc3a6cd5d919b841e2086c8dc053a3c30a6b2777e.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.410962 | 479.590466 | 19.820496 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,380.269 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,248.166398 | 0.000000 | 0.000000 | 6.725594 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,110.964966 | 0.000000 | 0.000000 | 6.764720 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,248.166398 | 0.000000 | 0.000000 | 6.725594 | none |
| 107 (day 5, h11) | 1.000 | 440.134703 | 59.865297 | -0.000000 | 440.134703 | 440.134703 | 0.105117 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 19.820496 | 480.179504 | 500.000000 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 440.134703 | 59.865297 | -0.000000 | 440.134703 | 440.134703 | 0.105117 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 109 | 109 | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 9, 17, 24, 25, 26, 27, 28, 29, 30, 44, 45, 46, 47, 56, 57, 65, 66, 77, 78, 92, 93, 99, 119 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 57, 65, 78, 92, 96, 97, 98, 99, 100, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.3e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b1714502076af1ed48adf4d537bdc9e81fee8df8ed45b024f826ba2a1cc2c2c2.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 480.179504 | 19.820496 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `e71650eb2b6d8c8e2d9e0a380c5fa8540a286df9b0e09be9510a5df5d7a8a8d6`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
