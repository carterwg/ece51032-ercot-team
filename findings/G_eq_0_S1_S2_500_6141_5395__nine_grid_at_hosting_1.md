<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_S2_500_6141_5395","policy":"G_eq_0_S1_S2","portfolio":"bottleneck_ptdf_2_grid","buses":["6141","5395"],"weights":[0.5,0.5],"scenario":"nine_grid_at_hosting_1","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign","campaign_sha256":"c736f9262b6e5529adaee9f501b7d35688656d8bd2f77e87a956048b08b23745","score_usd":21758985346.34397,"it_value_usd":37218703232.2392,"grid_mwh":5299106.020956815,"generation_mwh":0.0,"modeled_generator_hours":0.0,"annual_generator_hours":0.0,"required_annual_hours":0.0,"minimum_admission":6.0486148057958644e-05,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/c736f9262b6e5529adaee9f501b7d35688656d8bd2f77e87a956048b08b23745-3eea05334a1d.json"} -->
# G_eq_0_S1_S2_500_6141_5395 — nine_grid_at_hosting_1

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 302.430146 | 302.430146 | 18.607491 | 11.046737 |
| week-2-submission-2 | 500.000 | 0.000 | 0.030243 | 302.460389 | 0.001861 | 0.001105 |
| week-3-submission-1 | 500.000 | 0.000 | 302.430146 | 302.430146 | 18.607491 | 10.710072 |
| week-3-submission-2 | 500.000 | 0.000 | 0.030243 | 302.460389 | 0.001861 | 0.001071 |
| Campaign total | — | — | — | — | 37.218703 | 21.758985 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,649,288.081 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 264.929 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-1 | 2,649,288.081 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 264.929 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.000000 | 0.000000 | 0.000756 | 0.000000 |
| week-3-submission-1 | 0.336665 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-3-submission-2 | 0.000034 | 0.000000 | 0.000000 | 0.000756 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_S2`.
- Layout: 6141: 250 MW per submission, 5395: 250 MW per submission.
- Opponents: 9. Each uses 1079 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430146 MW** (60.486029%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267393 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430146 | 0.302460 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 9, 10, 11, 12, 13, 14, 15, 16, 17, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 7.44e-09 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/1b034c1dad32681a650c2e7afe6a724c5361fe095160d91a2d6ba17d2766ee8b.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 7.49e-09 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/7865c19da988406aabee0eab08176448603e1be8b33e1929a206bf57013a5a7e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.030243 MW** (0.006049%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 499.969727 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.030243 | 0.000030 | 0.000000 | 0.000000 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 9, 10, 11, 12, 13, 14, 15, 16, 17, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.015152 MW**; maximum nodal residual 2.88e-09 MW. Generation-only capacity ceiling = 0.015152 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/a7e0b7996a6ce38fdadffae87f3d7e62bcf30dbea57d31237e1b00d2a89f0258.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.015152 MW**; maximum nodal residual 6.22e-09 MW. Generation-only capacity ceiling = 0.015152 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d1fe0d0ec95d826aec5bf2013f127f82fbb56f1b5d779db9e32d54706a3f634.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430146 MW** (60.486029%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267393 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 302.430146 | 2,228.059324 | 0.000000 | 0.000000 | 4.026809 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 302.430146 | 2,090.857892 | 0.000000 | 0.000000 | 4.026809 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 302.430146 | 2,228.059324 | 0.000000 | 0.000000 | 4.026809 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430146 | 0.302460 | 0.000000 | 0.000000 | 0.061781 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 9, 10, 11, 12, 13, 14, 15, 16, 17, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 7.44e-09 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/1b034c1dad32681a650c2e7afe6a724c5361fe095160d91a2d6ba17d2766ee8b.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 7.49e-09 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/7865c19da988406aabee0eab08176448603e1be8b33e1929a206bf57013a5a7e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.030243 MW** (0.006049%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 499.969727 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 0.030243 | 2,227.756894 | 0.000000 | 0.000000 | 0.000403 | b02579:lower |
| 85 (day 4, h13) | 97.732 | 0.000000 | 0.030243 | 2,090.555462 | 0.000000 | 0.000000 | 0.000403 | b02579:lower |
| 86 (day 4, h14) | 97.732 | 0.000000 | 0.030243 | 2,227.756894 | 0.000000 | 0.000000 | 0.000403 | b02579:lower |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.030243 | 0.000030 | 0.000000 | 0.000000 | 0.000006 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02579 | 8004 → 7150 | lower | 647.000 | 647.000000 | 9, 10, 11, 12, 13, 14, 15, 16, 17, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119 | none | True |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.015152 MW**; maximum nodal residual 2.88e-09 MW. Generation-only capacity ceiling = 0.015152 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/a7e0b7996a6ce38fdadffae87f3d7e62bcf30dbea57d31237e1b00d2a89f0258.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.015152 MW**; maximum nodal residual 6.22e-09 MW. Generation-only capacity ceiling = 0.015152 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/9d1fe0d0ec95d826aec5bf2013f127f82fbb56f1b5d779db9e32d54706a3f634.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b01548:lower`, `b02136:lower`, `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/execution.json>).
Campaign SHA-256: `c736f9262b6e5529adaee9f501b7d35688656d8bd2f77e87a956048b08b23745`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_grid/nine_grid_at_hosting_1/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
