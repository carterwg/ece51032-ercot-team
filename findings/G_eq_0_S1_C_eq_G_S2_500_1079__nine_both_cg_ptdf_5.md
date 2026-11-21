<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_C_eq_G_S2_500_1079","policy":"G_eq_0_S1_C_eq_G_S2","portfolio":"hosting_1_s2_cg","buses":["1079"],"weights":[1.0],"scenario":"nine_both_cg_ptdf_5","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign","campaign_sha256":"446ed3df88f1bb9640889df06159fc9b82da47c681282f51164d87e7b1f1fe3a","score_usd":68548222251.657135,"it_value_usd":123053148597.11996,"grid_mwh":16482500.41611829,"generation_mwh":1037499.5838779843,"modeled_generator_hours":74.0,"annual_generator_hours":3733.835616437698,"required_annual_hours":604.3890410957065,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/446ed3df88f1bb9640889df06159fc9b82da47c681282f51164d87e7b1f1fe3a-3eea05334a1d.json"} -->
# G_eq_0_S1_C_eq_G_S2_500_1079 — nine_both_cg_ptdf_5

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 500.000000 | 500.000000 | 30.763287 | 18.263287 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.787785 |
| week-3-submission-1 | 500.000 | 0.000 | 500.000000 | 500.000000 | 30.763287 | 17.685932 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 15.811218 |
| Campaign total | — | — | — | — | 123.053149 | 68.548222 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,380,000.000 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 3,861,250.208 | 518,749.792 | 88.156397% | 37.000 | 1,866.918 | 302.195 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 3,861,250.208 | 518,749.792 | 88.156397% | 37.000 | 1,866.918 | 302.195 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.475502 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.577355 | 0.000000 | 0.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.976566 | 0.475502 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_C_eq_G_S2`.
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

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117; represented annual output was 518,749.792 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 101, 102, 103, 104, 114, 115, 116, 117, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 125.000000 | 375.000000 | 679.440816 | 0.000000 | 0.000000 | 0.000000 | b01607:upper, b01841:lower |
| 59 (day 3, h11) | 82.773 | 125.000000 | 375.000000 | 326.545195 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 209.613374 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 209.613374 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 125.000000 | 375.000000 | 326.545195 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 64 (day 3, h16) | 82.773 | 125.000000 | 375.000000 | 679.440816 | 0.000000 | 0.000000 | 0.000000 | b01607:upper, b01841:lower |
| 79 (day 4, h07) | 97.732 | 125.000000 | 375.000000 | 495.913044 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 375.000000 | 125.000000 | 51.719793 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 83 (day 4, h11) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 84 (day 4, h12) | 97.732 | 500.000000 | 0.000000 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 500.000000 | 0.000000 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 88 (day 4, h16) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 89 (day 4, h17) | 97.732 | 375.000000 | 125.000000 | 51.719793 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 91 (day 4, h19) | 97.732 | 125.000000 | 375.000000 | 495.913044 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 101 (day 5, h05) | 1.000 | 125.000000 | 375.000000 | 450.815542 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 375.000000 | 125.000000 | 41.795152 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 390.991860 | 109.008140 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 105 (day 5, h09) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 390.991860 | 109.008140 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 115 (day 5, h19) | 1.000 | 375.000000 | 125.000000 | 41.795152 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 117 (day 5, h21) | 1.000 | 125.000000 | 375.000000 | 450.815542 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 1, 2, 3, 23 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | 58, 64 | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 101, 102, 103, 115, 116, 117 | False |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b02e03d922288fa049297d904b5b0c41188eeeb6f65bfcafe9bf52b3253d02c9.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2513b61889dd1022fab3abeb0cee98bffbfe7ee3f2963573099e6014944355e0.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.79e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/21eb3fca17dc106a6de36098eb01306b2ad33a45e6033e5d027314a5f4b8b6ce.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.12e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d1e404b7a2e32ce0c47c721bfcaa1a065761f73375b6854462f40f3f26e0b11f.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.79e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/21eb3fca17dc106a6de36098eb01306b2ad33a45e6033e5d027314a5f4b8b6ce.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2513b61889dd1022fab3abeb0cee98bffbfe7ee3f2963573099e6014944355e0.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b02e03d922288fa049297d904b5b0c41188eeeb6f65bfcafe9bf52b3253d02c9.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.13e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/81f582fd5ac1e98b9ef97d8fc08b472d57242b9d6c1e857917eabd00ff1d5ac8.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c66bb88c54e030f3dc6d3161824708b7760adbe5466b0f6c20263fa95d20a812.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4944f1984017da790d9cf62058a6d53534268d278966f875d2dc3b6bdbca5f1.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.86e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a535719cc50c6b8afc9557298590261916bafc34dc561ed6654b329f2519977.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23ed8fae6b4ebf32421c45b3dfbc7bb5842acc67b3a1dc21cfbf44ffb31258ed.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/88972eff0bbfac1f0c8ddcdcaa985f365961ee28ec27e3b6d79d102e9d6a9866.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 6.76e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/432b6c350d9d887ac3a5d9e0781a8a3c32fae0ff4b19ad464e967005c99e82aa.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/88972eff0bbfac1f0c8ddcdcaa985f365961ee28ec27e3b6d79d102e9d6a9866.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23ed8fae6b4ebf32421c45b3dfbc7bb5842acc67b3a1dc21cfbf44ffb31258ed.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.86e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a535719cc50c6b8afc9557298590261916bafc34dc561ed6654b329f2519977.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4944f1984017da790d9cf62058a6d53534268d278966f875d2dc3b6bdbca5f1.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c66bb88c54e030f3dc6d3161824708b7760adbe5466b0f6c20263fa95d20a812.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.13e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/81f582fd5ac1e98b9ef97d8fc08b472d57242b9d6c1e857917eabd00ff1d5ac8.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b8d7bac7abfc292c8f45d24e563407561880ab5ba055fe2d3e320d840fa422cf.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.04e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7aa05d12dd5af338ff9d38399963bd357e925d1ff5bff76d700714f4c73049ad.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6451b842007dba49887f245e8e844a3470031de3a9697faf1a9ea06b94cf0851.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/28bbcc76737111b08fa8212310ecfaf1d6592dcb7a7a81d19fe60e6dc443141f.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 4.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d624e6f0e44edb861231c5a56a6f1335f49f8bf6e02dd15972ec9243da7c3504.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 4.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d624e6f0e44edb861231c5a56a6f1335f49f8bf6e02dd15972ec9243da7c3504.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/28bbcc76737111b08fa8212310ecfaf1d6592dcb7a7a81d19fe60e6dc443141f.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6451b842007dba49887f245e8e844a3470031de3a9697faf1a9ea06b94cf0851.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.04e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7aa05d12dd5af338ff9d38399963bd357e925d1ff5bff76d700714f4c73049ad.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b8d7bac7abfc292c8f45d24e563407561880ab5ba055fe2d3e320d840fa422cf.json>).

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

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117; represented annual output was 518,749.792 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 101, 102, 103, 104, 114, 115, 116, 117, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 125.000000 | 375.000000 | 679.440816 | 0.000000 | 0.000000 | 17.442096 | b01607:upper, b01841:lower |
| 59 (day 3, h11) | 82.773 | 125.000000 | 375.000000 | 326.545195 | 0.000000 | 0.000000 | 20.663508 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 209.613374 | 0.000000 | 0.000000 | 30.034061 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 30.916106 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 209.613374 | 0.000000 | 0.000000 | 30.034061 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 125.000000 | 375.000000 | 326.545195 | 0.000000 | 0.000000 | 20.663508 | b01841:lower |
| 64 (day 3, h16) | 82.773 | 125.000000 | 375.000000 | 679.440816 | 0.000000 | 0.000000 | 17.442096 | b01607:upper, b01841:lower |
| 79 (day 4, h07) | 97.732 | 125.000000 | 375.000000 | 495.913044 | 0.000000 | 0.000000 | 22.152149 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 36.503354 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 375.000000 | 125.000000 | 51.719793 | 0.000000 | 0.000000 | 12.871045 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 12.870473 | b01841:lower |
| 83 (day 4, h11) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 84 (day 4, h12) | 97.732 | 500.000000 | 0.000000 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 500.000000 | 0.000000 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 88 (day 4, h16) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 12.870473 | b01841:lower |
| 89 (day 4, h17) | 97.732 | 375.000000 | 125.000000 | 51.719793 | 0.000000 | 0.000000 | 12.871045 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 36.503354 | b01841:lower |
| 91 (day 4, h19) | 97.732 | 125.000000 | 375.000000 | 495.913044 | 0.000000 | 0.000000 | 22.152149 | b01841:lower |
| 101 (day 5, h05) | 1.000 | 125.000000 | 375.000000 | 450.815542 | 0.000000 | 0.000000 | 0.226663 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.373507 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 375.000000 | 125.000000 | 41.795152 | 0.000000 | 0.000000 | 0.131698 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 390.991860 | 109.008140 | -0.000000 | 0.000000 | 0.000000 | 0.191407 | none |
| 105 (day 5, h09) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 390.991860 | 109.008140 | -0.000000 | 0.000000 | 0.000000 | 0.191407 | none |
| 115 (day 5, h19) | 1.000 | 375.000000 | 125.000000 | 41.795152 | 0.000000 | 0.000000 | 0.131698 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.373507 | b01841:lower |
| 117 (day 5, h21) | 1.000 | 125.000000 | 375.000000 | 450.815542 | 0.000000 | 0.000000 | 0.226663 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 1, 2, 3, 23 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | 58, 64 | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 101, 102, 103, 115, 116, 117 | False |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b02e03d922288fa049297d904b5b0c41188eeeb6f65bfcafe9bf52b3253d02c9.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2513b61889dd1022fab3abeb0cee98bffbfe7ee3f2963573099e6014944355e0.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.79e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/21eb3fca17dc106a6de36098eb01306b2ad33a45e6033e5d027314a5f4b8b6ce.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.12e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d1e404b7a2e32ce0c47c721bfcaa1a065761f73375b6854462f40f3f26e0b11f.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.79e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/21eb3fca17dc106a6de36098eb01306b2ad33a45e6033e5d027314a5f4b8b6ce.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2513b61889dd1022fab3abeb0cee98bffbfe7ee3f2963573099e6014944355e0.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b02e03d922288fa049297d904b5b0c41188eeeb6f65bfcafe9bf52b3253d02c9.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.13e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/81f582fd5ac1e98b9ef97d8fc08b472d57242b9d6c1e857917eabd00ff1d5ac8.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c66bb88c54e030f3dc6d3161824708b7760adbe5466b0f6c20263fa95d20a812.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4944f1984017da790d9cf62058a6d53534268d278966f875d2dc3b6bdbca5f1.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.86e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a535719cc50c6b8afc9557298590261916bafc34dc561ed6654b329f2519977.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23ed8fae6b4ebf32421c45b3dfbc7bb5842acc67b3a1dc21cfbf44ffb31258ed.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/88972eff0bbfac1f0c8ddcdcaa985f365961ee28ec27e3b6d79d102e9d6a9866.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 6.76e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/432b6c350d9d887ac3a5d9e0781a8a3c32fae0ff4b19ad464e967005c99e82aa.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/88972eff0bbfac1f0c8ddcdcaa985f365961ee28ec27e3b6d79d102e9d6a9866.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23ed8fae6b4ebf32421c45b3dfbc7bb5842acc67b3a1dc21cfbf44ffb31258ed.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.86e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a535719cc50c6b8afc9557298590261916bafc34dc561ed6654b329f2519977.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b4944f1984017da790d9cf62058a6d53534268d278966f875d2dc3b6bdbca5f1.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c66bb88c54e030f3dc6d3161824708b7760adbe5466b0f6c20263fa95d20a812.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.13e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/81f582fd5ac1e98b9ef97d8fc08b472d57242b9d6c1e857917eabd00ff1d5ac8.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b8d7bac7abfc292c8f45d24e563407561880ab5ba055fe2d3e320d840fa422cf.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.04e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7aa05d12dd5af338ff9d38399963bd357e925d1ff5bff76d700714f4c73049ad.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6451b842007dba49887f245e8e844a3470031de3a9697faf1a9ea06b94cf0851.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/28bbcc76737111b08fa8212310ecfaf1d6592dcb7a7a81d19fe60e6dc443141f.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 4.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d624e6f0e44edb861231c5a56a6f1335f49f8bf6e02dd15972ec9243da7c3504.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 4.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d624e6f0e44edb861231c5a56a6f1335f49f8bf6e02dd15972ec9243da7c3504.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/28bbcc76737111b08fa8212310ecfaf1d6592dcb7a7a81d19fe60e6dc443141f.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6451b842007dba49887f245e8e844a3470031de3a9697faf1a9ea06b94cf0851.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.04e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7aa05d12dd5af338ff9d38399963bd357e925d1ff5bff76d700714f4c73049ad.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b8d7bac7abfc292c8f45d24e563407561880ab5ba055fe2d3e320d840fa422cf.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `446ed3df88f1bb9640889df06159fc9b82da47c681282f51164d87e7b1f1fe3a`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
