<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_1079_2054","policy":"C_eq_G_S1_S2","portfolio":"hosting_2_both_cg","buses":["1079","2054"],"weights":[0.5,0.5],"scenario":"nine_grid_at_hosting_1","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign","campaign_sha256":"cb725e6fbcffea46a2bb281aa66dc6613c218ea3a3a06cbad4be873c54632832","score_usd":67915654258.09393,"it_value_usd":123053148597.11996,"grid_mwh":17512224.047610357,"generation_mwh":7775.952385984578,"modeled_generator_hours":24.0,"annual_generator_hours":24.000000000228948,"required_annual_hours":24.000000000228948,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/cb725e6fbcffea46a2bb281aa66dc6613c218ea3a3a06cbad4be873c54632832-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_1079_2054 — nine_grid_at_hosting_1

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262091 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.260432 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.699468 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.693663 |
| Campaign total | — | — | — | — | 123.053149 | 67.915654 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,770.639 | 1,229.361 | 99.971932% | 5.000 | 5.000 | 5.000 | 0.000 | 499.697540 |
| week-2-submission-2 | 4,377,341.384 | 2,658.616 | 99.939301% | 7.000 | 7.000 | 7.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,770.639 | 1,229.361 | 99.971932% | 5.000 | 5.000 | 5.000 | 0.000 | 499.697540 |
| week-3-submission-2 | 4,377,341.384 | 2,658.616 | 99.939301% | 7.000 | 7.000 | 7.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001196 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.002855 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.562623 | 0.001196 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.566770 | 0.002855 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 1079: 250 MW per submission, 2054: 250 MW per submission.
- Opponents: 9. Each uses 1079 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,229.361 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 2.335466 | 497.664534 | 42.093690 | 0.000000 | 2.335466 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | 0.000000 | 499.697540 | 499.697540 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 2.335466 | 497.664534 | 42.093690 | 0.000000 | 2.335466 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 107, 111 | True |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **2.335466 MW**; maximum nodal residual 7.55e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0dddbcb801c950e161ec2d058e3dddd081d1d8ce8c33817bc1d7f66ee83cbaec.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 2.335466 | 0.000000 | 2.335466 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **2.335466 MW**; maximum nodal residual 7.55e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0dddbcb801c950e161ec2d058e3dddd081d1d8ce8c33817bc1d7f66ee83cbaec.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 2.335466 | 0.000000 | 2.335466 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 2,658.616 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 (day 5, h10) | 1.000 | 79.307775 | 420.692225 | 258.960198 | 0.000000 | 78.603123 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 499.999999 | 0.000001 | 42.093690 | 457.906309 | 499.999999 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 499.999999 | 0.000001 | 42.093690 | 457.906309 | 499.999999 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 79.307775 | 420.692225 | 258.960198 | 0.000000 | 78.603123 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00116 | 1081 → 1071 | upper | 350.000 | 350.000000 | 24, 25, 26, 27, 47 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 24, 25, 26 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 106, 107, 111, 112 | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **78.603123 MW**; maximum nodal residual 6.16e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/854592e4894c5517727f980a8e9ab1547b1fe2108f1a59ff5aa1f123c7e5ac9f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 78.603123 | 70.948566 | 7.654557 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 1.66e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/072ac0599f2e203b1a55051d73e41f51e5c2c057e930645066c2fdd31a0386f5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010488 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 1.66e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/072ac0599f2e203b1a55051d73e41f51e5c2c057e930645066c2fdd31a0386f5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010488 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **78.603123 MW**; maximum nodal residual 6.16e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/854592e4894c5517727f980a8e9ab1547b1fe2108f1a59ff5aa1f123c7e5ac9f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 78.603123 | 70.948566 | 7.654557 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,229.361 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.788627 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.857892 | 0.000000 | 0.000000 | 6.788627 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.788627 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 2.335466 | 497.664534 | 42.093690 | 0.000000 | 2.335466 | 0.275019 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | 0.000000 | 499.697540 | 499.697540 | 0.000531 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 111 (day 5, h15) | 1.000 | 2.335466 | 497.664534 | 42.093690 | 0.000000 | 2.335466 | 0.275019 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 107, 111 | True |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **2.335466 MW**; maximum nodal residual 7.55e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0dddbcb801c950e161ec2d058e3dddd081d1d8ce8c33817bc1d7f66ee83cbaec.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 2.335466 | 0.000000 | 2.335466 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **2.335466 MW**; maximum nodal residual 7.55e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/0dddbcb801c950e161ec2d058e3dddd081d1d8ce8c33817bc1d7f66ee83cbaec.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 2.335466 | 0.000000 | 2.335466 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 2,658.616 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,228.059324 | 0.000000 | 0.000000 | 7.107679 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,090.857892 | 0.000000 | 0.000000 | 7.107679 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,228.059324 | 0.000000 | 0.000000 | 7.107679 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 79.307775 | 420.692225 | 258.960198 | 0.000000 | 78.603123 | 0.239992 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 499.999999 | 0.000001 | 42.093690 | 457.906309 | 499.999999 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 499.999999 | 0.000001 | 42.093690 | 457.906309 | 499.999999 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 79.307775 | 420.692225 | 258.960198 | 0.000000 | 78.603123 | 0.239992 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00116 | 1081 → 1071 | upper | 350.000 | 350.000000 | 24, 25, 26, 27, 47 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 24, 25, 26 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 106, 107, 111, 112 | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **78.603123 MW**; maximum nodal residual 6.16e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/854592e4894c5517727f980a8e9ab1547b1fe2108f1a59ff5aa1f123c7e5ac9f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 78.603123 | 70.948566 | 7.654557 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 1.66e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/072ac0599f2e203b1a55051d73e41f51e5c2c057e930645066c2fdd31a0386f5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010488 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 1.66e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/072ac0599f2e203b1a55051d73e41f51e5c2c057e930645066c2fdd31a0386f5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 499.999999 | 492.010488 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **78.603123 MW**; maximum nodal residual 6.16e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/854592e4894c5517727f980a8e9ab1547b1fe2108f1a59ff5aa1f123c7e5ac9f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 78.603123 | 70.948566 | 7.654557 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/execution.json>).
Campaign SHA-256: `cb725e6fbcffea46a2bb281aa66dc6613c218ea3a3a06cbad4be873c54632832`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
