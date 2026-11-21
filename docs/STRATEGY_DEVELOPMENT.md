# Step-by-step strategy development guide

The finalized limit is **500 MW per team per submission**. The CLI defaults to
`configs/rounds/finalized_release_500mw.json`; batch evaluations must explicitly
use `configs/scoring/dispatch_scoring_rules_500mw.json`. Instructor code stays
unchanged.

Use this workflow for each teammate's idea: develop a strategy, generate a legal
candidate, evaluate it under competition, compare complete campaigns, and preserve
the chosen submission. Keep the `full_generation` strategy available as the C = G
baseline throughout development.

All terminal examples run from the **team repository root**, the directory
containing this project's `pyproject.toml` and `ercot-connection-game/`.
Replace `YOUR_TEAM_ID` with our actual fixed team ID. Use a new run directory for
every candidate or evaluation; do not mix outputs from different experiments.

## 1. Know what stays shared and what you change

These interfaces and functions normally stay unchanged when adding a strategy:

| Location | Interfaces or functions | Responsibility |
| --- | --- | --- |
| [`contracts.py`](../src/team_strategy/contracts.py) | `PlanningContext`, `Plan`, `SiteProposal` | Common inputs and outputs |
| [`context.py`](../src/team_strategy/context.py) | `load_context()` | Load round settings, active rules, and the scenario package |
| [`context.py`](../src/team_strategy/context.py) | `file_fingerprint()`, `scenario_fingerprint()`, `assert_inputs_current()` | Record input identity and detect changed inputs |
| [`validation.py`](../src/team_strategy/validation.py) | `validate_plan()` | Instructor legality checks plus our workflow checks |
| [`csv_export.py`](../src/team_strategy/submissions/csv_export.py) | `site_ids()`, `plan_csv()`, `export_plan()` | Generate site IDs and canonical CSVs |
| [`strategies/__init__.py`](../src/team_strategy/strategies/__init__.py) | `build_strategy()` | Instantiate a registered strategy from parameters |
| [`scoring.py`](../src/team_strategy/experiments/scoring.py) | `combined_score_usd()`, `ScoreBounds.normalize_usd()` | Combine graded scores and normalize them |
| [`comparison.py`](../src/team_strategy/experiments/comparison.py) | `summarize()`, `compare()`, `frontier_names()` | Compare return and downside risk |
| [`plotting.py`](../src/team_strategy/experiments/plotting.py) | `plot_frontier()` | Draw the risk-return comparison |
| [`cli.py`](../src/team_strategy/cli.py) | CLI entry points | Connect generation and reporting steps |

The instructor subtree, `ercot-connection-game/`, stays unchanged. Improvements
to shared code should be reviewed as framework changes, rather than embedded in
one teammate's strategy.

For a new strategy, you normally add a strategy module, a JSON configuration,
focused tests, and short documentation. The one existing code file you edit is
the strategy registry, to add your class.

## 2. Set up the environment once

From the team repository root, using Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ./ercot-connection-game
python -m pip install -e '.[test,plot]'
python -m pytest -q
```

Use this root-level environment for both team and instructor commands. In each
new terminal, return to the team repository root and run:

```bash
source .venv/bin/activate
```

Work on a separate feature branch for your idea. Choose strategy names by
approach, such as `network_diversified`, so ownership and implementation remain
separate. Record authorship in the strategy documentation.

## 3. Generate the existing baseline

```bash
team-strategy propose \
  --config configs/strategies/full_generation.json \
  --team-id YOUR_TEAM_ID \
  --week 2 --submission 1 \
  --seed 42 \
  --output-dir runs/baseline-w2s1-001
```

This calls `FullGeneration.propose(context)`, validates the returned plan, and
writes:

```text
runs/baseline-w2s1-001/
    candidate.csv       # Canonical site-level CSV
    config.json        # Parameters used
    validation.json    # Successful legality check
    manifest.json      # Round, budget, seed, input hashes, CSV hash, code identity
    source/            # Snapshot of the team implementation
