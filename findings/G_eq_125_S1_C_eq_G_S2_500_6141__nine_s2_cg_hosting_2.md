<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_125_S1_C_eq_G_S2_500_6141","policy":"G_eq_125_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_125_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"65661831dd14129dba877e2cf313e491430faa641d9b18a8ac4af4701db6554d","score_usd":68961998034.88841,"it_value_usd":123053148597.11996,"grid_mwh":17217710.430738796,"generation_mwh":302289.5692574818,"modeled_generator_hours":60.0,"annual_generator_hours":2678.728767122528,"required_annual_hours":12.000000000114472,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/65661831dd14129dba877e2cf313e491430faa641d9b18a8ac4af4701db6554d-3eea05334a1d.json"} -->
# G_eq_125_S1_C_eq_G_S2_500_6141 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 125.000 | 500.000000 | 500.000000 | 30.763287 | 18.013149 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.176910 |
| week-3-submission-1 | 500.000 | 125.000 | 500.000000 | 500.000000 | 30.763287 | 17.457281 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.314657 |
| Campaign total | — | — | — | — | 123.053149 | 68.961998 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,875.264 | 124.736 | 99.997152% | 1.000 | 1.000 | 1.000 | 0.000 | 124.735984 |
| week-2-submission-2 | 4,228,979.951 | 151,020.049 | 96.552054% | 29.000 | 1,338.364 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,875.264 | 124.736 | 99.997152% | 1.000 | 1.000 | 1.000 | 0.000 | 124.735984 |
| week-3-submission-2 | 4,228,979.951 | 151,020.049 | 96.552054% | 29.000 | 1,338.364 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000138 | 0.250000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.086377 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.555868 | 0.000138 | 0.250000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.862253 | 0.086377 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_125_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 125 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 109; represented annual output was 124.736 MWh. Own generation was physically necessary for admitted load at verified periods 109. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 124.735984 | 375.264016 | -0.000000 | 124.735984 | 124.735984 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 151,020.049 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 (day 3, h12) | 82.773 | 13.392344 | 486.607656 | 1,415.779646 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,418.671869 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 13.392344 | 486.607656 | 1,415.779646 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,344.733742 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 966.746252 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 648.052799 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 417.865581 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 283.198080 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 238.480269 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 283.198080 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 417.865581 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 648.052799 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 966.746252 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,344.733742 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,342.297813 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 936.667253 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 545.350283 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 213.292817 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 287.806502 | 212.193498 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 85.280222 | 85.280222 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 487.534532 | 487.534532 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999998 | 499.999998 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 487.534532 | 487.534532 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 85.280222 | 85.280222 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 287.806502 | 212.193498 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 213.292817 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 545.350283 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 936.667253 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,342.297813 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/84cf417339ef605697f9e7614f082c3531a05fa8e0d31e56175089812ee32f49.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/697a3c24df98065a34e716db29d76d7c97a64701e88042c1d787a5ad02e0bc48.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/84cf417339ef605697f9e7614f082c3531a05fa8e0d31e56175089812ee32f49.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4a88dde50cfc8eabfb7fc018cbd4b6eb34a5968b10603c77ca74ce9f5a52d5a.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8eaffc728ff6cfa19d8c18320fe1a15d3e4168b9c4a4c285efe8a5e6460a4ac5.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.48e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d7a0b2987d583c56db7a8a01e0d874015050f5c3f955d5e4971930795f27d49.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/935e0263867a831b8a60db0ad670785d4585a02b0c1bd69cc22a9a88686506b9.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/59e17a1a2df366e39232e3724cc1f467760eb8a1b02883d3a282be9dc4e7d088.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0cbad8145a093a111c54fef3d72e6ed60f752c5b38d03c8da2b6dde41f5973b3.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/59e17a1a2df366e39232e3724cc1f467760eb8a1b02883d3a282be9dc4e7d088.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/935e0263867a831b8a60db0ad670785d4585a02b0c1bd69cc22a9a88686506b9.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.48e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d7a0b2987d583c56db7a8a01e0d874015050f5c3f955d5e4971930795f27d49.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8eaffc728ff6cfa19d8c18320fe1a15d3e4168b9c4a4c285efe8a5e6460a4ac5.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4a88dde50cfc8eabfb7fc018cbd4b6eb34a5968b10603c77ca74ce9f5a52d5a.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/229face3be9c866488561ba76ae2b4a4a22c56652e37c9eb9a50be30f0695a67.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/525e97c67505cf01fb0b10ae314644be6b5847dbebea1d550155ce26889104d7.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7f346dc3b0be3b9ae27cf1a09b2169db69971db7c0c1fed9da91ac25ec2e8f15.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.87e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78796250468e0596af7db098dd00bde9b2ec86dcae308e3da36fbd7f7cc7ebe1.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/435bedc02ef88cf19f28198d89aa34a271fce6258d5c2d033f9753efe72a2459.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **85.280222 MW**; maximum nodal residual 3.94e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c6507e87ab4e0d561e67a67b579584fe03514f4ea284f9a841206decc7792aab.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **487.534532 MW**; maximum nodal residual 4.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d1505245c537eea0ce01b535ca590bb53a40c3dafa01ad3414d0f91ce89c42dd.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **487.534532 MW**; maximum nodal residual 4.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d1505245c537eea0ce01b535ca590bb53a40c3dafa01ad3414d0f91ce89c42dd.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **85.280222 MW**; maximum nodal residual 3.94e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c6507e87ab4e0d561e67a67b579584fe03514f4ea284f9a841206decc7792aab.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/435bedc02ef88cf19f28198d89aa34a271fce6258d5c2d033f9753efe72a2459.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.87e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78796250468e0596af7db098dd00bde9b2ec86dcae308e3da36fbd7f7cc7ebe1.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7f346dc3b0be3b9ae27cf1a09b2169db69971db7c0c1fed9da91ac25ec2e8f15.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/525e97c67505cf01fb0b10ae314644be6b5847dbebea1d550155ce26889104d7.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/229face3be9c866488561ba76ae2b4a4a22c56652e37c9eb9a50be30f0695a67.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 125 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 109; represented annual output was 124.736 MWh. Own generation was physically necessary for admitted load at verified periods 109.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 2,103.020880 | 0.000000 | 0.000000 | 6.576352 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,965.819448 | 0.000000 | 0.000000 | 6.717357 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 2,103.020880 | 0.000000 | 0.000000 | 6.576352 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 124.735984 | 375.264016 | -0.000000 | 124.735984 | 124.735984 | 0.658924 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 151,020.049 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 (day 3, h12) | 82.773 | 13.392344 | 486.607656 | 1,415.779646 | 0.000000 | 0.000000 | 22.631543 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,418.671869 | 0.000000 | 0.000000 | 18.221735 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 13.392344 | 486.607656 | 1,415.779646 | 0.000000 | 0.000000 | 22.631543 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,344.733742 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 966.746252 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 648.052799 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 417.865581 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 283.198080 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 238.480269 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 283.198080 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 417.865581 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 648.052799 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 966.746252 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,344.733742 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,342.297813 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 936.667253 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 545.350283 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 213.292817 | 0.000000 | 0.000000 | 0.242982 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 287.806502 | 212.193498 | 0.000000 | 0.000000 | 0.000000 | 0.223554 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 85.280222 | 85.280222 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 487.534532 | 487.534532 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999998 | 499.999998 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 487.534532 | 487.534532 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 85.280222 | 85.280222 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 287.806502 | 212.193498 | 0.000000 | 0.000000 | 0.000000 | 0.223554 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 213.292817 | 0.000000 | 0.000000 | 0.242982 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 545.350283 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 936.667253 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,342.297813 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/84cf417339ef605697f9e7614f082c3531a05fa8e0d31e56175089812ee32f49.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/697a3c24df98065a34e716db29d76d7c97a64701e88042c1d787a5ad02e0bc48.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/84cf417339ef605697f9e7614f082c3531a05fa8e0d31e56175089812ee32f49.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4a88dde50cfc8eabfb7fc018cbd4b6eb34a5968b10603c77ca74ce9f5a52d5a.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8eaffc728ff6cfa19d8c18320fe1a15d3e4168b9c4a4c285efe8a5e6460a4ac5.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.48e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d7a0b2987d583c56db7a8a01e0d874015050f5c3f955d5e4971930795f27d49.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/935e0263867a831b8a60db0ad670785d4585a02b0c1bd69cc22a9a88686506b9.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/59e17a1a2df366e39232e3724cc1f467760eb8a1b02883d3a282be9dc4e7d088.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0cbad8145a093a111c54fef3d72e6ed60f752c5b38d03c8da2b6dde41f5973b3.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/59e17a1a2df366e39232e3724cc1f467760eb8a1b02883d3a282be9dc4e7d088.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/935e0263867a831b8a60db0ad670785d4585a02b0c1bd69cc22a9a88686506b9.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.48e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d7a0b2987d583c56db7a8a01e0d874015050f5c3f955d5e4971930795f27d49.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.57e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8eaffc728ff6cfa19d8c18320fe1a15d3e4168b9c4a4c285efe8a5e6460a4ac5.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4a88dde50cfc8eabfb7fc018cbd4b6eb34a5968b10603c77ca74ce9f5a52d5a.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/229face3be9c866488561ba76ae2b4a4a22c56652e37c9eb9a50be30f0695a67.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/525e97c67505cf01fb0b10ae314644be6b5847dbebea1d550155ce26889104d7.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7f346dc3b0be3b9ae27cf1a09b2169db69971db7c0c1fed9da91ac25ec2e8f15.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.87e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78796250468e0596af7db098dd00bde9b2ec86dcae308e3da36fbd7f7cc7ebe1.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/435bedc02ef88cf19f28198d89aa34a271fce6258d5c2d033f9753efe72a2459.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **85.280222 MW**; maximum nodal residual 3.94e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c6507e87ab4e0d561e67a67b579584fe03514f4ea284f9a841206decc7792aab.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **487.534532 MW**; maximum nodal residual 4.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d1505245c537eea0ce01b535ca590bb53a40c3dafa01ad3414d0f91ce89c42dd.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **487.534532 MW**; maximum nodal residual 4.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d1505245c537eea0ce01b535ca590bb53a40c3dafa01ad3414d0f91ce89c42dd.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **85.280222 MW**; maximum nodal residual 3.94e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c6507e87ab4e0d561e67a67b579584fe03514f4ea284f9a841206decc7792aab.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/435bedc02ef88cf19f28198d89aa34a271fce6258d5c2d033f9753efe72a2459.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.87e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78796250468e0596af7db098dd00bde9b2ec86dcae308e3da36fbd7f7cc7ebe1.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7f346dc3b0be3b9ae27cf1a09b2169db69971db7c0c1fed9da91ac25ec2e8f15.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/525e97c67505cf01fb0b10ae314644be6b5847dbebea1d550155ce26889104d7.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/229face3be9c866488561ba76ae2b4a4a22c56652e37c9eb9a50be30f0695a67.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `65661831dd14129dba877e2cf313e491430faa641d9b18a8ac4af4701db6554d`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_125_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
