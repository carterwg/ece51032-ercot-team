<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_C_eq_G_S2_500_1079","policy":"G_eq_0_S1_C_eq_G_S2","portfolio":"hosting_1_s2_cg","buses":["1079"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"8707dbdb7f995096abec05ac584f5fd5346317d9d106636d6f1e44a505c42de0","score_usd":54302629310.57262,"it_value_usd":98741559374.82913,"grid_mwh":13069130.644706823,"generation_mwh":989445.9944863651,"modeled_generator_hours":114.0,"annual_generator_hours":6085.413698628793,"required_annual_hours":10.000000000095394,"minimum_admission":0.6048603469402027,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/8707dbdb7f995096abec05ac584f5fd5346317d9d106636d6f1e44a505c42de0-3eea05334a1d.json"} -->
# G_eq_0_S1_C_eq_G_S2_500_1079 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 302.430173 | 302.430173 | 18.607493 | 11.046738 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430173 | 30.763287 | 16.899418 |
| week-3-submission-1 | 500.000 | 0.000 | 302.430173 | 302.430173 | 18.607493 | 10.708734 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430173 | 30.763287 | 15.647739 |
| Campaign total | — | — | — | — | 98.741559 | 54.302629 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,649,288.320 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 3,885,277.003 | 494,722.997 | 88.704954% | 57.000 | 3,042.707 | 5.000 | 0.000 | 499.945007 |
| week-3-submission-1 | 2,649,288.320 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 3,885,277.003 | 494,722.997 | 88.704954% | 57.000 | 3,042.707 | 5.000 | 0.000 | 499.945007 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.363869 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.338005 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-3-submission-2 | 1.251679 | 0.363869 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_C_eq_G_S2`.
- Layout: 1079: 500 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430173 MW** (60.486035%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267366 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430173 | 0.302460 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **302.732634 MW**; maximum nodal residual 5.65e-09 MW. Generation-only capacity ceiling = 302.732634 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/ea47872d79f7610f3d9f773f4158e7cb5ea16cf7bcfb78b0cb76b810951f513d.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 494,722.997 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 (day 1, h12) | 83.770 | 26.545286 | 473.454714 | 4,208.102009 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 13 (day 1, h13) | 83.770 | 36.623625 | 463.376375 | 4,128.140098 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 14 (day 1, h14) | 83.770 | 26.545286 | 473.454714 | 4,208.102009 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 56 (day 3, h08) | 82.773 | 76.350801 | 423.649199 | 3,820.900681 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 57 (day 3, h09) | 82.773 | 125.000000 | 375.000000 | 3,258.465662 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 137.278851 | 362.721149 | 2,762.107929 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 185.860324 | 314.139676 | 2,389.411828 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 216.412092 | 283.587908 | 2,155.192253 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 226.832733 | 273.167267 | 2,075.304318 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 216.412092 | 283.587908 | 2,155.192253 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 185.860324 | 314.139676 | 2,389.411828 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 137.278851 | 362.721149 | 2,762.107929 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 125.000000 | 375.000000 | 3,258.465662 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 66 (day 3, h18) | 82.773 | 76.350801 | 423.649199 | 3,820.900681 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 76 (day 4, h04) | 97.732 | 23.240216 | 476.759784 | 4,234.324571 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 77 (day 4, h05) | 97.732 | 85.087835 | 414.912165 | 3,751.580739 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 125.000000 | 375.000000 | 3,190.510842 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 162.108015 | 337.891985 | 2,571.504577 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 241.260634 | 258.739366 | 1,964.695457 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 1,427.199985 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 82 (day 4, h10) | 97.732 | 206.134998 | 293.865002 | 1,091.450347 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 83 (day 4, h11) | 97.732 | 276.764794 | 223.235206 | 840.020013 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 323.592538 | 176.407462 | 695.318282 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 339.564606 | 160.435394 | 645.963225 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 323.592538 | 176.407462 | 695.318282 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 276.764794 | 223.235206 | 840.020013 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 206.134998 | 293.865002 | 1,091.450347 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 1,427.199985 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 90 (day 4, h18) | 97.732 | 241.260634 | 258.739366 | 1,964.695457 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 162.108015 | 337.891985 | 2,571.504577 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 125.000000 | 375.000000 | 3,190.510842 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 93 (day 4, h21) | 97.732 | 85.087835 | 414.912165 | 3,751.580739 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 94 (day 4, h22) | 97.732 | 23.240216 | 476.759784 | 4,234.324571 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 96 (day 5, h00) | 1.000 | 100.842825 | 399.157175 | 3,626.580033 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 97 (day 5, h01) | 1.000 | 90.764488 | 409.235512 | 3,706.541939 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 98 (day 5, h02) | 1.000 | 100.842825 | 399.157175 | 3,626.580033 | 0.000000 | 0.000000 | 0.000000 | b00220:lower, b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 125.000000 | 375.000000 | 3,392.985870 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 125.000000 | 375.000000 | 3,025.069876 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 167.977471 | 332.022529 | 2,526.507452 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 241.735969 | 258.264031 | 1,961.051393 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 1,394.619834 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 104 (day 5, h08) | 1.000 | 237.263819 | 262.736181 | 977.157548 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 105 (day 5, h09) | 1.000 | 348.560922 | 151.439078 | 618.163830 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 375.000000 | 125.000000 | 307.450881 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 418.372873 | 81.627127 | 90.809027 | 0.000000 | 51.050804 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 474.999289 | 25.000711 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.945007 | 0.054993 | -0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 474.999289 | 25.000711 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 418.372873 | 81.627127 | 90.809027 | 0.000000 | 51.050804 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 375.000000 | 125.000000 | 307.450881 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 348.560922 | 151.439078 | 618.163830 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 237.263819 | 262.736181 | 977.157548 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 1,394.619834 | 0.000000 | 0.000000 | 0.000000 | b01983:upper, b02579:lower |
| 116 (day 5, h20) | 1.000 | 241.735969 | 258.264031 | 1,961.051393 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 167.977471 | 332.022529 | 2,526.507452 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 125.000000 | 375.000000 | 3,025.069876 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 125.000000 | 375.000000 | 3,392.985870 | 0.000000 | 0.000000 | 0.000000 | b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 93, 94, 95, 96, 97, 98 | 12, 13, 14, 56, 66, 76, 77, 93, 94, 96, 97, 98 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | 81, 82, 88, 89, 103, 104, 114, 115 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 12: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9f4fdbaefc11bfbcee84f507bc7cba8ff46252c02223dfb31d596360bb574d0c.json>).
- Period 13: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/74ca01c190ffe05f5f5c6b045fa878caad829c703c9fd24549fecc540a196f7f.json>).
- Period 14: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9f4fdbaefc11bfbcee84f507bc7cba8ff46252c02223dfb31d596360bb574d0c.json>).
- Period 56: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef9c74d9c400d9ca3d5af47a575b9c7ac650642a042bab038a77371c9e9e2d84.json>).
- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/face15a4e3182a1fb59e69fee1cce89fcdb1951730bd9bc49f4369d034a48c72.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/208c420b4d5006a5370eb02699dc4a7c45109d48803d45a13bf4a18c34a1337f.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/495c53cecda98e1f1ce8b339db0cf1a87aac8f3a297fea8f8ad1b6d09a3ba8aa.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1dafe12776eaa086ce2c88da215fb8c03232ce7c7af89787bb0f286ed1e59fba.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d737520933329b6e0284599446f5b44837425debea02f20d096055ab2afe02e5.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1dafe12776eaa086ce2c88da215fb8c03232ce7c7af89787bb0f286ed1e59fba.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/495c53cecda98e1f1ce8b339db0cf1a87aac8f3a297fea8f8ad1b6d09a3ba8aa.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/208c420b4d5006a5370eb02699dc4a7c45109d48803d45a13bf4a18c34a1337f.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/face15a4e3182a1fb59e69fee1cce89fcdb1951730bd9bc49f4369d034a48c72.json>).
- Period 66: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef9c74d9c400d9ca3d5af47a575b9c7ac650642a042bab038a77371c9e9e2d84.json>).
- Period 76: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fd56e99428b05c84c5d99ad76adb26e69f29b9eb13f6d4a17e88e56450497aee.json>).
- Period 77: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce769871d645f109c0d50ea7dcdcd20badcd8eedf65652fba2d3006abbac6df7.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c63a93610c199a400f45fd02a92f15731aeab44dc21be33375a2596e180570b.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6fdfcbf85b2e4cab6e2dcb7780fbc9059902a4f709c6cade48fdd8025ae8063.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.9e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4ee936b2f3cb12c202b04239aca447d74a263596829e060aeac3e363e69a6cbc.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.81e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/80fba4c2cdd97946c35cd63f7c840312cc5da07fadb2d768e63873d6dee42e2b.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bd76e0c3cc12dea06b369d2aa2b7aee141eed1141094f31b4628b0ddc9fdbcb5.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.08e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27dedd66ac27f42bf2440cd73a0d67eb8d358ea50b35f3af8a68e3d75fa79803.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d5c66dd1181c0f6a16056b0cbba7797f16f2672937191ad2ae650f120c3f28b.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bf1078f340b6f5d29c498cd5d6d813e0fddb8ac9f292dcf8fd74b62c99018f34.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d5c66dd1181c0f6a16056b0cbba7797f16f2672937191ad2ae650f120c3f28b.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.08e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27dedd66ac27f42bf2440cd73a0d67eb8d358ea50b35f3af8a68e3d75fa79803.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bd76e0c3cc12dea06b369d2aa2b7aee141eed1141094f31b4628b0ddc9fdbcb5.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.81e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/80fba4c2cdd97946c35cd63f7c840312cc5da07fadb2d768e63873d6dee42e2b.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.9e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4ee936b2f3cb12c202b04239aca447d74a263596829e060aeac3e363e69a6cbc.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6fdfcbf85b2e4cab6e2dcb7780fbc9059902a4f709c6cade48fdd8025ae8063.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c63a93610c199a400f45fd02a92f15731aeab44dc21be33375a2596e180570b.json>).
- Period 93: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce769871d645f109c0d50ea7dcdcd20badcd8eedf65652fba2d3006abbac6df7.json>).
- Period 94: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fd56e99428b05c84c5d99ad76adb26e69f29b9eb13f6d4a17e88e56450497aee.json>).
- Period 96: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a8c5d253412b4d2acd5aed9fe9661b9609e5f41a52e98b9a2a14e31d82b2a923.json>).
- Period 97: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/234de463df3e13347d736c50e947d4b7535281c538260e23b3755dcee2d6b27b.json>).
- Period 98: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a8c5d253412b4d2acd5aed9fe9661b9609e5f41a52e98b9a2a14e31d82b2a923.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.43e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2f37fa94c428eda153a9024ae1309fa34e5f5d01fcbfadda2d75dec181bdc629.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1051bc7c308793a60cd91aae2ae05438acc2e41be1d910b1f055aa5847044a93.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/203acb3d99f257ff3b49efcb78ddeadc92b39999207816ab5a940192ef33633d.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2e626113e66bd63a757340bcd9c083c2a1df8f6f5edd905f43646938132747a.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/046c154268cdef569290ab4e453100e486671c08389a8f56d8babe33c575ee45.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.89e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7c0fd89cde9cec6ed2f5e9586c3d820669a2b3d3ccb0eaa39d8803d6aa53b86.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e57c6d6154954d7d151394de6b5e25e390bd3e061f50fe5a4c28b77d9d577de.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/454ff3e458d8935c2e36b354f325d7d29421a83cf6cf9d0352c40f44ce533c30.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **51.050804 MW**; maximum nodal residual 4.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a97760360e2fc9937c26d7def1e9d270ee9c521f0e7dda168b7d54491ef638d0.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 51.050804 | 43.061293 | 7.989511 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a099446e79783e968050f9a1222d68a15578513d1e4dba693ff79090a2454d3.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.697540 MW**; maximum nodal residual 3.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b07b9ba17bc94bdbc2caeea311b8a07be0b593dadf49ad6cf44dd3713d71b96.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a099446e79783e968050f9a1222d68a15578513d1e4dba693ff79090a2454d3.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **51.050804 MW**; maximum nodal residual 4.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a97760360e2fc9937c26d7def1e9d270ee9c521f0e7dda168b7d54491ef638d0.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 51.050804 | 43.061293 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/454ff3e458d8935c2e36b354f325d7d29421a83cf6cf9d0352c40f44ce533c30.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e57c6d6154954d7d151394de6b5e25e390bd3e061f50fe5a4c28b77d9d577de.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.89e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7c0fd89cde9cec6ed2f5e9586c3d820669a2b3d3ccb0eaa39d8803d6aa53b86.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/046c154268cdef569290ab4e453100e486671c08389a8f56d8babe33c575ee45.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2e626113e66bd63a757340bcd9c083c2a1df8f6f5edd905f43646938132747a.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/203acb3d99f257ff3b49efcb78ddeadc92b39999207816ab5a940192ef33633d.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1051bc7c308793a60cd91aae2ae05438acc2e41be1d910b1f055aa5847044a93.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.43e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2f37fa94c428eda153a9024ae1309fa34e5f5d01fcbfadda2d75dec181bdc629.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430173 MW** (60.486035%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267366 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 302.430173 | 2,228.059324 | 0.000000 | 0.000000 | 4.073197 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 302.430173 | 2,090.857892 | 0.000000 | 0.000000 | 4.073197 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 302.430173 | 2,228.059324 | 0.000000 | 0.000000 | 4.073197 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430173 | 0.302460 | 0.000000 | 0.000000 | 0.061781 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **302.732634 MW**; maximum nodal residual 5.65e-09 MW. Generation-only capacity ceiling = 302.732634 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/ea47872d79f7610f3d9f773f4158e7cb5ea16cf7bcfb78b0cb76b810951f513d.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119; represented annual output was 494,722.997 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 (day 1, h12) | 83.770 | 26.545286 | 473.454714 | 4,208.102009 | 0.000000 | 0.000000 | 22.285114 | b00220:lower, b01347:lower, b02579:lower |
| 13 (day 1, h13) | 83.770 | 36.623625 | 463.376375 | 4,128.140098 | 0.000000 | 0.000000 | 21.810735 | b00220:lower, b01347:lower, b02579:lower |
| 14 (day 1, h14) | 83.770 | 26.545286 | 473.454714 | 4,208.102009 | 0.000000 | 0.000000 | 22.285114 | b00220:lower, b01347:lower, b02579:lower |
| 56 (day 3, h08) | 82.773 | 76.350801 | 423.649199 | 3,820.900681 | 0.000000 | 0.000000 | 19.703420 | b00220:lower, b01347:lower, b02579:lower |
| 57 (day 3, h09) | 82.773 | 125.000000 | 375.000000 | 3,258.465662 | 0.000000 | 0.000000 | 17.802730 | b01347:lower, b02579:lower |
| 58 (day 3, h10) | 82.773 | 137.278851 | 362.721149 | 2,762.107929 | 0.000000 | 0.000000 | 31.630742 | b01347:lower, b02579:lower |
| 59 (day 3, h11) | 82.773 | 185.860324 | 314.139676 | 2,389.411828 | 0.000000 | 0.000000 | 27.394242 | b01347:lower, b02579:lower |
| 60 (day 3, h12) | 82.773 | 216.412092 | 283.587908 | 2,155.192253 | 0.000000 | 0.000000 | 24.730005 | b01347:lower, b02579:lower |
| 61 (day 3, h13) | 82.773 | 226.832733 | 273.167267 | 2,075.304318 | 0.000000 | 0.000000 | 23.821283 | b01347:lower, b02579:lower |
| 62 (day 3, h14) | 82.773 | 216.412092 | 283.587908 | 2,155.192253 | 0.000000 | 0.000000 | 24.730005 | b01347:lower, b02579:lower |
| 63 (day 3, h15) | 82.773 | 185.860324 | 314.139676 | 2,389.411828 | 0.000000 | 0.000000 | 27.394242 | b01347:lower, b02579:lower |
| 64 (day 3, h16) | 82.773 | 137.278851 | 362.721149 | 2,762.107929 | 0.000000 | 0.000000 | 31.630742 | b01347:lower, b02579:lower |
| 65 (day 3, h17) | 82.773 | 125.000000 | 375.000000 | 3,258.465662 | 0.000000 | 0.000000 | 17.802730 | b01347:lower, b02579:lower |
| 66 (day 3, h18) | 82.773 | 76.350801 | 423.649199 | 3,820.900681 | 0.000000 | 0.000000 | 19.703420 | b00220:lower, b01347:lower, b02579:lower |
| 76 (day 4, h04) | 97.732 | 23.240216 | 476.759784 | 4,234.324571 | 0.000000 | 0.000000 | 26.180795 | b00220:lower, b01347:lower, b02579:lower |
| 77 (day 4, h05) | 97.732 | 85.087835 | 414.912165 | 3,751.580739 | 0.000000 | 0.000000 | 22.784493 | b00220:lower, b01347:lower, b02579:lower |
| 78 (day 4, h06) | 97.732 | 125.000000 | 375.000000 | 3,190.510842 | 0.000000 | 0.000000 | 21.020091 | b01347:lower, b02579:lower |
| 79 (day 4, h07) | 97.732 | 162.108015 | 337.891985 | 2,571.504577 | 0.000000 | 0.000000 | 34.790636 | b01347:lower, b02579:lower |
| 80 (day 4, h08) | 97.732 | 241.260634 | 258.739366 | 1,964.695457 | 0.000000 | 0.000000 | 26.640783 | b01347:lower, b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 1,427.199985 | 0.000000 | 0.000000 | 37.412292 | b01983:upper, b02579:lower |
| 82 (day 4, h10) | 97.732 | 206.134998 | 293.865002 | 1,091.450347 | 0.000000 | 0.000000 | 30.257452 | b01983:upper, b02579:lower |
| 83 (day 4, h11) | 97.732 | 276.764794 | 223.235206 | 840.020013 | 0.000000 | 0.000000 | 22.985141 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 323.592538 | 176.407462 | 695.318282 | 0.000000 | 0.000000 | 18.163579 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 339.564606 | 160.435394 | 645.963225 | 0.000000 | 0.000000 | 16.519035 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 323.592538 | 176.407462 | 695.318282 | 0.000000 | 0.000000 | 18.163579 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 276.764794 | 223.235206 | 840.020013 | 0.000000 | 0.000000 | 22.985141 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 206.134998 | 293.865002 | 1,091.450347 | 0.000000 | 0.000000 | 30.257452 | b01983:upper, b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 1,427.199985 | 0.000000 | 0.000000 | 37.412292 | b01983:upper, b02579:lower |
| 90 (day 4, h18) | 97.732 | 241.260634 | 258.739366 | 1,964.695457 | 0.000000 | 0.000000 | 26.640783 | b01347:lower, b02579:lower |
| 91 (day 4, h19) | 97.732 | 162.108015 | 337.891985 | 2,571.504577 | 0.000000 | 0.000000 | 34.790636 | b01347:lower, b02579:lower |
| 92 (day 4, h20) | 97.732 | 125.000000 | 375.000000 | 3,190.510842 | 0.000000 | 0.000000 | 21.020091 | b01347:lower, b02579:lower |
| 93 (day 4, h21) | 97.732 | 85.087835 | 414.912165 | 3,751.580739 | 0.000000 | 0.000000 | 22.784493 | b00220:lower, b01347:lower, b02579:lower |
| 94 (day 4, h22) | 97.732 | 23.240216 | 476.759784 | 4,234.324571 | 0.000000 | 0.000000 | 26.180795 | b00220:lower, b01347:lower, b02579:lower |
| 96 (day 5, h00) | 1.000 | 100.842825 | 399.157175 | 3,626.580033 | 0.000000 | 0.000000 | 0.224281 | b00220:lower, b01347:lower, b02579:lower |
| 97 (day 5, h01) | 1.000 | 90.764488 | 409.235512 | 3,706.541939 | 0.000000 | 0.000000 | 0.229944 | b00220:lower, b01347:lower, b02579:lower |
| 98 (day 5, h02) | 1.000 | 100.842825 | 399.157175 | 3,626.580033 | 0.000000 | 0.000000 | 0.224281 | b00220:lower, b01347:lower, b02579:lower |
| 99 (day 5, h03) | 1.000 | 125.000000 | 375.000000 | 3,392.985870 | 0.000000 | 0.000000 | 0.215080 | b01347:lower, b02579:lower |
| 100 (day 5, h04) | 1.000 | 125.000000 | 375.000000 | 3,025.069876 | 0.000000 | 0.000000 | 0.215047 | b01347:lower, b02579:lower |
| 101 (day 5, h05) | 1.000 | 167.977471 | 332.022529 | 2,526.507452 | 0.000000 | 0.000000 | 0.349798 | b01347:lower, b02579:lower |
| 102 (day 5, h06) | 1.000 | 241.735969 | 258.264031 | 1,961.051393 | 0.000000 | 0.000000 | 0.272091 | b01347:lower, b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 1,394.619834 | 0.000000 | 0.000000 | 0.382807 | b01983:upper, b02579:lower |
| 104 (day 5, h08) | 1.000 | 237.263819 | 262.736181 | 977.157548 | 0.000000 | 0.000000 | 0.276802 | b01983:upper, b02579:lower |
| 105 (day 5, h09) | 1.000 | 348.560922 | 151.439078 | 618.163830 | 0.000000 | 0.000000 | 0.159547 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 375.000000 | 125.000000 | 307.450881 | 0.000000 | 0.000000 | 0.210924 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 418.372873 | 81.627127 | 90.809027 | 0.000000 | 51.050804 | 0.143329 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 474.999289 | 25.000711 | -0.000000 | 362.496087 | 362.496087 | 0.043899 | none |
| 109 (day 5, h13) | 1.000 | 499.945007 | 0.054993 | -0.000000 | 499.697540 | 499.697540 | 0.000097 | none |
| 110 (day 5, h14) | 1.000 | 474.999289 | 25.000711 | -0.000000 | 362.496087 | 362.496087 | 0.043899 | none |
| 111 (day 5, h15) | 1.000 | 418.372873 | 81.627127 | 90.809027 | 0.000000 | 51.050804 | 0.143329 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 375.000000 | 125.000000 | 307.450881 | 0.000000 | 0.000000 | 0.210924 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 348.560922 | 151.439078 | 618.163830 | 0.000000 | 0.000000 | 0.159547 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 237.263819 | 262.736181 | 977.157548 | 0.000000 | 0.000000 | 0.276802 | b01983:upper, b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 1,394.619834 | 0.000000 | 0.000000 | 0.382807 | b01983:upper, b02579:lower |
| 116 (day 5, h20) | 1.000 | 241.735969 | 258.264031 | 1,961.051393 | 0.000000 | 0.000000 | 0.272091 | b01347:lower, b02579:lower |
| 117 (day 5, h21) | 1.000 | 167.977471 | 332.022529 | 2,526.507452 | 0.000000 | 0.000000 | 0.349798 | b01347:lower, b02579:lower |
| 118 (day 5, h22) | 1.000 | 125.000000 | 375.000000 | 3,025.069876 | 0.000000 | 0.000000 | 0.215047 | b01347:lower, b02579:lower |
| 119 (day 5, h23) | 1.000 | 125.000000 | 375.000000 | 3,392.985870 | 0.000000 | 0.000000 | 0.215080 | b01347:lower, b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 93, 94, 95, 96, 97, 98 | 12, 13, 14, 56, 66, 76, 77, 93, 94, 96, 97, 98 | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | 81, 82, 88, 89, 103, 104, 114, 115 | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 12, 13, 14, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | True |

### Snapshot counterfactuals for this round

- Period 12: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9f4fdbaefc11bfbcee84f507bc7cba8ff46252c02223dfb31d596360bb574d0c.json>).
- Period 13: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/74ca01c190ffe05f5f5c6b045fa878caad829c703c9fd24549fecc540a196f7f.json>).
- Period 14: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9f4fdbaefc11bfbcee84f507bc7cba8ff46252c02223dfb31d596360bb574d0c.json>).
- Period 56: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef9c74d9c400d9ca3d5af47a575b9c7ac650642a042bab038a77371c9e9e2d84.json>).
- Period 57: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/face15a4e3182a1fb59e69fee1cce89fcdb1951730bd9bc49f4369d034a48c72.json>).
- Period 58: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/208c420b4d5006a5370eb02699dc4a7c45109d48803d45a13bf4a18c34a1337f.json>).
- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/495c53cecda98e1f1ce8b339db0cf1a87aac8f3a297fea8f8ad1b6d09a3ba8aa.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1dafe12776eaa086ce2c88da215fb8c03232ce7c7af89787bb0f286ed1e59fba.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d737520933329b6e0284599446f5b44837425debea02f20d096055ab2afe02e5.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1dafe12776eaa086ce2c88da215fb8c03232ce7c7af89787bb0f286ed1e59fba.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/495c53cecda98e1f1ce8b339db0cf1a87aac8f3a297fea8f8ad1b6d09a3ba8aa.json>).
- Period 64: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/208c420b4d5006a5370eb02699dc4a7c45109d48803d45a13bf4a18c34a1337f.json>).
- Period 65: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/face15a4e3182a1fb59e69fee1cce89fcdb1951730bd9bc49f4369d034a48c72.json>).
- Period 66: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef9c74d9c400d9ca3d5af47a575b9c7ac650642a042bab038a77371c9e9e2d84.json>).
- Period 76: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fd56e99428b05c84c5d99ad76adb26e69f29b9eb13f6d4a17e88e56450497aee.json>).
- Period 77: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce769871d645f109c0d50ea7dcdcd20badcd8eedf65652fba2d3006abbac6df7.json>).
- Period 78: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c63a93610c199a400f45fd02a92f15731aeab44dc21be33375a2596e180570b.json>).
- Period 79: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6fdfcbf85b2e4cab6e2dcb7780fbc9059902a4f709c6cade48fdd8025ae8063.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.9e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4ee936b2f3cb12c202b04239aca447d74a263596829e060aeac3e363e69a6cbc.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.81e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/80fba4c2cdd97946c35cd63f7c840312cc5da07fadb2d768e63873d6dee42e2b.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bd76e0c3cc12dea06b369d2aa2b7aee141eed1141094f31b4628b0ddc9fdbcb5.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.08e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27dedd66ac27f42bf2440cd73a0d67eb8d358ea50b35f3af8a68e3d75fa79803.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d5c66dd1181c0f6a16056b0cbba7797f16f2672937191ad2ae650f120c3f28b.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.53e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bf1078f340b6f5d29c498cd5d6d813e0fddb8ac9f292dcf8fd74b62c99018f34.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 9.63e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d5c66dd1181c0f6a16056b0cbba7797f16f2672937191ad2ae650f120c3f28b.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.08e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/27dedd66ac27f42bf2440cd73a0d67eb8d358ea50b35f3af8a68e3d75fa79803.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.92e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/bd76e0c3cc12dea06b369d2aa2b7aee141eed1141094f31b4628b0ddc9fdbcb5.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.81e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/80fba4c2cdd97946c35cd63f7c840312cc5da07fadb2d768e63873d6dee42e2b.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.9e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/4ee936b2f3cb12c202b04239aca447d74a263596829e060aeac3e363e69a6cbc.json>).
- Period 91: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.98e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b6fdfcbf85b2e4cab6e2dcb7780fbc9059902a4f709c6cade48fdd8025ae8063.json>).
- Period 92: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.26e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0c63a93610c199a400f45fd02a92f15731aeab44dc21be33375a2596e180570b.json>).
- Period 93: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.85e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce769871d645f109c0d50ea7dcdcd20badcd8eedf65652fba2d3006abbac6df7.json>).
- Period 94: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.64e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fd56e99428b05c84c5d99ad76adb26e69f29b9eb13f6d4a17e88e56450497aee.json>).
- Period 96: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a8c5d253412b4d2acd5aed9fe9661b9609e5f41a52e98b9a2a14e31d82b2a923.json>).
- Period 97: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.39e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/234de463df3e13347d736c50e947d4b7535281c538260e23b3755dcee2d6b27b.json>).
- Period 98: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.51e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a8c5d253412b4d2acd5aed9fe9661b9609e5f41a52e98b9a2a14e31d82b2a923.json>).
- Period 99: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.43e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2f37fa94c428eda153a9024ae1309fa34e5f5d01fcbfadda2d75dec181bdc629.json>).
- Period 100: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1051bc7c308793a60cd91aae2ae05438acc2e41be1d910b1f055aa5847044a93.json>).
- Period 101: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/203acb3d99f257ff3b49efcb78ddeadc92b39999207816ab5a940192ef33633d.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2e626113e66bd63a757340bcd9c083c2a1df8f6f5edd905f43646938132747a.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/046c154268cdef569290ab4e453100e486671c08389a8f56d8babe33c575ee45.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.89e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7c0fd89cde9cec6ed2f5e9586c3d820669a2b3d3ccb0eaa39d8803d6aa53b86.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e57c6d6154954d7d151394de6b5e25e390bd3e061f50fe5a4c28b77d9d577de.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/454ff3e458d8935c2e36b354f325d7d29421a83cf6cf9d0352c40f44ce533c30.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **51.050804 MW**; maximum nodal residual 4.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a97760360e2fc9937c26d7def1e9d270ee9c521f0e7dda168b7d54491ef638d0.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 51.050804 | 43.061293 | 7.989511 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a099446e79783e968050f9a1222d68a15578513d1e4dba693ff79090a2454d3.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.697540 MW**; maximum nodal residual 3.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b07b9ba17bc94bdbc2caeea311b8a07be0b593dadf49ad6cf44dd3713d71b96.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 5.32e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/3a099446e79783e968050f9a1222d68a15578513d1e4dba693ff79090a2454d3.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **51.050804 MW**; maximum nodal residual 4.92e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a97760360e2fc9937c26d7def1e9d270ee9c521f0e7dda168b7d54491ef638d0.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 51.050804 | 43.061293 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.35e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/454ff3e458d8935c2e36b354f325d7d29421a83cf6cf9d0352c40f44ce533c30.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2e57c6d6154954d7d151394de6b5e25e390bd3e061f50fe5a4c28b77d9d577de.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.89e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c7c0fd89cde9cec6ed2f5e9586c3d820669a2b3d3ccb0eaa39d8803d6aa53b86.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/046c154268cdef569290ab4e453100e486671c08389a8f56d8babe33c575ee45.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.73e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f2e626113e66bd63a757340bcd9c083c2a1df8f6f5edd905f43646938132747a.json>).
- Period 117: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/203acb3d99f257ff3b49efcb78ddeadc92b39999207816ab5a940192ef33633d.json>).
- Period 118: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.28e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1051bc7c308793a60cd91aae2ae05438acc2e41be1d910b1f055aa5847044a93.json>).
- Period 119: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.43e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/2f37fa94c428eda153a9024ae1309fa34e5f5d01fcbfadda2d75dec181bdc629.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `8707dbdb7f995096abec05ac584f5fd5346317d9d106636d6f1e44a505c42de0`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
