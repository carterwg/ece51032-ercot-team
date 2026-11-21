<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_6141_5395","policy":"C_eq_G_S1_S2","portfolio":"bottleneck_ptdf_2_both_cg","buses":["6141","5395"],"weights":[0.5,0.5],"scenario":"nine_both_cg_ptdf_5","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign","campaign_sha256":"973b47acc7f34ba647118e0d9f5b0a33734fba5b09ab7e945860354a3e49b5ac","score_usd":66714536762.850136,"it_value_usd":123053148597.11996,"grid_mwh":16653950.766239844,"generation_mwh":866049.2337564306,"modeled_generator_hours":88.0,"annual_generator_hours":3747.8356164378315,"required_annual_hours":604.3890410957065,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/973b47acc7f34ba647118e0d9f5b0a33734fba5b09ab7e945860354a3e49b5ac-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_6141_5395 — nine_both_cg_ptdf_5

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262385 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.880988 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.687403 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 15.883760 |
| Campaign total | — | — | — | — | 123.053149 | 66.714537 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,794.156 | 1,205.844 | 99.972469% | 7.000 | 7.000 | 0.000 | 0.000 | 250.000000 |
| week-2-submission-2 | 3,948,181.227 | 431,818.773 | 90.141124% | 37.000 | 1,866.918 | 302.195 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,794.156 | 1,205.844 | 99.972469% | 7.000 | 7.000 | 0.000 | 0.000 | 250.000000 |
| week-3-submission-2 | 3,948,181.227 | 431,818.773 | 90.141124% | 37.000 | 1,866.918 | 302.195 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000902 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.382299 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.574982 | 0.000902 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.997228 | 0.382299 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 6141: 250 MW per submission, 5395: 250 MW per submission.
- Opponents: 9. Each uses 6141 (100 MW), 5395 (100 MW), 6342 (100 MW), 5451 (100 MW), 6004 (100 MW) per submission. G/C is 1 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 1,205.844 MWh. At periods 106, 107, 108, 109, 110, 111, 112, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 (day 5, h10) | 1.000 | 62.500000 | 437.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 165.421778 | 334.578222 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 165.421778 | 334.578222 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 62.500000 | 437.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 10, 16, 56, 66, 72, 74 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 9, 12, 13, 14, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 68, 69, 70, 71, 73, 76, 94 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 25 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 11, 12, 13, 14, 15, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 75, 76, 77, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bdbde27ad0c4995291f100b7847e3c9b1571504faa527c56a217d6726eea3186.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e72611360fbd0450207ac0445251abb27b873bce0493289f042314f7755a513a.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c8fe834746ac8d614dab3cc564ed477efcc7a8bb274567074e996451ae18b91.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.94e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bb89df7bc1841a2fe5bbb725f8f5ce6f521a1a4bfb3f4070362056c475b7f6b3.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c8fe834746ac8d614dab3cc564ed477efcc7a8bb274567074e996451ae18b91.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e72611360fbd0450207ac0445251abb27b873bce0493289f042314f7755a513a.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bdbde27ad0c4995291f100b7847e3c9b1571504faa527c56a217d6726eea3186.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117; represented annual output was 431,818.773 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 101, 102, 103, 104, 114, 115, 116, 117, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 62.500000 | 437.500000 | 607.120584 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 59 (day 3, h11) | 82.773 | 62.500000 | 437.500000 | 233.699847 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 165.859768 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 62.500000 | 437.500000 | 233.699847 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 64 (day 3, h16) | 82.773 | 62.500000 | 437.500000 | 607.120584 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 79 (day 4, h07) | 97.732 | 62.500000 | 437.500000 | 416.198817 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 134.073485 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 230.632511 | 269.367489 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 83 (day 4, h11) | 97.732 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 84 (day 4, h12) | 97.732 | 445.138930 | 54.861070 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 474.965328 | 25.034672 | -0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 445.138930 | 54.861070 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 88 (day 4, h16) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 89 (day 4, h17) | 97.732 | 230.632511 | 269.367489 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 134.073485 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 91 (day 4, h19) | 97.732 | 62.500000 | 437.500000 | 416.198817 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 101 (day 5, h05) | 1.000 | 62.500000 | 437.500000 | 371.101315 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 133.026269 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 250.000000 | 250.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 378.476491 | 121.523509 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 105 (day 5, h09) | 1.000 | 491.765140 | 8.234860 | -0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 491.765140 | 8.234860 | -0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 378.476491 | 121.523509 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 115 (day 5, h19) | 1.000 | 250.000000 | 250.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 133.026269 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 117 (day 5, h21) | 1.000 | 62.500000 | 437.500000 | 371.101315 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 1, 2, 3, 23, 30, 44 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 89, 90, 91, 101, 102, 103, 115, 116, 117 | False |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/016e50d29e1e7a2b7aef7d002c8949e7b133762ca9e14c731c6ab560d24a3300.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.17e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/800541c552c56ff6feb6ad4afc1f922894787afc26fe10520bbf9951730410b7.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db056532b976dd7cf0a09509ad5b9ddb019e415485264040b3a6b18bbadb974c.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.72e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9511d499cf1c45e65dc2671b21e4076defcd9db5c24d175d18fa6aa0c43a05bf.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db056532b976dd7cf0a09509ad5b9ddb019e415485264040b3a6b18bbadb974c.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.17e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/800541c552c56ff6feb6ad4afc1f922894787afc26fe10520bbf9951730410b7.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/016e50d29e1e7a2b7aef7d002c8949e7b133762ca9e14c731c6ab560d24a3300.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cbf116e660fd90d2adcd0f2d7b67dd180469c282ef5bf438aeecd9f69d18f192.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/44a6a6519bbed084e5bd9d3d3edd484ba16bd5f6e0b5f219b0050893190f8de1.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2e8d9363893d166b732daf4044c2f144b36e2a809d9c09631df5f186eab896.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.38e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d7ebf02334f73d8ddedf4593f5584c25629e9b5a8b53208dbee47b90d2135a97.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.61e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d6dde89ead6c2b52a1417e67cceba9b950fa9e0030b16d204e12bdae389b53a6.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 2.72e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bb38c94b39b4b09ed2d225b85d544a61ee98b680b90fb4fb057915c41c274869.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 3.7e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c0db123e8eaa26d4256d6b34c316110e3e181c73f062e30e91e4a971a1ad53d.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 2.72e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bb38c94b39b4b09ed2d225b85d544a61ee98b680b90fb4fb057915c41c274869.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.61e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d6dde89ead6c2b52a1417e67cceba9b950fa9e0030b16d204e12bdae389b53a6.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.38e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d7ebf02334f73d8ddedf4593f5584c25629e9b5a8b53208dbee47b90d2135a97.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2e8d9363893d166b732daf4044c2f144b36e2a809d9c09631df5f186eab896.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/44a6a6519bbed084e5bd9d3d3edd484ba16bd5f6e0b5f219b0050893190f8de1.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cbf116e660fd90d2adcd0f2d7b67dd180469c282ef5bf438aeecd9f69d18f192.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/26ca813f987453145744d15791d6bddb0275e016d4f4318f046bd73b6a2dfb70.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b1e457bea9574b3d9386a46bdf9e7e23b9b926af99fc13b740d44062a5b95eb2.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc1c5b896330e5661965e15dd37f945bee6f71b301e8136b5289d1441fb61e97.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/056b7fac77570715cfb6d6bf8c8f6867b91daa6cb6b040743d62f97830b89909.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/87b4b1ea7bdefc939ac9eaf1c63eb9b9eda0d75d67653e9bf2b88aa5dce4fdf6.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/87b4b1ea7bdefc939ac9eaf1c63eb9b9eda0d75d67653e9bf2b88aa5dce4fdf6.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/056b7fac77570715cfb6d6bf8c8f6867b91daa6cb6b040743d62f97830b89909.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc1c5b896330e5661965e15dd37f945bee6f71b301e8136b5289d1441fb61e97.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b1e457bea9574b3d9386a46bdf9e7e23b9b926af99fc13b740d44062a5b95eb2.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/26ca813f987453145744d15791d6bddb0275e016d4f4318f046bd73b6a2dfb70.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 1,205.844 MWh. At periods 106, 107, 108, 109, 110, 111, 112, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 115.159491 | 0.000000 | 0.000000 | 9.982339 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 106 (day 5, h10) | 1.000 | 62.500000 | 437.500000 | 0.000000 | 0.000000 | 0.000000 | 0.245825 | none |
| 107 (day 5, h11) | 1.000 | 165.421778 | 334.578222 | 0.000000 | 0.000000 | 0.000000 | 0.352491 | none |
| 108 (day 5, h12) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 109 (day 5, h13) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 110 (day 5, h14) | 1.000 | 250.000000 | 250.000000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 111 (day 5, h15) | 1.000 | 165.421778 | 334.578222 | 0.000000 | 0.000000 | 0.000000 | 0.352491 | none |
| 112 (day 5, h16) | 1.000 | 62.500000 | 437.500000 | 0.000000 | 0.000000 | 0.000000 | 0.245825 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 10, 16, 56, 66, 72, 74 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 9, 12, 13, 14, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 68, 69, 70, 71, 73, 76, 94 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 25 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 11, 12, 13, 14, 15, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 75, 76, 77, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bdbde27ad0c4995291f100b7847e3c9b1571504faa527c56a217d6726eea3186.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e72611360fbd0450207ac0445251abb27b873bce0493289f042314f7755a513a.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c8fe834746ac8d614dab3cc564ed477efcc7a8bb274567074e996451ae18b91.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.94e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bb89df7bc1841a2fe5bbb725f8f5ce6f521a1a4bfb3f4070362056c475b7f6b3.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c8fe834746ac8d614dab3cc564ed477efcc7a8bb274567074e996451ae18b91.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e72611360fbd0450207ac0445251abb27b873bce0493289f042314f7755a513a.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.79e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bdbde27ad0c4995291f100b7847e3c9b1571504faa527c56a217d6726eea3186.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117; represented annual output was 431,818.773 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 101, 102, 103, 104, 114, 115, 116, 117, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 (day 3, h10) | 82.773 | 62.500000 | 437.500000 | 607.120584 | 0.000000 | 0.000000 | 19.982239 | b01841:lower |
| 59 (day 3, h11) | 82.773 | 62.500000 | 437.500000 | 233.699847 | 0.000000 | 0.000000 | 19.982239 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 28.496912 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 165.859768 | 0.000000 | 0.000000 | 29.653558 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 169.400000 | 0.000000 | 0.000000 | 28.496912 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 62.500000 | 437.500000 | 233.699847 | 0.000000 | 0.000000 | 19.982239 | b01841:lower |
| 64 (day 3, h16) | 82.773 | 62.500000 | 437.500000 | 607.120584 | 0.000000 | 0.000000 | 19.982239 | b01841:lower |
| 79 (day 4, h07) | 97.732 | 62.500000 | 437.500000 | 416.198817 | 0.000000 | 0.000000 | 23.593487 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 134.073485 | 0.000000 | 0.000000 | 35.012635 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 230.632511 | 269.367489 | -0.000000 | 0.000000 | 0.000000 | 27.735095 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 12.870473 | none |
| 83 (day 4, h11) | 97.732 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 10.725394 | none |
| 84 (day 4, h12) | 97.732 | 445.138930 | 54.861070 | -0.000000 | 247.639077 | 247.639077 | 9.414505 | none |
| 85 (day 4, h13) | 97.732 | 474.965328 | 25.034672 | -0.000000 | 384.840509 | 384.840509 | 4.296107 | none |
| 86 (day 4, h14) | 97.732 | 445.138930 | 54.861070 | -0.000000 | 247.639077 | 247.639077 | 9.414505 | none |
| 87 (day 4, h15) | 97.732 | 437.500000 | 62.500000 | 0.000000 | 0.000000 | 0.000000 | 10.725394 | none |
| 88 (day 4, h16) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 12.870473 | none |
| 89 (day 4, h17) | 97.732 | 230.632511 | 269.367489 | -0.000000 | 0.000000 | 0.000000 | 27.735095 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 134.073485 | 0.000000 | 0.000000 | 35.012635 | b01841:lower |
| 91 (day 4, h19) | 97.732 | 62.500000 | 437.500000 | 416.198817 | 0.000000 | 0.000000 | 23.593487 | b01841:lower |
| 101 (day 5, h05) | 1.000 | 62.500000 | 437.500000 | 371.101315 | 0.000000 | 0.000000 | 0.241411 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 133.026269 | 0.000000 | 0.000000 | 0.358253 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 250.000000 | 250.000000 | -0.000000 | 0.000000 | 0.000000 | 0.263384 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 378.476491 | 121.523509 | -0.000000 | 0.000000 | 0.000000 | 0.213383 | none |
| 105 (day 5, h09) | 1.000 | 491.765140 | 8.234860 | -0.000000 | 462.119642 | 462.119642 | 0.014460 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 491.765140 | 8.234860 | -0.000000 | 462.119642 | 462.119642 | 0.014460 | none |
| 114 (day 5, h18) | 1.000 | 378.476491 | 121.523509 | -0.000000 | 0.000000 | 0.000000 | 0.213383 | none |
| 115 (day 5, h19) | 1.000 | 250.000000 | 250.000000 | -0.000000 | 0.000000 | 0.000000 | 0.263384 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 133.026269 | 0.000000 | 0.000000 | 0.358253 | b01841:lower |
| 117 (day 5, h21) | 1.000 | 62.500000 | 437.500000 | 371.101315 | 0.000000 | 0.000000 | 0.241411 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00577 | 4037 → 4054 | upper | 98.000 | 98.000000 | 0, 1, 2, 3, 23, 30, 44 | none | False |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 89, 90, 91, 101, 102, 103, 115, 116, 117 | False |

