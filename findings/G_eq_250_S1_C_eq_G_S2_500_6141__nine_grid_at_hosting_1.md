<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_250_S1_C_eq_G_S2_500_6141","policy":"G_eq_250_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_1_s1_250_s2_cg","buses":["6141"],"weights":[1.0],"scenario":"nine_grid_at_hosting_1","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign","campaign_sha256":"4c1dbcead714467c4de56dde8805109eab70c3b697d0782a6b6fdae69a17374e","score_usd":68933638063.41907,"it_value_usd":123053148597.11996,"grid_mwh":17515209.400190227,"generation_mwh":4790.5998060485,"modeled_generator_hours":16.0,"annual_generator_hours":16.00000000015263,"required_annual_hours":16.00000000015263,"minimum_admission":1.0,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/4c1dbcead714467c4de56dde8805109eab70c3b697d0782a6b6fdae69a17374e-3eea05334a1d.json"} -->
# G_eq_250_S1_C_eq_G_S2_500_6141 — nine_grid_at_hosting_1

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 250.000 | 500.000000 | 500.000000 | 30.763287 | 17.762835 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 17.261308 |
| week-3-submission-1 | 500.000 | 250.000 | 500.000000 | 500.000000 | 30.763287 | 17.205947 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 1,000.000000 | 30.763287 | 16.703548 |
| Campaign total | — | — | — | — | 123.053149 | 68.933638 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,525.234 | 474.766 | 99.989161% | 3.000 | 3.000 | 3.000 | 0.000 | 249.722867 |
| week-2-submission-2 | 4,378,079.466 | 1,920.534 | 99.956152% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |
| week-3-submission-1 | 4,379,525.234 | 474.766 | 99.989161% | 3.000 | 3.000 | 3.000 | 0.000 | 249.722867 |
| week-3-submission-2 | 4,378,079.466 | 1,920.534 | 99.956152% | 5.000 | 5.000 | 5.000 | 0.000 | 500.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000452 | 0.500000 | 12.500000 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.001979 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.556888 | 0.000452 | 0.500000 | 12.500000 | 0.000000 |
| week-3-submission-2 | 0.557760 | 0.001979 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_250_S1_C_eq_G_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 1079 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
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
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,920.534 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 (day 5, h11) | 1.000 | 210.267104 | 289.732896 | -0.000000 | 210.267104 | 210.267104 | 0.000000 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 210.267104 | 289.732896 | -0.000000 | 210.267104 | 210.267104 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 25 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 250 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 474.766 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,978.033997 | 0.000000 | 0.000000 | 6.717357 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,840.832565 | 0.000000 | 0.000000 | 6.717357 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 500.000000 | 1,978.033997 | 0.000000 | 0.000000 | 6.717357 | b02579:lower |
| 108 (day 5, h12) | 1.000 | 112.521414 | 387.478586 | -0.000000 | 112.521414 | 112.521414 | 0.408223 | none |
| 109 (day 5, h13) | 1.000 | 249.722867 | 250.277133 | -0.000000 | 249.722867 | 249.722867 | 0.439460 | none |
| 110 (day 5, h14) | 1.000 | 112.521414 | 387.478586 | -0.000000 | 112.521414 | 112.521414 | 0.408223 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 107, 108, 109, 110, 111; represented annual output was 1,920.534 MWh. Own generation was physically necessary for admitted load at verified periods 107, 108, 109, 110, 111.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 1,880.288319 | 0.000000 | 0.000000 | 6.717357 | none |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,478.033997 | 0.000000 | 0.000000 | 6.717357 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,340.832565 | 0.000000 | 0.000000 | 6.725594 | none |
| 107 (day 5, h11) | 1.000 | 210.267104 | 289.732896 | -0.000000 | 210.267104 | 210.267104 | 0.305244 | none |
| 108 (day 5, h12) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 500.000000 | 0.000000 | -0.000000 | 500.000000 | 500.000000 | 0.000000 | none |
| 111 (day 5, h15) | 1.000 | 210.267104 | 289.732896 | -0.000000 | 210.267104 | 210.267104 | 0.305244 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 25 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 115, 116, 117, 118, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/execution.json>).
Campaign SHA-256: `4c1dbcead714467c4de56dde8805109eab70c3b697d0782a6b6fdae69a17374e`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_s1_250_s2_cg/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
