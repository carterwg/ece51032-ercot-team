<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_1079","policy":"C_eq_G_S1_S2","portfolio":"hosting_1_both_cg","buses":["1079"],"weights":[1.0],"scenario":"nine_grid_at_hosting_1","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign","campaign_sha256":"13461b9e52f3912620bf74232457a47ecb3206f1858a94e631dab3ff670dbdcb","score_usd":67916901073.4677,"it_value_usd":123053148597.11996,"grid_mwh":17512343.975332975,"generation_mwh":7656.024663301234,"modeled_generator_hours":20.0,"annual_generator_hours":20.00000000019079,"required_annual_hours":20.00000000019079,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/13461b9e52f3912620bf74232457a47ecb3206f1858a94e631dab3ff670dbdcb-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_1079 — nine_grid_at_hosting_1

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262094 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.260484 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.700120 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.694204 |
| Campaign total | — | — | — | — | 123.053149 | 67.916901 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,775.310 | 1,224.690 | 99.972039% | 3.000 | 3.000 | 3.000 | 0.000 | 499.697540 |
| week-2-submission-2 | 4,377,396.677 | 2,603.323 | 99.940563% | 7.000 | 7.000 | 7.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,775.310 | 1,224.690 | 99.972039% | 3.000 | 3.000 | 3.000 | 0.000 | 499.697540 |
| week-3-submission-2 | 4,377,396.677 | 2,603.323 | 99.940563% | 7.000 | 7.000 | 7.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001193 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.002803 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.561974 | 0.001193 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.566280 | 0.002803 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 1079: 500 MW per submission.
- Opponents: 9. Each uses 1079 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
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
| b00116 | 1081 → 1071 | upper | 350.000 | 350.000000 | 24, 26, 27, 28, 46, 47 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 2,603.323 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 (day 5, h10) | 1.000 | 60.163329 | 439.836671 | 239.815752 | 0.000000 | 60.163329 | 0.000000 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 491.497981 | 8.502019 | 31.256204 | 460.241777 | 491.497980 | 0.000000 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 491.497981 | 8.502019 | 31.256204 | 460.241777 | 491.497980 | 0.000000 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 60.163329 | 439.836671 | 239.815752 | 0.000000 | 60.163329 | 0.000000 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00116 | 1081 → 1071 | upper | 350.000 | 350.000000 | 6, 7, 19, 20, 24, 25, 26, 27, 33, 34, 40, 41, 47, 48, 49, 50, 51, 71 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 24, 25, 26 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 106, 107, 111, 112 | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **60.163329 MW**; maximum nodal residual 5.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/75e465a7d6b102b145624b7cc06495e0014f059ad47c49a7b03b9e8e39960920.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 60.163329 | 52.173818 | 7.989511 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **491.497980 MW**; maximum nodal residual 2.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/64c299dda73dbb33b94ad98f6accb6abeb6a3afe53fa5773ec7387ebfc8cadff.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 491.497980 | 483.508470 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **491.497980 MW**; maximum nodal residual 2.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/64c299dda73dbb33b94ad98f6accb6abeb6a3afe53fa5773ec7387ebfc8cadff.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 491.497980 | 483.508470 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **60.163329 MW**; maximum nodal residual 5.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/75e465a7d6b102b145624b7cc06495e0014f059ad47c49a7b03b9e8e39960920.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 60.163329 | 52.173818 | 7.989511 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,224.690 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.779592 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.857892 | 0.000000 | 0.000000 | 6.779592 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,728.059324 | 0.000000 | 0.000000 | 6.779592 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |
| 109 (day 5, h13) | 1.000 | 499.697540 | 0.302460 | -0.000000 | 499.697540 | 499.697540 | 0.000531 | none |
| 110 (day 5, h14) | 1.000 | 362.496087 | 137.503913 | -0.000000 | 362.496087 | 362.496087 | 0.144865 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00116 | 1081 → 1071 | upper | 350.000 | 350.000000 | 24, 26, 27, 28, 46, 47 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 2,603.323 MWh. Own generation was physically necessary for admitted load at verified periods 106, 107, 108, 109, 110, 111, 112.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 1,630.313646 | 0.000000 | 0.000000 | 7.089000 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,228.059324 | 0.000000 | 0.000000 | 7.089000 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,090.857892 | 0.000000 | 0.000000 | 7.089000 | b02579:lower |
| 106 (day 5, h10) | 1.000 | 60.163329 | 439.836671 | 239.815752 | 0.000000 | 60.163329 | 0.247138 | b02579:lower |
| 107 (day 5, h11) | 1.000 | 491.497981 | 8.502019 | 31.256204 | 460.241777 | 491.497980 | 0.014929 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 491.497981 | 8.502019 | 31.256204 | 460.241777 | 491.497980 | 0.014929 | b02579:lower |
| 112 (day 5, h16) | 1.000 | 60.163329 | 439.836671 | 239.815752 | 0.000000 | 60.163329 | 0.247138 | b02579:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00116 | 1081 → 1071 | upper | 350.000 | 350.000000 | 6, 7, 19, 20, 24, 25, 26, 27, 33, 34, 40, 41, 47, 48, 49, 50, 51, 71 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 24, 25, 26 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | 106, 107, 111, 112 | True |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **60.163329 MW**; maximum nodal residual 5.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/75e465a7d6b102b145624b7cc06495e0014f059ad47c49a7b03b9e8e39960920.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 60.163329 | 52.173818 | 7.989511 | True |

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **491.497980 MW**; maximum nodal residual 2.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/64c299dda73dbb33b94ad98f6accb6abeb6a3afe53fa5773ec7387ebfc8cadff.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 491.497980 | 483.508470 | 7.989511 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **491.497980 MW**; maximum nodal residual 2.82e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/64c299dda73dbb33b94ad98f6accb6abeb6a3afe53fa5773ec7387ebfc8cadff.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 491.497980 | 483.508470 | 7.989511 | True |

- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **60.163329 MW**; maximum nodal residual 5.23e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/75e465a7d6b102b145624b7cc06495e0014f059ad47c49a7b03b9e8e39960920.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02579 | verified | 60.163329 | 52.173818 | 7.989511 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `13461b9e52f3912620bf74232457a47ecb3206f1858a94e631dab3ff670dbdcb`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_1_both_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
