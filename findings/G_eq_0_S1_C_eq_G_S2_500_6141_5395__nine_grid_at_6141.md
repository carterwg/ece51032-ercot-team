<!-- findings-record: {"schema":1,"kind":"campaign","stem":"G_eq_0_S1_C_eq_G_S2_500_6141_5395","policy":"G_eq_0_S1_C_eq_G_S2","portfolio":"bottleneck_ptdf_2_s2_cg","buses":["6141","5395"],"weights":[0.5,0.5],"scenario":"nine_grid_at_6141","risk":true,"exploratory":false,"bundle":"analysis/strategy/ten-teams-500mw","campaign_output":"runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign","campaign_sha256":"96eef5bf74f21c4d291cd4b3ee9838782f0c0d4125657ebce837c6e0c9dd1584","score_usd":55724391669.71039,"it_value_usd":98741556025.31665,"grid_mwh":14056124.968291413,"generation_mwh":2451.194006551183,"modeled_generator_hours":6.0,"annual_generator_hours":6.000000000057237,"required_annual_hours":6.000000000057237,"minimum_admission":0.604860292500109,"scenario_count_in_bundle":4,"bundle_status":"complete","diagnostic_cache":"runs/findings-diagnostics/cases/96eef5bf74f21c4d291cd4b3ee9838782f0c0d4125657ebce837c6e0c9dd1584-3eea05334a1d.json"} -->
# G_eq_0_S1_C_eq_G_S2_500_6141_5395 — nine_grid_at_6141

| Round | Requested C MW | Requested G MW | Admitted new C MW | Own operating C incl. S1 MW | Gross IT value $B | Net score $B |
| --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000 | 0.000 | 302.430146 | 302.430146 | 18.607491 | 11.046737 |
| week-2-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430146 | 30.763287 | 17.262093 |
| week-3-submission-1 | 500.000 | 0.000 | 302.430146 | 302.430146 | 18.607491 | 10.710784 |
| week-3-submission-2 | 500.000 | 500.000 | 500.000000 | 802.430146 | 30.763287 | 16.704778 |
| Campaign total | — | — | — | — | 98.741556 | 55.724392 |

| Round | Grid MWh/year | Private gen MWh/year | Grid energy share | Gen on: modeled h | Gen on: annual h | Verified required-on annual h | Unresolved-on annual h | Peak private MW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 2,649,288.081 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-2-submission-2 | 4,378,774.403 | 1,225.597 | 99.972018% | 3.000 | 3.000 | 3.000 | 0.000 | 499.999970 |
| week-3-submission-1 | 2,649,288.081 | 0.000 | 100.000000% | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 |
| week-3-submission-2 | 4,378,774.403 | 1,225.597 | 99.972018% | 3.000 | 3.000 | 3.000 | 0.000 | 499.999970 |

| Round | Grid energy $B | Generator operation $B | Generator capital $B | Site capital $B | Storage capital $B |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 0.000000 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-2-submission-2 | 0.000000 | 0.001195 | 1.000000 | 12.500000 | 0.000000 |
| week-3-submission-1 | 0.335953 | 0.000000 | 0.000000 | 7.560754 | 0.000000 |
| week-3-submission-2 | 0.557315 | 0.001195 | 1.000000 | 12.500000 | 0.000000 |

**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.

**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.

## Test setup

- Policy: `G_eq_0_S1_C_eq_G_S2`.
- Layout: 6141: 250 MW per submission, 5395: 250 MW per submission.
- Opponents: 9. Each uses 6141 (500 MW) per submission. G/C is 0 in S1 and 0 in S2.
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
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 111 | none | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 78, 92 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 4.41e-09 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/2174298808cf1665961b77d4360e05a3ce0457f071a5a0a879bc5759155f4e8e.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 1.64e-08 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a366fdba2d6f052cfa0e7cbdc0cc4ecfbe1d27e164a12c5cb35cc0d5091230e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-2-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,225.597 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110. Week 2 does not charge grid purchases, but network constraints still apply.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 108 (day 5, h12) | 1.000 | 362.798517 | 137.201483 | -0.000000 | 362.798517 | 362.798517 | 0.000000 | none |
| 109 (day 5, h13) | 1.000 | 499.999970 | 0.000030 | 0.000000 | 499.999970 | 499.999970 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 362.798517 | 137.201483 | -0.000000 | 362.798517 | 362.798517 | 0.000000 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 96, 97, 98 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 99, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-1