```

The baseline requests the available connection budget, sets G = C at each site,
and uses no batteries. The evaluator may still use cheaper grid electricity;
C = G permits full private supply but does not force off-grid dispatch.

**`propose` generates and validates a candidate. It does not calculate allocation
or score, select a final submission, or upload anything.**

## 4. Decide whether you need new parameters or a new algorithm

If the existing algorithm already expresses your idea, create another config.
For example, save this as `configs/strategies/full_generation_four_sites.json`:

```json
{
  "strategy": "full_generation",
  "params": {
    "site_count": 4,
    "bus_ids": []
  }
}
```

Run `propose` with that config and a different output directory. No Python
changes are needed. An empty `bus_ids` list lets this baseline choose catalog
buses deterministically; explicit IDs must exist in the selected network.

If you need a different way to select buses or capacities, follow the next step.
Keep the original baseline intact.

## 5. Add your strategy class

Create `src/team_strategy/strategies/my_strategy.py`. This is a template to
complete, not an implemented strategy:

```python
from dataclasses import dataclass

from ..contracts import Plan, PlanningContext, SiteProposal


@dataclass(frozen=True)
class MyStrategy:
    site_count: int = 4

    def __post_init__(self) -> None:
        if type(self.site_count) is not int or self.site_count < 1:
            raise ValueError("site_count must be a positive integer")

    def propose(self, context: PlanningContext) -> Plan:
        # Select buses from this context's network.
        # Decide connection, generation, and battery capacities.
        # Return Plan(sites=(SiteProposal(...), ...)).
        raise NotImplementedError("Implement this strategy's planning logic")
```

Your main development work belongs in `propose(context)`. Add helper functions
inside your strategy module as needed. Put tunable parameters in constructor
fields and check their validity in `__post_init__()`.

Useful context fields are:

| Field | Use |
| --- | --- |
| `bus_ids` | Valid source bus IDs, represented as strings |
| `connection_budget_mw` | Available connection budget for this submission |
| `max_generator_to_connection_ratio` | Active generator-capacity constraint |
| `scenario_dir`, `rules_file` | Actual network/base-load package and scoring rules |
| `round`, `energy_cost_enabled` | Week, submission number, and energy-charge setting |
| `seed` | Reproducible random choices |

Return a `Plan` containing `SiteProposal` objects with these fields:

```text
bus_id
connection_mw
generator_mw
storage_power_mw
storage_energy_mwh
```

Use MW for power and MWh for energy. The shared validator checks the active
capacity limits, G <= C, valid buses, finite nonnegative capacities, and the
four-hour battery rule. The framework adds the team and site IDs.

For stochastic strategies, construct a local RNG from `context.seed`, such as
`random.Random(context.seed)`. Sort unordered collections before using their
order to make decisions. Identical context and parameters should reproduce the
same plan.

The CLI currently does not populate `context.candidate_buses` from `analysis/`.
Do not assume those screening results are present or current. Read the supplied
scenario data for your algorithm; any shared screening integration should retain
the matching scenario fingerprint. Individual-bus hosting capacities are
screening information, not additive guarantees of joint feasibility.

## 6. Register and configure the strategy

In `src/team_strategy/strategies/__init__.py`, import your completed class and
add it to the existing registry, preserving the baseline:

```python
from .full_generation import FullGeneration
from .my_strategy import MyStrategy

STRATEGIES = {
    "full_generation": FullGeneration,
    "my_strategy": MyStrategy,
}
```

Leave `build_strategy()` unchanged. Create
`configs/strategies/my_strategy.json`:

```json
{
  "strategy": "my_strategy",
  "params": {
    "site_count": 4
  }
}
```

The `strategy` value must match the registry key. Each `params` key must match a
constructor parameter. Add `docs/strategies/my_strategy.md` explaining the idea,
authors, assumptions, parameters, and later findings.

## 7. Test the strategy

Add focused tests in `tests/test_my_strategy.py` for your algorithm's assumptions
and important edge cases. For example: insufficient candidate buses, parameter
boundaries, or reproducibility of randomized choices.

Run the shared suite:

```bash
python -m pytest -q
```

Every registered strategy automatically enters the common contract test, which
checks that default parameters produce a reproducible, valid `Plan`. Defaults
must therefore work on the small IEEE-14 teaching network as well as supporting
explicit full-network configurations. Registering the unfinished template will
fail these tests until its method is implemented.

The suite also covers CSV legality, round handling, normalization, and a baseline
evaluation over all 120 teaching-network periods. Passing these checks establishes
the checked contracts; it does not establish competitive performance.

## 8. Generate your candidate

```bash
team-strategy propose \
  --config configs/strategies/my_strategy.json \
  --team-id YOUR_TEAM_ID \
  --week 2 --submission 1 \
  --seed 42 \
  --output-dir runs/my-strategy-w2s1-001
