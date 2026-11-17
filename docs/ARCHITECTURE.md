# Team architecture

The instructor repository is an unchanged Git subtree under
`ercot-connection-game/`. Team code calls its CSV validator and evaluator;
it does not redefine dispatch, allocation, storage physics, or official scoring.

```text
src/team_strategy/
  contracts.py         Plan, round context, strategy/scenario/evaluator interfaces
  context.py           Active release settings, package checks, input fingerprints
  validation.py        Instructor CSV validation plus team workflow checks
  strategies/          Independent team ideas; full_generation is the baseline
  opponents/           Reserved for simulated rival strategies
  scenarios/           Reserved for assembling joint competition scenarios
  evaluation/          Reserved for an adapter implementing Evaluator
  experiments/         Campaign normalization, risk summaries, frontier plots
  submissions/         Canonical CSV export and deterministic site IDs
  cli.py               Candidate generation and reports from supplied scores
configs/               Strategy parameters, scoring assumptions, future round/scenario configs
tests/                 Common legality, round, scoring, and integration checks
notebooks/             Exploratory work
analysis/              Existing screening outputs
runs/                  Generated local artifacts, ignored by Git
submissions/           Deliberately selected submission bundles
```

## Strategy boundary

Every strategy provides `propose(context: PlanningContext) -> Plan`.
Parameters are constructor arguments. Return site capacities and source bus IDs;
the framework adds team IDs and deterministic round-specific site IDs.

Strategies may read the supplied scenario package through shared utilities.
Use only supplied feedback and explicit seeds. Keep official evaluations and
parameter sweeps in the experiment layer so all ideas receive comparable budgets.

The common checker exports the actual canonical CSV and calls the instructor's
`validate_csv_submission` with the context's budget and generator limit.
Exports are refused when inputs changed or site IDs collide with prior sites.
These are legality and workflow checks, not proofs of a strategy's profitability.

## Inputs and rounds

`load_context` reads the finalized team release and rules. The default profile is
`configs/rounds/finalized_release_500mw.json`, with paths relative to the team
root. Context construction and reporting enforce the finalized 500 MW ceiling,
so an older imported release cannot raise it. Smaller smoke-test budgets are
allowed. Instructor files remain intact.

Submission 1 starts from the reset package. Submission 2 must use an explicitly
supplied, instructor-compatible carried-base-load package; the original package
is rejected. The CLI also requires our prior submitted CSV for site-ID checks.
Each weekly energy-price flag comes from the release. No week-to-week assets
are carried by the team framework.

Scenario content and rules are hashed. Screening features must carry the
matching scenario fingerprint. The existing analysis CSVs have no recorded
package fingerprint, so they are not automatically treated as fresh inputs.

## Candidate bundles

`propose` writes the CSV, configuration, validation, source snapshot, Git revision,
input fingerprints, seed, and comparison assumptions into a new directory.
It does not run dispatch, choose a final submission, or upload a CSV. Failed
commands leave no partial bundle; existing output directories are refused.

## Comparison boundary

The reporting command consumes complete campaign scores produced elsewhere.
Each campaign scenario must include exactly W2S1, W2S2, W3S1, W3S2 in USD.
Every strategy must have the same scenario IDs. Scenario IDs must identify the
same opponent assumptions and coupled S1/S2 history across strategies; matching
names alone cannot prove that the simulations used matching inputs.

Scenario assembly, parameter search, and an automatic official-evaluator adapter
remain future work. `Scenario`, `NamedPlan`, `Evaluator`, and `EvaluationResult`
define their boundaries now. Invalid plans, evaluator failures, and valid zero
allocations have distinct statuses; infrastructure failures must never silently
become zero-score observations.

Tests include a baseline CSV passing through all 120 periods of the unchanged
official evaluator on IEEE-14. This verifies integration, not full-scale strategy
performance on ACTIVSg2000 or unknown competitors.
