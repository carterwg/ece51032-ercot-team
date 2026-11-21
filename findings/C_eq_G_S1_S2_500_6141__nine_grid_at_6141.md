<!-- findings-record: {"schema":1,"kind":"campaign","stem":"C_eq_G_S1_S2_500_6141","policy":"C_eq_G_S1_S2","portfolio":"bottleneck_ptdf_1_both_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign","campaign_sha256":"264951a746b6b6d1a15f041e8029d089cf981b3c22f1e93f1778935b405478c0","score_usd":67922102755.8172,"it_value_usd":123053148597.11996,"grid_mwh":17512324.18613805,"generation_mwh":7675.813859361223,"modeled_generator_hours":20.0,"annual_generator_hours":20.000000000190788,"required_annual_hours":20.000000000190788,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/264951a746b6b6d1a15f041e8029d089cf981b3c22f1e93f1778935b405478c0-3eea05334a1d.json"} -->
# C_eq_G_S1_S2_500_6141 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 17.262001 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.260522 |
| week-3-submission-1 | 500.000 | 500.000 | 500.000000 | 500.000000 | 30.763287 | 16.703560 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.696020 |
| Campaign total | — | — | — | — | 123.053149 | 67.922103 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,662.093 | 1,337.907 | 99.969454% | 5.000 | 5.000 | 5.000 | 0.000 | 499.699551 |
| week-2-submission-2 | 4,377,500.000 | 2,500.000 | 99.942922% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,378,662.093 | 1,337.907 | 99.969454% | 5.000 | 5.000 | 5.000 | 0.000 | 499.699551 |
| week-3-submission-2 | 4,377,500.000 | 2,500.000 | 99.942922% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.001286 | 1.000000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.002766 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.558441 | 0.001286 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.564502 | 0.002766 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `C_eq_G_S1_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,337.907 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 37.066933 | 462.933067 | 96.932230 | 0.000000 | 37.066933 | 0.000000 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 382.036756 | 117.963244 | 39.647743 | 342.389013 | 382.036756 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 499.699551 | 0.300449 | 20.109085 | 479.590466 | 499.699551 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 382.036756 | 117.963244 | 39.647743 | 342.389013 | 382.036756 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 37.066933 | 462.933067 | 96.932230 | 0.000000 | 37.066933 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 9, 13, 17, 54, 56, 57, 65, 66, 68, 72, 73, 74, 77, 78, 92, 93, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 30, 44, 45, 46, 47, 57, 65, 78, 92, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **37.066933 MW**; maximum nodal residual 5.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/974b373f460022667524351de5ff1a0d882e98479acc2175990b1ede946476b5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 37.066933 | 4.316230 | 32.750703 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **382.036756 MW**; maximum nodal residual 1.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a06ea41eb4638e72bd7e33d786a02946a8724659581f3242f49abe9bad320c1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 382.036756 | 349.286053 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.699551 MW**; maximum nodal residual 6.6e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8e3212257ef3db7f1f8175c42b317b689845dafb84b174bd959dd8b19629474f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.699551 | 479.590466 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **382.036756 MW**; maximum nodal residual 1.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a06ea41eb4638e72bd7e33d786a02946a8724659581f3242f49abe9bad320c1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 382.036756 | 349.286053 | 32.750703 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **37.066933 MW**; maximum nodal residual 5.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/974b373f460022667524351de5ff1a0d882e98479acc2175990b1ede946476b5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 37.066933 | 4.316230 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,500.000 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 96.932230 | 403.067770 | 500.000000 | 0.000000 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 96.932230 | 403.067770 | 500.000000 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 32, 34, 35, 36, 37, 38, 39, 40, 42, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b02090 | 6239 → 7414 | lower | 2,000.000 | 2,000.000000 | 10, 16, 72, 74, 75, 95 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 85, 105, 106, 107, 108, 109, 110, 111, 112, 113 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 3, 4, 10, 16, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 43, 44, 45, 46, 47, 57, 58, 64, 65, 72, 73, 74, 75, 78, 92, 95, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.26e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/df11fdf1ccd583578c799274c0315338a4cbf92d1af2ca4df4b535195743ea29.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 6.85e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54bfa136f724d3bb1fbe104355a65fc572e844f16ca0f90df0f917db4576df5e.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.999999 | 479.890915 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.26e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/df11fdf1ccd583578c799274c0315338a4cbf92d1af2ca4df4b535195743ea29.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,337.907 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 2,150.420720 | 0.000000 | 0.000000 | 6.717357 | none |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,748.166398 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,610.964966 | 0.000000 | 0.000000 | 6.717357 | none |
| 107 (day 5, h11) | 1.000 | 37.066933 | 462.933067 | 96.932230 | 0.000000 | 37.066933 | 0.260116 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 382.036756 | 117.963244 | 39.647743 | 342.389013 | 382.036756 | 0.207131 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 499.699551 | 0.300449 | 20.109085 | 479.590466 | 499.699551 | 0.000528 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 382.036756 | 117.963244 | 39.647743 | 342.389013 | 382.036756 | 0.207131 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 37.066933 | 462.933067 | 96.932230 | 0.000000 | 37.066933 | 0.260116 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 9, 13, 17, 54, 56, 57, 65, 66, 68, 72, 73, 74, 77, 78, 92, 93, 96, 97, 98, 99, 119 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 106, 107, 108, 109, 110, 111, 112 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 30, 44, 45, 46, 47, 57, 65, 78, 92, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **37.066933 MW**; maximum nodal residual 5.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/974b373f460022667524351de5ff1a0d882e98479acc2175990b1ede946476b5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 37.066933 | 4.316230 | 32.750703 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **382.036756 MW**; maximum nodal residual 1.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a06ea41eb4638e72bd7e33d786a02946a8724659581f3242f49abe9bad320c1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 382.036756 | 349.286053 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.699551 MW**; maximum nodal residual 6.6e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/8e3212257ef3db7f1f8175c42b317b689845dafb84b174bd959dd8b19629474f.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.699551 | 479.590466 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **382.036756 MW**; maximum nodal residual 1.29e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/7a06ea41eb4638e72bd7e33d786a02946a8724659581f3242f49abe9bad320c1.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 382.036756 | 349.286053 | 32.750703 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **37.066933 MW**; maximum nodal residual 5.7e-08 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/974b373f460022667524351de5ff1a0d882e98479acc2175990b1ede946476b5.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 37.066933 | 4.316230 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 2,500.000 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,248.166398 | 0.000000 | 0.000000 | 6.725594 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,110.964966 | 0.000000 | 0.000000 | 7.522163 | b02136:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,248.166398 | 0.000000 | 0.000000 | 6.725594 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 96.932230 | 403.067770 | 500.000000 | 0.000000 | b02136:lower |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 20.109085 | 479.890915 | 499.999999 | 0.000000 | b02136:lower |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 39.647743 | 460.352257 | 500.000000 | 0.000000 | b02136:lower |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 96.932230 | 403.067770 | 500.000000 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 32, 34, 35, 36, 37, 38, 39, 40, 42, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b02090 | 6239 → 7414 | lower | 2,000.000 | 2,000.000000 | 10, 16, 72, 74, 75, 95 | none | False |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 85, 105, 106, 107, 108, 109, 110, 111, 112, 113 | 107, 108, 109, 110, 111 | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 0, 1, 2, 3, 4, 10, 16, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 43, 44, 45, 46, 47, 57, 58, 64, 65, 72, 73, 74, 75, 78, 92, 95, 96, 98, 99, 100, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.26e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/df11fdf1ccd583578c799274c0315338a4cbf92d1af2ca4df4b535195743ea29.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **499.999999 MW**; maximum nodal residual 6.85e-09 MW. [diagnostic evidence](<../runs/findings-diagnostics/probes/54bfa136f724d3bb1fbe104355a65fc572e844f16ca0f90df0f917db4576df5e.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 499.999999 | 479.890915 | 20.109084 | True |

- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 8.28e-09 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/3c7060df87fed20b7d1319393e6598e34551159cf1b106373dd33860b2f8bbce.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |

- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **500.000000 MW**; maximum nodal residual 2.26e-08 MW. The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. [diagnostic evidence](<../runs/findings-diagnostics/probes/df11fdf1ccd583578c799274c0315338a4cbf92d1af2ca4df4b535195743ea29.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 500.000000 | 467.249297 | 32.750703 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

This accepted campaign used a recorded numerical retry: `audited_numerical_retry`. [retry audit](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/execution.json>).

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/execution.json>).

| Earlier attempt | Outcome | Log |
| --- | --- | --- |
| official | evaluator exited 1 | [evaluation log](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/attempt-01/evaluation.log>) |
| audited_numerical_retry | evaluator exited 1 | [evaluation log](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/attempt-02/evaluation.log>) |
Campaign SHA-256: `264951a746b6b6d1a15f041e8029d089cf981b3c22f1e93f1778935b405478c0`.

[accepted campaign](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-team-recovery/bottleneck_ptdf_1_both_cg/nine_grid_at_6141/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
