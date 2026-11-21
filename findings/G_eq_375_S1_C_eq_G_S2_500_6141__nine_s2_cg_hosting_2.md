<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_375_S1_C_eq_G_S2_500_6141","policy":"G_eq_375_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_375_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"e306b06d40cb5de1e37f1461fdf34888d6ee47c84f254aa54c520ca548ff376b","score_usd":67918165188.10603,"it_value_usd":123053148597.11996,"grid_mwh":17176589.19307821,"generation_mwh":343410.80691806646,"modeled_generator_hours":68.0,"annual_generator_hours":3013.81917808163,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/e306b06d40cb5de1e37f1461fdf34888d6ee47c84f254aa54c520ca548ff376b-3eea05334a1d.json"} -->
# G_eq_375_S1_C_eq_G_S2_500_6141 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 375.000 | 500.000000 | 500.000000 | 30.763287 | 17.512465 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.165754 |
| week-3-submission-1 | 500.000 | 375.000 | 500.000000 | 500.000000 | 30.763287 | 16.955582 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.284366 |
| Campaign total | — | — | — | — | 123.053149 | 67.918165 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,150.272 | 849.728 | 99.980600% | 3.000 | 3.000 | 3.000 | 0.000 | 374.710153 |
| week-2-submission-2 | 4,209,144.324 | 170,855.676 | 96.099185% | 31.000 | 1,503.910 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,150.272 | 849.728 | 99.980600% | 3.000 | 3.000 | 3.000 | 0.000 | 374.710153 |
| week-3-submission-2 | 4,209,144.324 | 170,855.676 | 96.099185% | 31.000 | 1,503.910 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000823 | 0.750000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.097534 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.556883 | 0.000823 | 0.750000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.881388 | 0.097534 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_375_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 375 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 849.728 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 237.508700 | 262.491300 | -0.000000 | 237.508700 | 237.508700 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 374.710153 | 125.289847 | -0.000000 | 374.710153 | 374.710153 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 237.508700 | 262.491300 | -0.000000 | 237.508700 | 237.508700 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 170,855.676 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59 (day 3, h11) | 82.773 | 8.074425 | 491.925575 | 1,562.741859 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 1,466.157470 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,412.913535 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 1,466.157470 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 63 (day 3, h15) | 82.773 | 8.074425 | 491.925575 | 1,562.741859 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,338.975408 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 960.987918 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 654.089241 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 423.902023 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 288.667357 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 242.771297 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 288.667357 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 423.902023 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 654.089241 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 960.987918 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,338.975408 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,336.539479 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 930.908919 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 551.386724 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 215.399944 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 299.222788 | 200.777212 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 335.254390 | 335.254390 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 335.254390 | 335.254390 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 299.222788 | 200.777212 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 215.399944 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 551.386724 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 930.908919 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,336.539479 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 57, 65, 78, 92, 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.83e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ad8dbd2c6ff805f7cea36308e4bb3152412f2035e54f0864e553d1a0c920d947.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.61e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c3f65dbc9371314405ce5bacfc7ba023c878e9f7de55d2d65f6d4e5ea00a102.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.18e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3b55af041c292a25b35dbda76f0c52b93384a8a8864fa4ed9adaa6587e42e12e.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.61e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c3f65dbc9371314405ce5bacfc7ba023c878e9f7de55d2d65f6d4e5ea00a102.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.83e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ad8dbd2c6ff805f7cea36308e4bb3152412f2035e54f0864e553d1a0c920d947.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.27e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/593f94cf71c58c4c9c5f8ba8f72d8367a68b319179d7cf91e38a733a89110615.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a5eac2ebbe0c3e1d8a13a89ee9f737c8fef72bf47b2e39e5960be4c5fd89ff4.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/07d69d0c22766aad724ae28399e5dda251ba77b1bb934e04f3bc158730c7e728.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/141042fa63a5547e6253e54a0991cd4f7322f4eed6ae55bde3e567ecbefbdb37.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/09170116b5d936fe5aec5af95bf06af3520c19fda70e2ba18af2484600e7f075.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0ac7c68832ae19eedccf59bbd40aa17874855feaa9705354b7609a95da1c886c.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/09170116b5d936fe5aec5af95bf06af3520c19fda70e2ba18af2484600e7f075.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/141042fa63a5547e6253e54a0991cd4f7322f4eed6ae55bde3e567ecbefbdb37.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/07d69d0c22766aad724ae28399e5dda251ba77b1bb934e04f3bc158730c7e728.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a5eac2ebbe0c3e1d8a13a89ee9f737c8fef72bf47b2e39e5960be4c5fd89ff4.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.27e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/593f94cf71c58c4c9c5f8ba8f72d8367a68b319179d7cf91e38a733a89110615.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5776f5baa9bdda0778f9c35ebf1553c3debce25d9c768332b190c6dcb3640eac.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.95e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d20b73aaac092646945ef1ae835492bc563092a170019d0908797a75c5bd086e.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.86e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2b491b044828fda868638e470253b89a0c8e58f822b7ba109acfaa2be5732f.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec83a12db9a2264486103bd43fb428fb3b164e674eecb5b8de2f5682d7905a71.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/50bc05f7845b94ebfc2897a3ae35b3d048fc884607df7993710824bdbfd5f258.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **335.254390 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8874622dca242b5f5cc896468e91db213e35dce754c232aa1d02a6b1cd90d0f.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **335.254390 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8874622dca242b5f5cc896468e91db213e35dce754c232aa1d02a6b1cd90d0f.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/50bc05f7845b94ebfc2897a3ae35b3d048fc884607df7993710824bdbfd5f258.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec83a12db9a2264486103bd43fb428fb3b164e674eecb5b8de2f5682d7905a71.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.86e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2b491b044828fda868638e470253b89a0c8e58f822b7ba109acfaa2be5732f.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.95e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d20b73aaac092646945ef1ae835492bc563092a170019d0908797a75c5bd086e.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5776f5baa9bdda0778f9c35ebf1553c3debce25d9c768332b190c6dcb3640eac.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 375 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 849.728 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,853.046711 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,715.845279 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,853.046711 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 237.508700 | 262.491300 | -0.000000 | 237.508700 | 237.508700 | 0.276544 | none |
| 109 (day 5, h13) | 1.000 | 374.710153 | 125.289847 | -0.000000 | 374.710153 | 374.710153 | 0.219996 | none |
| 110 (day 5, h14) | 1.000 | 237.508700 | 262.491300 | -0.000000 | 237.508700 | 237.508700 | 0.276544 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 170,855.676 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59 (day 3, h11) | 82.773 | 8.074425 | 491.925575 | 1,562.741859 | 0.000000 | 0.000000 | 22.878873 | b02579:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 1,466.157470 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,412.913535 | 0.000000 | 0.000000 | 18.221735 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 1,466.157470 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 63 (day 3, h15) | 82.773 | 8.074425 | 491.925575 | 1,562.741859 | 0.000000 | 0.000000 | 22.878873 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,338.975408 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 960.987918 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 654.089241 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 423.902023 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 288.667357 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 242.771297 | 0.000000 | 0.000000 | 36.864686 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 288.667357 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 423.902023 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 654.089241 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 960.987918 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,338.975408 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,336.539479 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 930.908919 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 551.386724 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 215.399944 | 0.000000 | 0.000000 | 0.377204 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 299.222788 | 200.777212 | 0.000000 | 0.000000 | 0.000000 | 0.211526 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 335.254390 | 335.254390 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 335.254390 | 335.254390 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 299.222788 | 200.777212 | 0.000000 | 0.000000 | 0.000000 | 0.211526 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 215.399944 | 0.000000 | 0.000000 | 0.377204 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 551.386724 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 930.908919 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,336.539479 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 57, 65, 78, 92, 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.83e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ad8dbd2c6ff805f7cea36308e4bb3152412f2035e54f0864e553d1a0c920d947.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.61e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c3f65dbc9371314405ce5bacfc7ba023c878e9f7de55d2d65f6d4e5ea00a102.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.18e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3b55af041c292a25b35dbda76f0c52b93384a8a8864fa4ed9adaa6587e42e12e.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.61e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c3f65dbc9371314405ce5bacfc7ba023c878e9f7de55d2d65f6d4e5ea00a102.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.83e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ad8dbd2c6ff805f7cea36308e4bb3152412f2035e54f0864e553d1a0c920d947.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.27e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/593f94cf71c58c4c9c5f8ba8f72d8367a68b319179d7cf91e38a733a89110615.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a5eac2ebbe0c3e1d8a13a89ee9f737c8fef72bf47b2e39e5960be4c5fd89ff4.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/07d69d0c22766aad724ae28399e5dda251ba77b1bb934e04f3bc158730c7e728.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/141042fa63a5547e6253e54a0991cd4f7322f4eed6ae55bde3e567ecbefbdb37.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/09170116b5d936fe5aec5af95bf06af3520c19fda70e2ba18af2484600e7f075.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0ac7c68832ae19eedccf59bbd40aa17874855feaa9705354b7609a95da1c886c.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/09170116b5d936fe5aec5af95bf06af3520c19fda70e2ba18af2484600e7f075.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/141042fa63a5547e6253e54a0991cd4f7322f4eed6ae55bde3e567ecbefbdb37.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/07d69d0c22766aad724ae28399e5dda251ba77b1bb934e04f3bc158730c7e728.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a5eac2ebbe0c3e1d8a13a89ee9f737c8fef72bf47b2e39e5960be4c5fd89ff4.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.27e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/593f94cf71c58c4c9c5f8ba8f72d8367a68b319179d7cf91e38a733a89110615.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5776f5baa9bdda0778f9c35ebf1553c3debce25d9c768332b190c6dcb3640eac.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.95e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d20b73aaac092646945ef1ae835492bc563092a170019d0908797a75c5bd086e.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.86e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2b491b044828fda868638e470253b89a0c8e58f822b7ba109acfaa2be5732f.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec83a12db9a2264486103bd43fb428fb3b164e674eecb5b8de2f5682d7905a71.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/50bc05f7845b94ebfc2897a3ae35b3d048fc884607df7993710824bdbfd5f258.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **335.254390 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8874622dca242b5f5cc896468e91db213e35dce754c232aa1d02a6b1cd90d0f.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **335.254390 MW**; maximum nodal residual 4.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8874622dca242b5f5cc896468e91db213e35dce754c232aa1d02a6b1cd90d0f.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/50bc05f7845b94ebfc2897a3ae35b3d048fc884607df7993710824bdbfd5f258.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ec83a12db9a2264486103bd43fb428fb3b164e674eecb5b8de2f5682d7905a71.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.86e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2b491b044828fda868638e470253b89a0c8e58f822b7ba109acfaa2be5732f.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.95e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d20b73aaac092646945ef1ae835492bc563092a170019d0908797a75c5bd086e.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5776f5baa9bdda0778f9c35ebf1553c3debce25d9c768332b190c6dcb3640eac.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `e306b06d40cb5de1e37f1461fdf34888d6ee47c84f254aa54c520ca548ff376b`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_375_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
