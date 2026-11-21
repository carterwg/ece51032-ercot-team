# Reusable Strategy-Testing Framework

## Purpose

This document defines a framework for turning candidate plans into reproducible,
comparable experiment records. It is a design specification. It does not describe
or propose implementation code yet.

The framework must support:

- hand-written plans
- strategy-generated plans
- candidate plans supplied as site lists
- candidate plans supplied as JSON/CSV-like objects
- one plan or a batch of plans
- one or more scenario assumptions
- preview runs
- official batch evaluation when available
- reruns of the exact same inputs
- incomplete, invalid, infeasible, and evaluator-failure outcomes

The framework must not treat a missing result or evaluator failure as a scored
zero. A deliberately valid score of zero is distinct from an invalid plan or
failed evaluation.

## Core model

The framework has three types of records:

1. **Plan**: the requested bus and asset values.
2. **Experiment**: a collection of candidate plans evaluated under matching
   scenario assumptions.
3. **Run**: one plan under one round, scenario, and evaluator mode.

The run record is the unit of analysis. The experiment log is append-only
operational history.

## Inputs

The framework accepts a candidate-plan definition in one of these forms:

### A. Candidate-plan object

```yaml
plan_name: network-diversified-a
team_id: team-example
week: 2
submission: 1
seed: 42
sites:
  - bus_id: "2054"
    connection_capacity_mw: 250
    generator_capacity_mw: 0
    storage_power_mw: 0
    storage_energy_mwh: 0
  - bus_id: "6062"
    connection_capacity_mw: 250
    generator_capacity_mw: 0
    storage_power_mw: 0
    storage_energy_mwh: 0
```

The input is named rather than an official submission name. The framework derives
the canonical CSV and a deterministic site ID for the selected round.

### B. Candidate list

A batch may be declared as a list of plan objects or as a directory containing
canonical candidate CSVs. The framework may accept all of the following:

- plan name
- site list
- bus list
- connection capacity list or uniform allocation
- generator capacities
- storage power/energy pairs
- optional prebuilt canonical CSV
- optional opponent scenario
- optional prior Submission 1 CSV
- optional Submission 2 base-load artifact

Prebuilt CSVs remain inputs, not silently changed output files. The framework
records their SHA-256 and source path.

### C. Experiment manifest

The manifest defines an experiment across one or more plans:

```yaml
experiment_id: week2-resource-screen
team_id: team-example
week: 2
submission: 1
scenario_dir: ercot-connection-game/data/processed/activsg2000_representative_v1
rules: configs/scoring/dispatch_scoring_rules_500mw.json
release: configs/rounds/finalized_release_500mw.json
evaluator_modes:
  - preview
  - official_when_available
plans:
  - plan-a
  - plan-b
```

A manifest should require matching scenario and rules inputs for every plan in
the experiment. A comparison is invalid if plans use mismatched scenarios or
capacities unless the manifest explicitly records the difference.

## Candidate execution workflow

For each candidate plan:

```text
input plan
  -> normalize plan
  -> generate canonical CSV
  -> validate CSV
  -> write candidate manifest
  -> run student preview
  -> collect preview outputs
  -> optionally run official batch evaluation
  -> normalize every output
  -> append run record
  -> append lifecycle events
```

The framework must stop invalid plans from entering preview or official
evaluation. It must still create a run record for the validation failure.

### 1. Normalize

Normalize the plan by:

- validating finite numeric values
- converting bus IDs to strings
- deriving/detecting site IDs
- checking S1/S2 site-ID reuse
- applying the active team connection cap
- applying G <= C
- applying B = 4P
- recording the active scenario fingerprint
- recording the active rules and release fingerprints
- recording the Git revision and local code state

### 2. Generate CSV

Write a canonical seven-column CSV:

```text
team_id,site_id,bus_id,connection_capacity_mw,generator_capacity_mw,storage_power_mw,storage_energy_mwh
```

Each candidate run gets a run-specific directory and no existing output may be
overwritten.

Recommended directory structure:

```text
runs/<experiment-id>/<run-id>/
  candidate.csv
  plan.json
  validation.json
  preview/
  official/
  manifest.json
```

This is a proposed layout only; the implementation may use an equivalent
content-addressed structure.

### 3. Validate

Validation has two levels:

- **Structural validation**: UTF-8, header, exactly seven fields, valid IDs,
  numeric ranges, team cap, G <= C, and B = 4P.
- **Workflow validation**: correct round, valid scenario bus IDs, no reused
  Submission 1 site ID, matching prior submission, matching release/rules, and
  matching scenario fingerprints.

Every issue is recorded with stage and field/row information.

### 4. Run preview

The preview run must execute one candidate in one isolated folder. If it receives
opponent plans, they must be explicitly supplied and recorded.

The framework should preserve:

- raw preview JSON
- normalized preview row
- preview mode and exactness flag
- storage-dispatch policy
- allocation/projection output
- any warning text

The preview is not labeled as official. It must not replace official results.

