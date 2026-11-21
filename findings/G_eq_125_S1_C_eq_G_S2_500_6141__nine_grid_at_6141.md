<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_125_S1_C_eq_G_S2_500_6141","policy":"G_eq_125_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_125_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign","campaign_sha256":"35447952727ba11104e835b69d86357a2af0083b67310abb6b3f53b83b7af1b6","score_usd":69433215501.58987,"it_value_usd":123053148597.11996,"grid_mwh":17516073.801749866,"generation_mwh":3926.1982464814537,"modeled_generator_hours":16.0,"annual_generator_hours":16.00000000015263,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/35447952727ba11104e835b69d86357a2af0083b67310abb6b3f53b83b7af1b6-3eea05334a1d.json"} -->
# G_eq_125_S1_C_eq_G_S2_500_6141 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 125.000 | 500.000000 | 500.000000 | 30.763287 | 18.013141 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.261409 |
| week-3-submission-1 | 500.000 | 125.000 | 500.000000 | 500.000000 | 30.763287 | 17.456205 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.702460 |
| Campaign total | — | — | — | — | 123.053149 | 69.433216 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,861.112 | 138.888 | 99.996829% | 3.000 | 3.000 | 3.000 | 0.000 | 124.737989 |
| week-2-submission-2 | 4,378,175.789 | 1,824.211 | 99.958351% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,861.112 | 138.888 | 99.996829% | 3.000 | 3.000 | 3.000 | 0.000 | 124.737989 |
| week-3-submission-2 | 4,378,175.789 | 1,824.211 | 99.958351% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000146 | 0.250000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.001878 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.556936 | 0.000146 | 0.250000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.558950 | 0.001878 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_125_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 125 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 138.888 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 7.075195 | 492.924805 | 39.647743 | 0.000000 | 7.075195 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 124.737989 | 375.262011 | 20.109085 | 104.628905 | 124.737989 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 7.075195 | 492.924805 | 39.647743 | 0.000000 | 7.075195 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | 108, 109, 110 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 100, 118 | none | False |

### Snapshot counterfactuals for this round

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **7.075195 MW**; maximum nodal residual 1.75e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54a73bc74a3b0207b9d60c10973e0ba66e324827ee465423f9484f08a4e75b69.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 7.075195 | 0.000000 | 7.075195 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **124.737989 MW**; maximum nodal residual 6.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4fc9b564a31f7152ad5946bf9fc63f0f70efdfc9e703ca22aaf83d896671c923.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 124.737989 | 104.628905 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **7.075195 MW**; maximum nodal residual 1.75e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54a73bc74a3b0207b9d60c10973e0ba66e324827ee465423f9484f08a4e75b69.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 7.075195 | 0.000000 | 7.075195 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,824.211 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 162.105372 | 337.894628 | 96.932230 | 65.173142 | 162.105372 | 0.000000 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 162.105372 | 337.894628 | 96.932230 | 65.173142 | 162.105372 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 5, 8, 9, 10, 12, 13, 14, 16, 17, 18, 21, 24, 25, 26, 37, 53, 54, 56, 57, 65, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 1, 24, 25, 26, 27, 28, 29, 30, 44, 45, 46, 47, 57, 65, 78, 92, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **162.105372 MW**; maximum nodal residual 4.74e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a550bd2a2af4877643edb9845b983ec50bfeb8b0bfe62ef85275b4f8264138d8.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 162.105372 | 129.354669 | 32.750703 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 6.85e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54bfa136f724d3bb1fbe104355a65fc572e844f16ca0f90df0f917db4576df5e.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.999999 | 479.890915 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **162.105372 MW**; maximum nodal residual 4.74e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a550bd2a2af4877643edb9845b983ec50bfeb8b0bfe62ef85275b4f8264138d8.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 162.105372 | 129.354669 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 125 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 138.888 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 2,123.127959 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,985.926527 | 0.000000 | 0.000000 | 6.717357 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 2,123.127959 | 0.000000 | 0.000000 | 6.717357 | none |
| 108 (day 5, h12) | 1.000 | 7.075195 | 492.924805 | 39.647743 | 0.000000 | 7.075195 | 0.276968 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 124.737989 | 375.262011 | 20.109085 | 104.628905 | 124.737989 | 0.658921 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 7.075195 | 492.924805 | 39.647743 | 0.000000 | 7.075195 | 0.276968 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | 108, 109, 110 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 100, 118 | none | False |

### Snapshot counterfactuals for this round

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **7.075195 MW**; maximum nodal residual 1.75e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54a73bc74a3b0207b9d60c10973e0ba66e324827ee465423f9484f08a4e75b69.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 7.075195 | 0.000000 | 7.075195 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **124.737989 MW**; maximum nodal residual 6.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4fc9b564a31f7152ad5946bf9fc63f0f70efdfc9e703ca22aaf83d896671c923.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 124.737989 | 104.628905 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **7.075195 MW**; maximum nodal residual 1.75e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54a73bc74a3b0207b9d60c10973e0ba66e324827ee465423f9484f08a4e75b69.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 7.075195 | 0.000000 | 7.075195 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,824.211 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 2,025.382281 | 0.000000 | 0.000000 | 6.717357 | none |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,623.127959 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,485.926527 | 0.000000 | 0.000000 | 6.725594 | none |
| 107 (day 5, h11) | 1.000 | 162.105372 | 337.894628 | 96.932230 | 65.173142 | 162.105372 | 0.355985 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 162.105372 | 337.894628 | 96.932230 | 65.173142 | 162.105372 | 0.355985 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 5, 8, 9, 10, 12, 13, 14, 16, 17, 18, 21, 24, 25, 26, 37, 53, 54, 56, 57, 65, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 1, 24, 25, 26, 27, 28, 29, 30, 44, 45, 46, 47, 57, 65, 78, 92, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **162.105372 MW**; maximum nodal residual 4.74e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a550bd2a2af4877643edb9845b983ec50bfeb8b0bfe62ef85275b4f8264138d8.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 162.105372 | 129.354669 | 32.750703 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 6.85e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54bfa136f724d3bb1fbe104355a65fc572e844f16ca0f90df0f917db4576df5e.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.999999 | 479.890915 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **162.105372 MW**; maximum nodal residual 4.74e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a550bd2a2af4877643edb9845b983ec50bfeb8b0bfe62ef85275b4f8264138d8.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 162.105372 | 129.354669 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

This accepted campaign used a recorded numerical retry: `audited_numerical_retry`. [retry audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/execution.json>).

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/execution.json>).

| Earlier attempt | Outcome | Log |
| --- | --- | --- |
| official | evaluator exited 1 | [evaluation log](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-01/evaluation.log>) |
Campaign SHA-256: `35447952727ba11104e835b69d86357a2af0083b67310abb6b3f53b83b7af1b6`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
