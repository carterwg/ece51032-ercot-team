<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_250_S1_C_eq_G_S2_500_6141","policy":"G_eq_250_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_250_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign","campaign_sha256":"8896afb9b0768d906055359c8982e15d61d82df2176c048bcbf884fadfeda06a","score_usd":68930090075.62537,"it_value_usd":123053148597.11996,"grid_mwh":17514823.932885878,"generation_mwh":5176.067110467777,"modeled_generator_hours":16.0,"annual_generator_hours":16.00000000015263,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/8896afb9b0768d906055359c8982e15d61d82df2176c048bcbf884fadfeda06a-3eea05334a1d.json"} -->
# G_eq_250_S1_C_eq_G_S2_500_6141 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 250.000 | 500.000000 | 500.000000 | 30.763287 | 17.762794 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.261146 |
| week-3-submission-1 | 500.000 | 250.000 | 500.000000 | 500.000000 | 30.763287 | 17.205638 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.700512 |
| Campaign total | — | — | — | — | 123.053149 | 68.930090 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,486.151 | 513.849 | 99.988268% | 3.000 | 3.000 | 3.000 | 0.000 | 249.724876 |
| week-2-submission-2 | 4,377,925.815 | 2,074.185 | 99.952644% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,486.151 | 513.849 | 99.988268% | 3.000 | 3.000 | 3.000 | 0.000 | 249.724876 |
| week-3-submission-2 | 4,377,925.815 | 2,074.185 | 99.952644% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000493 | 0.500000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.002141 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.557156 | 0.000493 | 0.500000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.560634 | 0.002141 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_250_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 250 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 513.849 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 132.062082 | 367.937918 | 39.647743 | 92.414338 | 132.062081 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 249.724876 | 250.275124 | 20.109085 | 229.615791 | 249.724876 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 132.062082 | 367.937918 | 39.647743 | 92.414338 | 132.062081 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 96, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | 108, 109, 110 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 100, 118 | none | False |

### Snapshot counterfactuals for this round

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **132.062081 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d500e0b0eab8277e579cf9111ac2416f838cd50663c77e43124d21d5ad37ec6f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 132.062081 | 99.311378 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **249.724876 MW**; maximum nodal residual 5.88e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/af0e6091c8e2b9dc0f4855eb38361c8e5af1f57fa724bda5790adf49c6a8c9f2.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 249.724876 | 229.615791 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **132.062081 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d500e0b0eab8277e579cf9111ac2416f838cd50663c77e43124d21d5ad37ec6f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 132.062081 | 99.311378 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,074.185 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 287.092258 | 212.907742 | 96.932230 | 190.160028 | 287.092258 | 0.000000 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 287.092258 | 212.907742 | 96.932230 | 190.160028 | 287.092258 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 24, 25, 26, 27, 32, 35, 36, 37, 38, 39, 42, 47, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 3, 4, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 43, 44, 45, 46, 47, 57, 65, 78, 92, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **287.092258 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a15e35bcefc9cadca908471a80be8fa99aa2a2a5c4217d1d7c6658e2cbe82e1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 287.092258 | 254.341555 | 32.750703 | True |

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

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **287.092258 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a15e35bcefc9cadca908471a80be8fa99aa2a2a5c4217d1d7c6658e2cbe82e1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 287.092258 | 254.341555 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 250 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 513.849 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,998.141073 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,860.939641 | 0.000000 | 0.000000 | 6.717357 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,998.141073 | 0.000000 | 0.000000 | 6.717357 | none |
| 108 (day 5, h12) | 1.000 | 132.062082 | 367.937918 | 39.647743 | 92.414338 | 132.062081 | 0.387636 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 249.724876 | 250.275124 | 20.109085 | 229.615791 | 249.724876 | 0.439457 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 132.062082 | 367.937918 | 39.647743 | 92.414338 | 132.062081 | 0.387636 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 96, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | 108, 109, 110 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 100, 118 | none | False |

### Snapshot counterfactuals for this round

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **132.062081 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d500e0b0eab8277e579cf9111ac2416f838cd50663c77e43124d21d5ad37ec6f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 132.062081 | 99.311378 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **249.724876 MW**; maximum nodal residual 5.88e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/af0e6091c8e2b9dc0f4855eb38361c8e5af1f57fa724bda5790adf49c6a8c9f2.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 249.724876 | 229.615791 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **132.062081 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d500e0b0eab8277e579cf9111ac2416f838cd50663c77e43124d21d5ad37ec6f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 132.062081 | 99.311378 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,074.185 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,498.141073 | 0.000000 | 0.000000 | 6.725594 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,360.939641 | 0.000000 | 0.000000 | 6.725594 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,498.141073 | 0.000000 | 0.000000 | 6.725594 | none |
| 107 (day 5, h11) | 1.000 | 287.092258 | 212.907742 | 96.932230 | 190.160028 | 287.092258 | 0.224306 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 287.092258 | 212.907742 | 96.932230 | 190.160028 | 287.092258 | 0.224306 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 24, 25, 26, 27, 32, 35, 36, 37, 38, 39, 42, 47, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 3, 4, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 43, 44, 45, 46, 47, 57, 65, 78, 92, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **287.092258 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a15e35bcefc9cadca908471a80be8fa99aa2a2a5c4217d1d7c6658e2cbe82e1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 287.092258 | 254.341555 | 32.750703 | True |

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

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **287.092258 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a15e35bcefc9cadca908471a80be8fa99aa2a2a5c4217d1d7c6658e2cbe82e1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 287.092258 | 254.341555 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

This accepted campaign used a recorded numerical retry: `audited_numerical_retry`. [retry audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/execution.json>).

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/execution.json>).

| Earlier attempt | Outcome | Log |
| --- | --- | --- |
| official | evaluator exited 1 | [evaluation log](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-01/evaluation.log>) |
Campaign SHA-256: `8896afb9b0768d906055359c8982e15d61d82df2176c048bcbf884fadfeda06a`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_6141/attempt-02/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