### 5. Run official evaluation

Official evaluation is optional unless the experiment explicitly requires it.
When run, it must receive:

- all valid submissions in the scenario
- the selected round
- the selected scenario artifact
- matching rules
- Submission 2 base-load artifact when applicable
- solver and worker settings
- roster or missing-team metadata if used

Official batch output and candidate preview output must not be merged before
normalization.

### 6. Collect and normalize

Every run is transformed into a fixed record in `run_database.csv`. Raw JSON and
diagnostic files remain linked from the record rather than replacing the raw
data.

## `analysis/run_database.csv`

`run_database.csv` is the master experimental results table. It should contain
one row per plan/run/evaluation.

The proposed schema is:

| Column | Meaning |
|---|---|
| `record_id` | Stable unique record identifier |
| `experiment_id` | Logical experiment or batch |
| `run_id` | Unique run/candidate execution |
| `timestamp_utc` | ISO-8601 UTC start or completion time |
| `plan_name` | Human-readable candidate name |
| `plan_source` | Hand-written, config, strategy name, or supplied CSV |
| `team_id` | Team submitting the candidate |
| `week` | 1, 2, or 3 |
| `submission` | 1 or 2 |
| `scenario_id` | Named scenario/opponent assumption |
| `scenario_sha256` | Scenario package fingerprint |
| `rules_sha256` | Scoring-rules fingerprint |
| `release_sha256` | Release configuration fingerprint |
| `base_load_sha256` | Submission 2 base load, or empty |
| `seed` | Reproducibility seed, or empty |
| `mode` | `preview`, `official_batch`, or `official_full` |
| `status` | `success`, `invalid_plan`, `infeasible`, `evaluator_failure`, or `not_run` |
| `valid` | CSV validity boolean |
| `allocation_triggered` | Whether site allocation/projection ran |
| `evaluation_status` | Machine-readable success/failure classification |
| `candidate_csv_path` | Generated or supplied candidate |
| `validation_output_path` | Validation report |
| `preview_output_path` | Preview result, if any |
| `official_output_path` | Official result, if any |
| `git_revision` | Source revision used |
| `buses_used_json` | JSON array of unique bus IDs |
| `connection_capacity_mw_by_bus_json` | JSON object, bus to aggregate C |
| `generator_capacity_mw_by_bus_json` | JSON object, bus to aggregate G |
| `storage_power_mw_by_bus_json` | JSON object, bus to aggregate P |
| `storage_energy_mwh_by_bus_json` | JSON object, bus to aggregate B |
| `total_connection_capacity_mw` | Sum C |
| `total_generator_capacity_mw` | Sum G |
| `total_storage_power_mw` | Sum P |
| `total_storage_energy_mwh` | Sum B |
| `requested_capacity_mw` | Requested before allocation |
| `allocated_capacity_mw` | Capacity after alpha allocation |
| `score_usd` | One-run score; numeric only for a valid result |
| `served_load_mwh` | Weighted/represented-year dispatch result as defined by output |
| `served_fraction` | Allocated/requested or dispatched fraction |
| `it_value_usd` | IT-service term |
| `energy_cost_usd` | Week-3 grid energy term |
| `generator_operating_cost_usd` | Generator variable cost |
| `generator_capital_cost_usd` | Generator construction capital |
| `storage_capital_cost_usd` | Storage power plus energy capital |
| `site_cost_usd` | Allocated site-construction cost |
| `alpha_min` | Minimum per-site allocation fraction |
| `alpha_mean` | C-weighted mean allocation fraction |
| `alpha_max` | Maximum per-site allocation fraction |
| `curtailment_mw` | Requested minus allocated capacity, or dispatched equivalent |
| `cpu_runtime_seconds` | Dispatch/preview duration |
| `peak_memory_gib` | Optional memory measurement |
| `binding_period_indices_json` | JSON array of period indices |
| `binding_branches_json` | JSON array of branch IDs |
| `congestion_indicators_json` | JSON object of congestion diagnostics |
| `maximum_branch_loading_pct` | Peak maximum branch loading |
| `maximum_generator_utilization_pct` | Peak aggregate generator utilization |
| `warning_text` | Preview/evaluator warning |
| `issues_json` | JSON array of structured problems |
| `raw_output_sha256` | Fingerprint of the raw output bundle |

The JSON object/array fields are recommended for CSV portability. Nested output
details remain available in the raw JSON and linked report directory.

## Handling of congestion and binding constraints

The framework should extract, rather than infer, these fields:

- binding period indices
- binding branch IDs
- branch loading and branch-flow values
- maximum branch loading percentage
- aggregate generator utilization
- periods with one or more private generators at Pmax
- LMP congestion indicators
- allocation cuts and projection status
- whether the submitted full dispatch was infeasible
- whether final dispatch required a backoff

No field should be labeled as binding unless the raw output marks or the
dispatch diagnostic proves it. “Likely congested” should remain a separate
hypothesis field.

