<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_S2_500_6141","policy":"G_eq_0_S1_S2","portfolio":"bottleneck_ptdf_1_grid","buses":["6141"],"weights":[1.0],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign","campaign_sha256":"7354607c34d1762484166abc8bce6465c6ef6daf6d7bee33bf43c4383e641ffd","score_usd":21615073282.723923,"it_value_usd":36971256281.84716,"grid_mwh":5263875.142102503,"generation_mwh":0.0,"modeled_generator_hours":0.0,"annual_generator_hours":0.0,"required_annual_hours":0.0,"minimum_admission":6.0083890216637636e-05,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/7354607c34d1762484166abc8bce6465c6ef6daf6d7bee33bf43c4383e641ffd-3eea05334a1d.json"} -->
# G_eq_0_S1_S2_500_6141 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 300.419452 | 300.419452 | 18.483780 | 10.973293 |
| week-2-submission-2 | 500.000 | 0.000 | 0.030042 | 300.449494 | 0.001848 | 0.001097 |
| week-3-submission-1 | 500.000 | 0.000 | 300.419452 | 300.419452 | 18.483780 | 10.639619 |
| week-3-submission-2 | 500.000 | 0.000 | 0.030042 | 300.449494 | 0.001848 | 0.001064 |
| Campaign total | — | — | — | — | 36.971256 | 21.615073 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,631,674.404 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 263.167 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-1 | 2,631,674.404 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 263.167 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.510486 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.000000 | 0.000000 | 0.000751 | 0.000000 |
| week-3-submission-1 | 0.333675 | 0.000000 | 0.000000 | 7.510486 | 0.000000 |
| week-3-submission-2 | 0.000033 | 0.000000 | 0.000000 | 0.000751 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_S2`.
- Layout: 6141: 500 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
- Seed: 17. Included in competitive means: True. No calibrated probability is assigned to this hypothesis.
- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.

## What happened and why

### week-2-submission-1

Requested 500 MW load and 0 MW generation; admitted **300.419452 MW** (60.083890%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 179.171013 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 300.419452 | 20.409534 | 0.000000 | 0.000000 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | none | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **300.719902 MW**; maximum nodal residual 2.86e-08 MW. Generation-only capacity ceiling = 320.828987 MW; limiting-resource diagnosis: transmission. [diagnostic evidence](<../runs/findings-diagnostics/probes/7c1a6a100d499ad97415ebfacb79a8cc866398df8825d8a6239f33aaea266a21.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 300.719902 | 320.828987 | 20.109084 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.030042 MW** (0.006008%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 479.860844 MW. Local line restrictions can be stronger. No own private output was dispatched. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.030042 | 20.109115 | 0.000000 | 0.000000 | 0.000000 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | none | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.030072 MW**; maximum nodal residual 2.41e-08 MW. Generation-only capacity ceiling = 20.139156 MW; limiting-resource diagnosis: transmission. [diagnostic evidence](<../runs/findings-diagnostics/probes/8cef16e46c2cb1a7f927c15885a78e4f2333c8e0e19495e592e2ba8449a42e37.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 0.030072 | 20.139156 | 20.109084 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **300.419452 MW** (60.083890%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 179.171013 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 300.419452 | 2,248.166398 | 0.000000 | 0.000000 | 4.035637 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 300.419452 | 2,110.964966 | 0.000000 | 0.000000 | 4.036049 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 300.419452 | 2,248.166398 | 0.000000 | 0.000000 | 4.035637 | none |
| 109 (day 5, h13) | 1.000 | 0.000000 | 300.419452 | 20.409534 | 0.000000 | 0.000000 | 0.060576 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | none | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **300.719902 MW**; maximum nodal residual 2.86e-08 MW. Generation-only capacity ceiling = 320.828987 MW; limiting-resource diagnosis: transmission. [diagnostic evidence](<../runs/findings-diagnostics/probes/7c1a6a100d499ad97415ebfacb79a8cc866398df8825d8a6239f33aaea266a21.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 300.719902 | 320.828987 | 20.109084 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 0 MW generation; admitted **0.030042 MW** (0.006008%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 479.860844 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 0.030042 | 2,247.865979 | 0.000000 | 0.000000 | 0.000404 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 0.030042 | 2,110.664547 | 0.000000 | 0.000000 | 0.000404 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 0.030042 | 2,247.865979 | 0.000000 | 0.000000 | 0.000404 | none |
| 109 (day 5, h13) | 1.000 | 0.000000 | 0.030042 | 20.109115 | 0.000000 | 0.000000 | 0.000006 | b02136:lower |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 108, 109, 110, 111 | none | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **0.030072 MW**; maximum nodal residual 2.41e-08 MW. Generation-only capacity ceiling = 20.139156 MW; limiting-resource diagnosis: transmission. [diagnostic evidence](<../runs/findings-diagnostics/probes/8cef16e46c2cb1a7f927c15885a78e4f2333c8e0e19495e592e2ba8449a42e37.json>).

| Rating increased by 1 MW on | Status | Objective before MW | Objective after MW | Improvement MW | Causal effect observed |
| --- | --- | --- | --- | --- | --- |
| b02136 | verified | 0.030072 | 20.139156 | 20.109084 | True |


These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b02136:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/execution.json>).
Campaign SHA-256: `7354607c34d1762484166abc8bce6465c6ef6daf6d7bee33bf43c4383e641ffd`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_1_grid/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
