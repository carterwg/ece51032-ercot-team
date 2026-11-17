# Reusable strategy interpretation

Open [main_template.ipynb](main_template.ipynb) for the team's common results
interpretation workflow. It ships with executed outputs for the baseline at bus
1001 and Carter's rank-1 bus 6141, using only the finalized 500 MW case.

## Executed strategy reports

| Notebook | Strategy |
| --- | --- |
| [01_full_generation_baseline.ipynb](01_full_generation_baseline.ipynb) | C = G baseline, one new site per submission at bus 1001 |
| [02_carter_rank1_cg.ipynb](02_carter_rank1_cg.ipynb) | Same C = G capacities at Carter's rank-1 bus 6141 |

Both reports are derived from the shared template and include executed plots,
500 MW campaign totals, and calculated findings. Each report focuses on its own
strategy; the main template compares them together. All three notebooks read
saved 500 MW results without rerunning the game. Obsolete capacity runs and
reports have been removed.

From the team repository root, with the team environment active:

```bash
python -m pip install -e '.[notebook]'
jupyter lab notebooks/main_template.ipynb
```

Select the team's Python environment as the notebook kernel. Edit only the
**Inputs and selectors** cell for ordinary reuse, then restart the kernel and
run all cells. Add a `ResultSource` per strategy, select the experiment and
scenario, and choose a focus strategy for the waterfall. The only experiment
is `finalized-500mw`. Budgets above 500 MW are rejected by the team framework.

## Figure templates

1. Per-submission scores.
2. Cumulative score contributions across the four graded submissions.
3. Combined campaign scores and unclipped normalized Q against the two anchors.
4. Cost components, gross IT value, and net score.
5. A focus-strategy economic waterfall.
6. Allocated/requested connection-capacity fractions.
7. Weighted electricity supplied by the grid and private generation.
8. Optional hourly grid withdrawal and served-load profiles, with site-plan tables.
9. Average normalized score versus downside risk and Pareto membership, when
   matched multi-scenario campaigns exist.

The current solo runs are not enough to estimate downside risk. The risk panel
explains that limitation instead of plotting a made-up zero-risk point. Different
capacity caps are never treated as two risk scenarios. To enable this panel,
load multiple matched campaign scenarios or set `RISK_CAMPAIGNS_FILE` to a real
[CLI-format campaign input](../docs/SCORING.md#report-input) at the same budget.

## Input contract

Each `ResultSource` supplies a strategy ID, display label, campaign summary JSON,
and optionally a per-round details CSV. The two existing files under `analysis/`
are concrete examples. Monetary values in summary JSON are **USD**; convenience
CSV monetary values are **billions**. The loader checks their agreement.

Summary JSON needs a `campaigns` list. Each campaign records:

- `experiment`, `capacity_per_submission_mw`, and `hypothetical_capacity_override`.
- `source_scenario_sha256`, `effective_rules_sha256`, and `effective_release_sha256`
  so comparisons use a matching initial network and rules.
- An optional `scenario_id` (default `solo`). IDs must describe matched opponent
  assumptions across strategies; each strategy retains its own S1-to-S2 history.
- `rounds`, with unique graded round keys, validity/feasibility flags, service
  fractions, and the complete official score breakdown: IT value, grid energy,
  generator operation, generator capital, storage capital, and site cost.

The optional CSV supplies matching `experiment`, capacity, `round`, and
`score_billions`, plus `bus_id`, `grid_supply_share`, and
`private_generation_share`. Include `scenario_id` when needed. Missing energy
details skip the supply chart; they are not inferred from installed capacities.

Missing rounds remain missing, and incomplete campaigns do not receive Q.
Genuinely rejected submissions may have a scored zero; evaluator failures and
missing scores must not be substituted with zero. Storage costs come from the
summary even when an older CSV omits that column. Storage is an energy-shifting
asset and is not added as a third primary electricity source.

Raw run folders are optional and ignored by Git. The notebook uses
`raw_run_directory` only for the site-plan table and hourly profiles. These
sections skip gracefully on a teammate's clone without raw files.

## Export and record findings

Set `EXPORT_FIGURES = True` to save PNG figures, per-round and campaign tables,
and an input-fingerprint manifest to a new folder under `runs/interpretation/`.
Export is off by default. The final Markdown cell provides questions for writing
the team's interpretation and identifying the next experiment.

The notebook reads saved evaluations. It does not run strategies or solvers,
change source results, upload submissions, or select a winner automatically.
Production plans must remain reproducible through strategy code and configs.
