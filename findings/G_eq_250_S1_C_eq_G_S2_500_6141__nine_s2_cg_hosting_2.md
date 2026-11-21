<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_250_S1_C_eq_G_S2_500_6141","policy":"G_eq_250_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_250_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"5511de9f684cfb1f9df9513a4f33944c00281366d146d09001ff2002f915f249","score_usd":68450985599.60754,"it_value_usd":123053148597.11996,"grid_mwh":17180035.314172357,"generation_mwh":339964.68582392205,"modeled_generator_hours":64.0,"annual_generator_hours":2682.7287671225663,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/5511de9f684cfb1f9df9513a4f33944c00281366d146d09001ff2002f915f249-3eea05334a1d.json"} -->
# G_eq_250_S1_C_eq_G_S2_500_6141 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 250.000 | 500.000000 | 500.000000 | 30.763287 | 17.762835 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.166517 |
| week-3-submission-1 | 500.000 | 250.000 | 500.000000 | 500.000000 | 30.763287 | 17.206081 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.315553 |
| Campaign total | — | — | — | — | 123.053149 | 68.450986 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,525.234 | 474.766 | 99.989161% | 3.000 | 3.000 | 3.000 | 0.000 | 249.722867 |
| week-2-submission-2 | 4,210,492.423 | 169,507.577 | 96.129964% | 29.000 | 1,338.364 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,525.234 | 474.766 | 99.989161% | 3.000 | 3.000 | 3.000 | 0.000 | 249.722867 |
| week-3-submission-2 | 4,210,492.423 | 169,507.577 | 96.129964% | 29.000 | 1,338.364 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000452 | 0.500000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.096771 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.556755 | 0.000452 | 0.500000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.850964 | 0.096771 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_250_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 250 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 474.766 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 112.521414 | 387.478586 | -0.000000 | 112.521414 | 112.521414 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 249.722867 | 250.277133 | -0.000000 | 249.722867 | 249.722867 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 112.521414 | 387.478586 | -0.000000 | 112.521414 | 112.521414 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 169,507.577 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 1,469.006952 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,415.792707 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 1,469.006952 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,341.854580 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 963.867089 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 651.071015 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 420.883797 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 285.932714 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 241.214903 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 285.932714 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 420.883797 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 651.071015 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 963.867089 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,341.854580 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,339.418651 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 933.788091 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 548.368499 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 216.027451 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 293.514636 | 206.485364 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 210.267104 | 210.267104 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 210.267104 | 210.267104 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 293.514636 | 206.485364 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 216.027451 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 548.368499 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 933.788091 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,339.418651 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 57, 65, 78, 92, 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cb0eccbe1ce19e2e1350f2a4d5881afe1cde27b0e4e5972cc8307fc9a35b5390.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/799e6849037f0267149e2c44ade0cba42a424aca8ff984759769a6f45361f5cc.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cb0eccbe1ce19e2e1350f2a4d5881afe1cde27b0e4e5972cc8307fc9a35b5390.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1d9695e3f9545e6cbc0757d03017634f8bbdad058062acbc2584301f03c7e8b2.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c45295cbced92ac84a96e834f41902c0a864d40fdb58e7c72ded0b94b948a5b2.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/115c7044744beae4a6a1611e0773c74cfd57d368876125d6227b35a38b9398c2.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/784449100a0fe54f14a74849be40eb253aec5a18c7ead5f501318e1b2d581457.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b0b0fa228351683d378e1f1221b543ba71ea5b6c0814fa62b5d731a1f9f56f0.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d59527c40b510ce22fa04becc615667b38ef9240e9b674a932ca1a188ae850b.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b0b0fa228351683d378e1f1221b543ba71ea5b6c0814fa62b5d731a1f9f56f0.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/784449100a0fe54f14a74849be40eb253aec5a18c7ead5f501318e1b2d581457.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/115c7044744beae4a6a1611e0773c74cfd57d368876125d6227b35a38b9398c2.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c45295cbced92ac84a96e834f41902c0a864d40fdb58e7c72ded0b94b948a5b2.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1d9695e3f9545e6cbc0757d03017634f8bbdad058062acbc2584301f03c7e8b2.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9df8d66c23d6d211c75f74d0de7c0ba16564c759f18054ac21f775257357d46e.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/98ec4f3fa0ee053c9beb46fe749b74a596045a82b4831a891960e409cb1ebb87.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.16e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6db8ea8bc1aa87ce96048c7a1e3e5df805be08783573e6457b327e5b83120cde.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0bf7a856a0c9beeca97b85ea385079c15e902aeb6b4596d9b113f702730fced8.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.65e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8dae65c78f050e4d1cdfdcbabb8f37c79661611cae64177f84e841ddf6d8889.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **210.267104 MW**; maximum nodal residual 5.53e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6dae48a86c9c1471a092528b0acf4ff579e44234026830ef50c79c5bf96549ff.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **210.267104 MW**; maximum nodal residual 5.53e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6dae48a86c9c1471a092528b0acf4ff579e44234026830ef50c79c5bf96549ff.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.65e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8dae65c78f050e4d1cdfdcbabb8f37c79661611cae64177f84e841ddf6d8889.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0bf7a856a0c9beeca97b85ea385079c15e902aeb6b4596d9b113f702730fced8.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.16e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6db8ea8bc1aa87ce96048c7a1e3e5df805be08783573e6457b327e5b83120cde.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/98ec4f3fa0ee053c9beb46fe749b74a596045a82b4831a891960e409cb1ebb87.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9df8d66c23d6d211c75f74d0de7c0ba16564c759f18054ac21f775257357d46e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 250 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 474.766 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,978.033997 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,840.832565 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,978.033997 | 0.000000 | 0.000000 | 6.670226 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 112.521414 | 387.478586 | -0.000000 | 112.521414 | 112.521414 | 0.408223 | none |
| 109 (day 5, h13) | 1.000 | 249.722867 | 250.277133 | -0.000000 | 249.722867 | 249.722867 | 0.439460 | none |
| 110 (day 5, h14) | 1.000 | 112.521414 | 387.478586 | -0.000000 | 112.521414 | 112.521414 | 0.408223 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 169,507.577 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. At periods 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 1,469.006952 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 1,415.792707 | 0.000000 | 0.000000 | 18.221735 | b02579:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 1,469.006952 | 0.000000 | 0.000000 | 18.173302 | b02579:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 1,341.854580 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 81 (day 4, h09) | 97.732 | 125.000000 | 375.000000 | 963.867089 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 82 (day 4, h10) | 97.732 | 125.000000 | 375.000000 | 651.071015 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 83 (day 4, h11) | 97.732 | 125.000000 | 375.000000 | 420.883797 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 125.000000 | 375.000000 | 285.932714 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 125.000000 | 375.000000 | 241.214903 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 125.000000 | 375.000000 | 285.932714 | 0.000000 | 0.000000 | 23.746993 | b02579:lower |
| 87 (day 4, h15) | 97.732 | 125.000000 | 375.000000 | 420.883797 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 88 (day 4, h16) | 97.732 | 125.000000 | 375.000000 | 651.071015 | 0.000000 | 0.000000 | 22.326132 | b02579:lower |
| 89 (day 4, h17) | 97.732 | 125.000000 | 375.000000 | 963.867089 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 1,341.854580 | 0.000000 | 0.000000 | 21.514820 | b02579:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 1,339.418651 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 103 (day 5, h07) | 1.000 | 125.000000 | 375.000000 | 933.788091 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 104 (day 5, h08) | 1.000 | 125.000000 | 375.000000 | 548.368499 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 105 (day 5, h09) | 1.000 | 125.000000 | 375.000000 | 216.027451 | 0.000000 | 0.000000 | 0.242982 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 293.514636 | 206.485364 | 0.000000 | 0.000000 | 0.000000 | 0.217540 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 210.267104 | 210.267104 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 210.267104 | 210.267104 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 293.514636 | 206.485364 | 0.000000 | 0.000000 | 0.000000 | 0.217540 | b02579:lower |
| 113 (day 5, h17) | 1.000 | 125.000000 | 375.000000 | 216.027451 | 0.000000 | 0.000000 | 0.242982 | b02579:lower |
| 114 (day 5, h18) | 1.000 | 125.000000 | 375.000000 | 548.368499 | 0.000000 | 0.000000 | 0.228444 | b02579:lower |
| 115 (day 5, h19) | 1.000 | 125.000000 | 375.000000 | 933.788091 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 1,339.418651 | 0.000000 | 0.000000 | 0.220142 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 57, 65, 78, 92, 100, 118 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | 60, 61, 62, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116 | False |

