<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_1079","policy":"C_eq_G_S1_S2","portfolio":"hosting_1_both_cg","buses":["1079"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"a6bd3e9ae0f43828f4af82b61295aa05e50af9bd437ac8e288024766c902a1be","score_usd":66015040913.1532,"it_value_usd":123053148597.11996,"grid_mwh":16034374.892254421,"generation_mwh":1485625.1077418553,"modeled_generator_hours":146.0,"annual_generator_hours":8073.978082189529,"required_annual_hours":24.000000000228948,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/a6bd3e9ae0f43828f4af82b61295aa05e50af9bd437ac8e288024766c902a1be-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_1079 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262029 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.676954 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.698958 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 15.377100 |
| Campaign total | — | — | — | — | 123.053149 | 66.015041 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,659.975 | 1,340.025 | 99.969406% | 5.000 | 5.000 | 5.000 | 0.000 | 499.697540 |
| week-2-submission-2 | 3,638,527.471 | 741,472.529 | 83.071403% | 68.000 | 4,031.989 | 7.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,659.975 | 1,340.025 | 99.969406% | 5.000 | 5.000 | 5.000 | 0.000 | 499.697540 |
| week-3-submission-2 | 3,638,527.471 | 741,472.529 | 83.071403% | 68.000 | 4,031.989 | 7.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001258 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.586333 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.563071 | 0.001258 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 1.299853 | 0.586333 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 1079: 500 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,340.025 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 57.667784 | 442.332216 | 97.426008 | 0.000000 | 57.667784 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 57.667784 | 442.332216 | 97.426008 | 0.000000 | 57.667784 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 34, 35, 36, 37, 38, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 107, 111 | True |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **57.667784 MW**; maximum nodal residual 2.96e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60cef3b7db653dc33f4e58d48eb6330b422c136b167230c9ecd4f1c105fc0785.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 57.667784 | 49.678273 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **57.667784 MW**; maximum nodal residual 2.96e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60cef3b7db653dc33f4e58d48eb6330b422c136b167230c9ecd4f1c105fc0785.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 57.667784 | 49.678273 | 7.989511 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 741,472.529 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112. At periods 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 (day 1, h10) | 83.770 | 13.408150 | 486.591850 | 4,815.473115 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 11 (day 1, h11) | 83.770 | 60.412533 | 439.587467 | 4,442.538521 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 12 (day 1, h12) | 83.770 | 89.960725 | 410.039275 | 4,208.102009 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 13 (day 1, h13) | 83.770 | 100.039063 | 399.960937 | 4,128.140098 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 14 (day 1, h14) | 83.770 | 89.960725 | 410.039275 | 4,208.102009 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 15 (day 1, h15) | 83.770 | 60.412533 | 439.587467 | 4,442.538521 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 16 (day 1, h16) | 83.770 | 13.408150 | 486.591850 | 4,815.473115 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 55 (day 3, h07) | 82.773 | 62.623353 | 437.376647 | 4,424.997787 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 56 (day 3, h08) | 82.773 | 125.000000 | 375.000000 | 3,823.207886 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 57 (day 3, h09) | 82.773 | 163.636738 | 336.363262 | 3,241.002643 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 227.432751 | 272.567249 | 2,757.954377 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 275.990701 | 224.009299 | 2,385.128903 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 306.542469 | 193.457531 | 2,150.909328 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 316.963110 | 183.036890 | 2,071.021393 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 306.542469 | 193.457531 | 2,150.909328 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 275.990701 | 224.009299 | 2,385.128903 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 227.432751 | 272.567249 | 2,757.954377 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 163.636738 | 336.363262 | 3,241.002643 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 66 (day 3, h18) | 82.773 | 125.000000 | 375.000000 | 3,823.207886 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 67 (day 3, h19) | 82.773 | 62.623353 | 437.376647 | 4,424.997787 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 72 (day 4, h00) | 97.732 | 10.103080 | 489.896920 | 4,841.695665 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 73 (day 4, h01) | 97.732 | 0.024742 | 499.975258 | 4,921.657590 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 74 (day 4, h02) | 97.732 | 10.103080 | 489.896920 | 4,841.695665 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 75 (day 4, h03) | 97.732 | 39.651270 | 460.348730 | 4,607.259173 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 76 (day 4, h04) | 97.732 | 86.655655 | 413.344345 | 4,234.324571 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 77 (day 4, h05) | 97.732 | 125.000000 | 375.000000 | 3,755.253093 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 172.650978 | 327.349022 | 3,171.639360 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 252.238393 | 247.761607 | 2,567.221652 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 331.391011 | 168.608989 | 1,960.412532 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 207.130217 | 292.869783 | 1,430.850384 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 82 (day 4, h10) | 97.732 | 298.054986 | 201.945014 | 1,097.010284 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 83 (day 4, h11) | 97.732 | 369.001733 | 130.998267 | 847.323176 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 375.000000 | 125.000000 | 689.568973 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 375.000000 | 125.000000 | 636.166707 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 375.000000 | 125.000000 | 689.568973 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 369.001733 | 130.998267 | 847.323176 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 298.054986 | 201.945014 | 1,097.010284 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 89 (day 4, h17) | 97.732 | 207.130217 | 292.869783 | 1,430.850384 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 90 (day 4, h18) | 97.732 | 331.391011 | 168.608989 | 1,960.412532 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 252.238393 | 247.761607 | 2,567.221652 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 172.650978 | 327.349022 | 3,171.639360 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 93 (day 4, h21) | 97.732 | 125.000000 | 375.000000 | 3,755.253093 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 94 (day 4, h22) | 97.732 | 86.655655 | 413.344345 | 4,234.324571 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 95 (day 4, h23) | 97.732 | 39.651270 | 460.348730 | 4,607.259173 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 96 (day 5, h00) | 1.000 | 125.000000 | 375.000000 | 3,632.714083 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 97 (day 5, h01) | 1.000 | 125.000000 | 375.000000 | 3,711.101263 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 98 (day 5, h02) | 1.000 | 125.000000 | 375.000000 | 3,632.714083 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 145.792558 | 354.207442 | 3,378.310980 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 194.288300 | 305.711700 | 3,005.143358 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 258.107848 | 241.892152 | 2,522.224527 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 331.866346 | 168.133654 | 1,956.768468 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 215.556124 | 284.443876 | 1,399.913743 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 104 (day 5, h08) | 1.000 | 329.183808 | 170.816192 | 982.717485 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 105 (day 5, h09) | 1.000 | 375.000000 | 125.000000 | 606.362229 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 432.060569 | 67.939431 | 305.985556 | 0.000000 | 126.333132 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 97.426008 | 402.573992 | 499.999999 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 97.426008 | 402.573992 | 499.999999 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 432.060569 | 67.939431 | 305.985556 | 0.000000 | 126.333132 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 375.000000 | 125.000000 | 606.362229 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 329.183808 | 170.816192 | 982.717485 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 115 (day 5, h19) | 1.000 | 215.556124 | 284.443876 | 1,399.913743 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 116 (day 5, h20) | 1.000 | 331.866346 | 168.133654 | 1,956.768468 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 258.107848 | 241.892152 | 2,522.224527 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 194.288300 | 305.711700 | 3,005.143358 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 145.792558 | 354.207442 | 3,378.310980 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 94, 95 | 10, 11, 12, 13, 14, 15, 16, 55, 67, 72, 73, 74, 75, 76, 94, 95 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | 81, 82, 88, 89, 103, 104, 114, 115 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 10: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/405b6403916569891bb43c3b502114201bfc9e4b9ba88afb0f874cd2696ede0d.json>).
- Period 11: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27632c01fa046ccc5c83eb642a864e96fa83cddb0b08d42c4879e2f77fc5e40a.json>).
- Period 12: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6d10e2b20f7e989671950b9550af52f4fcb1ee436733bc0c1d1106f12bb62fa7.json>).
- Period 13: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cf64fecb3704491cf0d61df040b2ad085c90fa8795e2d3fc68ee0b0b1d832592.json>).
- Period 14: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6d10e2b20f7e989671950b9550af52f4fcb1ee436733bc0c1d1106f12bb62fa7.json>).
- Period 15: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27632c01fa046ccc5c83eb642a864e96fa83cddb0b08d42c4879e2f77fc5e40a.json>).
- Period 16: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/405b6403916569891bb43c3b502114201bfc9e4b9ba88afb0f874cd2696ede0d.json>).
- Period 55: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3e775eb2ec97f5cbefa17db4f96fff5f3c8c5ccf16ef8b550b404d9562ee9561.json>).
- Period 56: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3d86193e7cada0218860c83d0ea8df09a2ec2a7a94022c4ba41b7f74f9e92911.json>).
- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.94e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b56cdc26c5c605900bd19c7e2d98c4eece9b2e49ad8a199b4a6096db7439cff8.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7ece4c944b0a50748f885c06cd8a917f9aed76c09ff7788d7a9e302d7d18613.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b3ffd34618e8412628347a50f61ac383c294b8ef3e235ad0f8389b3bca647daa.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f47eaeedfb34e5b8455fbd77ae1b9b14a590bf95de6402a9752b4b338ebe7d3.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.7e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0934e4e0ac0d81479eeadcfa7dedbd0754679247553ff2e91359a68f4c226d0a.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f47eaeedfb34e5b8455fbd77ae1b9b14a590bf95de6402a9752b4b338ebe7d3.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b3ffd34618e8412628347a50f61ac383c294b8ef3e235ad0f8389b3bca647daa.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7ece4c944b0a50748f885c06cd8a917f9aed76c09ff7788d7a9e302d7d18613.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.94e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b56cdc26c5c605900bd19c7e2d98c4eece9b2e49ad8a199b4a6096db7439cff8.json>).
- Period 66: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3d86193e7cada0218860c83d0ea8df09a2ec2a7a94022c4ba41b7f74f9e92911.json>).
- Period 67: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3e775eb2ec97f5cbefa17db4f96fff5f3c8c5ccf16ef8b550b404d9562ee9561.json>).
- Period 72: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0ac881f7e8f271ed606e95419aa3696b0b2f4673c68e9ff39959d69051d2a553.json>).
- Period 73: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.21e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5e75503636dbbd7fda9c329333870044ae1754cc9010d9be1f155f2879d4895d.json>).
- Period 74: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0ac881f7e8f271ed606e95419aa3696b0b2f4673c68e9ff39959d69051d2a553.json>).
- Period 75: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.39e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c26b862f9a7ce5c71dfb0ce1927f62919133a0682f874e9e76dcbebe218bbc8.json>).
- Period 76: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fb2a90e6f5223e6bc424181a4b00c78b3e20b4e33c54f23bb3be4ed2bc73c618.json>).
- Period 77: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db9d67c3c1c1265a28fc430f6c5afb2f6304b49bdf7c404ef74d4d89f4d285de.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.41e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/55ba1699c0bd0458d8617b36818e7ed1ab5a19c49d2b08724cfaa3fbb7a41ac4.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1152223fe5077bb7d88ba79365a37f311cbadb27be2300d5509ce4b9f184ee1f.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8051999ba4d3e1ddc238d309dc3191cb90673a657a70d0cb184e144942f88d35.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c91e463a3df9d3342bd3186869c465bb2247aa8cf0124ea3818d557745507194.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.3e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c978f5dcffb36644d1dabee28c5e694032ce098e9cda0d0f04ebd30ca35d344.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f96e794d6df48c0e13b6d04b6f73752b59e379f382c61c25729ddcc19e02cca7.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d845cde236409fe23fd746cc5826fd657798ab3ea1f269d8780e8e46b61378cb.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2b375f1aebc51c3656bb7a772ad0c43907ace91ec6c815ed202e9ab16f5ab502.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d845cde236409fe23fd746cc5826fd657798ab3ea1f269d8780e8e46b61378cb.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f96e794d6df48c0e13b6d04b6f73752b59e379f382c61c25729ddcc19e02cca7.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.3e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c978f5dcffb36644d1dabee28c5e694032ce098e9cda0d0f04ebd30ca35d344.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c91e463a3df9d3342bd3186869c465bb2247aa8cf0124ea3818d557745507194.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8051999ba4d3e1ddc238d309dc3191cb90673a657a70d0cb184e144942f88d35.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1152223fe5077bb7d88ba79365a37f311cbadb27be2300d5509ce4b9f184ee1f.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.41e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/55ba1699c0bd0458d8617b36818e7ed1ab5a19c49d2b08724cfaa3fbb7a41ac4.json>).
- Period 93: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db9d67c3c1c1265a28fc430f6c5afb2f6304b49bdf7c404ef74d4d89f4d285de.json>).
- Period 94: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fb2a90e6f5223e6bc424181a4b00c78b3e20b4e33c54f23bb3be4ed2bc73c618.json>).
- Period 95: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.39e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c26b862f9a7ce5c71dfb0ce1927f62919133a0682f874e9e76dcbebe218bbc8.json>).
- Period 96: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/410b1daf77503a20eda608673aa64ff45c37b7d932e118f4e97f5e7ca884af18.json>).
- Period 97: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.17e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef18cc27cca84b383f0d6c6975eb45828b2cb9eb10f15b0feee4a726e31ecc63.json>).
- Period 98: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/410b1daf77503a20eda608673aa64ff45c37b7d932e118f4e97f5e7ca884af18.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/35bb4642635a358fcfaaad5720cfce256e335ba53dd0e44d8890ab6f621d370b.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.09e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d026805bd0f2c8fc8b34b68f2931406347fb1505c5ab27e838e475cb97c887f4.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cfbbeb2ceb3913a58892fcba693e109340e1460e7c8673fc119cbc5c9abe70bd.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0e5f5fb2a1222814f103873c57310258c193d81ebbb287a17b21461429af12cb.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bafe4caafc8bca31327c2bf4052f09a6cc1188ec31634b3294c907841b5c3fb6.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e9f1301fe0c44cb4ddbf4d747dd57c497ca59ebe2ffe47cfeae028d611884197.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b95e854854d0800f7bc322299de2e7a6ba3a044aa7f2496ff2e10107dc4ec5a.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **126.333132 MW**; maximum nodal residual 4.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/16d993a342f66a533fed0c7098749decda8ff5bd47ae0715d84161f8d3157b20.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 126.333132 | 118.343621 | 7.989511 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 3.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/95ea18e691d6871eb9a65e6a1ddc6525830366da176057cf2bf0ae542e696c68.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010489 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 3.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/95ea18e691d6871eb9a65e6a1ddc6525830366da176057cf2bf0ae542e696c68.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010489 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **126.333132 MW**; maximum nodal residual 4.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/16d993a342f66a533fed0c7098749decda8ff5bd47ae0715d84161f8d3157b20.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 126.333132 | 118.343621 | 7.989511 | True |

- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b95e854854d0800f7bc322299de2e7a6ba3a044aa7f2496ff2e10107dc4ec5a.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e9f1301fe0c44cb4ddbf4d747dd57c497ca59ebe2ffe47cfeae028d611884197.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bafe4caafc8bca31327c2bf4052f09a6cc1188ec31634b3294c907841b5c3fb6.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0e5f5fb2a1222814f103873c57310258c193d81ebbb287a17b21461429af12cb.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cfbbeb2ceb3913a58892fcba693e109340e1460e7c8673fc119cbc5c9abe70bd.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.09e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d026805bd0f2c8fc8b34b68f2931406347fb1505c5ab27e838e475cb97c887f4.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/35bb4642635a358fcfaaad5720cfce256e335ba53dd0e44d8890ab6f621d370b.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,340.025 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 2,130.313646 | 0.000000 | 0.000000 | 6.799340 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.857892 | 0.000000 | 0.000000 | 7.007347 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 0.000000 | 500.000000 | 2,130.313646 | 0.000000 | 0.000000 | 6.799340 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 57.667784 | 442.332216 | 97.426008 | 0.000000 | 57.667784 | 0.248541 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000531 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 111 (day 5, h15) | 1.000 | 57.667784 | 442.332216 | 97.426008 | 0.000000 | 57.667784 | 0.248541 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 34, 35, 36, 37, 38, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 107, 111 | True |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **57.667784 MW**; maximum nodal residual 2.96e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60cef3b7db653dc33f4e58d48eb6330b422c136b167230c9ecd4f1c105fc0785.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 57.667784 | 49.678273 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **57.667784 MW**; maximum nodal residual 2.96e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/60cef3b7db653dc33f4e58d48eb6330b422c136b167230c9ecd4f1c105fc0785.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 57.667784 | 49.678273 | 7.989511 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 741,472.529 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112. At periods 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 (day 1, h10) | 83.770 | 13.408150 | 486.591850 | 4,815.473115 | 0.000000 | 0.000000 | 22.903468 | b00220:lower, b01347:lower, b02579:lower |
| 11 (day 1, h11) | 83.770 | 60.412533 | 439.587467 | 4,442.538521 | 0.000000 | 0.000000 | 20.691012 | b00220:lower, b01347:lower, b02579:lower |
| 12 (day 1, h12) | 83.770 | 89.960725 | 410.039275 | 4,208.102009 | 0.000000 | 0.000000 | 19.300203 | b00220:lower, b01347:lower, b02579:lower |
| 13 (day 1, h13) | 83.770 | 100.039063 | 399.960937 | 4,128.140098 | 0.000000 | 0.000000 | 18.825824 | b00220:lower, b01347:lower, b02579:lower |
| 14 (day 1, h14) | 83.770 | 89.960725 | 410.039275 | 4,208.102009 | 0.000000 | 0.000000 | 19.300203 | b00220:lower, b01347:lower, b02579:lower |
| 15 (day 1, h15) | 83.770 | 60.412533 | 439.587467 | 4,442.538521 | 0.000000 | 0.000000 | 20.691012 | b00220:lower, b01347:lower, b02579:lower |
| 16 (day 1, h16) | 83.770 | 13.408150 | 486.591850 | 4,815.473115 | 0.000000 | 0.000000 | 22.903468 | b00220:lower, b01347:lower, b02579:lower |
| 55 (day 3, h07) | 82.773 | 62.623353 | 437.376647 | 4,424.997787 | 0.000000 | 0.000000 | 20.341867 | b00220:lower, b01347:lower, b02579:lower |
| 56 (day 3, h08) | 82.773 | 125.000000 | 375.000000 | 3,823.207886 | 0.000000 | 0.000000 | 17.802730 | b01347:lower, b02579:lower |
| 57 (day 3, h09) | 82.773 | 163.636738 | 336.363262 | 3,241.002643 | 0.000000 | 0.000000 | 29.332228 | b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 227.432751 | 272.567249 | 2,757.954377 | 0.000000 | 0.000000 | 23.768960 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 275.990701 | 224.009299 | 2,385.128903 | 0.000000 | 0.000000 | 19.534511 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 306.542469 | 193.457531 | 2,150.909328 | 0.000000 | 0.000000 | 16.870274 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 316.963110 | 183.036890 | 2,071.021393 | 0.000000 | 0.000000 | 15.961552 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 306.542469 | 193.457531 | 2,150.909328 | 0.000000 | 0.000000 | 16.870274 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 275.990701 | 224.009299 | 2,385.128903 | 0.000000 | 0.000000 | 19.534511 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 227.432751 | 272.567249 | 2,757.954377 | 0.000000 | 0.000000 | 23.768960 | b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 163.636738 | 336.363262 | 3,241.002643 | 0.000000 | 0.000000 | 29.332228 | b01347:lower, b02579:lower |
| 66 (day 3, h18) | 82.773 | 125.000000 | 375.000000 | 3,823.207886 | 0.000000 | 0.000000 | 17.802730 | b01347:lower, b02579:lower |
| 67 (day 3, h19) | 82.773 | 62.623353 | 437.376647 | 4,424.997787 | 0.000000 | 0.000000 | 20.341867 | b00220:lower, b01347:lower, b02579:lower |
| 72 (day 4, h00) | 97.732 | 10.103080 | 489.896920 | 4,841.695665 | 0.000000 | 0.000000 | 26.902208 | b00220:lower, b01347:lower, b02579:lower |
| 73 (day 4, h01) | 97.732 | 0.024742 | 499.975258 | 4,921.657590 | 0.000000 | 0.000000 | 27.455650 | b00220:lower, b01347:lower, b02579:lower |
| 74 (day 4, h02) | 97.732 | 10.103080 | 489.896920 | 4,841.695665 | 0.000000 | 0.000000 | 26.902208 | b00220:lower, b01347:lower, b02579:lower |
| 75 (day 4, h03) | 97.732 | 39.651270 | 460.348730 | 4,607.259173 | 0.000000 | 0.000000 | 25.279598 | b00220:lower, b01347:lower, b02579:lower |
| 76 (day 4, h04) | 97.732 | 86.655655 | 413.344345 | 4,234.324571 | 0.000000 | 0.000000 | 22.698398 | b00220:lower, b01347:lower, b02579:lower |
| 77 (day 4, h05) | 97.732 | 125.000000 | 375.000000 | 3,755.253093 | 0.000000 | 0.000000 | 21.020091 | b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 172.650978 | 327.349022 | 3,171.639360 | 0.000000 | 0.000000 | 33.705093 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 252.238393 | 247.761607 | 2,567.221652 | 0.000000 | 0.000000 | 25.510472 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 331.391011 | 168.608989 | 1,960.412532 | 0.000000 | 0.000000 | 17.360619 | b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 207.130217 | 292.869783 | 1,430.850384 | 0.000000 | 0.000000 | 30.154980 | b01983:upper, b02579:lower |
| 82 (day 4, h10) | 97.732 | 298.054986 | 201.945014 | 1,097.010284 | 0.000000 | 0.000000 | 20.793022 | b01983:upper, b02579:lower |
| 83 (day 4, h11) | 97.732 | 369.001733 | 130.998267 | 847.323176 | 0.000000 | 0.000000 | 13.488077 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 375.000000 | 125.000000 | 689.568973 | 0.000000 | 0.000000 | 20.534947 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 375.000000 | 125.000000 | 636.166707 | 0.000000 | 0.000000 | 20.534947 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 375.000000 | 125.000000 | 689.568973 | 0.000000 | 0.000000 | 20.534947 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 369.001733 | 130.998267 | 847.323176 | 0.000000 | 0.000000 | 13.488077 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 298.054986 | 201.945014 | 1,097.010284 | 0.000000 | 0.000000 | 20.793022 | b01983:upper, b02579:lower |
| 89 (day 4, h17) | 97.732 | 207.130217 | 292.869783 | 1,430.850384 | 0.000000 | 0.000000 | 30.154980 | b01983:upper, b02579:lower |
| 90 (day 4, h18) | 97.732 | 331.391011 | 168.608989 | 1,960.412532 | 0.000000 | 0.000000 | 17.360619 | b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 252.238393 | 247.761607 | 2,567.221652 | 0.000000 | 0.000000 | 25.510472 | b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 172.650978 | 327.349022 | 3,171.639360 | 0.000000 | 0.000000 | 33.705093 | b01347:lower, b02579:lower |
| 93 (day 4, h21) | 97.732 | 125.000000 | 375.000000 | 3,755.253093 | 0.000000 | 0.000000 | 21.020091 | b01347:lower, b02579:lower |
| 94 (day 4, h22) | 97.732 | 86.655655 | 413.344345 | 4,234.324571 | 0.000000 | 0.000000 | 22.698398 | b00220:lower, b01347:lower, b02579:lower |
| 95 (day 4, h23) | 97.732 | 39.651270 | 460.348730 | 4,607.259173 | 0.000000 | 0.000000 | 25.279598 | b00220:lower, b01347:lower, b02579:lower |
| 96 (day 5, h00) | 1.000 | 125.000000 | 375.000000 | 3,632.714083 | 0.000000 | 0.000000 | 0.215080 | b01347:lower, b02579:lower |
| 97 (day 5, h01) | 1.000 | 125.000000 | 375.000000 | 3,711.101263 | 0.000000 | 0.000000 | 0.215080 | b01347:lower, b02579:lower |
| 98 (day 5, h02) | 1.000 | 125.000000 | 375.000000 | 3,632.714083 | 0.000000 | 0.000000 | 0.215080 | b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 145.792558 | 354.207442 | 3,378.310980 | 0.000000 | 0.000000 | 0.373171 | b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 194.288300 | 305.711700 | 3,005.143358 | 0.000000 | 0.000000 | 0.322079 | b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 258.107848 | 241.892152 | 2,522.224527 | 0.000000 | 0.000000 | 0.254842 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 331.866346 | 168.133654 | 1,956.768468 | 0.000000 | 0.000000 | 0.177135 | b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 215.556124 | 284.443876 | 1,399.913743 | 0.000000 | 0.000000 | 0.299672 | b01983:upper, b02579:lower |
| 104 (day 5, h08) | 1.000 | 329.183808 | 170.816192 | 982.717485 | 0.000000 | 0.000000 | 0.179961 | b01983:upper, b02579:lower |
| 105 (day 5, h09) | 1.000 | 375.000000 | 125.000000 | 606.362229 | 0.000000 | 0.000000 | 0.210140 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 432.060569 | 67.939431 | 305.985556 | 0.000000 | 126.333132 | 0.119295 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 97.426008 | 402.573992 | 499.999999 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 97.426008 | 402.573992 | 499.999999 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 432.060569 | 67.939431 | 305.985556 | 0.000000 | 126.333132 | 0.119295 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 375.000000 | 125.000000 | 606.362229 | 0.000000 | 0.000000 | 0.210140 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 329.183808 | 170.816192 | 982.717485 | 0.000000 | 0.000000 | 0.179961 | b01983:upper, b02579:lower |
| 115 (day 5, h19) | 1.000 | 215.556124 | 284.443876 | 1,399.913743 | 0.000000 | 0.000000 | 0.299672 | b01983:upper, b02579:lower |
| 116 (day 5, h20) | 1.000 | 331.866346 | 168.133654 | 1,956.768468 | 0.000000 | 0.000000 | 0.177135 | b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 258.107848 | 241.892152 | 2,522.224527 | 0.000000 | 0.000000 | 0.254842 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 194.288300 | 305.711700 | 3,005.143358 | 0.000000 | 0.000000 | 0.322079 | b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 145.792558 | 354.207442 | 3,378.310980 | 0.000000 | 0.000000 | 0.373171 | b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 94, 95 | 10, 11, 12, 13, 14, 15, 16, 55, 67, 72, 73, 74, 75, 76, 94, 95 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | 81, 82, 88, 89, 103, 104, 114, 115 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 10, 11, 12, 13, 14, 15, 16, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 10: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/405b6403916569891bb43c3b502114201bfc9e4b9ba88afb0f874cd2696ede0d.json>).
- Period 11: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27632c01fa046ccc5c83eb642a864e96fa83cddb0b08d42c4879e2f77fc5e40a.json>).
- Period 12: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6d10e2b20f7e989671950b9550af52f4fcb1ee436733bc0c1d1106f12bb62fa7.json>).
- Period 13: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.12e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cf64fecb3704491cf0d61df040b2ad085c90fa8795e2d3fc68ee0b0b1d832592.json>).
- Period 14: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.18e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6d10e2b20f7e989671950b9550af52f4fcb1ee436733bc0c1d1106f12bb62fa7.json>).
- Period 15: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27632c01fa046ccc5c83eb642a864e96fa83cddb0b08d42c4879e2f77fc5e40a.json>).
- Period 16: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/405b6403916569891bb43c3b502114201bfc9e4b9ba88afb0f874cd2696ede0d.json>).
- Period 55: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3e775eb2ec97f5cbefa17db4f96fff5f3c8c5ccf16ef8b550b404d9562ee9561.json>).
- Period 56: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3d86193e7cada0218860c83d0ea8df09a2ec2a7a94022c4ba41b7f74f9e92911.json>).
- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.94e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b56cdc26c5c605900bd19c7e2d98c4eece9b2e49ad8a199b4a6096db7439cff8.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7ece4c944b0a50748f885c06cd8a917f9aed76c09ff7788d7a9e302d7d18613.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b3ffd34618e8412628347a50f61ac383c294b8ef3e235ad0f8389b3bca647daa.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f47eaeedfb34e5b8455fbd77ae1b9b14a590bf95de6402a9752b4b338ebe7d3.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.7e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0934e4e0ac0d81479eeadcfa7dedbd0754679247553ff2e91359a68f4c226d0a.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1f47eaeedfb34e5b8455fbd77ae1b9b14a590bf95de6402a9752b4b338ebe7d3.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b3ffd34618e8412628347a50f61ac383c294b8ef3e235ad0f8389b3bca647daa.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.46e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7ece4c944b0a50748f885c06cd8a917f9aed76c09ff7788d7a9e302d7d18613.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.94e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b56cdc26c5c605900bd19c7e2d98c4eece9b2e49ad8a199b4a6096db7439cff8.json>).
- Period 66: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.22e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3d86193e7cada0218860c83d0ea8df09a2ec2a7a94022c4ba41b7f74f9e92911.json>).
- Period 67: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3e775eb2ec97f5cbefa17db4f96fff5f3c8c5ccf16ef8b550b404d9562ee9561.json>).
- Period 72: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0ac881f7e8f271ed606e95419aa3696b0b2f4673c68e9ff39959d69051d2a553.json>).
- Period 73: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.21e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5e75503636dbbd7fda9c329333870044ae1754cc9010d9be1f155f2879d4895d.json>).
- Period 74: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.31e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0ac881f7e8f271ed606e95419aa3696b0b2f4673c68e9ff39959d69051d2a553.json>).
- Period 75: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.39e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c26b862f9a7ce5c71dfb0ce1927f62919133a0682f874e9e76dcbebe218bbc8.json>).
- Period 76: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fb2a90e6f5223e6bc424181a4b00c78b3e20b4e33c54f23bb3be4ed2bc73c618.json>).
- Period 77: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db9d67c3c1c1265a28fc430f6c5afb2f6304b49bdf7c404ef74d4d89f4d285de.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.41e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/55ba1699c0bd0458d8617b36818e7ed1ab5a19c49d2b08724cfaa3fbb7a41ac4.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1152223fe5077bb7d88ba79365a37f311cbadb27be2300d5509ce4b9f184ee1f.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8051999ba4d3e1ddc238d309dc3191cb90673a657a70d0cb184e144942f88d35.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c91e463a3df9d3342bd3186869c465bb2247aa8cf0124ea3818d557745507194.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.3e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c978f5dcffb36644d1dabee28c5e694032ce098e9cda0d0f04ebd30ca35d344.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f96e794d6df48c0e13b6d04b6f73752b59e379f382c61c25729ddcc19e02cca7.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d845cde236409fe23fd746cc5826fd657798ab3ea1f269d8780e8e46b61378cb.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2b375f1aebc51c3656bb7a772ad0c43907ace91ec6c815ed202e9ab16f5ab502.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d845cde236409fe23fd746cc5826fd657798ab3ea1f269d8780e8e46b61378cb.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.54e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f96e794d6df48c0e13b6d04b6f73752b59e379f382c61c25729ddcc19e02cca7.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.3e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c978f5dcffb36644d1dabee28c5e694032ce098e9cda0d0f04ebd30ca35d344.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c91e463a3df9d3342bd3186869c465bb2247aa8cf0124ea3818d557745507194.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8051999ba4d3e1ddc238d309dc3191cb90673a657a70d0cb184e144942f88d35.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.78e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1152223fe5077bb7d88ba79365a37f311cbadb27be2300d5509ce4b9f184ee1f.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.41e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/55ba1699c0bd0458d8617b36818e7ed1ab5a19c49d2b08724cfaa3fbb7a41ac4.json>).
- Period 93: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/db9d67c3c1c1265a28fc430f6c5afb2f6304b49bdf7c404ef74d4d89f4d285de.json>).
- Period 94: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.52e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fb2a90e6f5223e6bc424181a4b00c78b3e20b4e33c54f23bb3be4ed2bc73c618.json>).
- Period 95: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.39e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4c26b862f9a7ce5c71dfb0ce1927f62919133a0682f874e9e76dcbebe218bbc8.json>).
- Period 96: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/410b1daf77503a20eda608673aa64ff45c37b7d932e118f4e97f5e7ca884af18.json>).
- Period 97: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.17e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef18cc27cca84b383f0d6c6975eb45828b2cb9eb10f15b0feee4a726e31ecc63.json>).
- Period 98: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.43e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/410b1daf77503a20eda608673aa64ff45c37b7d932e118f4e97f5e7ca884af18.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/35bb4642635a358fcfaaad5720cfce256e335ba53dd0e44d8890ab6f621d370b.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.09e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d026805bd0f2c8fc8b34b68f2931406347fb1505c5ab27e838e475cb97c887f4.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cfbbeb2ceb3913a58892fcba693e109340e1460e7c8673fc119cbc5c9abe70bd.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0e5f5fb2a1222814f103873c57310258c193d81ebbb287a17b21461429af12cb.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bafe4caafc8bca31327c2bf4052f09a6cc1188ec31634b3294c907841b5c3fb6.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e9f1301fe0c44cb4ddbf4d747dd57c497ca59ebe2ffe47cfeae028d611884197.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b95e854854d0800f7bc322299de2e7a6ba3a044aa7f2496ff2e10107dc4ec5a.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **126.333132 MW**; maximum nodal residual 4.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/16d993a342f66a533fed0c7098749decda8ff5bd47ae0715d84161f8d3157b20.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 126.333132 | 118.343621 | 7.989511 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 3.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/95ea18e691d6871eb9a65e6a1ddc6525830366da176057cf2bf0ae542e696c68.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010489 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 3.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/95ea18e691d6871eb9a65e6a1ddc6525830366da176057cf2bf0ae542e696c68.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010489 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **126.333132 MW**; maximum nodal residual 4.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/16d993a342f66a533fed0c7098749decda8ff5bd47ae0715d84161f8d3157b20.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 126.333132 | 118.343621 | 7.989511 | True |

- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.1e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b95e854854d0800f7bc322299de2e7a6ba3a044aa7f2496ff2e10107dc4ec5a.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e9f1301fe0c44cb4ddbf4d747dd57c497ca59ebe2ffe47cfeae028d611884197.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bafe4caafc8bca31327c2bf4052f09a6cc1188ec31634b3294c907841b5c3fb6.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0e5f5fb2a1222814f103873c57310258c193d81ebbb287a17b21461429af12cb.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cfbbeb2ceb3913a58892fcba693e109340e1460e7c8673fc119cbc5c9abe70bd.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.09e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d026805bd0f2c8fc8b34b68f2931406347fb1505c5ab27e838e475cb97c887f4.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/35bb4642635a358fcfaaad5720cfce256e335ba53dd0e44d8890ab6f621d370b.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `a6bd3e9ae0f43828f4af82b61295aa05e50af9bd437ac8e288024766c902a1be`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
