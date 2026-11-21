<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_1079_2054","policy":"C_eq_G_S1_S2","portfolio":"hosting_2_both_cg","buses":["1079","2054"],"weights":[0.5,0.5],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"3869110b854cc08d7ffed8e368863cec06b955547b8df64e45b1de211d37fc23","score_usd":64841067755.6917,"it_value_usd":123053148597.11996,"grid_mwh":15384265.433744414,"generation_mwh":2135734.566251863,"modeled_generator_hours":250.0,"annual_generator_hours":17529.99999999637,"required_annual_hours":24.000000000228948,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/3869110b854cc08d7ffed8e368863cec06b955547b8df64e45b1de211d37fc23-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_1079_2054 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262020 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.477088 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.698646 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 14.403314 |
| Campaign total | — | — | — | — | 123.053149 | 64.841068 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,643.565 | 1,356.435 | 99.969031% | 5.000 | 5.000 | 5.000 | 0.000 | 499.697540 |
| week-2-submission-2 | 3,313,489.152 | 1,066,510.848 | 75.650437% | 120.000 | 8,760.000 | 7.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,643.565 | 1,356.435 | 99.969031% | 5.000 | 5.000 | 5.000 | 0.000 | 499.697540 |
| week-3-submission-2 | 3,313,489.152 | 1,066,510.848 | 75.650437% | 120.000 | 8,760.000 | 7.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001267 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.786199 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.563374 | 0.001267 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 2.073774 | 0.786199 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 1079: 250 MW per submission, 2054: 250 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,356.435 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 65.872547 | 434.127453 | 105.630770 | 0.000000 | 65.731155 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 65.872547 | 434.127453 | 105.630770 | 0.000000 | 65.731155 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 34, 35, 36, 37, 38, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 107, 111 | True |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **65.731155 MW**; maximum nodal residual 4.04e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8f4ed5d7d1d1637ac0c79e18f135dc82c2219cbf9b020955938ee45ebf1f4336.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 65.731155 | 58.076598 | 7.654557 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **65.731155 MW**; maximum nodal residual 4.04e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8f4ed5d7d1d1637ac0c79e18f135dc82c2219cbf9b020955938ee45ebf1f4336.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 65.731155 | 58.076598 | 7.654557 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 1,066,510.848 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112. At periods 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 (day 1, h00) | 83.770 | 69.191789 | 430.808211 | 11,890.239756 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 1 (day 1, h01) | 83.770 | 69.059148 | 430.940852 | 12,026.114790 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 2 (day 1, h02) | 83.770 | 69.191789 | 430.808211 | 11,890.239756 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 3 (day 1, h03) | 83.770 | 69.580672 | 430.419328 | 11,491.874293 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 4 (day 1, h04) | 83.770 | 70.218762 | 429.781238 | 10,858.360980 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 5 (day 1, h05) | 83.770 | 71.069721 | 428.930279 | 10,032.944224 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 6 (day 1, h06) | 83.770 | 72.060132 | 427.939868 | 9,071.720544 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 7 (day 1, h07) | 83.770 | 73.006372 | 426.993628 | 8,039.034427 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 8 (day 1, h08) | 83.770 | 75.068604 | 424.931396 | 7,017.508247 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 9 (day 1, h09) | 83.770 | 76.331928 | 423.668072 | 6,059.013689 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 10 (day 1, h10) | 83.770 | 77.221342 | 422.778658 | 5,233.981484 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 11 (day 1, h11) | 83.770 | 78.153992 | 421.846008 | 4,603.413811 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 12 (day 1, h12) | 83.770 | 79.372282 | 420.627718 | 4,213.342381 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 13 (day 1, h13) | 83.770 | 84.572199 | 415.427801 | 4,128.140098 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 14 (day 1, h14) | 83.770 | 79.372282 | 420.627718 | 4,213.342381 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 15 (day 1, h15) | 83.770 | 78.153992 | 421.846008 | 4,603.413811 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 16 (day 1, h16) | 83.770 | 77.221342 | 422.778658 | 5,233.981484 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 17 (day 1, h17) | 83.770 | 76.331928 | 423.668072 | 6,059.013689 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 18 (day 1, h18) | 83.770 | 75.068604 | 424.931396 | 7,017.508247 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 19 (day 1, h19) | 83.770 | 73.006372 | 426.993628 | 8,039.034427 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 20 (day 1, h20) | 83.770 | 72.060132 | 427.939868 | 9,071.720544 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 21 (day 1, h21) | 83.770 | 71.069721 | 428.930279 | 10,032.944224 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 22 (day 1, h22) | 83.770 | 70.218762 | 429.781238 | 10,858.360980 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 23 (day 1, h23) | 83.770 | 69.580672 | 430.419328 | 11,491.874293 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 24 (day 2, h00) | 99.726 | 65.650576 | 434.349424 | 15,029.481689 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 25 (day 2, h01) | 99.726 | 65.452767 | 434.547233 | 15,164.705046 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 26 (day 2, h02) | 99.726 | 65.650576 | 434.349424 | 15,029.481689 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 27 (day 2, h03) | 99.726 | 66.296738 | 433.703262 | 14,633.689008 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 28 (day 2, h04) | 99.726 | 66.993422 | 433.006578 | 14,000.761674 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 29 (day 2, h05) | 99.726 | 67.859900 | 432.140100 | 13,175.500070 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 30 (day 2, h06) | 99.726 | 68.868527 | 431.131473 | 12,214.458555 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 31 (day 2, h07) | 99.726 | 69.886249 | 430.113751 | 11,182.487259 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 32 (day 2, h08) | 99.726 | 70.944506 | 429.055494 | 10,150.921346 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 33 (day 2, h09) | 99.726 | 71.937785 | 428.062215 | 9,189.726321 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 34 (day 2, h10) | 99.726 | 72.712579 | 427.287421 | 8,363.547918 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 35 (day 2, h11) | 99.726 | 73.515923 | 426.484077 | 7,731.687195 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 36 (day 2, h12) | 99.726 | 74.372041 | 425.627959 | 7,337.994056 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 37 (day 2, h13) | 99.726 | 74.664046 | 425.335954 | 7,203.712637 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 38 (day 2, h14) | 99.726 | 74.372041 | 425.627959 | 7,337.994056 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 39 (day 2, h15) | 99.726 | 73.515923 | 426.484077 | 7,731.687195 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 40 (day 2, h16) | 99.726 | 72.712579 | 427.287421 | 8,363.547918 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 41 (day 2, h17) | 99.726 | 71.937785 | 428.062215 | 9,189.726321 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 42 (day 2, h18) | 99.726 | 70.944506 | 429.055494 | 10,150.921346 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 43 (day 2, h19) | 99.726 | 69.886249 | 430.113751 | 11,182.487259 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 44 (day 2, h20) | 99.726 | 68.868527 | 431.131473 | 12,214.458555 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 45 (day 2, h21) | 99.726 | 67.859900 | 432.140100 | 13,175.500070 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 46 (day 2, h22) | 99.726 | 66.993422 | 433.006578 | 14,000.761674 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 47 (day 2, h23) | 99.726 | 66.296738 | 433.703262 | 14,633.689008 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b02579:lower |
| 48 (day 3, h00) | 82.773 | 72.672468 | 427.327532 | 8,407.852723 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 49 (day 3, h01) | 82.773 | 72.549370 | 427.450630 | 8,543.823186 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 50 (day 3, h02) | 82.773 | 72.672468 | 427.327532 | 8,407.852723 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 51 (day 3, h03) | 82.773 | 73.033375 | 426.966625 | 8,009.207494 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 52 (day 3, h04) | 82.773 | 74.276893 | 425.723107 | 7,381.748482 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 53 (day 3, h05) | 82.773 | 75.734818 | 424.265182 | 6,562.401370 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 54 (day 3, h06) | 82.773 | 76.841969 | 423.158031 | 5,602.345076 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 55 (day 3, h07) | 82.773 | 78.245953 | 421.754047 | 4,574.236417 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 56 (day 3, h08) | 82.773 | 107.127230 | 392.872770 | 3,820.900681 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 57 (day 3, h09) | 82.773 | 145.566756 | 354.433244 | 3,234.168145 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 180.685006 | 319.314994 | 2,751.424312 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 207.399242 | 292.600758 | 2,378.672472 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 224.217739 | 275.782261 | 2,144.603140 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 229.954216 | 270.045784 | 2,064.766451 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 224.217739 | 275.782261 | 2,144.603140 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 207.399242 | 292.600758 | 2,378.672472 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 180.685006 | 319.314994 | 2,751.424312 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 145.566756 | 354.433244 | 3,234.168145 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 66 (day 3, h18) | 82.773 | 107.127230 | 392.872770 | 3,820.900681 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 67 (day 3, h19) | 82.773 | 78.245953 | 421.754047 | 4,574.236417 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 68 (day 3, h20) | 82.773 | 76.841969 | 423.158031 | 5,602.345076 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 69 (day 3, h21) | 82.773 | 75.734818 | 424.265182 | 6,562.401370 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 70 (day 3, h22) | 82.773 | 74.276893 | 425.723107 | 7,381.748482 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 71 (day 3, h23) | 82.773 | 73.033375 | 426.966625 | 8,009.207494 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 72 (day 4, h00) | 97.732 | 77.181709 | 422.818291 | 5,278.578727 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 73 (day 4, h01) | 97.732 | 77.049392 | 422.950608 | 5,414.457010 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 74 (day 4, h02) | 97.732 | 77.181709 | 422.818291 | 5,278.578727 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 75 (day 4, h03) | 97.732 | 77.536037 | 422.463963 | 4,879.867704 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 76 (day 4, h04) | 97.732 | 79.245597 | 420.754403 | 4,257.069102 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 77 (day 4, h05) | 97.732 | 112.089395 | 387.910605 | 3,751.580739 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 150.528920 | 349.471080 | 3,164.848175 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 194.334060 | 305.665940 | 2,560.751096 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 237.868928 | 262.131072 | 1,953.951247 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 283.820632 | 216.179368 | 1,442.340509 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 82 (day 4, h10) | 97.732 | 333.829255 | 166.170745 | 1,108.500409 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 83 (day 4, h11) | 97.732 | 373.210219 | 126.789781 | 862.415839 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 397.590697 | 102.409303 | 703.966295 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 405.970614 | 94.029386 | 650.564030 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 397.590697 | 102.409303 | 703.966295 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 373.210219 | 126.789781 | 862.415839 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 333.829255 | 166.170745 | 1,108.500409 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 89 (day 4, h17) | 97.732 | 283.820632 | 216.179368 | 1,442.340509 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 90 (day 4, h18) | 97.732 | 237.868928 | 262.131072 | 1,953.951247 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 194.334060 | 305.665940 | 2,560.751096 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 150.528920 | 349.471080 | 3,164.848175 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 93 (day 4, h21) | 97.732 | 112.089395 | 387.910605 | 3,751.580739 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 94 (day 4, h22) | 97.732 | 79.245597 | 420.754403 | 4,257.069102 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 95 (day 4, h23) | 97.732 | 77.536037 | 422.463963 | 4,879.867704 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 96 (day 5, h00) | 1.000 | 121.037380 | 378.962620 | 3,626.580033 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 97 (day 5, h01) | 1.000 | 115.313428 | 384.686572 | 3,706.541939 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 98 (day 5, h02) | 1.000 | 121.037380 | 378.962620 | 3,626.580033 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 137.819162 | 362.180838 | 3,392.143531 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 162.470331 | 337.529669 | 2,998.761014 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 197.558093 | 302.441907 | 2,515.712297 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 238.123522 | 261.876478 | 1,950.238787 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 288.454881 | 211.545119 | 1,411.403868 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 104 (day 5, h08) | 1.000 | 350.950107 | 149.049893 | 994.207610 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 105 (day 5, h09) | 1.000 | 410.703233 | 89.296767 | 620.611092 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 463.727282 | 36.272718 | 316.925239 | 0.000000 | 141.998811 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 105.630770 | 394.369230 | 500.000000 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 105.630770 | 394.369230 | 500.000000 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 463.727282 | 36.272718 | 316.925239 | 0.000000 | 141.998811 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 410.703233 | 89.296767 | 620.611092 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 350.950107 | 149.049893 | 994.207610 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 115 (day 5, h19) | 1.000 | 288.454881 | 211.545119 | 1,411.403868 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 116 (day 5, h20) | 1.000 | 238.123522 | 261.876478 | 1,950.238787 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 197.558093 | 302.441907 | 2,515.712297 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 162.470331 | 337.529669 | 2,998.761014 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 137.819162 | 362.180838 | 3,392.143531 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | 81, 82, 88, 89, 103, 104, 114, 115 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 0: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9614aa7346b3b182abc9935cd928c83c02b44b77a8a24afbaaa0e338dc702506.json>).
- Period 1: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3b52094f0976bcafdf67ae7070fcf221d82ed4c6de0ba420562be1b61c2f8680.json>).
- Period 2: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9614aa7346b3b182abc9935cd928c83c02b44b77a8a24afbaaa0e338dc702506.json>).
- Period 3: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5341b883612ea6721fe1243d04eff8de70f08f0ac771a7e19dcdbed2b2fa5f1c.json>).
- Period 4: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9ac0b1c4a81fd49e6d743c036640ab8ab9a84f42d11ffa9e5ec50b5136457512.json>).
- Period 5: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.66e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d86d17e044a4cd117cf12da915858d10c68f1bd34ee4e965b5efd098a5e351c0.json>).
- Period 6: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.81e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b98944075fca6120362b32576e1a46b0a82ec1c7b5702bb1de2a2260f20d81fc.json>).
- Period 7: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.37e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4aeec020fe478f137a0b3505b676accc548cc34b1f8f6a138169e2abc465963c.json>).
- Period 8: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae35a5bb3d7cc183bd2134d588611c8381217b2f6706ab9458b6a683ed51aaf5.json>).
- Period 9: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96e6a4f85e43d1ba48ddfd10545c652d88a339fcc892651a97251d032eca868d.json>).
- Period 10: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.2e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/578e4fae7005e36e404db23019ae7377b15da0abd6ffbeeb495a37b7f112a3ff.json>).
- Period 11: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b9d251c3f94d90d97b3f09c1f4e745af513d4e45f372f41a63463d52cf321f6.json>).
- Period 12: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78bcd4dcbba0bfd28e6f1e04a8d64fdbf2068c976d4b366b83ca077a1877c6ca.json>).
- Period 13: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/93aec3178f5de342e5828f3a3d36d0c0cc63703f75f6db23a9cb2f39edf2d69d.json>).
- Period 14: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78bcd4dcbba0bfd28e6f1e04a8d64fdbf2068c976d4b366b83ca077a1877c6ca.json>).
- Period 15: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b9d251c3f94d90d97b3f09c1f4e745af513d4e45f372f41a63463d52cf321f6.json>).
- Period 16: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.2e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/578e4fae7005e36e404db23019ae7377b15da0abd6ffbeeb495a37b7f112a3ff.json>).
- Period 17: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96e6a4f85e43d1ba48ddfd10545c652d88a339fcc892651a97251d032eca868d.json>).
- Period 18: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae35a5bb3d7cc183bd2134d588611c8381217b2f6706ab9458b6a683ed51aaf5.json>).
- Period 19: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.37e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4aeec020fe478f137a0b3505b676accc548cc34b1f8f6a138169e2abc465963c.json>).
- Period 20: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.81e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b98944075fca6120362b32576e1a46b0a82ec1c7b5702bb1de2a2260f20d81fc.json>).
- Period 21: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.66e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d86d17e044a4cd117cf12da915858d10c68f1bd34ee4e965b5efd098a5e351c0.json>).
- Period 22: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9ac0b1c4a81fd49e6d743c036640ab8ab9a84f42d11ffa9e5ec50b5136457512.json>).
- Period 23: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5341b883612ea6721fe1243d04eff8de70f08f0ac771a7e19dcdbed2b2fa5f1c.json>).
- Period 24: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2ae2d503d5302ac0a5a54a58fefb23a6a2c81d44fca88be601fd75127892fe80.json>).
- Period 25: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b7765c5981c62014b37e10f8686272ba233ac5c4e64fb4a5ec1f5d2a48da6d37.json>).
- Period 26: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2ae2d503d5302ac0a5a54a58fefb23a6a2c81d44fca88be601fd75127892fe80.json>).
- Period 27: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6f52490925e111e7b3e787a51fc7f26494d95bd39d8b26745372b55b996ea648.json>).
- Period 28: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a25fa5548ea35d70906806375d784bc57b22f0c845cbfe28a03874ed188ebd2.json>).
- Period 29: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.8e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d9b084e870ae6ddb15d799a6daa5480b44dcbc7141c69223529fac3c04289b9c.json>).
- Period 30: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60c6bbcb91794378ba436b794a587263b20f94e67dc81dd84de3012c722b5e8d.json>).
- Period 31: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.48e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/530b6db4081f893a6979ab66ba724a547498bedddae1ab72cc9c10163d8d35d8.json>).
- Period 32: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.67e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6356df7f47b945e46d302fd692b5ea5541118a41094dbb2251aeb8ac3fa20aa.json>).
- Period 33: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/11143b304488df34385f4ed576819b84c6f95703f1ff95a5413d34c4292bae89.json>).
- Period 34: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/428cf374bb0b9362b02c54359e9955f9c21844a87bfb274d8d935173ed95c592.json>).
- Period 35: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e05bf46958464426c3b133782221a35f68b2d6c5b7f4a5b5f78c0c89ea6a2545.json>).
- Period 36: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a346d0e75748ce92ce3f8a65da777a0ee9aef96d3d50fb12faf5f491e706419d.json>).
- Period 37: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.68e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6225e93e3c7de33332124fea529c9fe55070b5c231c90b4eca39ec60224c6c90.json>).
- Period 38: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a346d0e75748ce92ce3f8a65da777a0ee9aef96d3d50fb12faf5f491e706419d.json>).
- Period 39: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e05bf46958464426c3b133782221a35f68b2d6c5b7f4a5b5f78c0c89ea6a2545.json>).
- Period 40: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/428cf374bb0b9362b02c54359e9955f9c21844a87bfb274d8d935173ed95c592.json>).
- Period 41: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/11143b304488df34385f4ed576819b84c6f95703f1ff95a5413d34c4292bae89.json>).
- Period 42: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.67e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6356df7f47b945e46d302fd692b5ea5541118a41094dbb2251aeb8ac3fa20aa.json>).
- Period 43: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.48e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/530b6db4081f893a6979ab66ba724a547498bedddae1ab72cc9c10163d8d35d8.json>).
- Period 44: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60c6bbcb91794378ba436b794a587263b20f94e67dc81dd84de3012c722b5e8d.json>).
- Period 45: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.8e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d9b084e870ae6ddb15d799a6daa5480b44dcbc7141c69223529fac3c04289b9c.json>).
- Period 46: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a25fa5548ea35d70906806375d784bc57b22f0c845cbfe28a03874ed188ebd2.json>).
- Period 47: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6f52490925e111e7b3e787a51fc7f26494d95bd39d8b26745372b55b996ea648.json>).
- Period 48: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c16781473398ae7d034db5f0a5f0aa5b1944d499f3195bdb37ddaeaf5f9a5c7.json>).
- Period 49: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.95e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d71fba94865a907b4f9bc72d9a775e3c9c2fd8d652dc89e398766c87de21fed7.json>).
- Period 50: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c16781473398ae7d034db5f0a5f0aa5b1944d499f3195bdb37ddaeaf5f9a5c7.json>).
- Period 51: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.42e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aafcd65187eb50bedb0167b88f0c050ce78ba6bd87ae9002d8edd37e3329954a.json>).
- Period 52: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7e25ed796a7aba0849223ef833bb1f22070e26a5cb0afdd23490501d3abc1ab7.json>).
- Period 53: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dc7fd69bf5eec86030ff8eac8d9b5c9e04df3a61f312ddda75a6f085289a3ffc.json>).
- Period 54: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c9ab768c38904643668f5be80d363a1cb65ec667873660d7cc56e0680024ed0.json>).
- Period 55: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c74f5350e6c257925cf08634a119b7f815261d86d75d7f3945f8a1846af1047d.json>).
- Period 56: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/93cc0417ff906782fcb41380e14dd8cd16ef1c4489005e9daa0f7bad9a9e5242.json>).
- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f8989dbbfef34d7f890340c462c3956f11e59f09451994481d4f3be658e72ef.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db4fd33c70a08156271504a8d90d111bc51585ceb9fc587b11c96281988e9775.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/927dd9967ca3a69daade975fabcc6ea9eed1f3743c2263843fc14f3d996746d3.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c5fee851fa3f2c72899dcc99633fe770840100077c4a758785b2ec9f677ae572.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ac58a05e0393346adc3e9330ab658dd181fddad10d504419a960ae64215f2c70.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c5fee851fa3f2c72899dcc99633fe770840100077c4a758785b2ec9f677ae572.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/927dd9967ca3a69daade975fabcc6ea9eed1f3743c2263843fc14f3d996746d3.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db4fd33c70a08156271504a8d90d111bc51585ceb9fc587b11c96281988e9775.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f8989dbbfef34d7f890340c462c3956f11e59f09451994481d4f3be658e72ef.json>).
- Period 66: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/93cc0417ff906782fcb41380e14dd8cd16ef1c4489005e9daa0f7bad9a9e5242.json>).
- Period 67: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c74f5350e6c257925cf08634a119b7f815261d86d75d7f3945f8a1846af1047d.json>).
- Period 68: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c9ab768c38904643668f5be80d363a1cb65ec667873660d7cc56e0680024ed0.json>).
- Period 69: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dc7fd69bf5eec86030ff8eac8d9b5c9e04df3a61f312ddda75a6f085289a3ffc.json>).
- Period 70: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7e25ed796a7aba0849223ef833bb1f22070e26a5cb0afdd23490501d3abc1ab7.json>).
- Period 71: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.42e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aafcd65187eb50bedb0167b88f0c050ce78ba6bd87ae9002d8edd37e3329954a.json>).
- Period 72: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.99e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc618b8049d64d511a8e0c1fcbaab9509e14a375708442d873106fa11f30162d.json>).
- Period 73: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ed7708676a7b1a0c47ab1f870f4ab05ed38ca3c01e07e2e91bdbcba286f25e11.json>).
- Period 74: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.99e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc618b8049d64d511a8e0c1fcbaab9509e14a375708442d873106fa11f30162d.json>).
- Period 75: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/14875dc273bfb5a2fdc5bce4549e0522c580d30ced7d7540dbd94235bdd30709.json>).
- Period 76: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.83e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d039ca8950368cc5a7be3c0af01806d775b8c855dc1d14231b9b0cd89601fd7.json>).
- Period 77: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f31cfc6ce8c053dda11b57e592df204256fb0e082dfa34fd20bd9ebe7b878857.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.56e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4cfc9b3c2481aea23cb15bce6094b5bfa189cf14f93f99e575827db79cc6be1.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a0a246068103aa6a9ccb4716eaff37f3914689812ef8ca85cac8f9c7f81078d.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d35d65a90002bdcec9fcbab6811c495294513c4cdffb62edf03aef8d754eb12.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/19995c190e30e91a23d5377b4de34cf8eba88ce785ce8c6e3e9288d9f102ecf0.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d187e193b765897de668018064b063470aa3a57f0b13ee6cca4e6691e2530fd.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/044ed65efb27505851249e3d63329f1dcfc4d89b16118b62d7e74019a9e6921a.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/13b61c48ae7f5e9fc7fbdfab3e8cb0ed9b7725760c5e9ad5e52d18600381fac8.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.09e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ed781a16cc2d6566850c9ce52b158ea3a4a1dce65727d99657dfef0c04370122.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/13b61c48ae7f5e9fc7fbdfab3e8cb0ed9b7725760c5e9ad5e52d18600381fac8.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/044ed65efb27505851249e3d63329f1dcfc4d89b16118b62d7e74019a9e6921a.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d187e193b765897de668018064b063470aa3a57f0b13ee6cca4e6691e2530fd.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/19995c190e30e91a23d5377b4de34cf8eba88ce785ce8c6e3e9288d9f102ecf0.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d35d65a90002bdcec9fcbab6811c495294513c4cdffb62edf03aef8d754eb12.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a0a246068103aa6a9ccb4716eaff37f3914689812ef8ca85cac8f9c7f81078d.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.56e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4cfc9b3c2481aea23cb15bce6094b5bfa189cf14f93f99e575827db79cc6be1.json>).
- Period 93: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f31cfc6ce8c053dda11b57e592df204256fb0e082dfa34fd20bd9ebe7b878857.json>).
- Period 94: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.83e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d039ca8950368cc5a7be3c0af01806d775b8c855dc1d14231b9b0cd89601fd7.json>).
- Period 95: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/14875dc273bfb5a2fdc5bce4549e0522c580d30ced7d7540dbd94235bdd30709.json>).
- Period 96: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5a8a35d38be0c3ffaa167e7265744d58b1252d9a05d33325404f7b1fbbf3555d.json>).
- Period 97: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8785fd54f049f65761b4e3392b057a04ff355fdc9b8085387dbac21a70b8fef5.json>).
- Period 98: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5a8a35d38be0c3ffaa167e7265744d58b1252d9a05d33325404f7b1fbbf3555d.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.49e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b087198d40c7f023219224d7a34e5e0b142a8eafcd78ec1a605aa81a5e3766b5.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8dc6cdf473d58926116262f66a09cbcce585175617b0aaf5a1e1d801eeaa5a79.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dea11f05a687ae39877d7591f00f71ac450bdf7cbd8fd0770e298a85ece9fd81.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d48f158486c5010d18172f7296bc1b552fc5a1b71c6f8eb6f70abb9bf48b6ebb.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/285a5cd2c6ea3f7f2697fd5d1436ff5a621afa03da817a68d71d9acf68be9da5.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/106239fe7e75f26d913483458861df1665bb5461d16b8fdec4eecd39e5f3a7d9.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7ecfd2028cc70fca66251d8b49b16b1ee853196c32b04879c74a7e7361023d19.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **141.998811 MW**; maximum nodal residual 3.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/25679ddfde8d02281d5576cb88a57cb5b5b0d85b71dc0d856daf2193397ed166.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 141.998811 | 134.344253 | 7.654557 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.11e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/016663dfb12b74c3a176d1aabbaed65cbc33c9b14ceba8f1e21e8c7ffd4dfa8f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 500.000000 | 492.010489 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.11e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/016663dfb12b74c3a176d1aabbaed65cbc33c9b14ceba8f1e21e8c7ffd4dfa8f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 500.000000 | 492.010489 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **141.998811 MW**; maximum nodal residual 3.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/25679ddfde8d02281d5576cb88a57cb5b5b0d85b71dc0d856daf2193397ed166.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 141.998811 | 134.344253 | 7.654557 | True |

- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7ecfd2028cc70fca66251d8b49b16b1ee853196c32b04879c74a7e7361023d19.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/106239fe7e75f26d913483458861df1665bb5461d16b8fdec4eecd39e5f3a7d9.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/285a5cd2c6ea3f7f2697fd5d1436ff5a621afa03da817a68d71d9acf68be9da5.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d48f158486c5010d18172f7296bc1b552fc5a1b71c6f8eb6f70abb9bf48b6ebb.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dea11f05a687ae39877d7591f00f71ac450bdf7cbd8fd0770e298a85ece9fd81.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8dc6cdf473d58926116262f66a09cbcce585175617b0aaf5a1e1d801eeaa5a79.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.49e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b087198d40c7f023219224d7a34e5e0b142a8eafcd78ec1a605aa81a5e3766b5.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,356.435 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 2,130.313646 | 0.000000 | 0.000000 | 6.811680 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.857892 | 0.000000 | 0.000000 | 7.021922 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 0.000000 | 500.000000 | 2,130.313646 | 0.000000 | 0.000000 | 6.811680 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 65.872547 | 434.127453 | 105.630770 | 0.000000 | 65.731155 | 0.247541 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000531 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 111 (day 5, h15) | 1.000 | 65.872547 | 434.127453 | 105.630770 | 0.000000 | 65.731155 | 0.247541 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 34, 35, 36, 37, 38, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 107, 111 | True |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **65.731155 MW**; maximum nodal residual 4.04e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8f4ed5d7d1d1637ac0c79e18f135dc82c2219cbf9b020955938ee45ebf1f4336.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 65.731155 | 58.076598 | 7.654557 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **65.731155 MW**; maximum nodal residual 4.04e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8f4ed5d7d1d1637ac0c79e18f135dc82c2219cbf9b020955938ee45ebf1f4336.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 65.731155 | 58.076598 | 7.654557 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 1,066,510.848 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112. At periods 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 (day 1, h00) | 83.770 | 69.191789 | 430.808211 | 11,890.239756 | 0.000000 | 0.000000 | 18.599894 | b00220:lower, b01347:lower, b02579:lower |
| 1 (day 1, h01) | 83.770 | 69.059148 | 430.940852 | 12,026.114790 | 0.000000 | 0.000000 | 18.611600 | b00220:lower, b01347:lower, b02579:lower |
| 2 (day 1, h02) | 83.770 | 69.191789 | 430.808211 | 11,890.239756 | 0.000000 | 0.000000 | 18.599894 | b00220:lower, b01347:lower, b02579:lower |
| 3 (day 1, h03) | 83.770 | 69.580672 | 430.419328 | 11,491.874293 | 0.000000 | 0.000000 | 18.565573 | b00220:lower, b01347:lower, b02579:lower |
| 4 (day 1, h04) | 83.770 | 70.218762 | 429.781238 | 10,858.360980 | 0.000000 | 0.000000 | 18.510576 | b00220:lower, b01347:lower, b02579:lower |
| 5 (day 1, h05) | 83.770 | 71.069721 | 428.930279 | 10,032.944224 | 0.000000 | 0.000000 | 18.437121 | b00220:lower, b01347:lower, b02579:lower |
| 6 (day 1, h06) | 83.770 | 72.060132 | 427.939868 | 9,071.720544 | 0.000000 | 0.000000 | 18.402993 | b00220:lower, b01347:lower, b02579:lower |
| 7 (day 1, h07) | 83.770 | 73.006372 | 426.993628 | 8,039.034427 | 0.000000 | 0.000000 | 18.327150 | b00220:lower, b01347:lower, b02579:lower |
| 8 (day 1, h08) | 83.770 | 75.068604 | 424.931396 | 7,017.508247 | 0.000000 | 0.000000 | 18.256179 | b00220:lower, b01347:lower, b02579:lower |
| 9 (day 1, h09) | 83.770 | 76.331928 | 423.668072 | 6,059.013689 | 0.000000 | 0.000000 | 18.146799 | b00220:lower, b01347:lower, b02579:lower |
| 10 (day 1, h10) | 83.770 | 77.221342 | 422.778658 | 5,233.981484 | 0.000000 | 0.000000 | 18.220406 | b00220:lower, b01347:lower, b02579:lower |
| 11 (day 1, h11) | 83.770 | 78.153992 | 421.846008 | 4,603.413811 | 0.000000 | 0.000000 | 18.572777 | b00220:lower, b01347:lower, b02579:lower |
| 12 (day 1, h12) | 83.770 | 79.372282 | 420.627718 | 4,213.342381 | 0.000000 | 0.000000 | 23.334500 | b00220:lower, b01347:lower, b02579:lower |
| 13 (day 1, h13) | 83.770 | 84.572199 | 415.427801 | 4,128.140098 | 0.000000 | 0.000000 | 26.573878 | b00220:lower, b01347:lower, b02579:lower |
| 14 (day 1, h14) | 83.770 | 79.372282 | 420.627718 | 4,213.342381 | 0.000000 | 0.000000 | 23.334500 | b00220:lower, b01347:lower, b02579:lower |
| 15 (day 1, h15) | 83.770 | 78.153992 | 421.846008 | 4,603.413811 | 0.000000 | 0.000000 | 18.572777 | b00220:lower, b01347:lower, b02579:lower |
| 16 (day 1, h16) | 83.770 | 77.221342 | 422.778658 | 5,233.981484 | 0.000000 | 0.000000 | 18.220406 | b00220:lower, b01347:lower, b02579:lower |
| 17 (day 1, h17) | 83.770 | 76.331928 | 423.668072 | 6,059.013689 | 0.000000 | 0.000000 | 18.146799 | b00220:lower, b01347:lower, b02579:lower |
| 18 (day 1, h18) | 83.770 | 75.068604 | 424.931396 | 7,017.508247 | 0.000000 | 0.000000 | 18.256179 | b00220:lower, b01347:lower, b02579:lower |
| 19 (day 1, h19) | 83.770 | 73.006372 | 426.993628 | 8,039.034427 | 0.000000 | 0.000000 | 18.327150 | b00220:lower, b01347:lower, b02579:lower |
| 20 (day 1, h20) | 83.770 | 72.060132 | 427.939868 | 9,071.720544 | 0.000000 | 0.000000 | 18.402993 | b00220:lower, b01347:lower, b02579:lower |
| 21 (day 1, h21) | 83.770 | 71.069721 | 428.930279 | 10,032.944224 | 0.000000 | 0.000000 | 18.437121 | b00220:lower, b01347:lower, b02579:lower |
| 22 (day 1, h22) | 83.770 | 70.218762 | 429.781238 | 10,858.360980 | 0.000000 | 0.000000 | 18.510576 | b00220:lower, b01347:lower, b02579:lower |
| 23 (day 1, h23) | 83.770 | 69.580672 | 430.419328 | 11,491.874293 | 0.000000 | 0.000000 | 18.565573 | b00220:lower, b01347:lower, b02579:lower |
| 24 (day 2, h00) | 99.726 | 65.650576 | 434.349424 | 15,029.481689 | 0.000000 | 0.000000 | 22.433363 | b00220:lower, b02579:lower |
| 25 (day 2, h01) | 99.726 | 65.452767 | 434.547233 | 15,164.705046 | 0.000000 | 0.000000 | 22.454146 | b00220:lower, b02579:lower |
| 26 (day 2, h02) | 99.726 | 65.650576 | 434.349424 | 15,029.481689 | 0.000000 | 0.000000 | 22.433363 | b00220:lower, b02579:lower |
| 27 (day 2, h03) | 99.726 | 66.296738 | 433.703262 | 14,633.689008 | 0.000000 | 0.000000 | 22.368304 | b00220:lower, b02579:lower |
| 28 (day 2, h04) | 99.726 | 66.993422 | 433.006578 | 14,000.761674 | 0.000000 | 0.000000 | 22.298489 | b00220:lower, b02579:lower |
| 29 (day 2, h05) | 99.726 | 67.859900 | 432.140100 | 13,175.500070 | 0.000000 | 0.000000 | 22.230758 | b00220:lower, b02579:lower |
| 30 (day 2, h06) | 99.726 | 68.868527 | 431.131473 | 12,214.458555 | 0.000000 | 0.000000 | 22.133899 | b00220:lower, b01347:lower, b02579:lower |
| 31 (day 2, h07) | 99.726 | 69.886249 | 430.113751 | 11,182.487259 | 0.000000 | 0.000000 | 22.071335 | b00220:lower, b01347:lower, b02579:lower |
| 32 (day 2, h08) | 99.726 | 70.944506 | 429.055494 | 10,150.921346 | 0.000000 | 0.000000 | 21.960149 | b00220:lower, b01347:lower, b02579:lower |
| 33 (day 2, h09) | 99.726 | 71.937785 | 428.062215 | 9,189.726321 | 0.000000 | 0.000000 | 21.921179 | b00220:lower, b01347:lower, b02579:lower |
| 34 (day 2, h10) | 99.726 | 72.712579 | 427.287421 | 8,363.547918 | 0.000000 | 0.000000 | 21.848903 | b00220:lower, b01347:lower, b02579:lower |
| 35 (day 2, h11) | 99.726 | 73.515923 | 426.484077 | 7,731.687195 | 0.000000 | 0.000000 | 21.900658 | b00220:lower, b01347:lower, b02579:lower |
| 36 (day 2, h12) | 99.726 | 74.372041 | 425.627959 | 7,337.994056 | 0.000000 | 0.000000 | 21.813359 | b00220:lower, b01347:lower, b02579:lower |
| 37 (day 2, h13) | 99.726 | 74.664046 | 425.335954 | 7,203.712637 | 0.000000 | 0.000000 | 21.782680 | b00220:lower, b01347:lower, b02579:lower |
| 38 (day 2, h14) | 99.726 | 74.372041 | 425.627959 | 7,337.994056 | 0.000000 | 0.000000 | 21.813359 | b00220:lower, b01347:lower, b02579:lower |
| 39 (day 2, h15) | 99.726 | 73.515923 | 426.484077 | 7,731.687195 | 0.000000 | 0.000000 | 21.900658 | b00220:lower, b01347:lower, b02579:lower |
| 40 (day 2, h16) | 99.726 | 72.712579 | 427.287421 | 8,363.547918 | 0.000000 | 0.000000 | 21.848903 | b00220:lower, b01347:lower, b02579:lower |
| 41 (day 2, h17) | 99.726 | 71.937785 | 428.062215 | 9,189.726321 | 0.000000 | 0.000000 | 21.921179 | b00220:lower, b01347:lower, b02579:lower |
| 42 (day 2, h18) | 99.726 | 70.944506 | 429.055494 | 10,150.921346 | 0.000000 | 0.000000 | 21.960149 | b00220:lower, b01347:lower, b02579:lower |
| 43 (day 2, h19) | 99.726 | 69.886249 | 430.113751 | 11,182.487259 | 0.000000 | 0.000000 | 22.071335 | b00220:lower, b01347:lower, b02579:lower |
| 44 (day 2, h20) | 99.726 | 68.868527 | 431.131473 | 12,214.458555 | 0.000000 | 0.000000 | 22.133899 | b00220:lower, b01347:lower, b02579:lower |
| 45 (day 2, h21) | 99.726 | 67.859900 | 432.140100 | 13,175.500070 | 0.000000 | 0.000000 | 22.230758 | b00220:lower, b02579:lower |
| 46 (day 2, h22) | 99.726 | 66.993422 | 433.006578 | 14,000.761674 | 0.000000 | 0.000000 | 22.298489 | b00220:lower, b02579:lower |
| 47 (day 2, h23) | 99.726 | 66.296738 | 433.703262 | 14,633.689008 | 0.000000 | 0.000000 | 22.368304 | b00220:lower, b02579:lower |
| 48 (day 3, h00) | 82.773 | 72.672468 | 427.327532 | 8,407.852723 | 0.000000 | 0.000000 | 18.138087 | b00220:lower, b01347:lower, b02579:lower |
| 49 (day 3, h01) | 82.773 | 72.549370 | 427.450630 | 8,543.823186 | 0.000000 | 0.000000 | 18.148822 | b00220:lower, b01347:lower, b02579:lower |
| 50 (day 3, h02) | 82.773 | 72.672468 | 427.327532 | 8,407.852723 | 0.000000 | 0.000000 | 18.138087 | b00220:lower, b01347:lower, b02579:lower |
| 51 (day 3, h03) | 82.773 | 73.033375 | 426.966625 | 8,009.207494 | 0.000000 | 0.000000 | 18.106614 | b00220:lower, b01347:lower, b02579:lower |
| 52 (day 3, h04) | 82.773 | 74.276893 | 425.723107 | 7,381.748482 | 0.000000 | 0.000000 | 18.113386 | b00220:lower, b01347:lower, b02579:lower |
| 53 (day 3, h05) | 82.773 | 75.734818 | 424.265182 | 6,562.401370 | 0.000000 | 0.000000 | 17.986325 | b00220:lower, b01347:lower, b02579:lower |
| 54 (day 3, h06) | 82.773 | 76.841969 | 423.158031 | 5,602.345076 | 0.000000 | 0.000000 | 17.927350 | b00220:lower, b01347:lower, b02579:lower |
| 55 (day 3, h07) | 82.773 | 78.245953 | 421.754047 | 4,574.236417 | 0.000000 | 0.000000 | 18.343653 | b00220:lower, b01347:lower, b02579:lower |
| 56 (day 3, h08) | 82.773 | 107.127230 | 392.872770 | 3,820.900681 | 0.000000 | 0.000000 | 25.179821 | b00220:lower, b01347:lower, b02579:lower |
| 57 (day 3, h09) | 82.773 | 145.566756 | 354.433244 | 3,234.168145 | 0.000000 | 0.000000 | 30.908003 | b00220:lower, b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 180.685006 | 319.314994 | 2,751.424312 | 0.000000 | 0.000000 | 27.845551 | b00220:lower, b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 207.399242 | 292.600758 | 2,378.672472 | 0.000000 | 0.000000 | 25.515962 | b00220:lower, b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 224.217739 | 275.782261 | 2,144.603140 | 0.000000 | 0.000000 | 24.049321 | b00220:lower, b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 229.954216 | 270.045784 | 2,064.766451 | 0.000000 | 0.000000 | 23.549078 | b00220:lower, b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 224.217739 | 275.782261 | 2,144.603140 | 0.000000 | 0.000000 | 24.049321 | b00220:lower, b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 207.399242 | 292.600758 | 2,378.672472 | 0.000000 | 0.000000 | 25.515962 | b00220:lower, b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 180.685006 | 319.314994 | 2,751.424312 | 0.000000 | 0.000000 | 27.845551 | b00220:lower, b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 145.566756 | 354.433244 | 3,234.168145 | 0.000000 | 0.000000 | 30.908003 | b00220:lower, b01347:lower, b02579:lower |
| 66 (day 3, h18) | 82.773 | 107.127230 | 392.872770 | 3,820.900681 | 0.000000 | 0.000000 | 25.179821 | b00220:lower, b01347:lower, b02579:lower |
| 67 (day 3, h19) | 82.773 | 78.245953 | 421.754047 | 4,574.236417 | 0.000000 | 0.000000 | 18.343653 | b00220:lower, b01347:lower, b02579:lower |
| 68 (day 3, h20) | 82.773 | 76.841969 | 423.158031 | 5,602.345076 | 0.000000 | 0.000000 | 17.927350 | b00220:lower, b01347:lower, b02579:lower |
| 69 (day 3, h21) | 82.773 | 75.734818 | 424.265182 | 6,562.401370 | 0.000000 | 0.000000 | 17.986325 | b00220:lower, b01347:lower, b02579:lower |
| 70 (day 3, h22) | 82.773 | 74.276893 | 425.723107 | 7,381.748482 | 0.000000 | 0.000000 | 18.113386 | b00220:lower, b01347:lower, b02579:lower |
| 71 (day 3, h23) | 82.773 | 73.033375 | 426.966625 | 8,009.207494 | 0.000000 | 0.000000 | 18.106614 | b00220:lower, b01347:lower, b02579:lower |
| 72 (day 4, h00) | 97.732 | 77.181709 | 422.818291 | 5,278.578727 | 0.000000 | 0.000000 | 21.261221 | b00220:lower, b01347:lower, b02579:lower |
| 73 (day 4, h01) | 97.732 | 77.049392 | 422.950608 | 5,414.457010 | 0.000000 | 0.000000 | 21.145876 | b00220:lower, b01347:lower, b02579:lower |
| 74 (day 4, h02) | 97.732 | 77.181709 | 422.818291 | 5,278.578727 | 0.000000 | 0.000000 | 21.261221 | b00220:lower, b01347:lower, b02579:lower |
| 75 (day 4, h03) | 97.732 | 77.536037 | 422.463963 | 4,879.867704 | 0.000000 | 0.000000 | 21.224738 | b00220:lower, b01347:lower, b02579:lower |
| 76 (day 4, h04) | 97.732 | 79.245597 | 420.754403 | 4,257.069102 | 0.000000 | 0.000000 | 21.555844 | b00220:lower, b01347:lower, b02579:lower |
| 77 (day 4, h05) | 97.732 | 112.089395 | 387.910605 | 3,751.580739 | 0.000000 | 0.000000 | 29.450364 | b00220:lower, b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 150.528920 | 349.471080 | 3,164.848175 | 0.000000 | 0.000000 | 35.982864 | b00220:lower, b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 194.334060 | 305.665940 | 2,560.751096 | 0.000000 | 0.000000 | 31.472521 | b00220:lower, b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 237.868928 | 262.131072 | 1,953.951247 | 0.000000 | 0.000000 | 26.990006 | b00220:lower, b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 283.820632 | 216.179368 | 1,442.340509 | 0.000000 | 0.000000 | 22.465848 | b01983:upper, b02579:lower |
| 82 (day 4, h10) | 97.732 | 333.829255 | 166.170745 | 1,108.500409 | 0.000000 | 0.000000 | 17.316771 | b01983:upper, b02579:lower |
| 83 (day 4, h11) | 97.732 | 373.210219 | 126.789781 | 862.415839 | 0.000000 | 0.000000 | 13.327592 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 397.590697 | 102.409303 | 703.966295 | 0.000000 | 0.000000 | 17.116162 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 405.970614 | 94.029386 | 650.564030 | 0.000000 | 0.000000 | 15.678115 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 397.590697 | 102.409303 | 703.966295 | 0.000000 | 0.000000 | 17.116162 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 373.210219 | 126.789781 | 862.415839 | 0.000000 | 0.000000 | 13.327592 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 333.829255 | 166.170745 | 1,108.500409 | 0.000000 | 0.000000 | 17.316771 | b01983:upper, b02579:lower |
| 89 (day 4, h17) | 97.732 | 283.820632 | 216.179368 | 1,442.340509 | 0.000000 | 0.000000 | 22.465848 | b01983:upper, b02579:lower |
| 90 (day 4, h18) | 97.732 | 237.868928 | 262.131072 | 1,953.951247 | 0.000000 | 0.000000 | 26.990006 | b00220:lower, b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 194.334060 | 305.665940 | 2,560.751096 | 0.000000 | 0.000000 | 31.472521 | b00220:lower, b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 150.528920 | 349.471080 | 3,164.848175 | 0.000000 | 0.000000 | 35.982864 | b00220:lower, b01347:lower, b02579:lower |
| 93 (day 4, h21) | 97.732 | 112.089395 | 387.910605 | 3,751.580739 | 0.000000 | 0.000000 | 29.450364 | b00220:lower, b01347:lower, b02579:lower |
| 94 (day 4, h22) | 97.732 | 79.245597 | 420.754403 | 4,257.069102 | 0.000000 | 0.000000 | 21.555844 | b00220:lower, b01347:lower, b02579:lower |
| 95 (day 4, h23) | 97.732 | 77.536037 | 422.463963 | 4,879.867704 | 0.000000 | 0.000000 | 21.224738 | b00220:lower, b01347:lower, b02579:lower |
| 96 (day 5, h00) | 1.000 | 121.037380 | 378.962620 | 3,626.580033 | 0.000000 | 0.000000 | 0.296173 | b00220:lower, b01347:lower, b02579:lower |
| 97 (day 5, h01) | 1.000 | 115.313428 | 384.686572 | 3,706.541939 | 0.000000 | 0.000000 | 0.299478 | b00220:lower, b01347:lower, b02579:lower |
| 98 (day 5, h02) | 1.000 | 121.037380 | 378.962620 | 3,626.580033 | 0.000000 | 0.000000 | 0.296173 | b00220:lower, b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 137.819162 | 362.180838 | 3,392.143531 | 0.000000 | 0.000000 | 0.286483 | b00220:lower, b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 162.470331 | 337.529669 | 2,998.761014 | 0.000000 | 0.000000 | 0.355600 | b00220:lower, b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 197.558093 | 302.441907 | 2,515.712297 | 0.000000 | 0.000000 | 0.318634 | b00220:lower, b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 238.123522 | 261.876478 | 1,950.238787 | 0.000000 | 0.000000 | 0.275897 | b00220:lower, b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 288.454881 | 211.545119 | 1,411.403868 | 0.000000 | 0.000000 | 0.224991 | b01983:upper, b02579:lower |
| 104 (day 5, h08) | 1.000 | 350.950107 | 149.049893 | 994.207610 | 0.000000 | 0.000000 | 0.159150 | b01983:upper, b02579:lower |
| 105 (day 5, h09) | 1.000 | 410.703233 | 89.296767 | 620.611092 | 0.000000 | 0.000000 | 0.152122 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 463.727282 | 36.272718 | 316.925239 | 0.000000 | 141.998811 | 0.063691 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 105.630770 | 394.369230 | 500.000000 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 105.630770 | 394.369230 | 500.000000 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 463.727282 | 36.272718 | 316.925239 | 0.000000 | 141.998811 | 0.063691 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 410.703233 | 89.296767 | 620.611092 | 0.000000 | 0.000000 | 0.152122 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 350.950107 | 149.049893 | 994.207610 | 0.000000 | 0.000000 | 0.159150 | b01983:upper, b02579:lower |
| 115 (day 5, h19) | 1.000 | 288.454881 | 211.545119 | 1,411.403868 | 0.000000 | 0.000000 | 0.224991 | b01983:upper, b02579:lower |
| 116 (day 5, h20) | 1.000 | 238.123522 | 261.876478 | 1,950.238787 | 0.000000 | 0.000000 | 0.275897 | b00220:lower, b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 197.558093 | 302.441907 | 2,515.712297 | 0.000000 | 0.000000 | 0.318634 | b00220:lower, b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 162.470331 | 337.529669 | 2,998.761014 | 0.000000 | 0.000000 | 0.355600 | b00220:lower, b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 137.819162 | 362.180838 | 3,392.143531 | 0.000000 | 0.000000 | 0.286483 | b00220:lower, b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | 81, 82, 88, 89, 103, 104, 114, 115 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 0: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9614aa7346b3b182abc9935cd928c83c02b44b77a8a24afbaaa0e338dc702506.json>).
- Period 1: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.58e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3b52094f0976bcafdf67ae7070fcf221d82ed4c6de0ba420562be1b61c2f8680.json>).
- Period 2: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9614aa7346b3b182abc9935cd928c83c02b44b77a8a24afbaaa0e338dc702506.json>).
- Period 3: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5341b883612ea6721fe1243d04eff8de70f08f0ac771a7e19dcdbed2b2fa5f1c.json>).
- Period 4: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9ac0b1c4a81fd49e6d743c036640ab8ab9a84f42d11ffa9e5ec50b5136457512.json>).
- Period 5: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.66e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d86d17e044a4cd117cf12da915858d10c68f1bd34ee4e965b5efd098a5e351c0.json>).
- Period 6: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.81e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b98944075fca6120362b32576e1a46b0a82ec1c7b5702bb1de2a2260f20d81fc.json>).
- Period 7: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.37e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4aeec020fe478f137a0b3505b676accc548cc34b1f8f6a138169e2abc465963c.json>).
- Period 8: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae35a5bb3d7cc183bd2134d588611c8381217b2f6706ab9458b6a683ed51aaf5.json>).
- Period 9: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96e6a4f85e43d1ba48ddfd10545c652d88a339fcc892651a97251d032eca868d.json>).
- Period 10: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.2e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/578e4fae7005e36e404db23019ae7377b15da0abd6ffbeeb495a37b7f112a3ff.json>).
- Period 11: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b9d251c3f94d90d97b3f09c1f4e745af513d4e45f372f41a63463d52cf321f6.json>).
- Period 12: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78bcd4dcbba0bfd28e6f1e04a8d64fdbf2068c976d4b366b83ca077a1877c6ca.json>).
- Period 13: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/93aec3178f5de342e5828f3a3d36d0c0cc63703f75f6db23a9cb2f39edf2d69d.json>).
- Period 14: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/78bcd4dcbba0bfd28e6f1e04a8d64fdbf2068c976d4b366b83ca077a1877c6ca.json>).
- Period 15: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.59e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b9d251c3f94d90d97b3f09c1f4e745af513d4e45f372f41a63463d52cf321f6.json>).
- Period 16: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.2e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/578e4fae7005e36e404db23019ae7377b15da0abd6ffbeeb495a37b7f112a3ff.json>).
- Period 17: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/96e6a4f85e43d1ba48ddfd10545c652d88a339fcc892651a97251d032eca868d.json>).
- Period 18: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae35a5bb3d7cc183bd2134d588611c8381217b2f6706ab9458b6a683ed51aaf5.json>).
- Period 19: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.37e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4aeec020fe478f137a0b3505b676accc548cc34b1f8f6a138169e2abc465963c.json>).
- Period 20: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.81e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b98944075fca6120362b32576e1a46b0a82ec1c7b5702bb1de2a2260f20d81fc.json>).
- Period 21: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.66e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d86d17e044a4cd117cf12da915858d10c68f1bd34ee4e965b5efd098a5e351c0.json>).
- Period 22: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9ac0b1c4a81fd49e6d743c036640ab8ab9a84f42d11ffa9e5ec50b5136457512.json>).
- Period 23: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5341b883612ea6721fe1243d04eff8de70f08f0ac771a7e19dcdbed2b2fa5f1c.json>).
- Period 24: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2ae2d503d5302ac0a5a54a58fefb23a6a2c81d44fca88be601fd75127892fe80.json>).
- Period 25: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b7765c5981c62014b37e10f8686272ba233ac5c4e64fb4a5ec1f5d2a48da6d37.json>).
- Period 26: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2ae2d503d5302ac0a5a54a58fefb23a6a2c81d44fca88be601fd75127892fe80.json>).
- Period 27: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6f52490925e111e7b3e787a51fc7f26494d95bd39d8b26745372b55b996ea648.json>).
- Period 28: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a25fa5548ea35d70906806375d784bc57b22f0c845cbfe28a03874ed188ebd2.json>).
- Period 29: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.8e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d9b084e870ae6ddb15d799a6daa5480b44dcbc7141c69223529fac3c04289b9c.json>).
- Period 30: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60c6bbcb91794378ba436b794a587263b20f94e67dc81dd84de3012c722b5e8d.json>).
- Period 31: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.48e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/530b6db4081f893a6979ab66ba724a547498bedddae1ab72cc9c10163d8d35d8.json>).
- Period 32: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.67e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6356df7f47b945e46d302fd692b5ea5541118a41094dbb2251aeb8ac3fa20aa.json>).
- Period 33: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/11143b304488df34385f4ed576819b84c6f95703f1ff95a5413d34c4292bae89.json>).
- Period 34: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/428cf374bb0b9362b02c54359e9955f9c21844a87bfb274d8d935173ed95c592.json>).
- Period 35: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e05bf46958464426c3b133782221a35f68b2d6c5b7f4a5b5f78c0c89ea6a2545.json>).
- Period 36: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a346d0e75748ce92ce3f8a65da777a0ee9aef96d3d50fb12faf5f491e706419d.json>).
- Period 37: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.68e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6225e93e3c7de33332124fea529c9fe55070b5c231c90b4eca39ec60224c6c90.json>).
- Period 38: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a346d0e75748ce92ce3f8a65da777a0ee9aef96d3d50fb12faf5f491e706419d.json>).
- Period 39: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.25e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e05bf46958464426c3b133782221a35f68b2d6c5b7f4a5b5f78c0c89ea6a2545.json>).
- Period 40: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/428cf374bb0b9362b02c54359e9955f9c21844a87bfb274d8d935173ed95c592.json>).
- Period 41: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.45e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/11143b304488df34385f4ed576819b84c6f95703f1ff95a5413d34c4292bae89.json>).
- Period 42: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.67e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6356df7f47b945e46d302fd692b5ea5541118a41094dbb2251aeb8ac3fa20aa.json>).
- Period 43: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.48e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/530b6db4081f893a6979ab66ba724a547498bedddae1ab72cc9c10163d8d35d8.json>).
- Period 44: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.34e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60c6bbcb91794378ba436b794a587263b20f94e67dc81dd84de3012c722b5e8d.json>).
- Period 45: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.8e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d9b084e870ae6ddb15d799a6daa5480b44dcbc7141c69223529fac3c04289b9c.json>).
- Period 46: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a25fa5548ea35d70906806375d784bc57b22f0c845cbfe28a03874ed188ebd2.json>).
- Period 47: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6f52490925e111e7b3e787a51fc7f26494d95bd39d8b26745372b55b996ea648.json>).
- Period 48: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c16781473398ae7d034db5f0a5f0aa5b1944d499f3195bdb37ddaeaf5f9a5c7.json>).
- Period 49: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.95e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d71fba94865a907b4f9bc72d9a775e3c9c2fd8d652dc89e398766c87de21fed7.json>).
- Period 50: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c16781473398ae7d034db5f0a5f0aa5b1944d499f3195bdb37ddaeaf5f9a5c7.json>).
- Period 51: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.42e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aafcd65187eb50bedb0167b88f0c050ce78ba6bd87ae9002d8edd37e3329954a.json>).
- Period 52: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7e25ed796a7aba0849223ef833bb1f22070e26a5cb0afdd23490501d3abc1ab7.json>).
- Period 53: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dc7fd69bf5eec86030ff8eac8d9b5c9e04df3a61f312ddda75a6f085289a3ffc.json>).
- Period 54: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c9ab768c38904643668f5be80d363a1cb65ec667873660d7cc56e0680024ed0.json>).
- Period 55: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c74f5350e6c257925cf08634a119b7f815261d86d75d7f3945f8a1846af1047d.json>).
- Period 56: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/93cc0417ff906782fcb41380e14dd8cd16ef1c4489005e9daa0f7bad9a9e5242.json>).
- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f8989dbbfef34d7f890340c462c3956f11e59f09451994481d4f3be658e72ef.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db4fd33c70a08156271504a8d90d111bc51585ceb9fc587b11c96281988e9775.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/927dd9967ca3a69daade975fabcc6ea9eed1f3743c2263843fc14f3d996746d3.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c5fee851fa3f2c72899dcc99633fe770840100077c4a758785b2ec9f677ae572.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ac58a05e0393346adc3e9330ab658dd181fddad10d504419a960ae64215f2c70.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c5fee851fa3f2c72899dcc99633fe770840100077c4a758785b2ec9f677ae572.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/927dd9967ca3a69daade975fabcc6ea9eed1f3743c2263843fc14f3d996746d3.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.64e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db4fd33c70a08156271504a8d90d111bc51585ceb9fc587b11c96281988e9775.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f8989dbbfef34d7f890340c462c3956f11e59f09451994481d4f3be658e72ef.json>).
- Period 66: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/93cc0417ff906782fcb41380e14dd8cd16ef1c4489005e9daa0f7bad9a9e5242.json>).
- Period 67: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c74f5350e6c257925cf08634a119b7f815261d86d75d7f3945f8a1846af1047d.json>).
- Period 68: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c9ab768c38904643668f5be80d363a1cb65ec667873660d7cc56e0680024ed0.json>).
- Period 69: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dc7fd69bf5eec86030ff8eac8d9b5c9e04df3a61f312ddda75a6f085289a3ffc.json>).
- Period 70: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7e25ed796a7aba0849223ef833bb1f22070e26a5cb0afdd23490501d3abc1ab7.json>).
- Period 71: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.42e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aafcd65187eb50bedb0167b88f0c050ce78ba6bd87ae9002d8edd37e3329954a.json>).
- Period 72: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.99e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc618b8049d64d511a8e0c1fcbaab9509e14a375708442d873106fa11f30162d.json>).
- Period 73: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.68e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ed7708676a7b1a0c47ab1f870f4ab05ed38ca3c01e07e2e91bdbcba286f25e11.json>).
- Period 74: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.99e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bc618b8049d64d511a8e0c1fcbaab9509e14a375708442d873106fa11f30162d.json>).
- Period 75: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/14875dc273bfb5a2fdc5bce4549e0522c580d30ced7d7540dbd94235bdd30709.json>).
- Period 76: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.83e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d039ca8950368cc5a7be3c0af01806d775b8c855dc1d14231b9b0cd89601fd7.json>).
- Period 77: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f31cfc6ce8c053dda11b57e592df204256fb0e082dfa34fd20bd9ebe7b878857.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.56e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4cfc9b3c2481aea23cb15bce6094b5bfa189cf14f93f99e575827db79cc6be1.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a0a246068103aa6a9ccb4716eaff37f3914689812ef8ca85cac8f9c7f81078d.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d35d65a90002bdcec9fcbab6811c495294513c4cdffb62edf03aef8d754eb12.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/19995c190e30e91a23d5377b4de34cf8eba88ce785ce8c6e3e9288d9f102ecf0.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d187e193b765897de668018064b063470aa3a57f0b13ee6cca4e6691e2530fd.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/044ed65efb27505851249e3d63329f1dcfc4d89b16118b62d7e74019a9e6921a.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/13b61c48ae7f5e9fc7fbdfab3e8cb0ed9b7725760c5e9ad5e52d18600381fac8.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.09e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ed781a16cc2d6566850c9ce52b158ea3a4a1dce65727d99657dfef0c04370122.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/13b61c48ae7f5e9fc7fbdfab3e8cb0ed9b7725760c5e9ad5e52d18600381fac8.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/044ed65efb27505851249e3d63329f1dcfc4d89b16118b62d7e74019a9e6921a.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d187e193b765897de668018064b063470aa3a57f0b13ee6cca4e6691e2530fd.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/19995c190e30e91a23d5377b4de34cf8eba88ce785ce8c6e3e9288d9f102ecf0.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0d35d65a90002bdcec9fcbab6811c495294513c4cdffb62edf03aef8d754eb12.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9a0a246068103aa6a9ccb4716eaff37f3914689812ef8ca85cac8f9c7f81078d.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.56e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4cfc9b3c2481aea23cb15bce6094b5bfa189cf14f93f99e575827db79cc6be1.json>).
- Period 93: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.62e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f31cfc6ce8c053dda11b57e592df204256fb0e082dfa34fd20bd9ebe7b878857.json>).
- Period 94: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.83e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4d039ca8950368cc5a7be3c0af01806d775b8c855dc1d14231b9b0cd89601fd7.json>).
- Period 95: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/14875dc273bfb5a2fdc5bce4549e0522c580d30ced7d7540dbd94235bdd30709.json>).
- Period 96: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5a8a35d38be0c3ffaa167e7265744d58b1252d9a05d33325404f7b1fbbf3555d.json>).
- Period 97: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.05e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8785fd54f049f65761b4e3392b057a04ff355fdc9b8085387dbac21a70b8fef5.json>).
- Period 98: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5a8a35d38be0c3ffaa167e7265744d58b1252d9a05d33325404f7b1fbbf3555d.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.49e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b087198d40c7f023219224d7a34e5e0b142a8eafcd78ec1a605aa81a5e3766b5.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8dc6cdf473d58926116262f66a09cbcce585175617b0aaf5a1e1d801eeaa5a79.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dea11f05a687ae39877d7591f00f71ac450bdf7cbd8fd0770e298a85ece9fd81.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d48f158486c5010d18172f7296bc1b552fc5a1b71c6f8eb6f70abb9bf48b6ebb.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/285a5cd2c6ea3f7f2697fd5d1436ff5a621afa03da817a68d71d9acf68be9da5.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/106239fe7e75f26d913483458861df1665bb5461d16b8fdec4eecd39e5f3a7d9.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7ecfd2028cc70fca66251d8b49b16b1ee853196c32b04879c74a7e7361023d19.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **141.998811 MW**; maximum nodal residual 3.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/25679ddfde8d02281d5576cb88a57cb5b5b0d85b71dc0d856daf2193397ed166.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 141.998811 | 134.344253 | 7.654557 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.11e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/016663dfb12b74c3a176d1aabbaed65cbc33c9b14ceba8f1e21e8c7ffd4dfa8f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 500.000000 | 492.010489 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.11e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/016663dfb12b74c3a176d1aabbaed65cbc33c9b14ceba8f1e21e8c7ffd4dfa8f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 500.000000 | 492.010489 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **141.998811 MW**; maximum nodal residual 3.97e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/25679ddfde8d02281d5576cb88a57cb5b5b0d85b71dc0d856daf2193397ed166.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 141.998811 | 134.344253 | 7.654557 | True |

- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.91e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7ecfd2028cc70fca66251d8b49b16b1ee853196c32b04879c74a7e7361023d19.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/106239fe7e75f26d913483458861df1665bb5461d16b8fdec4eecd39e5f3a7d9.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.82e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/285a5cd2c6ea3f7f2697fd5d1436ff5a621afa03da817a68d71d9acf68be9da5.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d48f158486c5010d18172f7296bc1b552fc5a1b71c6f8eb6f70abb9bf48b6ebb.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/dea11f05a687ae39877d7591f00f71ac450bdf7cbd8fd0770e298a85ece9fd81.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8dc6cdf473d58926116262f66a09cbcce585175617b0aaf5a1e1d801eeaa5a79.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.49e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b087198d40c7f023219224d7a34e5e0b142a8eafcd78ec1a605aa81a5e3766b5.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `3869110b854cc08d7ffed8e368863cec06b955547b8df64e45b1de211d37fc23`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
