<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_C_eq_G_S2_500_6141","policy":"G_eq_0_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"10b4238e8924cc03192eb188e8a14bde9324924c424d6dd86ea4350d0ef4d4b5","score_usd":55286670233.03679,"it_value_usd":98741559374.66504,"grid_mwh":13761621.844649343,"generation_mwh":296954.7945204665,"modeled_generator_hours":54.0,"annual_generator_hours":2345.6383561634457,"required_annual_hours":6.000000000057237,"minimum_admission":0.6048603469375339,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/10b4238e8924cc03192eb188e8a14bde9324924c424d6dd86ea4350d0ef4d4b5-3eea05334a1d.json"} -->
# G_eq_0_S1_C_eq_G_S2_500_6141 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 302.430173 | 302.430173 | 18.607493 | 11.046738 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430173 | 30.763287 | 17.178499 |
| week-3-submission-1 | 500.000 | 0.000 | 302.430173 | 302.430173 | 18.607493 | 10.711143 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430173 | 30.763287 | 16.350290 |
| Campaign total | — | — | — | — | 98.741559 | 55.286670 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,649,288.320 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 4,231,522.603 | 148,477.397 | 96.610105% | 27.000 | 1,172.819 | 3.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 2,649,288.320 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 4,231,522.603 | 148,477.397 | 96.610105% | 27.000 | 1,172.819 | 3.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.084788 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.335595 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-3-submission-2 | 0.828209 | 0.084788 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
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
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 9, 10, 11, 12, 13, 14, 15, 16, 17, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **302.732634 MW**; maximum nodal residual 3.76e-09 MW. Generation-only capacity ceiling = 302.732634 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/890dcf82b5ce2fbb0e0b0d0be1159aa18c8b9d46572cb3e7e0b0cc600a78dfac.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 61, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 148,477.397 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. At periods 61, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,515.977149 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,442.716442 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 1,064.728952 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 744.728801 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 514.541583 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 370.790709 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 326.072898 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 370.790709 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 514.541583 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 744.728801 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 1,064.728952 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,442.716442 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,440.280513 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 1,034.649953 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 642.026284 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 300.885446 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 125.000000 | 375.000000 | 14.435671 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 125.000000 | 375.000000 | 14.435671 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 300.885446 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 642.026284 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 1,034.649953 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,440.280513 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 9, 17, 57, 58, 64, 65, 78, 92, 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 61, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5f8f214b80677187fcb353d48e7f454ce85bc546e02bbd1a0b69d6285e97d8f4.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/01eaa6082f62f281222fa352b01b4c8c00dea20217fcf5bfa91e1a2022091689.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f5d28d5d8377e6f6613d501daa83d02d7ea5facca0078505ff2603d3afe4d228.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f4b95ba49755ee79ebd0d58bda047ff61cc892f333bceddded3079c81e41fea5.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/be642be3a706e6ff8dd8684f7be520369b2d7e853d671062cfad174c9d05d235.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b887be231c7b0bb8ad46b31e107e5d6d55b54dd3fd81d75fe91b0b90755cbeb3.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef4ae7010317090c1f31147b9708ecf6a3ef3b0b7474c85df4ec71b38152971c.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b887be231c7b0bb8ad46b31e107e5d6d55b54dd3fd81d75fe91b0b90755cbeb3.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/be642be3a706e6ff8dd8684f7be520369b2d7e853d671062cfad174c9d05d235.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f4b95ba49755ee79ebd0d58bda047ff61cc892f333bceddded3079c81e41fea5.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f5d28d5d8377e6f6613d501daa83d02d7ea5facca0078505ff2603d3afe4d228.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/01eaa6082f62f281222fa352b01b4c8c00dea20217fcf5bfa91e1a2022091689.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/966fceeb8c1569be9c687e164d6199624b33d4c6c59a51210dd77b32819b212e.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d2e9a40155458ce32321ea52b1cf8933ba20aa941df64cb2bf782e7473cc5535.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/626baf238d924048c51b6e943a08da59e2d4c4fb8272238060b97b9ff992079c.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8996317cbfe6d125a3d7a4a7e8afde2cf02c2b40e33f5a4e58c9c1477268b37.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.5e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c9b12c8d16a50d063890a55900fd37352a95f8eed8791d769c6d49ca2724192d.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f1ac67459d22178b03de5be02929189ab33977e59e89a417ed3e54bb1e816e34.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 6.48e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7045f5413af0780b554432f8cd4da34f2495528e7c8ac2bb2ed9172ccdd296c9.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.697540 MW**; maximum nodal residual 3.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fa3420d0061d53a3805f750ec0edfaed774790812ca39ad03facca65d602b724.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 6.48e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7045f5413af0780b554432f8cd4da34f2495528e7c8ac2bb2ed9172ccdd296c9.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f1ac67459d22178b03de5be02929189ab33977e59e89a417ed3e54bb1e816e34.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.5e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c9b12c8d16a50d063890a55900fd37352a95f8eed8791d769c6d49ca2724192d.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8996317cbfe6d125a3d7a4a7e8afde2cf02c2b40e33f5a4e58c9c1477268b37.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/626baf238d924048c51b6e943a08da59e2d4c4fb8272238060b97b9ff992079c.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d2e9a40155458ce32321ea52b1cf8933ba20aa941df64cb2bf782e7473cc5535.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/966fceeb8c1569be9c687e164d6199624b33d4c6c59a51210dd77b32819b212e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430173 MW** (60.486035%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267366 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 302.430173 | 2,228.059324 | 0.000000 | 0.000000 | 3.977774 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 302.430173 | 2,090.857892 | 0.000000 | 0.000000 | 3.977774 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 302.430173 | 2,228.059324 | 0.000000 | 0.000000 | 3.977774 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430173 | 0.302460 | 0.000000 | 0.000000 | 0.061781 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 9, 10, 11, 12, 13, 14, 15, 16, 17, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **302.732634 MW**; maximum nodal residual 3.76e-09 MW. Generation-only capacity ceiling = 302.732634 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/890dcf82b5ce2fbb0e0b0d0be1159aa18c8b9d46572cb3e7e0b0cc600a78dfac.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 61, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 148,477.397 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. At periods 61, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,515.977149 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,442.716442 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 1,064.728952 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 744.728801 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 514.541583 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 370.790709 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 326.072898 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 370.790709 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 514.541583 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 744.728801 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 1,064.728952 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,442.716442 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,440.280513 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 1,034.649953 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 642.026284 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 300.885446 | 0.000000 | 0.000000 | 0.242982 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 125.000000 | 375.000000 | 14.435671 | 0.000000 | 0.000000 | 0.377204 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 125.000000 | 375.000000 | 14.435671 | 0.000000 | 0.000000 | 0.377204 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 300.885446 | 0.000000 | 0.000000 | 0.242982 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 642.026284 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 1,034.649953 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,440.280513 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 9, 17, 57, 58, 64, 65, 78, 92, 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 61, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.02e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5f8f214b80677187fcb353d48e7f454ce85bc546e02bbd1a0b69d6285e97d8f4.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/01eaa6082f62f281222fa352b01b4c8c00dea20217fcf5bfa91e1a2022091689.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f5d28d5d8377e6f6613d501daa83d02d7ea5facca0078505ff2603d3afe4d228.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f4b95ba49755ee79ebd0d58bda047ff61cc892f333bceddded3079c81e41fea5.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/be642be3a706e6ff8dd8684f7be520369b2d7e853d671062cfad174c9d05d235.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b887be231c7b0bb8ad46b31e107e5d6d55b54dd3fd81d75fe91b0b90755cbeb3.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.24e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/ef4ae7010317090c1f31147b9708ecf6a3ef3b0b7474c85df4ec71b38152971c.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.88e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/b887be231c7b0bb8ad46b31e107e5d6d55b54dd3fd81d75fe91b0b90755cbeb3.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.36e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/be642be3a706e6ff8dd8684f7be520369b2d7e853d671062cfad174c9d05d235.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.97e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f4b95ba49755ee79ebd0d58bda047ff61cc892f333bceddded3079c81e41fea5.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f5d28d5d8377e6f6613d501daa83d02d7ea5facca0078505ff2603d3afe4d228.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.8e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/01eaa6082f62f281222fa352b01b4c8c00dea20217fcf5bfa91e1a2022091689.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/966fceeb8c1569be9c687e164d6199624b33d4c6c59a51210dd77b32819b212e.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d2e9a40155458ce32321ea52b1cf8933ba20aa941df64cb2bf782e7473cc5535.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/626baf238d924048c51b6e943a08da59e2d4c4fb8272238060b97b9ff992079c.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8996317cbfe6d125a3d7a4a7e8afde2cf02c2b40e33f5a4e58c9c1477268b37.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.5e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c9b12c8d16a50d063890a55900fd37352a95f8eed8791d769c6d49ca2724192d.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f1ac67459d22178b03de5be02929189ab33977e59e89a417ed3e54bb1e816e34.json>).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 6.48e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7045f5413af0780b554432f8cd4da34f2495528e7c8ac2bb2ed9172ccdd296c9.json>).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.697540 MW**; maximum nodal residual 3.89e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/fa3420d0061d53a3805f750ec0edfaed774790812ca39ad03facca65d602b724.json>).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **362.496087 MW**; maximum nodal residual 6.48e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7045f5413af0780b554432f8cd4da34f2495528e7c8ac2bb2ed9172ccdd296c9.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 5.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/f1ac67459d22178b03de5be02929189ab33977e59e89a417ed3e54bb1e816e34.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.5e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c9b12c8d16a50d063890a55900fd37352a95f8eed8791d769c6d49ca2724192d.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.07e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8996317cbfe6d125a3d7a4a7e8afde2cf02c2b40e33f5a4e58c9c1477268b37.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.23e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/626baf238d924048c51b6e943a08da59e2d4c4fb8272238060b97b9ff992079c.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.08e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/d2e9a40155458ce32321ea52b1cf8933ba20aa941df64cb2bf782e7473cc5535.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.06e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/966fceeb8c1569be9c687e164d6199624b33d4c6c59a51210dd77b32819b212e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `10b4238e8924cc03192eb188e8a14bde9324924c424d6dd86ea4350d0ef4d4b5`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
