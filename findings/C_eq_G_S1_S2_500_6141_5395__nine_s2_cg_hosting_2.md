<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_6141_5395","policy":"C_eq_G_S1_S2","portfolio":"bottleneck_ptdf_2_both_cg","buses":["6141","5395"],"weights":[0.5,0.5],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"a5608972329721e01dec805c40425115194cefc0f7e205e1d89c535c7eea49f0","score_usd":67046205783.44057,"it_value_usd":123053148597.11996,"grid_mwh":16870642.854109395,"generation_mwh":649357.1458868814,"modeled_generator_hours":96.0,"annual_generator_hours":4469.852054793918,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/a5608972329721e01dec805c40425115194cefc0f7e205e1d89c535c7eea49f0-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_6141_5395 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262094 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.025485 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.702779 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.055848 |
| Campaign total | — | — | — | — | 123.053149 | 67.046206 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,775.310 | 1,224.690 | 99.972039% | 3.000 | 3.000 | 3.000 | 0.000 | 499.697540 |
| week-2-submission-2 | 4,056,546.117 | 323,453.883 | 92.615208% | 45.000 | 2,231.926 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,775.310 | 1,224.690 | 99.972039% | 3.000 | 3.000 | 3.000 | 0.000 | 499.697540 |
| week-3-submission-2 | 4,056,546.117 | 323,453.883 | 92.615208% | 45.000 | 2,231.926 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001193 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.237802 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.559314 | 0.001193 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.969637 | 0.237802 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 6141: 250 MW per submission, 5395: 250 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,224.690 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 35, 36, 37, 38, 39, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 323,453.883 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 57 (day 3, h09) | 82.773 | 62.500000 | 437.500000 | 2,746.241961 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 62.500000 | 437.500000 | 2,251.194167 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 62.500000 | 437.500000 | 1,868.283896 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 62.500000 | 437.500000 | 1,641.910279 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 98.713799 | 401.286201 | 1,601.287320 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 62.500000 | 437.500000 | 1,641.910279 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 62.500000 | 437.500000 | 1,868.283896 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 62.500000 | 437.500000 | 2,251.194167 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 62.500000 | 437.500000 | 2,746.241961 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 62.500000 | 437.500000 | 2,678.287141 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 62.500000 | 437.500000 | 2,058.282247 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,541.233565 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 250.000000 | 250.000000 | 1,171.458524 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 250.000000 | 250.000000 | 871.472705 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 250.000000 | 250.000000 | 641.285487 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 250.000000 | 250.000000 | 488.764587 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 250.000000 | 250.000000 | 435.912988 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 250.000000 | 250.000000 | 488.764587 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 250.000000 | 250.000000 | 641.285487 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 250.000000 | 250.000000 | 871.472705 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 250.000000 | 250.000000 | 1,171.458524 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,541.233565 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 91 (day 4, h19) | 97.732 | 62.500000 | 437.500000 | 2,058.282247 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 62.500000 | 437.500000 | 2,678.287141 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 5.069992 | 494.930008 | 2,881.481075 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 62.500000 | 437.500000 | 2,515.171939 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 62.500000 | 437.500000 | 2,011.131769 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,538.822754 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 250.000000 | 250.000000 | 1,143.659128 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 250.000000 | 250.000000 | 768.770188 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 250.000000 | 250.000000 | 406.144155 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 312.500000 | 187.500000 | 118.552008 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 312.500000 | 187.500000 | 118.552008 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 250.000000 | 250.000000 | 406.144155 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 250.000000 | 250.000000 | 768.770188 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 250.000000 | 250.000000 | 1,143.659128 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,538.822754 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 117 (day 5, h21) | 1.000 | 62.500000 | 437.500000 | 2,011.131769 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 62.500000 | 437.500000 | 2,515.171939 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 5.069992 | 494.930008 | 2,881.481075 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 93, 94, 95, 96, 97, 98, 99, 119 | 99, 119 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 117, 118, 119 | 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 91, 92, 99, 100, 101, 117, 118, 119 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.19e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/06cc915747ad4a34356144f976dfc3c4ee3f04d591c8d3847887f36eac9946c8.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.71e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae3646a8fbbc98d26222de560033f0f6eb22713f0d8375780c058135d4f3639c.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.72e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/92598347fd687245800a615d219224cb4118411274f8a42ac1f15074e5157dc0.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa5af93b17becf441ded857108efff34a5548b75ea537917195392127199bb8.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.87e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/50792cb22ca57b5876e69b79f66103b8165a52a88a6e1adabc66c0a29eebc590.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa5af93b17becf441ded857108efff34a5548b75ea537917195392127199bb8.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.72e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/92598347fd687245800a615d219224cb4118411274f8a42ac1f15074e5157dc0.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.71e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae3646a8fbbc98d26222de560033f0f6eb22713f0d8375780c058135d4f3639c.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.19e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/06cc915747ad4a34356144f976dfc3c4ee3f04d591c8d3847887f36eac9946c8.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/710ff7266761d94795284e1489dbad76a0e7acfac04f8844216ea405c3ee5a52.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47020e1b536d8b0b1359bcc6df5d03851e68d647d84d8d8ca35d4703328146ed.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e59ec8a77b78d79e7c12ebc555dc335b5db21152bc39bb968fd4950104906114.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4a854b1029b2608d97cee9a3b651aeef9eae33cdb61ad520430791408cda50f.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c8877d0551b93d22ae4113a74b6ecd2eacb105afa58ace8cfabd56587a6a3905.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aaebacc7e478fb1e147982a9d55218a203b20eee5b42d7c164318541b5603268.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b48cc18a916e5b709e0e4fd7d3bd3a6345d596f0817b09da7c4eece0a6a6aaf8.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.84e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bd3c661ed79916c8a0d16e1ced9155bfd78a7617e648e2c0e103df71801a2559.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b48cc18a916e5b709e0e4fd7d3bd3a6345d596f0817b09da7c4eece0a6a6aaf8.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aaebacc7e478fb1e147982a9d55218a203b20eee5b42d7c164318541b5603268.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c8877d0551b93d22ae4113a74b6ecd2eacb105afa58ace8cfabd56587a6a3905.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4a854b1029b2608d97cee9a3b651aeef9eae33cdb61ad520430791408cda50f.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e59ec8a77b78d79e7c12ebc555dc335b5db21152bc39bb968fd4950104906114.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47020e1b536d8b0b1359bcc6df5d03851e68d647d84d8d8ca35d4703328146ed.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/710ff7266761d94795284e1489dbad76a0e7acfac04f8844216ea405c3ee5a52.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e9f29cf0c47f4c3c31648707afbef4a4307d31e2bfead6368c24219f9531153.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f3b089e8e9e3142491343189bffbc2a8e92f31d54157018cfd5197f9f6b008e.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/91e59ecc3a033329530f8b4ea5c154dc8fffde429b2065ace3d8c4cbb07fa358.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e01cbe099fc6624ae718b2ca7ed964780197bc3930b178be1b3b07dbbdc34419.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/deaf5849d9db2b640cd4204040fafb5ce88b699f76e39960d699ad9e66dfb712.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a8c0b23378bc0c12a790879ae032d76acaaa783e1f15a9e8ab4a89515979e80.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/502cd3c32bb5ed8d66773a49db4e44679d97a9ae240c6ec3a89fdf11f94d7c02.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.44e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/97a4f598e39ec9ee6fbb488c6718479ea491da09504fbef3ed0d77d583a5bbac.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 7.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a3f4a9718321f13a20a8420a014d0f723b6b6ee16fcb32dac4b00a581cd15bd7.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 7.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a3f4a9718321f13a20a8420a014d0f723b6b6ee16fcb32dac4b00a581cd15bd7.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.44e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/97a4f598e39ec9ee6fbb488c6718479ea491da09504fbef3ed0d77d583a5bbac.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/502cd3c32bb5ed8d66773a49db4e44679d97a9ae240c6ec3a89fdf11f94d7c02.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a8c0b23378bc0c12a790879ae032d76acaaa783e1f15a9e8ab4a89515979e80.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/deaf5849d9db2b640cd4204040fafb5ce88b699f76e39960d699ad9e66dfb712.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e01cbe099fc6624ae718b2ca7ed964780197bc3930b178be1b3b07dbbdc34419.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/91e59ecc3a033329530f8b4ea5c154dc8fffde429b2065ace3d8c4cbb07fa358.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f3b089e8e9e3142491343189bffbc2a8e92f31d54157018cfd5197f9f6b008e.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e9f29cf0c47f4c3c31648707afbef4a4307d31e2bfead6368c24219f9531153.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,224.690 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.692200 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.857892 | 0.000000 | 0.000000 | 6.692200 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.692200 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000531 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 35, 36, 37, 38, 39, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 323,453.883 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 57 (day 3, h09) | 82.773 | 62.500000 | 437.500000 | 2,746.241961 | 0.000000 | 0.000000 | 11.632904 | b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 62.500000 | 437.500000 | 2,251.194167 | 0.000000 | 0.000000 | 18.982922 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 62.500000 | 437.500000 | 1,868.283896 | 0.000000 | 0.000000 | 19.676646 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 62.500000 | 437.500000 | 1,641.910279 | 0.000000 | 0.000000 | 22.561812 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 98.713799 | 401.286201 | 1,601.287320 | 0.000000 | 0.000000 | 25.846575 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 62.500000 | 437.500000 | 1,641.910279 | 0.000000 | 0.000000 | 22.561812 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 62.500000 | 437.500000 | 1,868.283896 | 0.000000 | 0.000000 | 19.676646 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 62.500000 | 437.500000 | 2,251.194167 | 0.000000 | 0.000000 | 18.982922 | b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 62.500000 | 437.500000 | 2,746.241961 | 0.000000 | 0.000000 | 11.632904 | b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 62.500000 | 437.500000 | 2,678.287141 | 0.000000 | 0.000000 | 13.735236 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 62.500000 | 437.500000 | 2,058.282247 | 0.000000 | 0.000000 | 22.580124 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,541.233565 | 0.000000 | 0.000000 | 29.467243 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 250.000000 | 250.000000 | 1,171.458524 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 250.000000 | 250.000000 | 871.472705 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 250.000000 | 250.000000 | 641.285487 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 250.000000 | 250.000000 | 488.764587 | 0.000000 | 0.000000 | 27.569061 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 250.000000 | 250.000000 | 435.912988 | 0.000000 | 0.000000 | 27.569061 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 250.000000 | 250.000000 | 488.764587 | 0.000000 | 0.000000 | 27.569061 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 250.000000 | 250.000000 | 641.285487 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 250.000000 | 250.000000 | 871.472705 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 250.000000 | 250.000000 | 1,171.458524 | 0.000000 | 0.000000 | 17.673573 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,541.233565 | 0.000000 | 0.000000 | 29.467243 | b02579:lower |
| 91 (day 4, h19) | 97.732 | 62.500000 | 437.500000 | 2,058.282247 | 0.000000 | 0.000000 | 22.580124 | b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 62.500000 | 437.500000 | 2,678.287141 | 0.000000 | 0.000000 | 13.735236 | b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 5.069992 | 494.930008 | 2,881.481075 | 0.000000 | 0.000000 | 0.171989 | b00220:lower, b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 62.500000 | 437.500000 | 2,515.171939 | 0.000000 | 0.000000 | 0.140541 | b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 62.500000 | 437.500000 | 2,011.131769 | 0.000000 | 0.000000 | 0.237719 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,538.822754 | 0.000000 | 0.000000 | 0.301512 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 250.000000 | 250.000000 | 1,143.659128 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 250.000000 | 250.000000 | 768.770188 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 250.000000 | 250.000000 | 406.144155 | 0.000000 | 0.000000 | 0.282090 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 312.500000 | 187.500000 | 118.552008 | 0.000000 | 0.000000 | 0.195855 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 312.500000 | 187.500000 | 118.552008 | 0.000000 | 0.000000 | 0.195855 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 250.000000 | 250.000000 | 406.144155 | 0.000000 | 0.000000 | 0.282090 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 250.000000 | 250.000000 | 768.770188 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 250.000000 | 250.000000 | 1,143.659128 | 0.000000 | 0.000000 | 0.180838 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,538.822754 | 0.000000 | 0.000000 | 0.301512 | b02579:lower |
| 117 (day 5, h21) | 1.000 | 62.500000 | 437.500000 | 2,011.131769 | 0.000000 | 0.000000 | 0.237719 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 62.500000 | 437.500000 | 2,515.171939 | 0.000000 | 0.000000 | 0.140541 | b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 5.069992 | 494.930008 | 2,881.481075 | 0.000000 | 0.000000 | 0.171989 | b00220:lower, b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 93, 94, 95, 96, 97, 98, 99, 119 | 99, 119 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 117, 118, 119 | 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 91, 92, 99, 100, 101, 117, 118, 119 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 57, 58, 59, 60, 61, 62, 63, 64, 65, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.19e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/06cc915747ad4a34356144f976dfc3c4ee3f04d591c8d3847887f36eac9946c8.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.71e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae3646a8fbbc98d26222de560033f0f6eb22713f0d8375780c058135d4f3639c.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.72e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/92598347fd687245800a615d219224cb4118411274f8a42ac1f15074e5157dc0.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa5af93b17becf441ded857108efff34a5548b75ea537917195392127199bb8.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.87e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/50792cb22ca57b5876e69b79f66103b8165a52a88a6e1adabc66c0a29eebc590.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3aa5af93b17becf441ded857108efff34a5548b75ea537917195392127199bb8.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.72e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/92598347fd687245800a615d219224cb4118411274f8a42ac1f15074e5157dc0.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.71e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ae3646a8fbbc98d26222de560033f0f6eb22713f0d8375780c058135d4f3639c.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.19e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/06cc915747ad4a34356144f976dfc3c4ee3f04d591c8d3847887f36eac9946c8.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/710ff7266761d94795284e1489dbad76a0e7acfac04f8844216ea405c3ee5a52.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47020e1b536d8b0b1359bcc6df5d03851e68d647d84d8d8ca35d4703328146ed.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e59ec8a77b78d79e7c12ebc555dc335b5db21152bc39bb968fd4950104906114.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4a854b1029b2608d97cee9a3b651aeef9eae33cdb61ad520430791408cda50f.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c8877d0551b93d22ae4113a74b6ecd2eacb105afa58ace8cfabd56587a6a3905.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aaebacc7e478fb1e147982a9d55218a203b20eee5b42d7c164318541b5603268.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b48cc18a916e5b709e0e4fd7d3bd3a6345d596f0817b09da7c4eece0a6a6aaf8.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.84e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bd3c661ed79916c8a0d16e1ced9155bfd78a7617e648e2c0e103df71801a2559.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b48cc18a916e5b709e0e4fd7d3bd3a6345d596f0817b09da7c4eece0a6a6aaf8.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/aaebacc7e478fb1e147982a9d55218a203b20eee5b42d7c164318541b5603268.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c8877d0551b93d22ae4113a74b6ecd2eacb105afa58ace8cfabd56587a6a3905.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.58e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a4a854b1029b2608d97cee9a3b651aeef9eae33cdb61ad520430791408cda50f.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.04e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e59ec8a77b78d79e7c12ebc555dc335b5db21152bc39bb968fd4950104906114.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/47020e1b536d8b0b1359bcc6df5d03851e68d647d84d8d8ca35d4703328146ed.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/710ff7266761d94795284e1489dbad76a0e7acfac04f8844216ea405c3ee5a52.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e9f29cf0c47f4c3c31648707afbef4a4307d31e2bfead6368c24219f9531153.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f3b089e8e9e3142491343189bffbc2a8e92f31d54157018cfd5197f9f6b008e.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/91e59ecc3a033329530f8b4ea5c154dc8fffde429b2065ace3d8c4cbb07fa358.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e01cbe099fc6624ae718b2ca7ed964780197bc3930b178be1b3b07dbbdc34419.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/deaf5849d9db2b640cd4204040fafb5ce88b699f76e39960d699ad9e66dfb712.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a8c0b23378bc0c12a790879ae032d76acaaa783e1f15a9e8ab4a89515979e80.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/502cd3c32bb5ed8d66773a49db4e44679d97a9ae240c6ec3a89fdf11f94d7c02.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.44e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/97a4f598e39ec9ee6fbb488c6718479ea491da09504fbef3ed0d77d583a5bbac.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 7.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a3f4a9718321f13a20a8420a014d0f723b6b6ee16fcb32dac4b00a581cd15bd7.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 7.57e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a3f4a9718321f13a20a8420a014d0f723b6b6ee16fcb32dac4b00a581cd15bd7.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.44e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/97a4f598e39ec9ee6fbb488c6718479ea491da09504fbef3ed0d77d583a5bbac.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/502cd3c32bb5ed8d66773a49db4e44679d97a9ae240c6ec3a89fdf11f94d7c02.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.15e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a8c0b23378bc0c12a790879ae032d76acaaa783e1f15a9e8ab4a89515979e80.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/deaf5849d9db2b640cd4204040fafb5ce88b699f76e39960d699ad9e66dfb712.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.65e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e01cbe099fc6624ae718b2ca7ed964780197bc3930b178be1b3b07dbbdc34419.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/91e59ecc3a033329530f8b4ea5c154dc8fffde429b2065ace3d8c4cbb07fa358.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f3b089e8e9e3142491343189bffbc2a8e92f31d54157018cfd5197f9f6b008e.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-07 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e9f29cf0c47f4c3c31648707afbef4a4307d31e2bfead6368c24219f9531153.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b01548:lower`, `b02136:lower`, `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `a5608972329721e01dec805c40425115194cefc0f7e205e1d89c535c7eea49f0`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