For preview runs, storage is idle and binding constraints may differ from the
official storage-aware result. The record's `mode` and warning text must make
this explicit.

## `analysis/experiment_log.csv`

`experiment_log.csv` is the append-only operational event log. It should have
one row per lifecycle event, such as:

- experiment created
- plan normalized
- CSV generated
- validation passed or failed
- preview started
- preview completed or failed
- official evaluation started
- official evaluation completed or failed
- database record appended
- rerun supersedes a prior run
- report created

The proposed columns are:

| Column | Meaning |
|---|---|
| `event_id` | Unique event identifier |
| `timestamp_utc` | Event timestamp |
| `experiment_id` | Logical experiment |
| `run_id` | Run, if applicable |
| `plan_name` | Candidate name |
| `phase` | `normalize`, `generate`, `validate`, `preview`, `official`, or `database` |
| `event_type` | Machine-readable event name |
| `status` | `started`, `success`, `warning`, `failure`, or `skipped` |
| `elapsed_seconds` | Event duration |
| `candidate_csv_path` | Related candidate |
| `validation_output_path` | Related validation artifact |
| `preview_output_path` | Related preview artifact |
| `official_output_path` | Related official artifact |
| `details_path` | Longer JSON/text diagnostics |
| `message` | Short human-readable summary |
| `git_revision` | Revision used |
| `scenario_sha256` | Scenario fingerprint |
| `rules_sha256` | Rules fingerprint |
| `base_load_sha256` | Base-load fingerprint |

`experiment_log.csv` is for debugging and provenance. Comparative analysis should
use `run_database.csv`.

## Data-quality and rerun rules

1. **Append-only first**
   - Never silently overwrite `run_database.csv`.
   - Never silently overwrite `experiment_log.csv`.
   - Never overwrite a prior run directory.

2. **Unique run identity**
   - A rerun gets a new run ID.
   - Replacing a record requires an explicit `supersedes_run_id`.
   - Original records remain in the database.

3. **Complete fingerprints**
   - Candidate SHA-256
   - scenario SHA-256
   - rules SHA-256
   - release SHA-256
   - base-load SHA-256 when applicable
   - raw output SHA-256
   - Git revision

4. **Failure preservation**
   - Valid but infeasible is not a valid zero.
   - Invalid CSV is not sent to preview.
   - Evaluator failure is not a numeric score.
   - `score_usd` should be blank rather than `0`.

5. **Matching comparisons**
   - Require matching experiment scenario
   - Require matching round and submission
   - Require matching capacity
   - Require matching opponent assumptions
   - Require matching rule and release fingerprints

6. **Storage**
   - Store P and B separately
   - Never infer B as 4P in the database for an actual invalid result
   - Preserve preview-vs-official storage differences

7. **Alpha**
   - Store per-site alpha as raw data if available
   - Store the C-weighted mean and min/max aggregates in the run record
   - Never infer alpha from a service fraction unless per-site or team data show
     that it is the same

## Recommended aggregation views

Future tooling may derive, but should not manually overwrite:

- best plans by score
- complete four-round campaigns
- score against no-opponent versus opponent assumptions
- served-fraction versus C
- score versus G
- storage benefit versus binding periods
- bus concentration and shared-bus totals
- binding-branch frequency
- alpha distribution
- curtailment distribution
- generator and storage utilization
- Week 2 versus Week 3 costs
- downside-risk and matched-scenario comparisons

The database should remain the source of truth. Derived views should include the
source run IDs.

## Baseline and controlled-experiment conventions

Each experiment should define a baseline plan and exactly one changed dimension
when possible:

| Dimension | Example change |
|---|---|
| Bus | move 250 MW from bus 2054 to bus 6062 |
| Connection capacity | 250 MW to 500 MW |
| Generation | add G=125 MW |
| Storage | add P=62.5 MW/B=250 MWh |
| Site count | one 500 MW site versus two 250 MW sites |
| Opponent plan | add a rival at bus 1079 |
| Scenario | add a matched opponent mix |
| Submission timing | S1 baseline versus S2 residual headroom |

The experiment manifest should identify:

- baseline run
- changed variables
- unchanged variables
- hypothesis
- success metric
- matching scenario
- target week/submission

## Result precedence

For a candidate plan:

1. Official batch result has precedence over preview for a matching scenario.
2. Preview is a screening result, not an official result.
3. A complete four-round official campaign is more comparable than isolated
   rounds.
4. A solo run is not evidence of competition robustness.
5. A preview and an official run must remain separate records even if the plan
   and round are identical.

## Initial implementation boundary

The implementation of this framework can be added later as:

- candidate-plan validation and normalization
- canonical CSV generation
- preview runner
- official batch runner or adapter
- raw-output normalization
- CSV append transaction
- experiment manifest reader
- report/query utilities

The design should be implemented only after:

- database field names are accepted
- rerun/supersession policy is accepted
- official and preview result precedence is accepted
- comparison matching rules are accepted
- failure and missing-result policies are accepted
