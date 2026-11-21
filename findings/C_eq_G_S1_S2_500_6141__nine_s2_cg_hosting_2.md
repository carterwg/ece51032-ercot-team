<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_6141","policy":"C_eq_G_S1_S2","portfolio":"bottleneck_ptdf_1_both_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"a7e9ba29e58ff2f542a48c9aefece1c4f48f2f49b5c25bcff0178ffa5171440d","score_usd":67378522037.33446,"it_value_usd":123053148597.11996,"grid_mwh":17137134.82865919,"generation_mwh":382865.1713370833,"modeled_generator_hours":68.0,"annual_generator_hours":3013.81917808163,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/a7e9ba29e58ff2f542a48c9aefece1c4f48f2f49b5c25bcff0178ffa5171440d-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_6141 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262094 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.154882 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.705440 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.256107 |
| Campaign total | — | — | — | — | 123.053149 | 67.378522 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,775.310 | 1,224.690 | 99.972039% | 3.000 | 3.000 | 3.000 | 0.000 | 499.697540 |
| week-2-submission-2 | 4,189,792.104 | 190,207.896 | 95.657354% | 31.000 | 1,503.910 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,775.310 | 1,224.690 | 99.972039% | 3.000 | 3.000 | 3.000 | 0.000 | 499.697540 |
| week-3-submission-2 | 4,189,792.104 | 190,207.896 | 95.657354% | 31.000 | 1,503.910 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001193 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.108405 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.556654 | 0.001193 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.898775 | 0.108405 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 6141: 500 MW per submission.
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
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 190,207.896 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59 (day 3, h11) | 82.773 | 125.000000 | 375.000000 | 1,618.261066 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 1,463.307985 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,410.034361 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 1,463.307985 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 63 (day 3, h15) | 82.773 | 125.000000 | 375.000000 | 1,618.261066 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,336.096234 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 958.108744 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 657.107469 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 426.920251 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 288.746412 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 240.151300 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 288.746412 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 426.920251 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 657.107469 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 958.108744 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,336.096234 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,333.660305 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 929.293891 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 554.404952 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 212.779947 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 297.098663 | 202.901337 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 297.098663 | 202.901337 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 212.779947 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 554.404952 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 929.293891 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,333.660305 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 57, 65, 78, 92, 99, 100, 118, 119 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1c6bc395c8c2767f658609a6875f6f66e3d27e6e513d3c670db3273551fef063.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/299faecc2257974b126d339d18d8371561a285b0e67c98a9f698e4337617c779.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/656e10c3eaa5f215aa2da2666505410e3a09efb2dbbad32fee072a240237790d.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/299faecc2257974b126d339d18d8371561a285b0e67c98a9f698e4337617c779.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1c6bc395c8c2767f658609a6875f6f66e3d27e6e513d3c670db3273551fef063.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce134560ae6d089a57e68d496890beab225d9de13285360ef6c48ac8366b4312.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b2fbcc9cd155c4475bf1f377a1f8ec69ed5e11c75e67dda05bf7f9a17f97915.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/636ea9da416cd10089da7ee9a6eb6b3bcb2df1c7587f3ff26951a0117d52c6ac.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.69e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/213d5e12187c57a11b1079ef7cbefef02dec5788761aaa811808030f8f5c7bd2.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/482e918b101ccdc6611c58af32a279eae74286825fe777a300b90a80fa66213c.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.13e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cbc20d7945773143da529db3d8ed55a1b642a599e4ccb898c4bf6c3aeee8b1ad.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/482e918b101ccdc6611c58af32a279eae74286825fe777a300b90a80fa66213c.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.69e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/213d5e12187c57a11b1079ef7cbefef02dec5788761aaa811808030f8f5c7bd2.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/636ea9da416cd10089da7ee9a6eb6b3bcb2df1c7587f3ff26951a0117d52c6ac.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b2fbcc9cd155c4475bf1f377a1f8ec69ed5e11c75e67dda05bf7f9a17f97915.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce134560ae6d089a57e68d496890beab225d9de13285360ef6c48ac8366b4312.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/689e003978be31ba532baeae0fd4c9826a21dda0d924b135e7071702cbdeefc8.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a9428c3ae06eebd56f1985794c7e4c487edc0882f17a94c6a9dacfdb17f75bc9.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/846e0857d29ccaf84324495b67a2cd282d7e47ab7331a7ce3e53aad1db06d207.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ee5a8bf0ea80bf049463b1767e42c88087a8bb42bf122133c0bf96a4f318ade8.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/555c18c0024d88decfeacbf4db43d45bdceaf985e210be4c3bb204dbb52daa79.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 3.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1a410d139da2e8712081ea92167907bb6bdf669e0025732799e56fab5b7f64e5.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 3.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1a410d139da2e8712081ea92167907bb6bdf669e0025732799e56fab5b7f64e5.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/555c18c0024d88decfeacbf4db43d45bdceaf985e210be4c3bb204dbb52daa79.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ee5a8bf0ea80bf049463b1767e42c88087a8bb42bf122133c0bf96a4f318ade8.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/846e0857d29ccaf84324495b67a2cd282d7e47ab7331a7ce3e53aad1db06d207.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a9428c3ae06eebd56f1985794c7e4c487edc0882f17a94c6a9dacfdb17f75bc9.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/689e003978be31ba532baeae0fd4c9826a21dda0d924b135e7071702cbdeefc8.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,224.690 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.857892 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000531 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 190,207.896 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59 (day 3, h11) | 82.773 | 125.000000 | 375.000000 | 1,618.261066 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 1,463.307985 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,410.034361 | 0.000000 | 0.000000 | 18.221735 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 1,463.307985 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 63 (day 3, h15) | 82.773 | 125.000000 | 375.000000 | 1,618.261066 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,336.096234 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 958.108744 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 657.107469 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 426.920251 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 288.746412 | 0.000000 | 0.000000 | 36.864686 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 240.151300 | 0.000000 | 0.000000 | 36.864686 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 288.746412 | 0.000000 | 0.000000 | 36.864686 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 426.920251 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 657.107469 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 958.108744 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,336.096234 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,333.660305 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 929.293891 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 554.404952 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 212.779947 | 0.000000 | 0.000000 | 0.377204 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 297.098663 | 202.901337 | -0.000000 | 0.000000 | 0.000000 | 0.213764 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.999999 | 499.999999 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 460.241776 | 460.241776 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 297.098663 | 202.901337 | -0.000000 | 0.000000 | 0.000000 | 0.213764 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 212.779947 | 0.000000 | 0.000000 | 0.377204 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 554.404952 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 929.293891 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,333.660305 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 57, 65, 78, 92, 99, 100, 118, 119 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1c6bc395c8c2767f658609a6875f6f66e3d27e6e513d3c670db3273551fef063.json>).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/299faecc2257974b126d339d18d8371561a285b0e67c98a9f698e4337617c779.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.17e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/656e10c3eaa5f215aa2da2666505410e3a09efb2dbbad32fee072a240237790d.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.03e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/299faecc2257974b126d339d18d8371561a285b0e67c98a9f698e4337617c779.json>).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.41e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1c6bc395c8c2767f658609a6875f6f66e3d27e6e513d3c670db3273551fef063.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce134560ae6d089a57e68d496890beab225d9de13285360ef6c48ac8366b4312.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b2fbcc9cd155c4475bf1f377a1f8ec69ed5e11c75e67dda05bf7f9a17f97915.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/636ea9da416cd10089da7ee9a6eb6b3bcb2df1c7587f3ff26951a0117d52c6ac.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.69e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/213d5e12187c57a11b1079ef7cbefef02dec5788761aaa811808030f8f5c7bd2.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/482e918b101ccdc6611c58af32a279eae74286825fe777a300b90a80fa66213c.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.13e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cbc20d7945773143da529db3d8ed55a1b642a599e4ccb898c4bf6c3aeee8b1ad.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.76e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/482e918b101ccdc6611c58af32a279eae74286825fe777a300b90a80fa66213c.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.69e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/213d5e12187c57a11b1079ef7cbefef02dec5788761aaa811808030f8f5c7bd2.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.21e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/636ea9da416cd10089da7ee9a6eb6b3bcb2df1c7587f3ff26951a0117d52c6ac.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6b2fbcc9cd155c4475bf1f377a1f8ec69ed5e11c75e67dda05bf7f9a17f97915.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.14e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ce134560ae6d089a57e68d496890beab225d9de13285360ef6c48ac8366b4312.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/689e003978be31ba532baeae0fd4c9826a21dda0d924b135e7071702cbdeefc8.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a9428c3ae06eebd56f1985794c7e4c487edc0882f17a94c6a9dacfdb17f75bc9.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/846e0857d29ccaf84324495b67a2cd282d7e47ab7331a7ce3e53aad1db06d207.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ee5a8bf0ea80bf049463b1767e42c88087a8bb42bf122133c0bf96a4f318ade8.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/555c18c0024d88decfeacbf4db43d45bdceaf985e210be4c3bb204dbb52daa79.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 3.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1a410d139da2e8712081ea92167907bb6bdf669e0025732799e56fab5b7f64e5.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **460.241776 MW**; maximum nodal residual 3.01e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1a410d139da2e8712081ea92167907bb6bdf669e0025732799e56fab5b7f64e5.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/555c18c0024d88decfeacbf4db43d45bdceaf985e210be4c3bb204dbb52daa79.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ee5a8bf0ea80bf049463b1767e42c88087a8bb42bf122133c0bf96a4f318ade8.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/846e0857d29ccaf84324495b67a2cd282d7e47ab7331a7ce3e53aad1db06d207.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/a9428c3ae06eebd56f1985794c7e4c487edc0882f17a94c6a9dacfdb17f75bc9.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.26e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/689e003978be31ba532baeae0fd4c9826a21dda0d924b135e7071702cbdeefc8.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `a7e9ba29e58ff2f542a48c9aefece1c4f48f2f49b5c25bcff0178ffa5171440d`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
