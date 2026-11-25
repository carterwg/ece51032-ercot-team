# ece51032-ercot-team

Private repository for the ECE51032 project.

For work from a fresh Codex Cloud workspace, start with the
[cloud handoff](CLOUD_HANDOFF.md). Codex also reads the concise
[repository guidance](AGENTS.md) automatically.

Start with the [step-by-step strategy development guide](docs/STRATEGY_DEVELOPMENT.md)
for setup, what to edit, testing, evaluation, and choosing a submission.
Interpret saved results with [main_template.ipynb](notebooks/main_template.ipynb),
the reusable plot notebook for all strategies. See its [usage guide](notebooks/README.md)
for notebook dependencies, inputs, and exports.
The [ten-team findings](findings/Ten_teams_500_MW_comparison.md) cover the current field of nine opponents.
Executed reports are also available for the [bus 1001 baseline](notebooks/01_full_generation_baseline.ipynb)
and [Carter's bus 6141 strategy](notebooks/02_carter_rank1_cg.ipynb).
See the [strategy findings for team discussion](notes/Saket_Strategy_Discussion.md)
for the ten-team corridor, S1 equipment, and S2 carryover results.

- `src/team_strategy/`: team interfaces, full-generation baseline, validation,
  campaign normalization, and risk–return comparisons.
- `configs/`, `tests/`, `docs/`, `notebooks/`: shared team development workflow.
- `runs/`: generated candidate/report bundles (ignored by Git).
- `submissions/`: deliberately selected submission bundles.
- `analysis/`: team bus-screening and hosting-capacity results.
- [`findings/`](findings/README.md): Markdown run records, with scores, grid/private
  energy, generator runtime, binding lines, and independently checked hourly
  counterfactuals. Experiment commands update these records automatically.
- [`notes/`](notes/README.md): Carter's research notes and [Saket's initial 500 MW findings](notes/Saket_Initial_Findings.md).
- `ercot-connection-game/`: complete course repository, imported as a Git subtree.
  See its [README](ercot-connection-game/README.md) and
  [tutorial](ercot-connection-game/docs/student_tutorial/tutorial.pdf).

## Team setup

From this team repository root (Python 3.11+):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ./ercot-connection-game
python -m pip install -e '.[test,plot]'
python -m pytest -q
```

Use this root-level `.venv` for both team and instructor tools. It stays active
when you change directories. In a new terminal, activate it from the team
repository root with `source .venv/bin/activate`.

Generate a baseline candidate with C = G using the finalized 500 MW cap:

```bash
team-strategy propose \
  --config configs/strategies/full_generation.json \
  --team-id YOUR_TEAM_ID --week 2 --submission 1 \
  --output-dir runs/baseline-w2s1-001
```

This validates and records a candidate; it does not run dispatch or upload a
submission. Existing output directories are never overwritten. Submission 2
also requires `--scenario-dir` pointing to the carried-base-load package and
`--prior-submission` pointing to our actual S1 CSV.

See [architecture](docs/ARCHITECTURE.md), [adding a strategy](docs/strategies/full_generation.md),
and [normalization and risk reporting](docs/SCORING.md).
The [Carter rank-1 variant](docs/strategies/carter_rank1_cg.md) uses bus `6141`
with the same C = G capacities as the baseline.
The finalized cap is **500 MW per team per submission**. The default CLI uses
`configs/rounds/finalized_release_500mw.json`; evaluations use
`configs/scoring/dispatch_scoring_rules_500mw.json`. These apply the finalized
capacity to the older imported course package without editing instructor files.
Only 500 MW runs and reports are retained. Comparison anchors are $49.67B and
$73.0525B; negative normalized scores remain visible.

## Corridor analysis and strategy comparison

[Part 1](analysis/clustering/part1/report.html) records signed bottleneck groups,
PTDF similarity, and directional electrical interactions for 101 candidates.
Its groups describe shared constraints; they do not predict competitors' choices.

Part 2 evaluates ten teams at **500 MW per team per submission**. It compares
one, two, and five sites using standalone hosting rank and Part 1 bottleneck/PTDF
selection. The matched policies are grid only, C = G in S2, and C = G in both
submissions. A separate sizing comparison tests 125, 250, and 375 MW of S1
generation with full S2 backup. All nine rivals use the same plan within each field.

From the repository root:

```bash
export PYTHONPATH=src:ercot-connection-game:ercot-connection-game/src
.venv/bin/python -m team_strategy.experiments.ten_teams --jobs 7
```

The report verifies the request CSVs and all ten teams' S1 carryover before
writing the [comparison](findings/Ten_teams_500_MW_comparison.md) and each
campaign's findings. Saved game scores and hourly line-relief results appear
with their respective evidence. Regenerating findings preserves personal notes.
Raw evaluations and diagnostic caches live under `runs/`. Links to local
solver evidence work after generating the corresponding runs. To use a new
experiment directory, set `--output` and `--summary`. To regenerate reporting
from saved dispatch, run `python -m team_strategy.experiments.ten_team_report`
and point `--run` at the saved experiment.

The [S1 battery study](findings/Battery_S1_comparison.md) compares generator and
four-hour storage sizes at bus 6141 against fields with rival generation and
storage. The [targeted optimization](findings/Battery_S1_targeted_optimization.md)
compares three finalists and two benchmarks across 36 distinct four-round
campaign fields. The [1 MW refinement](findings/Battery_S1_1MW_local_search.md)
records the cheaper S1 build and its exact allocation in each field. Run the
initial sweep with `python -m team_strategy.experiments.battery_s1` and regenerate
the Markdown from saved evaluations with `python -m team_strategy.experiments.battery_s1_report`.

## Instructor tools and updates

With the root-level environment activated, run course commands from
`ercot-connection-game/` so that data paths resolve. Starting from the team
repository root:

```bash
cd ercot-connection-game
ercot-game-check-csv --file examples/eight_team_round/submissions/team-01.csv
cd ..
```

For the course tutorial notebooks, install the optional dependencies into the
same environment from the team repository root:

```bash
python -m pip install -e './ercot-connection-game[tutorial,test]' pandas
```

The course files were imported from
[MhaoMou/ercot-connection-game](https://github.com/MhaoMou/ercot-connection-game)
at commit `b3b04c8a751d029506a49125b5c32fe93404d7dc` on November 15, 2026.
The source-code and course-material licenses remain in the imported directory.
All course files are tracked directly in this repository; cloning the team
repository also retrieves them.

To import future course updates, run from the team repository root on your
working branch, then review and test the changes:

```bash
git subtree pull --prefix=ercot-connection-game https://github.com/MhaoMou/ercot-connection-game.git main --squash
```
