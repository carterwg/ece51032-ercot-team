<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_C_eq_G_S2_500_6141_5395","policy":"G_eq_0_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_2_s2_cg","buses":["6141","5395"],"weights":[0.5,0.5],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"e81d114cbe621dd685a4677958acbd0a44d77b730de8fd04e134e444b54d0e28","score_usd":55000269022.64908,"it_value_usd":98741557699.9907,"grid_mwh":13522012.425141796,"generation_mwh":536563.9755920873,"modeled_generator_hours":78.0,"annual_generator_hours":3737.8356164377356,"required_annual_hours":6.000000000057237,"minimum_admission":0.6048603197188208,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/e81d114cbe621dd685a4677958acbd0a44d77b730de8fd04e134e444b54d0e28-3eea05334a1d.json"} -->
# G_eq_0_S1_C_eq_G_S2_500_6141_5395 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 302.430160 | 302.430160 | 18.607492 | 11.046738 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430160 | 30.763287 | 17.068919 |
| week-3-submission-1 | 500.000 | 0.000 | 302.430160 | 302.430160 | 18.607492 | 10.709892 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430160 | 30.763287 | 16.174720 |
| Campaign total | — | — | — | — | 98.741558 | 55.000269 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,649,288.200 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 4,111,718.012 | 268,281.988 | 93.874840% | 39.000 | 1,868.918 | 3.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 2,649,288.200 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 4,111,718.012 | 268,281.988 | 93.874840% | 39.000 | 1,868.918 | 3.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.194368 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.336846 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-3-submission-2 | 0.894199 | 0.194368 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_C_eq_G_S2`.
- Layout: 6141: 250 MW per submission, 5395: 250 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430160 MW** (60.486032%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267380 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430160 | 0.302460 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 7.24e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/57e76a1a04893120f8b9c7c437cb663dc5a50a96f8aa61e8227e1903f043760c.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 4.2e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/24c42d8698db083081fbe8f98f379e0a7b3baf0ff3dd52046dc8ad771bd614f7.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118; represented annual output was 268,281.988 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 62.500000 | 437.500000 | 2,363.047990 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 62.500000 | 437.500000 | 1,979.556293 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 62.500000 | 437.500000 | 1,735.779061 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 62.500000 | 437.500000 | 1,653.685881 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 62.500000 | 437.500000 | 1,735.779061 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 62.500000 | 437.500000 | 1,979.556293 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 62.500000 | 437.500000 | 2,363.047990 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 62.500000 | 437.500000 | 2,168.140771 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 101.839488 | 398.160512 | 1,589.141369 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 1,224.275683 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 250.000000 | 250.000000 | 910.315575 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 250.000000 | 250.000000 | 680.128357 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 250.000000 | 250.000000 | 535.426626 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 250.000000 | 250.000000 | 486.071569 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 250.000000 | 250.000000 | 535.426626 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 250.000000 | 250.000000 | 680.128357 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 250.000000 | 250.000000 | 910.315575 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 1,224.275683 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 101.839488 | 398.160512 | 1,589.141369 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 62.500000 | 437.500000 | 2,168.140771 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 12.670507 | 487.329493 | 2,609.048192 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 62.500000 | 437.500000 | 2,121.193414 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 104.163924 | 395.836076 | 1,587.890906 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 1,194.196685 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 250.000000 | 250.000000 | 807.613059 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 250.000000 | 250.000000 | 458.272174 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 250.000000 | 250.000000 | 163.415122 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 362.496086 | 362.496086 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.697539 | 499.697539 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 362.496086 | 362.496086 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 250.000000 | 250.000000 | 163.415122 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 250.000000 | 250.000000 | 458.272174 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 250.000000 | 250.000000 | 807.613059 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 1,194.196685 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 104.163924 | 395.836076 | 1,587.890906 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 62.500000 | 437.500000 | 2,121.193414 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 12.670507 | 487.329493 | 2,609.048192 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | 100, 118 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 30, 31, 35, 36, 37, 38, 39, 43, 44, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 90, 91, 100, 101, 102, 116, 117, 118 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118 | True |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/82a600543476fb51d791c67ca8344d641f0b3ef9af65d42c8fb723872272a4b9.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bfdf1c8ea72ffe8e2edea385a90690a3b09cba7e996d89aea63eca341db90b86.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.55e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aee4838c5d18886100c3b467fd25fc8740317645970aec6a54f80678a6d90dd.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.98e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96530b8d4fc1f1615cd56c5d91abfc238da6af7537d9f92610e7ac0d3da7d7c8.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.55e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aee4838c5d18886100c3b467fd25fc8740317645970aec6a54f80678a6d90dd.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bfdf1c8ea72ffe8e2edea385a90690a3b09cba7e996d89aea63eca341db90b86.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/82a600543476fb51d791c67ca8344d641f0b3ef9af65d42c8fb723872272a4b9.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4cae83915f92f1c7f0b3ebdf7ab6313d5d278612ad9662be2e7dec5a9f3c807d.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4391d2443483545ac13d47b87262562275137c05fa905a0469854f59eee8a595.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/370e60974b76c6b8dc1bb25b992ed65f54aaf0e60e75d278b0b24d28a3728bc3.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c84c49dffc90b4c6a10ef81c597def105510fef9041468fa9da09ff756a09de.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47fa5f066a27592a88c1e0c57e215089647401d4f17092d2548b0ff74fbf833f.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c5820f6e8b410bb24c968379de615b3f72dc7fbfc98651b9c54f4e7a422f541.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/25ef49188765e516461f704cce7c1f2ad0415fc6d7c260769d2e6959562c4d48.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c5820f6e8b410bb24c968379de615b3f72dc7fbfc98651b9c54f4e7a422f541.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47fa5f066a27592a88c1e0c57e215089647401d4f17092d2548b0ff74fbf833f.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c84c49dffc90b4c6a10ef81c597def105510fef9041468fa9da09ff756a09de.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/370e60974b76c6b8dc1bb25b992ed65f54aaf0e60e75d278b0b24d28a3728bc3.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4391d2443483545ac13d47b87262562275137c05fa905a0469854f59eee8a595.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4cae83915f92f1c7f0b3ebdf7ab6313d5d278612ad9662be2e7dec5a9f3c807d.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4f9f0e7a9545193e26f93970cf68d73d67f182d5b184a164b4cff32c9e0d530c.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8e02f49c0e3020e1b73b2d58b9d61560da44bdae0e9e2419363e8b5416bc6a6a.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2b3ebe522d19a64c1cf3cab1f87954cdace886d3242031558ffcd88e589a7558.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/58c11522341f71311e371d89b21980545eee0e0bac884cfa5a80c5add6c2f875.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/715da12085ba0f0a69dd077db7c2019c4e2812535404320a76372b7a7fc58f3b.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f0b885241636c05756ea50c846d38acb66870798eecad96c04615fabdb521089.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bf18ccec71b7f27495f6df00d26bfc11ee41132cd5df5cfec131047c734a01e8.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/48fbf2e321d3905fd50619ff130b974c465cdbca06a81af07ccb79faaa5559bb.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496086 MW**; maximum nodal residual 5.79e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cf1a0327112624869f2b4de9a64e7388a053327304ddaeec364cbd19ad83a8cc.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.697539 MW**; maximum nodal residual 7.88e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5dd61f5078d345a76ff2c52f5b018988d17cb5038b2718f7ea7e3b7f718c4681.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496086 MW**; maximum nodal residual 5.79e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cf1a0327112624869f2b4de9a64e7388a053327304ddaeec364cbd19ad83a8cc.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/48fbf2e321d3905fd50619ff130b974c465cdbca06a81af07ccb79faaa5559bb.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bf18ccec71b7f27495f6df00d26bfc11ee41132cd5df5cfec131047c734a01e8.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f0b885241636c05756ea50c846d38acb66870798eecad96c04615fabdb521089.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/715da12085ba0f0a69dd077db7c2019c4e2812535404320a76372b7a7fc58f3b.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/58c11522341f71311e371d89b21980545eee0e0bac884cfa5a80c5add6c2f875.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2b3ebe522d19a64c1cf3cab1f87954cdace886d3242031558ffcd88e589a7558.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8e02f49c0e3020e1b73b2d58b9d61560da44bdae0e9e2419363e8b5416bc6a6a.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4f9f0e7a9545193e26f93970cf68d73d67f182d5b184a164b4cff32c9e0d530c.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430160 MW** (60.486032%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267380 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 302.430160 | 2,228.059324 | 0.000000 | 0.000000 | 4.026809 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 302.430160 | 2,090.857892 | 0.000000 | 0.000000 | 4.026809 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 302.430160 | 2,228.059324 | 0.000000 | 0.000000 | 4.026809 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430160 | 0.302460 | 0.000000 | 0.000000 | 0.061781 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 7.24e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/57e76a1a04893120f8b9c7c437cb663dc5a50a96f8aa61e8227e1903f043760c.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 4.2e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/24c42d8698db083081fbe8f98f379e0a7b3baf0ff3dd52046dc8ad771bd614f7.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118; represented annual output was 268,281.988 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 62.500000 | 437.500000 | 2,363.047990 | 0.000000 | 0.000000 | 11.632904 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 62.500000 | 437.500000 | 1,979.556293 | 0.000000 | 0.000000 | 12.359441 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 62.500000 | 437.500000 | 1,735.779061 | 0.000000 | 0.000000 | 19.676646 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 62.500000 | 437.500000 | 1,653.685881 | 0.000000 | 0.000000 | 22.561812 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 62.500000 | 437.500000 | 1,735.779061 | 0.000000 | 0.000000 | 19.676646 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 62.500000 | 437.500000 | 1,979.556293 | 0.000000 | 0.000000 | 12.359441 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 62.500000 | 437.500000 | 2,363.047990 | 0.000000 | 0.000000 | 11.632904 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 62.500000 | 437.500000 | 2,168.140771 | 0.000000 | 0.000000 | 14.563479 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 101.839488 | 398.160512 | 1,589.141369 | 0.000000 | 0.000000 | 30.345998 | b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 1,224.275683 | 0.000000 | 0.000000 | 29.497727 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 250.000000 | 250.000000 | 910.315575 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 250.000000 | 250.000000 | 680.128357 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 250.000000 | 250.000000 | 535.426626 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 250.000000 | 250.000000 | 486.071569 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 250.000000 | 250.000000 | 535.426626 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 250.000000 | 250.000000 | 680.128357 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 250.000000 | 250.000000 | 910.315575 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 1,224.275683 | 0.000000 | 0.000000 | 29.497727 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 101.839488 | 398.160512 | 1,589.141369 | 0.000000 | 0.000000 | 30.345998 | b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 62.500000 | 437.500000 | 2,168.140771 | 0.000000 | 0.000000 | 14.563479 | b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 12.670507 | 487.329493 | 2,609.048192 | 0.000000 | 0.000000 | 0.167719 | b00220:lower, b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 62.500000 | 437.500000 | 2,121.193414 | 0.000000 | 0.000000 | 0.149015 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 104.163924 | 395.836076 | 1,587.890906 | 0.000000 | 0.000000 | 0.309198 | b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 1,194.196685 | 0.000000 | 0.000000 | 0.301824 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 250.000000 | 250.000000 | 807.613059 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 250.000000 | 250.000000 | 458.272174 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 250.000000 | 250.000000 | 163.415122 | 0.000000 | 0.000000 | 0.295245 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.109743 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 362.496086 | 362.496086 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.697539 | 499.697539 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 362.496086 | 362.496086 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.109743 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 250.000000 | 250.000000 | 163.415122 | 0.000000 | 0.000000 | 0.295245 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 250.000000 | 250.000000 | 458.272174 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 250.000000 | 250.000000 | 807.613059 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 1,194.196685 | 0.000000 | 0.000000 | 0.301824 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 104.163924 | 395.836076 | 1,587.890906 | 0.000000 | 0.000000 | 0.309198 | b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 62.500000 | 437.500000 | 2,121.193414 | 0.000000 | 0.000000 | 0.149015 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 12.670507 | 487.329493 | 2,609.048192 | 0.000000 | 0.000000 | 0.167719 | b00220:lower, b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | 100, 118 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 30, 31, 35, 36, 37, 38, 39, 43, 44, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 90, 91, 100, 101, 102, 116, 117, 118 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118 | True |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/82a600543476fb51d791c67ca8344d641f0b3ef9af65d42c8fb723872272a4b9.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bfdf1c8ea72ffe8e2edea385a90690a3b09cba7e996d89aea63eca341db90b86.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.55e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aee4838c5d18886100c3b467fd25fc8740317645970aec6a54f80678a6d90dd.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.98e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96530b8d4fc1f1615cd56c5d91abfc238da6af7537d9f92610e7ac0d3da7d7c8.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.55e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aee4838c5d18886100c3b467fd25fc8740317645970aec6a54f80678a6d90dd.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bfdf1c8ea72ffe8e2edea385a90690a3b09cba7e996d89aea63eca341db90b86.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/82a600543476fb51d791c67ca8344d641f0b3ef9af65d42c8fb723872272a4b9.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4cae83915f92f1c7f0b3ebdf7ab6313d5d278612ad9662be2e7dec5a9f3c807d.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4391d2443483545ac13d47b87262562275137c05fa905a0469854f59eee8a595.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/370e60974b76c6b8dc1bb25b992ed65f54aaf0e60e75d278b0b24d28a3728bc3.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c84c49dffc90b4c6a10ef81c597def105510fef9041468fa9da09ff756a09de.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47fa5f066a27592a88c1e0c57e215089647401d4f17092d2548b0ff74fbf833f.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c5820f6e8b410bb24c968379de615b3f72dc7fbfc98651b9c54f4e7a422f541.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/25ef49188765e516461f704cce7c1f2ad0415fc6d7c260769d2e6959562c4d48.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.52e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c5820f6e8b410bb24c968379de615b3f72dc7fbfc98651b9c54f4e7a422f541.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47fa5f066a27592a88c1e0c57e215089647401d4f17092d2548b0ff74fbf833f.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c84c49dffc90b4c6a10ef81c597def105510fef9041468fa9da09ff756a09de.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/370e60974b76c6b8dc1bb25b992ed65f54aaf0e60e75d278b0b24d28a3728bc3.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4391d2443483545ac13d47b87262562275137c05fa905a0469854f59eee8a595.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4cae83915f92f1c7f0b3ebdf7ab6313d5d278612ad9662be2e7dec5a9f3c807d.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4f9f0e7a9545193e26f93970cf68d73d67f182d5b184a164b4cff32c9e0d530c.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8e02f49c0e3020e1b73b2d58b9d61560da44bdae0e9e2419363e8b5416bc6a6a.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2b3ebe522d19a64c1cf3cab1f87954cdace886d3242031558ffcd88e589a7558.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/58c11522341f71311e371d89b21980545eee0e0bac884cfa5a80c5add6c2f875.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/715da12085ba0f0a69dd077db7c2019c4e2812535404320a76372b7a7fc58f3b.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f0b885241636c05756ea50c846d38acb66870798eecad96c04615fabdb521089.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bf18ccec71b7f27495f6df00d26bfc11ee41132cd5df5cfec131047c734a01e8.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/48fbf2e321d3905fd50619ff130b974c465cdbca06a81af07ccb79faaa5559bb.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496086 MW**; maximum nodal residual 5.79e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cf1a0327112624869f2b4de9a64e7388a053327304ddaeec364cbd19ad83a8cc.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.697539 MW**; maximum nodal residual 7.88e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5dd61f5078d345a76ff2c52f5b018988d17cb5038b2718f7ea7e3b7f718c4681.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496086 MW**; maximum nodal residual 5.79e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cf1a0327112624869f2b4de9a64e7388a053327304ddaeec364cbd19ad83a8cc.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/48fbf2e321d3905fd50619ff130b974c465cdbca06a81af07ccb79faaa5559bb.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bf18ccec71b7f27495f6df00d26bfc11ee41132cd5df5cfec131047c734a01e8.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.11e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f0b885241636c05756ea50c846d38acb66870798eecad96c04615fabdb521089.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/715da12085ba0f0a69dd077db7c2019c4e2812535404320a76372b7a7fc58f3b.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/58c11522341f71311e371d89b21980545eee0e0bac884cfa5a80c5add6c2f875.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2b3ebe522d19a64c1cf3cab1f87954cdace886d3242031558ffcd88e589a7558.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8e02f49c0e3020e1b73b2d58b9d61560da44bdae0e9e2419363e8b5416bc6a6a.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4f9f0e7a9545193e26f93970cf68d73d67f182d5b184a164b4cff32c9e0d530c.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b01548:lower`, `b02136:lower`, `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `e81d114cbe621dd685a4677958acbd0a44d77b730de8fd04e134e444b54d0e28`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