Requested 500 MW load and 0 MW generation; admitted **302.430146 MW** (60.486029%). The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at 3 modeled periods; the largest own backup lower bound is 197.267393 MW. Local line restrictions can be stronger. No own private output was dispatched.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 (day 4, h12) | 97.732 | 0.000000 | 302.430146 | 2,228.059324 | 0.000000 | 0.000000 | 4.062647 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 302.430146 | 2,090.857892 | 0.000000 | 0.000000 | 4.063063 | none |
| 86 (day 4, h14) | 97.732 | 0.000000 | 302.430146 | 2,228.059324 | 0.000000 | 0.000000 | 4.062647 | none |
| 109 (day 5, h13) | 1.000 | 0.000000 | 302.430146 | 0.302460 | 0.000000 | 0.000000 | 0.061781 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b02136 | 6294 → 6293 | lower | 217.800 | 217.800000 | 107, 111 | none | True |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 78, 92 | none | False |

### Snapshot counterfactuals for this round

- Period 109: maximum grid-only load at 6141, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 4.41e-09 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/2174298808cf1665961b77d4360e05a3ce0457f071a5a0a879bc5759155f4e8e.json>).
- Period 109: maximum grid-only load at 5395, keeping our other sites’ recorded net withdrawals fixed. Status **verified**. Objective = **151.517534 MW**; maximum nodal residual 1.64e-08 MW. Generation-only capacity ceiling = 151.517534 MW; limiting-resource diagnosis: system_generation. [diagnostic evidence](<../runs/findings-diagnostics/probes/2a366fdba2d6f052cfa0e7cbdc0cc4ecfbe1d27e164a12c5cb35cc0d5091230e.json>).

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

### week-3-submission-2

Requested 500 MW load and 500 MW generation; admitted **500.000000 MW** (100.000000%). All requested load was admitted. Private generation ran at periods 108, 109, 110; represented annual output was 1,225.597 MWh. Own generation was physically necessary for admitted load at verified periods 108, 109, 110.

| Period (zero-based) | Annual h represented | Actual private MW | Actual grid MW | Native spare after admitted net loads MW | Generation-only min own MW | Verified min own MW | Weighted grid bill $M | Actual tight lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 (day 4, h11) | 97.732 | 0.000000 | 500.000000 | 2,130.011216 | 0.000000 | 0.000000 | 6.717357 | none |
| 84 (day 4, h12) | 97.732 | 0.000000 | 500.000000 | 1,727.756894 | 0.000000 | 0.000000 | 6.717357 | none |
| 85 (day 4, h13) | 97.732 | 0.000000 | 500.000000 | 1,590.555462 | 0.000000 | 0.000000 | 6.717357 | none |
| 108 (day 5, h12) | 1.000 | 362.798517 | 137.201483 | -0.000000 | 362.798517 | 362.798517 | 0.144547 | none |
| 109 (day 5, h13) | 1.000 | 499.999970 | 0.000030 | 0.000000 | 499.999970 | 499.999970 | 0.000000 | none |
| 110 (day 5, h14) | 1.000 | 362.798517 | 137.201483 | -0.000000 | 362.798517 | 362.798517 | 0.144547 | none |

The generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.

| Observed binding branch | Endpoints | Direction | Rating MW | Max absolute flow MW | Binding periods | Binding while our gen on | Part 1 candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b01921 | 6239 → 6141 | upper | 2,400.000 | 2,400.000000 | 96, 97, 98 | none | False |
| b02355 | 7058 → 7095 | lower | 2,295.000 | 2,295.000000 | 24, 25, 26, 27, 28, 29, 45, 46, 47, 57, 65, 78, 92, 99, 119 | none | False |

### Snapshot counterfactuals for this round

No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.

These are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.

## Part 1 hypotheses and interpretation limits

Potential signatures from the electrical grouping: `b01548:lower`, `b02136:lower`, `b02579:lower`. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.
This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.

## Reproducibility and numerical history

No per-cell numerical retry is recorded in this cell.

The evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. [execution audit](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/execution.json>).
Campaign SHA-256: `96eef5bf74f21c4d291cd4b3ee9838782f0c0d4125657ebce837c6e0c9dd1584`.

[accepted campaign](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/campaign.json>) · [experiment bundle](<../analysis/strategy/ten-teams-500mw>) · [source/input manifest](<../analysis/strategy/ten-teams-500mw/manifest.json>)

- week-2-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-1/inputs>).
- week-2-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-2-submission-2/inputs>).
- week-3-submission-1: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-1/inputs>).
- week-3-submission-2: [official evaluation and flows](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/canonical/evaluation.json>); [hourly energy ledger](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/canonical/site_net_withdrawal.csv>); [requested CSVs](<../runs/ten-teams-500mw/campaigns/bottleneck_ptdf_2_s2_cg/nine_grid_at_6141/attempt-01/campaign/week-3-submission-2/inputs>).

## Personal notes

<!-- USER_NOTES -->
