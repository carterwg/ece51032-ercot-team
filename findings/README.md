# Findings register

| Coverage | Count |
| --- | --- |
| Matched Part 2 campaign cases | 96 |
| Exploratory duplicate probes | 0 |
| Earlier baseline campaign records | 0 |
| Policy/layout summary files | 24 |
| Accepted scored rounds | 384 |

This folder contains Markdown only. Start with a policy/layout summary, then open its opponent-specific cases. Links under `runs/` refer to locally generated solver evidence. Saved game scores are separate from new hourly physical diagnostics. Failed attempts are never converted to zero scores.

| Strategy summary | Scenario/probe notes |
| --- | --- |
| [C_eq_G_S1_S2_500_1079](<C_eq_G_S1_S2_500_1079.md>) | 4 |
| [C_eq_G_S1_S2_500_1079_2054](<C_eq_G_S1_S2_500_1079_2054.md>) | 4 |
| [C_eq_G_S1_S2_500_1079_2054_2127_3046_3048](<C_eq_G_S1_S2_500_1079_2054_2127_3046_3048.md>) | 4 |
| [C_eq_G_S1_S2_500_6141](<C_eq_G_S1_S2_500_6141.md>) | 4 |
| [C_eq_G_S1_S2_500_6141_5395](<C_eq_G_S1_S2_500_6141_5395.md>) | 4 |
| [C_eq_G_S1_S2_500_6141_5395_6342_5451_6004](<C_eq_G_S1_S2_500_6141_5395_6342_5451_6004.md>) | 4 |
| [G_eq_0_S1_C_eq_G_S2_500_1079](<G_eq_0_S1_C_eq_G_S2_500_1079.md>) | 4 |
| [G_eq_0_S1_C_eq_G_S2_500_1079_2054](<G_eq_0_S1_C_eq_G_S2_500_1079_2054.md>) | 4 |
| [G_eq_0_S1_C_eq_G_S2_500_1079_2054_2127_3046_3048](<G_eq_0_S1_C_eq_G_S2_500_1079_2054_2127_3046_3048.md>) | 4 |
| [G_eq_0_S1_C_eq_G_S2_500_6141](<G_eq_0_S1_C_eq_G_S2_500_6141.md>) | 4 |
| [G_eq_0_S1_C_eq_G_S2_500_6141_5395](<G_eq_0_S1_C_eq_G_S2_500_6141_5395.md>) | 4 |
| [G_eq_0_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004](<G_eq_0_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004.md>) | 4 |
| [G_eq_0_S1_S2_500_1079](<G_eq_0_S1_S2_500_1079.md>) | 4 |
| [G_eq_0_S1_S2_500_1079_2054](<G_eq_0_S1_S2_500_1079_2054.md>) | 4 |
| [G_eq_0_S1_S2_500_1079_2054_2127_3046_3048](<G_eq_0_S1_S2_500_1079_2054_2127_3046_3048.md>) | 4 |
| [G_eq_0_S1_S2_500_6141](<G_eq_0_S1_S2_500_6141.md>) | 4 |
| [G_eq_0_S1_S2_500_6141_5395](<G_eq_0_S1_S2_500_6141_5395.md>) | 4 |
| [G_eq_0_S1_S2_500_6141_5395_6342_5451_6004](<G_eq_0_S1_S2_500_6141_5395_6342_5451_6004.md>) | 4 |
| [G_eq_125_S1_C_eq_G_S2_500_6141](<G_eq_125_S1_C_eq_G_S2_500_6141.md>) | 4 |
| [G_eq_125_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004](<G_eq_125_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004.md>) | 4 |
| [G_eq_250_S1_C_eq_G_S2_500_6141](<G_eq_250_S1_C_eq_G_S2_500_6141.md>) | 4 |
| [G_eq_250_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004](<G_eq_250_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004.md>) | 4 |
| [G_eq_375_S1_C_eq_G_S2_500_6141](<G_eq_375_S1_C_eq_G_S2_500_6141.md>) | 4 |
| [G_eq_375_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004](<G_eq_375_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004.md>) | 4 |

## How to read the measurements

- C and G are requested new MW per submission; admitted capacity can be lower.
- Dollar scores use the course’s present-value economics, summed over four graded submissions. Gross IT value is shown separately from net score and costs.
- Modeled generator hours count distinct operating periods above 0.000001 MW output. Annual hours/MWh use the actual representative-day weights; 3 of 120 modeled hours need not mean 3/120 of a year.
- “Required” refers to fixed admitted loads with rival generation allowed to redispatch. Actual generator use alone does not establish necessity.
- Actual binding lines, Part 1 candidate lines, and finite-relaxation-confirmed causes are labeled separately. Observing a tight line does not prove it caused a shortage.
- A snapshot line-relief diagnostic is not a full horizon allocation rerun or a revised campaign score.
- Scenario means are descriptive equal-weight stress comparisons, not calibrated probabilities.

## Other evidence

- [Matched campaign comparison of Carter, Garcia, the two hybrids, and the 200 and 210 MW generators](Battery_S1_peer_campaign_comparison.md)

- [S1 sizing in 1 MW increments](Battery_S1_1MW_local_search.md)

- [Battery_S1_comparison](<Battery_S1_comparison.md>)
- [Battery_S1_targeted_optimization](<Battery_S1_targeted_optimization.md>)
- [HISTORY_intermediate_and_validation_runs](<HISTORY_intermediate_and_validation_runs.md>)
- [HISTORY_standalone_bottleneck_verification](<HISTORY_standalone_bottleneck_verification.md>)
- [Part1_alternative_split_500](<Part1_alternative_split_500.md>)
- [Part1_baseline](<Part1_baseline.md>)
- [Part1_directional_tests](<Part1_directional_tests.md>)
- [Part1_distributed_2000](<Part1_distributed_2000.md>)
- [Part1_generation_500](<Part1_generation_500.md>)
- [Part1_groups_and_interactions](<Part1_groups_and_interactions.md>)
- [Part1_hub_2000](<Part1_hub_2000.md>)
- [Part1_hub_2500](<Part1_hub_2500.md>)
- [Part1_hub_500](<Part1_hub_500.md>)
- [Part1_shared_line_2500](<Part1_shared_line_2500.md>)
- [Part1_shared_line_500](<Part1_shared_line_500.md>)
- [Ten_teams_500_MW_comparison](<Ten_teams_500_MW_comparison.md>)
- [Ten_teams_evaluator_controls](<Ten_teams_evaluator_controls.md>)

## Updating the register

Completed experiment commands export findings automatically. Rebuild/backfill with:

```bash
PYTHONPATH=src:ercot-connection-game:ercot-connection-game/src .venv/bin/python -m team_strategy.experiments.findings
```

For a particular saved experiment, add `--bundle runs/EXPERIMENT`. Diagnostic JSON caches remain outside this folder under `runs/findings-diagnostics/`. Text added below a file’s `Personal notes` marker is preserved on regeneration.

## Personal notes

<!-- USER_NOTES -->
