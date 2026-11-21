# G_eq_125_S1_C_eq_G_S2_500_6141 — nine_both_cg_ptdf_5

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 125.000 | 500.000000 | 500.000000 | 30.763287 | 18.012985 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.892114 |
| week-3-submission-1 | 500.000 | 125.000 | 500.000000 | 500.000000 | 30.763287 | 17.437414 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 15.930579 |
| Campaign total | — | — | — | — | 123.053149 | 68.273092 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,611.443 | 388.557 | 99.991129% | 7.000 | 7.000 | 0.000 | 0.000 | 76.267798 |
| week-2-submission-2 | 3,972,797.463 | 407,202.537 | 90.703138% | 31.000 | 1,503.910 | 302.195 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,611.443 | 388.557 | 99.991129% | 7.000 | 7.000 | 0.000 | 0.000 | 76.267798 |
| week-3-submission-2 | 3,972,797.463 | 407,202.537 | 90.703138% | 31.000 | 1,503.910 | 302.195 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000302 | 0.250000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.371173 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.575572 | 0.000302 | 0.250000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.961535 | 0.371173 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_125_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 6141 (100 MW), 5395 (100 MW), 6342 (100 MW), 5451 (100 MW), 6004 (100 MW) per submission. G/C is 1 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 125 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 388.557 MWh. At periods 106, 107, 108, 109, 110, 111, 112, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 (day 5, h10) | 1.000 | 31.250000 | 468.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 65.358558 | 434.641442 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 59.535913 | 440.464087 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 76.267798 | 423.732202 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 59.535913 | 440.464087 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 65.358558 | 434.641442 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 31.250000 | 468.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 99, 119 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 93, 94, 95, 96, 97, 98 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 12, 13, 14, 56, 57, 58, 59, 63, 64, 65, 66, 76, 77, 78, 79, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.9e-09 MW. diagnostic evidence (local solver artifact).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.1e-09 MW. diagnostic evidence (local solver artifact).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. diagnostic evidence (local solver artifact).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.67e-08 MW. diagnostic evidence (local solver artifact).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. diagnostic evidence (local solver artifact).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.1e-09 MW. diagnostic evidence (local solver artifact).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.9e-09 MW. diagnostic evidence (local solver artifact).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 407,202.537 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 87, 88, 89, 90, 102, 103, 104, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59 (day 3, h11) | 82.773 | 9.438491 | 490.561509 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 135.995512 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 113.037666 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 135.995512 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 9.438491 | 490.561509 | 169.400000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 81.251382 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 270.059892 | 229.940108 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 83 (day 4, h11) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 84 (day 4, h12) | 97.732 | 490.228242 | 9.771758 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 85 (day 4, h13) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 490.228242 | 9.771758 | -0.000000 | 247.639077 | 247.639077 | 0.000000 | none |
| 87 (day 4, h15) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 88 (day 4, h16) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 89 (day 4, h17) | 97.732 | 270.059892 | 229.940108 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 81.251382 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 80.204167 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 298.106995 | 201.893005 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 105 (day 5, h09) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999998 | 499.999998 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999998 | 499.999998 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 115 (day 5, h19) | 1.000 | 298.106995 | 201.893005 | -0.000000 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 80.204167 | 0.000000 | 0.000000 | 0.000000 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 59, 60, 61, 62, 63, 80, 81, 89, 90, 102, 103, 115, 116 | False |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 0, 1, 2, 3, 23, 28, 29, 30, 31, 43, 44, 45, 46 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 73 | none | False |

### Snapshot counterfactuals for this round

- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.56e-08 MW. diagnostic evidence (local solver artifact).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. diagnostic evidence (local solver artifact).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.54e-08 MW. diagnostic evidence (local solver artifact).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. diagnostic evidence (local solver artifact).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.56e-08 MW. diagnostic evidence (local solver artifact).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.32e-07 MW. diagnostic evidence (local solver artifact).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.47e-09 MW. diagnostic evidence (local solver artifact).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-09 MW. diagnostic evidence (local solver artifact).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.61e-09 MW. diagnostic evidence (local solver artifact).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 3.52e-09 MW. diagnostic evidence (local solver artifact).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 4.18e-09 MW. diagnostic evidence (local solver artifact).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 3.52e-09 MW. diagnostic evidence (local solver artifact).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.61e-09 MW. diagnostic evidence (local solver artifact).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-09 MW. diagnostic evidence (local solver artifact).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.47e-09 MW. diagnostic evidence (local solver artifact).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.32e-07 MW. diagnostic evidence (local solver artifact).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-06 MW. diagnostic evidence (local solver artifact).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.98e-09 MW. diagnostic evidence (local solver artifact).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.29e-09 MW. diagnostic evidence (local solver artifact).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.56e-09 MW. diagnostic evidence (local solver artifact).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.56e-09 MW. diagnostic evidence (local solver artifact).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.29e-09 MW. diagnostic evidence (local solver artifact).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.98e-09 MW. diagnostic evidence (local solver artifact).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-06 MW. diagnostic evidence (local solver artifact).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 125 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 106, 107, 108, 109, 110, 111, 112; represented annual output was 388.557 MWh. At periods 106, 107, 108, 109, 110, 111, 112, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 115.159491 | 0.000000 | 0.000000 | 9.982339 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 252.360923 | 0.000000 | 0.000000 | 9.858439 | none |
| 106 (day 5, h10) | 1.000 | 31.250000 | 468.750000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |
| 107 (day 5, h11) | 1.000 | 65.358558 | 434.641442 | -0.000000 | 0.000000 | 0.000000 | 0.457911 | none |
| 108 (day 5, h12) | 1.000 | 59.535913 | 440.464087 | -0.000000 | 0.000000 | 0.000000 | 0.464045 | none |
| 109 (day 5, h13) | 1.000 | 76.267798 | 423.732202 | -0.000000 | 0.000000 | 0.000000 | 0.446418 | none |
| 110 (day 5, h14) | 1.000 | 59.535913 | 440.464087 | -0.000000 | 0.000000 | 0.000000 | 0.464045 | none |
| 111 (day 5, h15) | 1.000 | 65.358558 | 434.641442 | -0.000000 | 0.000000 | 0.000000 | 0.457911 | none |
| 112 (day 5, h16) | 1.000 | 31.250000 | 468.750000 | 0.000000 | 0.000000 | 0.000000 | 0.263384 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 99, 119 | none | False |
| b01854 | 6108 → 6192 | lower | 523.000 | 523.000000 | 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 35, 36, 37, 38, 39, 51, 52, 53, 54, 55, 56, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 93, 94, 95, 96, 97, 98 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 12, 13, 14, 56, 57, 58, 59, 63, 64, 65, 66, 76, 77, 78, 79, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

- Period 106: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.9e-09 MW. diagnostic evidence (local solver artifact).
- Period 107: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.1e-09 MW. diagnostic evidence (local solver artifact).
- Period 108: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. diagnostic evidence (local solver artifact).
- Period 109: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.67e-08 MW. diagnostic evidence (local solver artifact).
- Period 110: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.88e-08 MW. diagnostic evidence (local solver artifact).
- Period 111: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.1e-09 MW. diagnostic evidence (local solver artifact).
- Period 112: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.9e-09 MW. diagnostic evidence (local solver artifact).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116; represented annual output was 407,202.537 MWh. Own generation was physically necessary for admitted load at verified periods 84, 85, 86, 105, 106, 107, 108, 109, 110, 111, 112, 113. At periods 59, 60, 61, 62, 63, 80, 81, 82, 83, 87, 88, 89, 90, 102, 103, 104, 114, 115, 116, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59 (day 3, h11) | 82.773 | 9.438491 | 490.561509 | 169.400000 | 0.000000 | 0.000000 | 22.815432 | b01841:lower |
| 60 (day 3, h12) | 82.773 | 125.000000 | 375.000000 | 135.995512 | 0.000000 | 0.000000 | 27.901256 | b01841:lower |
| 61 (day 3, h13) | 82.773 | 125.000000 | 375.000000 | 113.037666 | 0.000000 | 0.000000 | 27.901256 | b01841:lower |
| 62 (day 3, h14) | 82.773 | 125.000000 | 375.000000 | 135.995512 | 0.000000 | 0.000000 | 27.901256 | b01841:lower |
| 63 (day 3, h15) | 82.773 | 9.438491 | 490.561509 | 169.400000 | 0.000000 | 0.000000 | 22.815432 | b01841:lower |
| 80 (day 4, h08) | 97.732 | 125.000000 | 375.000000 | 81.251382 | 0.000000 | 0.000000 | 32.956167 | b01841:lower |
| 81 (day 4, h09) | 97.732 | 270.059892 | 229.940108 | -0.000000 | 0.000000 | 0.000000 | 23.675503 | b01841:lower |
| 82 (day 4, h10) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 12.870473 | none |
| 83 (day 4, h11) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 21.450788 | none |
| 84 (day 4, h12) | 97.732 | 490.228242 | 9.771758 | -0.000000 | 247.639077 | 247.639077 | 1.676895 | none |
| 85 (day 4, h13) | 97.732 | 500.000000 | 0.000000 | 0.000000 | 384.840509 | 384.840509 | 0.000000 | none |
| 86 (day 4, h14) | 97.732 | 490.228242 | 9.771758 | -0.000000 | 247.639077 | 247.639077 | 1.676895 | none |
| 87 (day 4, h15) | 97.732 | 375.000000 | 125.000000 | -0.000000 | 0.000000 | 0.000000 | 21.450788 | none |
| 88 (day 4, h16) | 97.732 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 12.870473 | none |
| 89 (day 4, h17) | 97.732 | 270.059892 | 229.940108 | -0.000000 | 0.000000 | 0.000000 | 23.675503 | b01841:lower |
| 90 (day 4, h18) | 97.732 | 125.000000 | 375.000000 | 81.251382 | 0.000000 | 0.000000 | 32.956167 | b01841:lower |
| 102 (day 5, h06) | 1.000 | 125.000000 | 375.000000 | 80.204167 | 0.000000 | 0.000000 | 0.337211 | b01841:lower |
| 103 (day 5, h07) | 1.000 | 298.106995 | 201.893005 | -0.000000 | 0.000000 | 0.000000 | 0.212702 | b01841:lower |
| 104 (day 5, h08) | 1.000 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.219487 | none |
| 105 (day 5, h09) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 106 (day 5, h10) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999998 | 499.999998 | 0.000000 | none |
| 107 (day 5, h11) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 112 (day 5, h16) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 499.999998 | 499.999998 | 0.000000 | none |
| 113 (day 5, h17) | 1.000 | 500.000000 | 0.000000 | 0.000000 | 462.119642 | 462.119642 | 0.000000 | none |
| 114 (day 5, h18) | 1.000 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.219487 | none |
| 115 (day 5, h19) | 1.000 | 298.106995 | 201.893005 | -0.000000 | 0.000000 | 0.000000 | 0.212702 | b01841:lower |
| 116 (day 5, h20) | 1.000 | 125.000000 | 375.000000 | 80.204167 | 0.000000 | 0.000000 | 0.337211 | b01841:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01607 | 6102 → 6004 | upper | 1,400.000 | 1,400.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01841 | 6102 → 6101 | lower | 1,307.000 | 1,307.000000 | 58, 59, 60, 61, 62, 63, 64, 79, 80, 81, 89, 90, 91, 100, 101, 102, 103, 115, 116, 117, 118 | 59, 60, 61, 62, 63, 80, 81, 89, 90, 102, 103, 115, 116 | False |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 0, 1, 2, 3, 23, 28, 29, 30, 31, 43, 44, 45, 46 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 73 | none | False |