### Snapshot counterfactuals for this round

- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cb0eccbe1ce19e2e1350f2a4d5881afe1cde27b0e4e5972cc8307fc9a35b5390.json>).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.96e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/799e6849037f0267149e2c44ade0cba42a424aca8ff984759769a6f45361f5cc.json>).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.9e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/cb0eccbe1ce19e2e1350f2a4d5881afe1cde27b0e4e5972cc8307fc9a35b5390.json>).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1d9695e3f9545e6cbc0757d03017634f8bbdad058062acbc2584301f03c7e8b2.json>).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c45295cbced92ac84a96e834f41902c0a864d40fdb58e7c72ded0b94b948a5b2.json>).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/115c7044744beae4a6a1611e0773c74cfd57d368876125d6227b35a38b9398c2.json>).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/784449100a0fe54f14a74849be40eb253aec5a18c7ead5f501318e1b2d581457.json>).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b0b0fa228351683d378e1f1221b543ba71ea5b6c0814fa62b5d731a1f9f56f0.json>).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d59527c40b510ce22fa04becc615667b38ef9240e9b674a932ca1a188ae850b.json>).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.38e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/5b0b0fa228351683d378e1f1221b543ba71ea5b6c0814fa62b5d731a1f9f56f0.json>).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.01e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/784449100a0fe54f14a74849be40eb253aec5a18c7ead5f501318e1b2d581457.json>).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.77e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/115c7044744beae4a6a1611e0773c74cfd57d368876125d6227b35a38b9398c2.json>).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/c45295cbced92ac84a96e834f41902c0a864d40fdb58e7c72ded0b94b948a5b2.json>).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.4e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/1d9695e3f9545e6cbc0757d03017634f8bbdad058062acbc2584301f03c7e8b2.json>).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9df8d66c23d6d211c75f74d0de7c0ba16564c759f18054ac21f775257357d46e.json>).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/98ec4f3fa0ee053c9beb46fe749b74a596045a82b4831a891960e409cb1ebb87.json>).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.16e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6db8ea8bc1aa87ce96048c7a1e3e5df805be08783573e6457b327e5b83120cde.json>).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0bf7a856a0c9beeca97b85ea385079c15e902aeb6b4596d9b113f702730fced8.json>).
- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.65e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8dae65c78f050e4d1cdfdcbabb8f37c79661611cae64177f84e841ddf6d8889.json>).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **210.267104 MW**; maximum nodal residual 5.53e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6dae48a86c9c1471a092528b0acf4ff579e44234026830ef50c79c5bf96549ff.json>).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **210.267104 MW**; maximum nodal residual 5.53e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6dae48a86c9c1471a092528b0acf4ff579e44234026830ef50c79c5bf96549ff.json>).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.65e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/e8dae65c78f050e4d1cdfdcbabb8f37c79661611cae64177f84e841ddf6d8889.json>).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0bf7a856a0c9beeca97b85ea385079c15e902aeb6b4596d9b113f702730fced8.json>).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.16e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/6db8ea8bc1aa87ce96048c7a1e3e5df805be08783573e6457b327e5b83120cde.json>).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.32e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/98ec4f3fa0ee053c9beb46fe749b74a596045a82b4831a891960e409cb1ebb87.json>).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.19e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/9df8d66c23d6d211c75f74d0de7c0ba16564c759f18054ac21f775257357d46e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/execution.json>).
Campaign SHA-256: `5511de9f684cfb1f9df9513a4f33944c00281366d146d09001ff2002f915f249`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