```

Inspect `candidate.csv`, `validation.json`, and `manifest.json`. If you change
parameters, code, or inputs, generate another run rather than editing a frozen
candidate CSV. The finalized project limit is 500 MW per submission;
`--budget-mw` can reduce that budget but cannot override the release cap.

## 9. Evaluate the candidate with the instructor tools

Create a fresh input directory containing only the canonical CSVs for one joint
evaluation. Keep manifests, configs, and other CSV outputs outside it:

```bash
mkdir -p runs/my-strategy-w2s1-eval-001/inputs
cp runs/my-strategy-w2s1-001/candidate.csv \
  runs/my-strategy-w2s1-eval-001/inputs/our-team.csv

ercot-game-batch run \
  --submissions-dir runs/my-strategy-w2s1-eval-001/inputs \
  --artifact-dir ercot-connection-game/data/processed/activsg2000_representative_v1 \
  --rules configs/scoring/dispatch_scoring_rules_500mw.json \
  --week 2 --submission-number 1 \
  --solver-backend highs --workers 1 \
  --output-mode compact \
  --output-dir runs/my-strategy-w2s1-eval-001/results
```

With only our CSV, this evaluates our plan alone. To simulate competition, place
one canonical CSV per mock opponent in the input directory **before** running
the command. Each mock team needs a distinct team ID. Our three candidate
strategies are evaluated separately, each occupying our team's slot.

Read `results/leaderboard.csv` for scores and service fractions, and
`results/diagnostics/` for explanations. These are local simulated results, not
classroom results. Keep opponent assumptions, CSV hashes, and seeds with the
experiment record.

Use all 120 periods for final comparisons, especially with batteries. The fast
preview omits battery operating benefits and cannot replace full evaluation of
storage strategies.

## 10. Handle Submission 2 and weekly resets

Submission 2 proposes **new sites only** against a base load incorporating the
corresponding joint Submission 1 dispatch. For a local simulation, build its
base-load package from that S1 evaluation:

```bash
ercot-game-batch base-load \
  --artifact-dir ercot-connection-game/data/processed/activsg2000_representative_v1 \
  --base-load-from runs/my-strategy-w2s1-eval-001/results \
  --workers 1 \
  --output-dir runs/my-strategy-w2s2-base-001

team-strategy propose \
  --config configs/strategies/my_strategy.json \
  --team-id YOUR_TEAM_ID \
  --week 2 --submission 2 \
  --scenario-dir runs/my-strategy-w2s2-base-001 \
  --prior-submission runs/my-strategy-w2s1-001/candidate.csv \
  --seed 42 \
  --output-dir runs/my-strategy-w2s2-001
```

For actual classroom planning, use the instructor-released compatible S2 package
and our actual submitted S1 CSV. Do not substitute a simulated S1 outcome for
released classroom data.

Evaluate the local S2 candidate as follows, adding any mock opponents' new-site
CSVs to the fresh input directory before evaluation:

```bash
mkdir -p runs/my-strategy-w2s2-eval-001/inputs
cp runs/my-strategy-w2s2-001/candidate.csv \
  runs/my-strategy-w2s2-eval-001/inputs/our-team.csv

ercot-game-batch run \
  --submissions-dir runs/my-strategy-w2s2-eval-001/inputs \
  --artifact-dir ercot-connection-game/data/processed/activsg2000_representative_v1 \
  --rules configs/scoring/dispatch_scoring_rules_500mw.json \
  --week 2 --submission-number 2 \
  --base-load-from runs/my-strategy-w2s1-eval-001/results \
  --solver-backend highs --workers 1 \
  --output-mode compact \
  --output-dir runs/my-strategy-w2s2-eval-001/results
