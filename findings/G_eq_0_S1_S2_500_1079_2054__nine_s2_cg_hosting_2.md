<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_S2_500_1079_2054","policy":"G_eq_0_S1_S2","portfolio":"hosting_2_grid","buses":["1079","2054"],"weights":[0.5,0.5],"scenario":"nine_s2_cg_hosting_2","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign","campaign_sha256":"a35d244451419033354d976176be03e585f6b7ce975ab3c3db95b3ba5bcae92b","score_usd":21776173395.962677,"it_value_usd":37252198458.04775,"grid_mwh":5303874.987560734,"generation_mwh":0.0,"modeled_generator_hours":0.0,"annual_generator_hours":0.0,"required_annual_hours":0.0,"minimum_admission":0.0006048615153424853,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/a35d244451419033354d976176be03e585f6b7ce975ab3c3db95b3ba5bcae92b-3eea05334a1d.json"} -->
# G_eq_0_S1_S2_500_1079_2054 — nine_s2_cg_hosting_2

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 302.430160 | 302.430160 | 18.607492 | 11.046738 |
| week-2-submission-2 | 500.000 | 0.000 | 0.302431 | 302.732591 | 0.018608 | 0.011047 |
| week-3-submission-1 | 500.000 | 0.000 | 302.430160 | 302.430160 | 18.607492 | 10.708609 |
| week-3-submission-2 | 500.000 | 0.000 | 0.302431 | 302.732591 | 0.018608 | 0.009780 |
| Campaign total | — | — | — | — | 37.252198 | 21.776173 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,649,288.200 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 2,649.293 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-1 | 2,649,288.200 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 2,649.293 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.000000 | 0.000000 | 0.007561 | 0.000000 |
| week-3-submission-1 | 0.338129 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-3-submission-2 | 0.001266 | 0.000000 | 0.000000 | 0.007561 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_S2`.
- Layout: 1079: 250 MW per submission, 2054: 250 MW per submission.
- Opponents: 9. Each uses 1079 (250 MW), 2054 (250 MW) per submission. G/C is 0 in S1 and 1 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430160 MW** (60.486032%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267380 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430160 | 0.302460 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 5.23e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/3519aae7c51a339690f6f0e98a260b94b5498878a8eab8dc4e018818f41cba1c.json>).
- Period 109: maximum grid-only load at 2054, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 7.18e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/a21a7d63a6e4463e8d8d4779dad8d3d884c6b91f112a072081e803291c69443d.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.302431 MW** (0.060486%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 499.697539 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.302431 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 30, 31, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | none | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.151246 MW**; maximum nodal residual 3.69e-09 MW. Generation-only capacity ceiling = 0.151246 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/e31bf8e21ad066989cef26697b02838b99ce983745ced6f67860d798cebce2d0.json>).
- Period 109: maximum grid-only load at 2054, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.151246 MW**; maximum nodal residual 5.21e-09 MW. Generation-only capacity ceiling = 0.151246 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/4dafa896e51147354b8e2c318747c758dba8c013a55cc73a66af74a6aa15e669.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430160 MW** (60.486032%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267380 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 302.430160 | 2,228.059324 | 0.000000 | 0.000000 | 4.077993 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 302.430160 | 2,090.857892 | 0.000000 | 0.000000 | 4.077993 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 302.430160 | 2,228.059324 | 0.000000 | 0.000000 | 4.077993 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430160 | 0.302460 | 0.000000 | 0.000000 | 0.061781 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 5.23e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/3519aae7c51a339690f6f0e98a260b94b5498878a8eab8dc4e018818f41cba1c.json>).
- Period 109: maximum grid-only load at 2054, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517540 MW**; maximum nodal residual 7.18e-09 MW. Generation-only capacity ceiling = 151.517540 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/a21a7d63a6e4463e8d8d4779dad8d3d884c6b91f112a072081e803291c69443d.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.302431 MW** (0.060486%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 499.697539 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 0.302431 | 847.330479 | 0.000000 | 0.000000 | 0.031800 | b02579:lower |
| 84 (day 4, h12) | 97.732 | 0.000000 | 0.302431 | 702.628748 | 0.000000 | 0.000000 | 0.031800 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 0.302431 | 653.273691 | 0.000000 | 0.000000 | 0.031800 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.302431 | 0.000000 | 0.000000 | 0.000000 | 0.000531 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b00220 | 2054 → 5236 | lower | 2,020.000 | 2,020.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 92, 93, 94, 95, 96, 97, 98, 99, 100, 118, 119 | none | False |
| b01347 | 5239 → 6210 | lower | 2,020.000 | 2,020.000000 | 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 30, 31, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 116, 117, 118, 119 | none | False |
| b01983 | 6230 → 6176 | upper | 221.000 | 221.000000 | 81, 82, 88, 89, 103, 104, 114, 115 | none | False |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 1079, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.151246 MW**; maximum nodal residual 3.69e-09 MW. Generation-only capacity ceiling = 0.151246 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/e31bf8e21ad066989cef26697b02838b99ce983745ced6f67860d798cebce2d0.json>).
- Period 109: maximum grid-only load at 2054, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.151246 MW**; maximum nodal residual 5.21e-09 MW. Generation-only capacity ceiling = 0.151246 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/4dafa896e51147354b8e2c318747c758dba8c013a55cc73a66af74a6aa15e669.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.
Campaign SHA-256: `a35d244451419033354d976176be03e585f6b7ce975ab3c3db95b3ba5bcae92b`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/hosting_2_grid/nine_s2_cg_hosting_2/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
