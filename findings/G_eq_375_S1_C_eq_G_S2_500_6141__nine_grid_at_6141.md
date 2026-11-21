<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_375_S1_C_eq_G_S2_500_6141","policy":"G_eq_375_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_375_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign","campaign_sha256":"61dfcaa62501d90516ee16eadf2dadca43b53fef79f330391a534b29ee67d995","score_usd":68426944438.74727,"it_value_usd":123053148597.11996,"grid_mwh":17513574.060010538,"generation_mwh":6425.9399858093,"modeled_generator_hours":16.0,"annual_generator_hours":16.00000000015263,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/61dfcaa62501d90516ee16eadf2dadca43b53fef79f330391a534b29ee67d995-3eea05334a1d.json"} -->
# G_eq_375_S1_C_eq_G_S2_500_6141 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 375.000 | 500.000000 | 500.000000 | 30.763287 | 17.512423 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.260830 |
| week-3-submission-1 | 500.000 | 375.000 | 500.000000 | 500.000000 | 30.763287 | 16.954940 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.698751 |
| Campaign total | — | — | — | — | 123.053149 | 68.426944 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,111.189 | 888.811 | 99.979708% | 3.000 | 3.000 | 3.000 | 0.000 | 374.712163 |
| week-2-submission-2 | 4,377,675.841 | 2,324.159 | 99.946937% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,111.189 | 888.811 | 99.979708% | 3.000 | 3.000 | 3.000 | 0.000 | 374.712163 |
| week-3-submission-2 | 4,377,675.841 | 2,324.159 | 99.946937% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000864 | 0.750000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.002457 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.557484 | 0.000864 | 0.750000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.562080 | 0.002457 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_375_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 375 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 888.811 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 257.049369 | 242.950631 | 39.647743 | 217.401626 | 257.049369 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 374.712163 | 125.287837 | 20.109085 | 354.603079 | 374.712163 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 257.049369 | 242.950631 | 39.647743 | 217.401626 | 257.049369 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 56, 57, 65, 66, 77, 78, 92, 93, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 108, 109, 110 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 54, 68, 78, 92, 100, 118 | none | False |

### Snapshot counterfactuals for this round

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **257.049369 MW**; maximum nodal residual 1.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d4cf66932a5766808e50a5a14a0c84e8062f89a561e49532114dc40ef679a2f9.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 257.049369 | 224.298665 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **374.712163 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/89c8d09014c73be34ba7cbf29414507eef96006751d6f4b36d2091e55c93e331.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 374.712163 | 354.603079 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **257.049369 MW**; maximum nodal residual 1.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d4cf66932a5766808e50a5a14a0c84e8062f89a561e49532114dc40ef679a2f9.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 257.049369 | 224.298665 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,324.159 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 412.079546 | 87.920454 | 96.932230 | 315.147316 | 412.079546 | 0.000000 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 412.079546 | 87.920454 | 96.932230 | 315.147316 | 412.079546 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 25, 26, 27, 28, 32, 34, 35, 36, 37, 38, 39, 40, 42, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 105, 106, 107, 108, 109, 110, 111, 112, 113 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 3, 4, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 43, 44, 45, 46, 47, 57, 58, 64, 65, 75, 78, 92, 95, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **412.079546 MW**; maximum nodal residual 2.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d3354b181ad4430300774f9abe3388954baa05465f3aab0286b2d3fdceb39038.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 412.079546 | 379.328843 | 32.750703 | True |

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

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **412.079546 MW**; maximum nodal residual 2.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d3354b181ad4430300774f9abe3388954baa05465f3aab0286b2d3fdceb39038.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 412.079546 | 379.328843 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 375 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 888.811 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,873.153785 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,735.952353 | 0.000000 | 0.000000 | 6.717357 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,873.153785 | 0.000000 | 0.000000 | 6.717357 | none |
| 108 (day 5, h12) | 1.000 | 257.049369 | 242.950631 | 39.647743 | 217.401626 | 257.049369 | 0.255958 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 374.712163 | 125.287837 | 20.109085 | 354.603079 | 374.712163 | 0.219992 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 257.049369 | 242.950631 | 39.647743 | 217.401626 | 257.049369 | 0.255958 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 56, 57, 65, 66, 77, 78, 92, 93, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 108, 109, 110 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 54, 68, 78, 92, 100, 118 | none | False |

### Snapshot counterfactuals for this round

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **257.049369 MW**; maximum nodal residual 1.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d4cf66932a5766808e50a5a14a0c84e8062f89a561e49532114dc40ef679a2f9.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 257.049369 | 224.298665 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **374.712163 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/89c8d09014c73be34ba7cbf29414507eef96006751d6f4b36d2091e55c93e331.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 374.712163 | 354.603079 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **257.049369 MW**; maximum nodal residual 1.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d4cf66932a5766808e50a5a14a0c84e8062f89a561e49532114dc40ef679a2f9.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 257.049369 | 224.298665 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,324.159 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,373.153785 | 0.000000 | 0.000000 | 6.725594 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,235.952353 | 0.000000 | 0.000000 | 6.725594 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,373.153785 | 0.000000 | 0.000000 | 6.725594 | none |
| 107 (day 5, h11) | 1.000 | 412.079546 | 87.920454 | 96.932230 | 315.147316 | 412.079546 | 0.154379 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 412.079546 | 87.920454 | 96.932230 | 315.147316 | 412.079546 | 0.154379 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 25, 26, 27, 28, 32, 34, 35, 36, 37, 38, 39, 40, 42, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 105, 106, 107, 108, 109, 110, 111, 112, 113 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 3, 4, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 43, 44, 45, 46, 47, 57, 58, 64, 65, 75, 78, 92, 95, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **412.079546 MW**; maximum nodal residual 2.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d3354b181ad4430300774f9abe3388954baa05465f3aab0286b2d3fdceb39038.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 412.079546 | 379.328843 | 32.750703 | True |

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

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **412.079546 MW**; maximum nodal residual 2.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d3354b181ad4430300774f9abe3388954baa05465f3aab0286b2d3fdceb39038.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 412.079546 | 379.328843 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

This accepted campaign used a recorded numerical retry: `audited_numerical_retry`. [retry audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/execution.json>).

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/execution.json>).

| Earlier attempt | Outcome | Log |
| --- | --- | --- |
| official | evaluator exited 1 | [evaluation log](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-01/evaluation.log>) |
Campaign SHA-256: `61dfcaa62501d90516ee16eadf2dadca43b53fef79f330391a534b29ee67d995`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
