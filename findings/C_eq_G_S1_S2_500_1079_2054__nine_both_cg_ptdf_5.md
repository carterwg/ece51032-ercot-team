<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_1079_2054","policy":"C_eq_G_S1_S2","portfolio":"hosting_2_both_cg","buses":["1079","2054"],"weights":[0.5,0.5],"scenario":"nine_both_cg_ptdf_5","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign","campaign_sha256":"47e8deff069a05724a484eda2fa9ae736834abe862f87607c83758f6e9b0d742","score_usd":66581377333.67454,"it_value_usd":123053148597.11996,"grid_mwh":16546676.051917259,"generation_mwh":973323.9480790163,"modeled_generator_hours":88.0,"annual_generator_hours":3747.8356164378315,"required_annual_hours":604.3890410957065,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/47e8deff069a05724a484eda2fa9ae736834abe862f87607c83758f6e9b0d742-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_1079_2054 — nine_both_cg_ptdf_5

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262137 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.821852 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.686129 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 15.811259 |
| Campaign total | — | — | — | — | 123.053149 | 66.581377 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,500.000 | 1,500.000 | 99.965753% | 7.000 | 7.000 | 0.000 | 0.000 | 250.000000 |
| week-2-submission-2 | 3,894,838.026 | 485,161.974 | 88.923243% | 37.000 | 1,866.918 | 302.195 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,500.000 | 1,500.000 | 99.965753% | 7.000 | 7.000 | 0.000 | 0.000 | 250.000000 |
| week-3-submission-2 | 3,894,838.026 | 485,161.974 | 88.923243% | 37.000 | 1,866.918 | 302.195 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001150 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.441435 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.576008 | 0.001150 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 1.010592 | 0.441435 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 1079: 250 MW per submission, 2054: 250 MW per submission.
- Opponents: 9. Each uses 6141 (100 MW), 5395 (100 MW), 6342 (100 MW), 5451 (100 MW), 6004 (100 MW) per submission. G/C is 1 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 1,500.000 MWh. At periods 106, 107, 108, 109, 110, 111, 112, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 (day 5, h10) | 1.000 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 9, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 68, 69, 70, 71, 73 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/30a8d5d490d08d256455ae1e05e2d50be2a751d2609a3fe67b533ca3262401cc.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa07db98565960f92259a6595f0167594a29068e21d9c07ccea1e0c62cd6f67.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.73e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a2bf0ce13d39fbe837b30c54f4e9b9962fa826cdc62683a02e6ef68363237ddf.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.89e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5e2d900de852211892a384b1922bab2ec9fbb4d3d4d378061932d08a89c1fe8c.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.73e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a2bf0ce13d39fbe837b30c54f4e9b9962fa826cdc62683a02e6ef68363237ddf.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa07db98565960f92259a6595f0167594a29068e21d9c07ccea1e0c62cd6f67.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/30a8d5d490d08d256455ae1e05e2d50be2a751d2609a3fe67b533ca3262401cc.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117; represented annual output was 485,161.974 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 101, 102, 103, 104, 114, 115, 116, 117, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 109.599135 | 390.400865 | 679.358453 | 0.000000 | 0.000000 | 0.000000 | b01607:upper, b01841:lower |
| 59 (day 3, h11) | 82.773 | 125.000000 | 375.000000 | 326.455653 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 209.575942 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 209.575942 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 125.000000 | 375.000000 | 326.455653 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 64 (day 3, h16) | 82.773 | 109.599135 | 390.400865 | 679.358453 | 0.000000 | 0.000000 | 0.000000 | b01607:upper, b01841:lower |
| 79 (day 4, h07) | 97.732 | 125.000000 | 375.000000 | 495.875612 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 250.000000 | 250.000000 | 51.678283 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 342.009523 | 157.990477 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 83 (day 4, h11) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 84 (day 4, h12) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 500.000000 | 0.000000 | -0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 88 (day 4, h16) | 97.732 | 342.009523 | 157.990477 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 89 (day 4, h17) | 97.732 | 250.000000 | 250.000000 | 51.678283 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 91 (day 4, h19) | 97.732 | 125.000000 | 375.000000 | 495.875612 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 101 (day 5, h05) | 1.000 | 125.000000 | 375.000000 | 450.778110 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 250.000000 | 250.000000 | 41.753642 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 105 (day 5, h09) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 115 (day 5, h19) | 1.000 | 250.000000 | 250.000000 | 41.753642 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 117 (day 5, h21) | 1.000 | 125.000000 | 375.000000 | 450.778110 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 1, 2, 3, 23 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | 58, 64 | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 101, 102, 103, 115, 116, 117 | False |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1e670552d78474879a358f54cf1a51acbe5260adc923b6caf90bf8937839cff8.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec268e3351229abb61ffab3555fa2507a6ee4febf53c0c19b807b5d08a954855.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b9f9b73100a0beca4d908f2b793c78fd0297a76a1a3792fe38aa68bce3148448.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.42e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/be4ed88d32f3985501d0068a63b03a5330a020518870e400ca46e69d5de71894.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b9f9b73100a0beca4d908f2b793c78fd0297a76a1a3792fe38aa68bce3148448.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec268e3351229abb61ffab3555fa2507a6ee4febf53c0c19b807b5d08a954855.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1e670552d78474879a358f54cf1a51acbe5260adc923b6caf90bf8937839cff8.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fa28d5399c4daf1d971eb73878e26951e7588cb33d5b8c3993dd0f269c18ba8d.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.75e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d735c0e81305b04338f36e4d0a9b31d7525994771071fb50009b6e75c625ceb4.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.09e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23f0fb6211679cde13cf33f8e9b5fa5e84c74879d2a64e920c59dbe2845c8017.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96ed04c216b3e4a08924f2f6e4947df713c0e3c0c9a48f79990d8f15905de1d5.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.12e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/71ea6fd292bf922b15a1067826c012f967c7f49f90135c92ac2dea3ea6d86feb.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8305db125847b7af6074923beea295d732c85e1f864faa5f450b1b0bc60beaa9.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 3.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/338acc37665a6000a9b787207350b6434d90b0b611444c1dd2ec5582d86df786.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8305db125847b7af6074923beea295d732c85e1f864faa5f450b1b0bc60beaa9.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.12e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/71ea6fd292bf922b15a1067826c012f967c7f49f90135c92ac2dea3ea6d86feb.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96ed04c216b3e4a08924f2f6e4947df713c0e3c0c9a48f79990d8f15905de1d5.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.09e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23f0fb6211679cde13cf33f8e9b5fa5e84c74879d2a64e920c59dbe2845c8017.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.75e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d735c0e81305b04338f36e4d0a9b31d7525994771071fb50009b6e75c625ceb4.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fa28d5399c4daf1d971eb73878e26951e7588cb33d5b8c3993dd0f269c18ba8d.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dd3a7638a46344062012394e824dea371a5c8388d98894982bda544615abd875.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.33e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2d52112891a23f8d8a711072ed3ae72ad33e9fddb6f6095a9bd4690a1591ed35.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1b70fd895c3f92086e795e99291c00214d853e4e2f5678549987fe0553fc41f7.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c207aafc730e95ea6141752d4ef2a0213393c7df6b59ffe59c8b28500035415b.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2deafb64e4b04fd3ccbfa191fd6b9bd8a6b66300872fafdba78810f275115f0.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2deafb64e4b04fd3ccbfa191fd6b9bd8a6b66300872fafdba78810f275115f0.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c207aafc730e95ea6141752d4ef2a0213393c7df6b59ffe59c8b28500035415b.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1b70fd895c3f92086e795e99291c00214d853e4e2f5678549987fe0553fc41f7.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.33e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2d52112891a23f8d8a711072ed3ae72ad33e9fddb6f6095a9bd4690a1591ed35.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dd3a7638a46344062012394e824dea371a5c8388d98894982bda544615abd875.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 1,500.000 MWh. At periods 106, 107, 108, 109, 110, 111, 112, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 115.159491 | 0.000000 | 0.000000 | 9.982339 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 106 (day 5, h10) | 1.000 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.210707 | none |
| 107 (day 5, h11) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 108 (day 5, h12) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 109 (day 5, h13) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 110 (day 5, h14) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 111 (day 5, h15) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 112 (day 5, h16) | 1.000 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.210707 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 9, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 68, 69, 70, 71, 73 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/30a8d5d490d08d256455ae1e05e2d50be2a751d2609a3fe67b533ca3262401cc.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa07db98565960f92259a6595f0167594a29068e21d9c07ccea1e0c62cd6f67.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.73e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a2bf0ce13d39fbe837b30c54f4e9b9962fa826cdc62683a02e6ef68363237ddf.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.89e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5e2d900de852211892a384b1922bab2ec9fbb4d3d4d378061932d08a89c1fe8c.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.73e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a2bf0ce13d39fbe837b30c54f4e9b9962fa826cdc62683a02e6ef68363237ddf.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa07db98565960f92259a6595f0167594a29068e21d9c07ccea1e0c62cd6f67.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/30a8d5d490d08d256455ae1e05e2d50be2a751d2609a3fe67b533ca3262401cc.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117; represented annual output was 485,161.974 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 101, 102, 103, 104, 114, 115, 116, 117, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 109.599135 | 390.400865 | 679.358453 | 0.000000 | 0.000000 | 18.158184 | b01607:upper, b01841:lower |
| 59 (day 3, h11) | 82.773 | 125.000000 | 375.000000 | 326.455653 | 0.000000 | 0.000000 | 20.662116 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 209.575942 | 0.000000 | 0.000000 | 30.031894 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 30.914016 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 209.575942 | 0.000000 | 0.000000 | 30.031894 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 125.000000 | 375.000000 | 326.455653 | 0.000000 | 0.000000 | 20.662116 | b01841:lower |
| 64 (day 3, h16) | 82.773 | 109.599135 | 390.400865 | 679.358453 | 0.000000 | 0.000000 | 18.158184 | b01607:upper, b01841:lower |
| 79 (day 4, h07) | 97.732 | 125.000000 | 375.000000 | 495.875612 | 0.000000 | 0.000000 | 22.150691 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 36.500887 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 250.000000 | 250.000000 | 51.678283 | 0.000000 | 0.000000 | 25.740223 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 342.009523 | 157.990477 | -0.000000 | 0.000000 | 0.000000 | 16.267297 | b01841:lower |
| 83 (day 4, h11) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 84 (day 4, h12) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 500.000000 | 0.000000 | -0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 88 (day 4, h16) | 97.732 | 342.009523 | 157.990477 | -0.000000 | 0.000000 | 0.000000 | 16.267297 | b01841:lower |
| 89 (day 4, h17) | 97.732 | 250.000000 | 250.000000 | 51.678283 | 0.000000 | 0.000000 | 25.740223 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 36.500887 | b01841:lower |
| 91 (day 4, h19) | 97.732 | 125.000000 | 375.000000 | 495.875612 | 0.000000 | 0.000000 | 22.150691 | b01841:lower |
| 101 (day 5, h05) | 1.000 | 125.000000 | 375.000000 | 450.778110 | 0.000000 | 0.000000 | 0.226648 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.373481 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 250.000000 | 250.000000 | 41.753642 | 0.000000 | 0.000000 | 0.263377 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.109743 | none |
| 105 (day 5, h09) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.109743 | none |
| 115 (day 5, h19) | 1.000 | 250.000000 | 250.000000 | 41.753642 | 0.000000 | 0.000000 | 0.263377 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.373481 | b01841:lower |
| 117 (day 5, h21) | 1.000 | 125.000000 | 375.000000 | 450.778110 | 0.000000 | 0.000000 | 0.226648 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 1, 2, 3, 23 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | 58, 64 | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 88, 89, 90, 91, 101, 102, 103, 115, 116, 117 | False |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1e670552d78474879a358f54cf1a51acbe5260adc923b6caf90bf8937839cff8.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec268e3351229abb61ffab3555fa2507a6ee4febf53c0c19b807b5d08a954855.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b9f9b73100a0beca4d908f2b793c78fd0297a76a1a3792fe38aa68bce3148448.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.42e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/be4ed88d32f3985501d0068a63b03a5330a020518870e400ca46e69d5de71894.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b9f9b73100a0beca4d908f2b793c78fd0297a76a1a3792fe38aa68bce3148448.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec268e3351229abb61ffab3555fa2507a6ee4febf53c0c19b807b5d08a954855.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1e670552d78474879a358f54cf1a51acbe5260adc923b6caf90bf8937839cff8.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fa28d5399c4daf1d971eb73878e26951e7588cb33d5b8c3993dd0f269c18ba8d.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.75e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d735c0e81305b04338f36e4d0a9b31d7525994771071fb50009b6e75c625ceb4.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.09e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23f0fb6211679cde13cf33f8e9b5fa5e84c74879d2a64e920c59dbe2845c8017.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96ed04c216b3e4a08924f2f6e4947df713c0e3c0c9a48f79990d8f15905de1d5.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.12e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/71ea6fd292bf922b15a1067826c012f967c7f49f90135c92ac2dea3ea6d86feb.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8305db125847b7af6074923beea295d732c85e1f864faa5f450b1b0bc60beaa9.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 3.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/338acc37665a6000a9b787207350b6434d90b0b611444c1dd2ec5582d86df786.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 4.77e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8305db125847b7af6074923beea295d732c85e1f864faa5f450b1b0bc60beaa9.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.12e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/71ea6fd292bf922b15a1067826c012f967c7f49f90135c92ac2dea3ea6d86feb.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96ed04c216b3e4a08924f2f6e4947df713c0e3c0c9a48f79990d8f15905de1d5.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.09e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/23f0fb6211679cde13cf33f8e9b5fa5e84c74879d2a64e920c59dbe2845c8017.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.75e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d735c0e81305b04338f36e4d0a9b31d7525994771071fb50009b6e75c625ceb4.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fa28d5399c4daf1d971eb73878e26951e7588cb33d5b8c3993dd0f269c18ba8d.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dd3a7638a46344062012394e824dea371a5c8388d98894982bda544615abd875.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.33e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2d52112891a23f8d8a711072ed3ae72ad33e9fddb6f6095a9bd4690a1591ed35.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1b70fd895c3f92086e795e99291c00214d853e4e2f5678549987fe0553fc41f7.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c207aafc730e95ea6141752d4ef2a0213393c7df6b59ffe59c8b28500035415b.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2deafb64e4b04fd3ccbfa191fd6b9bd8a6b66300872fafdba78810f275115f0.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2deafb64e4b04fd3ccbfa191fd6b9bd8a6b66300872fafdba78810f275115f0.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c207aafc730e95ea6141752d4ef2a0213393c7df6b59ffe59c8b28500035415b.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1b70fd895c3f92086e795e99291c00214d853e4e2f5678549987fe0553fc41f7.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.33e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2d52112891a23f8d8a711072ed3ae72ad33e9fddb6f6095a9bd4690a1591ed35.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dd3a7638a46344062012394e824dea371a5c8388d98894982bda544615abd875.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/execution.json>).
Campaign SHA-256: `47e8deff069a05724a484eda2fa9ae736834abe862f87607c83758f6e9b0d742`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