### Snapshot counterfactuals for this round

- Period 59: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.56e-08 MW. diagnostic evidence (local solver artifact).
- Period 60: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. diagnostic evidence (local solver artifact).
- Period 61: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.54e-08 MW. diagnostic evidence (local solver artifact).
- Period 62: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1e-08 MW. diagnostic evidence (local solver artifact).
- Period 63: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 1.56e-08 MW. diagnostic evidence (local solver artifact).
- Period 80: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.32e-07 MW. diagnostic evidence (local solver artifact).
- Period 81: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.47e-09 MW. diagnostic evidence (local solver artifact).
- Period 82: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-09 MW. diagnostic evidence (local solver artifact).
- Period 83: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.61e-09 MW. diagnostic evidence (local solver artifact).
- Period 84: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 3.52e-09 MW. diagnostic evidence (local solver artifact).
- Period 85: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **384.840509 MW**; maximum nodal residual 4.18e-09 MW. diagnostic evidence (local solver artifact).
- Period 86: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **247.639077 MW**; maximum nodal residual 3.52e-09 MW. diagnostic evidence (local solver artifact).
- Period 87: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 3.61e-09 MW. diagnostic evidence (local solver artifact).
- Period 88: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.65e-09 MW. diagnostic evidence (local solver artifact).
- Period 89: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 7.47e-09 MW. diagnostic evidence (local solver artifact).
- Period 90: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 8.32e-07 MW. diagnostic evidence (local solver artifact).
- Period 102: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-06 MW. diagnostic evidence (local solver artifact).
- Period 103: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.98e-09 MW. diagnostic evidence (local solver artifact).
- Period 104: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.29e-09 MW. diagnostic evidence (local solver artifact).
- Period 105: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.56e-09 MW. diagnostic evidence (local solver artifact).
- Period 113: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **462.119642 MW**; maximum nodal residual 5.56e-09 MW. diagnostic evidence (local solver artifact).
- Period 114: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 4.29e-09 MW. diagnostic evidence (local solver artifact).
- Period 115: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 6.98e-09 MW. diagnostic evidence (local solver artifact).
- Period 116: minimum total own private generation, allowing native/rival redispatch. Status **verified**. Objective = **0.000000 MW**; maximum nodal residual 2.38e-06 MW. diagnostic evidence (local solver artifact).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. execution audit (local solver artifact).
Campaign SHA-256: `bc5ede93fbe5d6afcf4e0026b14333c1952cdcfba678f5ae2740a1bb9a2d5c82`.

accepted campaign (local solver artifact) · [experiment bundle](https://github.com/carterwg/ece51032-ercot-team/tree/9ad5075b1ecdb501fd063f56a328d9cbcd4a972f/analysis/strategy/ten-teams-500mw) · [source/input manifest](https://github.com/carterwg/ece51032-ercot-team/blob/9ad5075b1ecdb501fd063f56a328d9cbcd4a972f/analysis/strategy/ten-teams-500mw/manifest.json)

- week-2-submission-1: official evaluation and flows (local solver artifact); hourly energy ledger (local solver artifact); requested CSVs (local solver artifact).
- week-2-submission-2: official evaluation and flows (local solver artifact); hourly energy ledger (local solver artifact); requested CSVs (local solver artifact).
- week-3-submission-1: official evaluation and flows (local solver artifact); hourly energy ledger (local solver artifact); requested CSVs (local solver artifact).
- week-3-submission-2: official evaluation and flows (local solver artifact); hourly energy ledger (local solver artifact); requested CSVs (local solver artifact).

## Personal notes

<!-- USER_NOTES -->