### Snapshot counterfactuals for this round

- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/016e50d29e1e7a2b7aef7d002c8949e7b133762ca9e14c731c6ab560d24a3300.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.17e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/800541c552c56ff6feb6ad4afc1f922894787afc26fe10520bbf9951730410b7.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db056532b976dd7cf0a09509ad5b9ddb019e415485264040b3a6b18bbadb974c.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.72e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9511d499cf1c45e65dc2671b21e4076defcd9db5c24d175d18fa6aa0c43a05bf.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.06e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db056532b976dd7cf0a09509ad5b9ddb019e415485264040b3a6b18bbadb974c.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.17e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/800541c552c56ff6feb6ad4afc1f922894787afc26fe10520bbf9951730410b7.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/016e50d29e1e7a2b7aef7d002c8949e7b133762ca9e14c731c6ab560d24a3300.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cbf116e660fd90d2adcd0f2d7b67dd180469c282ef5bf438aeecd9f69d18f192.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/44a6a6519bbed084e5bd9d3d3edd484ba16bd5f6e0b5f219b0050893190f8de1.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2e8d9363893d166b732daf4044c2f144b36e2a809d9c09631df5f186eab896.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.38e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d7ebf02334f73d8ddedf4593f5584c25629e9b5a8b53208dbee47b90d2135a97.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.61e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d6dde89ead6c2b52a1417e67cceba9b950fa9e0030b16d204e12bdae389b53a6.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 2.72e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bb38c94b39b4b09ed2d225b85d544a61ee98b680b90fb4fb057915c41c274869.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 3.7e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5c0db123e8eaa26d4256d6b34c316110e3e181c73f062e30e91e4a971a1ad53d.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 2.72e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bb38c94b39b4b09ed2d225b85d544a61ee98b680b90fb4fb057915c41c274869.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.61e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d6dde89ead6c2b52a1417e67cceba9b950fa9e0030b16d204e12bdae389b53a6.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.38e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d7ebf02334f73d8ddedf4593f5584c25629e9b5a8b53208dbee47b90d2135a97.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a2e8d9363893d166b732daf4044c2f144b36e2a809d9c09631df5f186eab896.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/44a6a6519bbed084e5bd9d3d3edd484ba16bd5f6e0b5f219b0050893190f8de1.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cbf116e660fd90d2adcd0f2d7b67dd180469c282ef5bf438aeecd9f69d18f192.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/26ca813f987453145744d15791d6bddb0275e016d4f4318f046bd73b6a2dfb70.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b1e457bea9574b3d9386a46bdf9e7e23b9b926af99fc13b740d44062a5b95eb2.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc1c5b896330e5661965e15dd37f945bee6f71b301e8136b5289d1441fb61e97.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/056b7fac77570715cfb6d6bf8c8f6867b91daa6cb6b040743d62f97830b89909.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/87b4b1ea7bdefc939ac9eaf1c63eb9b9eda0d75d67653e9bf2b88aa5dce4fdf6.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 3.84e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/87b4b1ea7bdefc939ac9eaf1c63eb9b9eda0d75d67653e9bf2b88aa5dce4fdf6.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/056b7fac77570715cfb6d6bf8c8f6867b91daa6cb6b040743d62f97830b89909.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc1c5b896330e5661965e15dd37f945bee6f71b301e8136b5289d1441fb61e97.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b1e457bea9574b3d9386a46bdf9e7e23b9b926af99fc13b740d44062a5b95eb2.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.37e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/26ca813f987453145744d15791d6bddb0275e016d4f4318f046bd73b6a2dfb70.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b01548:lower`, `b02136:lower`, `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/execution.json>).
Campaign SHA-256: `973b47acc7f34ba647118e0d9f5b0a33734fba5b09ab7e945860354a3e49b5ac`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_both_cg_ptdf_5/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