```

For this batch route, pass the original package to `--artifact-dir`: the
evaluator adds S1 withdrawal using `--base-load-from`. Passing an already carried
package there would count the S1 withdrawal again.

Week 3 starts from the original base package again. Repeat S1 and S2 with
`--week 3`; grid energy is then charged at joint-dispatch LMPs. S1 sites retain
their S1 score rather than being scored again in S2. Week 1 is practice only.

## 11. Compare complete campaigns

Collect actual numeric USD scores for W2S1, W2S2, W3S1, and W3S2. Each scenario
is a complete campaign, including its own S1-to-S2 history. Compare strategies
using the same opponent assumptions, seeds, rules, and capacity budget; each
candidate's carried base load must follow its corresponding joint S1 outcome.

Include the full-generation baseline in the comparison. Use at least two
campaign scenarios per strategy, with matching scenario IDs. Assemble
`campaign_scores.json` using the [documented input format](SCORING.md#report-input),
then run:

```bash
team-strategy report \
  --input campaign_scores.json \
  --output-dir runs/comparison-001 \
  --plot
```

The report writes `input.json`, `comparison.json`, `comparison.csv`, and
`frontier.png`. It keeps average normalized score, downside risk, worst-case
score, and the fraction of scenarios below the baseline separate. It identifies
Pareto trade-offs without assigning a weighted composite score or selecting a
winner automatically.

For the finalized 500 MW per submission, our comparison scale is:

```text
Q(S) = 100 * (S - 49.67) / (73.0525 - 49.67)
```

Here S is the combined four-submission score in **billions**, while report input
values are in **USD**. Both anchors assume a full new capacity budget in each
graded submission. Negative scores remain visible. The grid-only anchor assumes
full allocation and zero energy prices; it is not a promised network outcome.
The anchors are $49.67B and $73.0525B. See
[scoring assumptions and downside-risk definitions](SCORING.md) before comparing.

Do not replace missing scores or evaluator failures with zero. Record explicit
zero only for a genuinely scored zero or a deliberately empty new-build round.

## 12. Review and preserve the selected submission

Before the designated uploader submits the team's chosen file:

- Confirm the team ID, week, submission number, active inputs, and capacity cap.
- Run the shared tests and review the exact exported CSV's validation.
- Review full-horizon evaluation results, opponent scenarios, and the baseline
  comparison; record why this candidate was selected.
- Copy the selected candidate bundle and relevant evaluation evidence into a
  new directory under `submissions/`, with a short `decision.md`.
- Name the upload copy using the assignment convention, such as
  `team07_week2_sub1.csv`. Keep its contents identical to the selected candidate
  and retain the manifest's CSV hash.
- Have one designated teammate upload that file. Preserve the upload record and
  later instructor feedback alongside the submission evidence.

Generated `runs/` are ignored by Git. Preserve the selected evidence under
`submissions/` deliberately so it is available to all three teammates. Review
large dispatch exports before adding them; keep the report, diagnostics, and
references needed to explain the decision.

## Current automation boundary

Candidate generation, shared validation, CSV export, normalization, and frontier
reporting are implemented. The separate
`python -m team_strategy.experiments.concentration` command now runs matched
four-submission corridor experiments using `evaluation/campaign.py` and the
unchanged instructor evaluator. Its fixed opponent hypotheses are declared in
`configs/experiments/corridor_part2.json`; see the repository README for invocation,
resume, and result locations. The ordinary `team-strategy report` command still
consumes supplied scores rather than running simulations.

Adaptive opponent models, continuous parameter search, and automatic classroom
submission remain future work. Part 2's primary comparison holds the resource
mix constant; the C = G plan is a separately labeled benchmark.

## Checklist for each idea

- [ ] Create a feature branch and describe the strategy's hypothesis.
- [ ] Add a strategy class or a new parameter config; preserve the baseline.
- [ ] Register a new class, add focused tests, and document its assumptions.
- [ ] Pass `python -m pytest -q`.
- [ ] Generate a validated candidate in a new run directory.
- [ ] Evaluate alone and against matched simulated opponents.
- [ ] Complete coupled S1/S2 runs and reset correctly between weeks.
- [ ] Compare complete graded campaigns, retaining negative normalized scores.
- [ ] Review the return/downside trade-offs with the team.
- [ ] Preserve the selected CSV and evidence before the designated upload.
