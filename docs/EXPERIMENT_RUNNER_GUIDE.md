# Experiment Runner Guide

This guide describes the current implementation in
[`src/experiment_runner.py`](../src/experiment_runner.py). It is written for a
new teammate working from the team-repository root (the directory containing
`pyproject.toml` and `ercot-connection-game/`).

## Purpose

`experiment_runner.py` takes a list of candidate plans in JSON, turns each plan
into the game's canonical submission CSV, validates it against the selected
scenario and release limits, runs the ERCOT **student preview**, saves the
outputs, and appends one summary row per plan to `analysis/run_database.csv`.
It also appends a sequence of lifecycle events to
`analysis/experiment_log.csv`.

Use it to make repeatable solo-plan comparisons, such as comparing several
site locations, connection sizes, or generator capacities under the same
inputs. Each run records input-file hashes, the Git revision when available,
the normalized plan, and paths to the raw outputs.

The runner is a convenience wrapper, not the official evaluator:

- The preview is non-authoritative (`exact` is false). Use the official batch
  evaluator for final decisions and competition scenarios.
- Every candidate gets its **own** preview, containing only that candidate.
  The runner does not put candidate plans together or add mock opponents.
- Storage is validated and its capital cost is reported, but the student
  preview does not dispatch the battery. A battery comparison using this runner
  cannot measure storage's operating benefit.
- This runner does not compute hosting capacity or make charts/reports.
- It does not write an official-evaluator output; `official_output_path` is
  reserved and remains blank.

For general strategy development and official batch evaluation, see
[`docs/STRATEGY_DEVELOPMENT.md`](STRATEGY_DEVELOPMENT.md). For the proposed
experiment workflow and database design, see
[`docs/strategy_testing_framework.md`](strategy_testing_framework.md).

## Setup and first run

Run commands from the team repository root using Python 3.11 or newer. Install
the course package and the team project into the environment you will use:

```powershell
python -m pip install -e .\ercot-connection-game
python -m pip install -e ".[test]"
```

The runner is not registered as a standalone console command. Run the file
directly:

```powershell
python .\src\experiment_runner.py --help
```

The instructor package must be importable by that Python interpreter because
the runner uses its CSV validator and launches `ercot_game.student_preview` in
a child process.

## Inputs

### Candidate plans: JSON only

The required `--plans` argument accepts either a path to a JSON file or a JSON
string. The file may contain:

1. A JSON list of candidate plan objects;
2. An object with a `plans` list; or
3. An object with a `candidates` list.

Each candidate needs a non-empty `plan_name` (or `name`) and a non-empty
`sites` (or `site_list`) list. Each site is a JSON object with the following
fields:

| Field | Required? | Accepted alias / default | Meaning and notes |
|---|---|---|---|
| `bus_id` | Yes | `bus` | Bus identifier from the selected scenario package. It is written as a string to the submission CSV. |
| `connection_capacity_mw` | Yes in practice | `connection_mw`; defaults to `0` if omitted | Requested site connection capacity, MW. A zero or otherwise illegal value will fail CSV validation. |
| `generator_capacity_mw` | Yes in practice | `generator_mw`; defaults to `0` if omitted | Private generator capacity, MW. The release validator enforces the active generator-to-connection limit (normally `G <= C`). |
| `storage_power_mw` | Yes in practice | `storage_mw`; defaults to `0` if omitted | Battery charge/discharge power, MW. |
| `storage_energy_mwh` | No | Defaults to `4 × storage_power_mw` | Battery energy capacity, MWh. The active CSV validator enforces the release's storage rules; the finalized game uses four-hour storage (`B = 4P`). |
| `site_id` | No | Generated as `w<week>-s<submission>-<index>` | Must be unique within the candidate submission. |

The connection, generator, and storage capacities must be finite,
non-negative numbers. The selected CSV validator checks the complete
submission, including bus existence, site IDs, generator limits, storage
limits, and the total team connection cap. In this repository's finalized
configuration the cap is 500 MW per team per submission. Do not rely on the
course subtree's older default cap; explicitly use the finalized team rules
when running the official batch evaluator.

Candidate-level `team_id`, `week`, and `submission` are optional and override
the runner defaults. Optional metadata fields are `scenario_id`, `seed`, and
`plan_source`. `seed` is recorded for traceability; it does not make the
preview randomized.

Example `plans.json`:

```json
{
  "experiment_id": "bus6141-size-check-01",
  "team_id": "YOUR_TEAM_ID",
  "week": 2,
  "submission": 1,
  "plans": [
    {
      "plan_name": "bus6141-250mw-grid-only",
      "scenario_id": "representative-v1",
      "seed": 42,
      "sites": [
        {
          "site_id": "site-6141",
          "bus_id": 6141,
          "connection_capacity_mw": 250,
          "generator_capacity_mw": 0,
          "storage_power_mw": 0
        }
      ]
    }
  ]
}
```

The runner defaults `storage_energy_mwh` to zero when storage power is zero,
and to four times the storage power otherwise. Add the field explicitly when
you want the plan JSON to state it unambiguously.

#### Input behavior and common mistakes

- **CSV is not accepted as a candidate-plan input.** Supply candidate
  descriptions as JSON. The runner generates the canonical CSV; it does not
  import or discover candidate CSVs from a folder.
- JSON must be syntactically valid and the candidate/site fields must have the
  expected shapes. A missing plan name, missing bus, empty sites list, or
  non-numeric capacity stops the batch before that candidate is run.
- A JSON list item that is not an object is currently filtered out by the
  loader. Check that the run count printed at the end matches the number of
  candidates you intended to submit.
- A missing capacity field defaults to zero during normalization, but the
  resulting CSV may be invalid. Specify all three capacity fields explicitly
  to avoid accidental zeroes.
- An invalid but structurally readable plan is still written and validated.
  It will be recorded as invalid and **will not** be previewed.
- The candidate list is a set of independent solo runs. Repeating the same
  candidate twice creates two runs; duplicate detection is not implemented.

### Scenario, rules, release, and optional base load

The runner's defaults are:

| Input | Default | Purpose |
|---|---|---|
| Scenario directory | `ercot-connection-game/data/processed/activsg2000_representative_v1` | The bus/network and time-series package used for validation and preview. |
| Rules JSON | `configs/scoring/dispatch_scoring_rules_500mw.json` | Scoring and active capacity limits used by the preview. |
| Release JSON | `configs/rounds/finalized_release_500mw.json` | Release configuration fingerprinted in the record. |
| Week | `2` | Week context (1, 2, or 3). Week 3 enables grid energy charges under the finalized rules. |
| Submission | `1` | Submission number (1 or 2). |
| Team ID | `team-experiment` | Used when a candidate does not provide its own team ID. Replace it with the team's actual identifier. |
| Preview stride | `1` | Checks every available period. Larger values sample periods and are not appropriate for final comparisons. |

Override scenario/rules/release paths using CLI flags or fields in the
top-level JSON object. A top-level JSON manifest can also set `experiment_id`,
`team_id`, `week`, `submission`, `base_load_from`, and `preview_stride`.
Candidate-level team/week/submission values then override those defaults.
Paths in the manifest are interpreted relative to the process's current
working directory, not relative to the JSON file.

`--base-load-from` is for Submission 2. Point it to the compatible Submission
1 evaluator output folder containing `site_net_withdrawal.csv`; use the
original scenario package as `--scenario-dir` so withdrawal is applied once.
The base-load artifact must match the intended scenario. Submission 2 CSVs
should list only the new sites, not the sites already represented in that
base load. For official end-to-end handling and caveats, follow
[`docs/STRATEGY_DEVELOPMENT.md`](STRATEGY_DEVELOPMENT.md#10-handle-submission-2-and-weekly-resets).

The runner does not accept a separate strategy-code configuration, YAML
configuration, rival-plan file, or output-report configuration. Its input is a
list of complete candidate site plans.

### Output locations and command options

Each candidate creates a unique run folder:

```text
runs/experiments/<experiment-id>/<run-id>/
```

`run-id` is generated as a UUID, so a repeated experiment ID does not overwrite
previous candidates. By default, the master database and event log are
`analysis/run_database.csv` and `analysis/experiment_log.csv`.

CLI options:

| Option | Default | Use |
|---|---|---|
| `--plans` | Required | JSON candidate list, manifest, or JSON string. |
| `--experiment-id` | `strategy-experiment` | Groups runs in output paths and records. |
| `--team-id` | `team-experiment` | Default candidate team ID. |
| `--week` | `2` | Default week, choices 1, 2, or 3. |
| `--submission` | `1` | Default submission, choices 1 or 2. |
| `--scenario-dir` | Representative scenario package | Scenario package directory. |
| `--rules` | Finalized 500 MW scoring rules | Scoring/rules JSON. |
| `--release` | Finalized 500 MW release JSON | Release configuration to fingerprint. |
| `--base-load-from` | None | Compatible evaluator output folder for Submission 2. |
| `--runs-dir` | `runs/experiments` | Parent directory for per-run artifacts. |
| `--database` | `analysis/run_database.csv` | Master summary CSV. |
| `--experiment-log` | `analysis/experiment_log.csv` | Append-only lifecycle event CSV. |
| `--preview-stride` | `1` | Preview sampling stride; 1 evaluates all periods. |

`runs/` is Git-ignored by this repository. The master database and log are not
automatically ignored; decide with the team whether to retain or commit new
records.

## Outputs

For each candidate, the run directory contains:

| File | Meaning |
|---|---|
| `plan.json` | Normalized plan actually used to generate the CSV, including generated site IDs and defaulted storage energy. |
| `candidate.csv` | Canonical submission CSV generated by the runner. |
| `validation.json` | Machine-readable CSV validation result, including validity and validation issues. |
| `preview/preview.json` | Raw student-preview JSON when produced. It is the source to consult for the preview's score, team metrics, allocation projection, and warnings. |
| `preview/submissions/candidate.csv` | Copy of the validated candidate placed in the preview input folder. |
| `preview/preview.stdout.txt` | Captured preview standard output, when non-empty. |
| `preview/preview.stderr.txt` | Captured preview standard error, when non-empty. |

There is no generated report, plot, or summary JSON beyond the validator and
raw preview outputs. The runner appends a summary row to the run database and
several event rows to the experiment log. It prints the number of rows appended
after the candidate batch completes.

The preview process has a one-hour timeout. A preview error is saved as a
failure status and warning where possible; it does not become a zero score.
Validation failures skip preview and are recorded as invalid plans. An
input-normalization error (for example, an unparseable capacity) aborts the
batch before the runner can make a normal result row for that candidate.

## Running a Single Experiment

1. Create a JSON plan file such as the `plans.json` example above. Use the
   actual team ID and make sure the total connection capacity is within the
   selected rules' cap.
2. Run from the repository root:

   ```powershell
   python .\src\experiment_runner.py `
     --plans .\plans.json `
     --experiment-id bus6141-single-01 `
     --team-id YOUR_TEAM_ID `
     --week 2 `
     --submission 1
   ```

3. In the console output, confirm the runner appended one preview run. Open the
   unique folder under `runs/experiments/bus6141-single-01/`.
4. Inspect `validation.json` first. Continue to interpret the result only if
   `"valid": true`. Then inspect `preview/preview.json` and the matching row in
   `analysis/run_database.csv`.
5. Keep the candidate JSON, generated CSV, preview JSON, and database row
   together when preserving a result. The hash fields identify the scenario,
   rules, release, base-load input, and raw preview output used.

To keep a demonstration from appending to the shared database, pass isolated
paths:

```powershell
python .\src\experiment_runner.py `
  --plans .\plans.json `
  --experiment-id bus6141-demo `
  --runs-dir .\runs\demo `
  --database .\runs\demo\run_database.csv `
  --experiment-log .\runs\demo\experiment_log.csv
```

## Running Multiple Candidate Plans

Put each candidate object in the same JSON `plans` list. For example, a fair
connection-size sweep at one bus should hold the week, scenario, generator,
storage, and team ID constant:

```json
{
  "experiment_id": "bus6141-size-sweep",
  "team_id": "YOUR_TEAM_ID",
  "week": 2,
  "submission": 1,
  "plans": [
    {
      "plan_name": "bus6141-100mw",
      "sites": [{"bus_id": 6141, "connection_capacity_mw": 100, "generator_capacity_mw": 0, "storage_power_mw": 0}]
    },
    {
      "plan_name": "bus6141-250mw",
      "sites": [{"bus_id": 6141, "connection_capacity_mw": 250, "generator_capacity_mw": 0, "storage_power_mw": 0}]
    },
    {
      "plan_name": "bus6141-500mw",
      "sites": [{"bus_id": 6141, "connection_capacity_mw": 500, "generator_capacity_mw": 0, "storage_power_mw": 0}]
    }
  ]
}
```

Run it with the same command as the single experiment, changing the plans path
and experiment ID. The three previews are independent. Compare valid rows from
the same scenario, rules, week, stride, and base-load version. A larger score
may simply reflect a larger connection; compare score alongside served
fraction, served load, and costs.

For a quick PowerShell comparison of selected summary columns:

```powershell
Import-Csv .\analysis\run_database.csv |
  Where-Object { $_.experiment_id -eq "bus6141-size-sweep" } |
  Select-Object plan_name, status, score_usd, served_load_mwh, served_fraction,
    alpha_mean, it_value_usd, energy_cost_usd, generator_operating_cost_usd,
    generator_capital_cost_usd, storage_capital_cost_usd, site_cost_usd,
    curtailment_mw
```

Interpret `alpha_mean` carefully: in this implementation it is the plan's
`served_fraction` (team service fraction), not an independently computed mean
of per-site allocation factors. `alpha_min` and `alpha_max` are blank. Use the
raw preview JSON if a more detailed allocation view is needed.

## Adding New Plans

1. Store candidate plan JSON files in a team-managed directory such as
   `analysis/experiments/` or a dedicated study folder. Do not place hand-made
   files inside an existing generated run directory.
2. Use descriptive, unique `plan_name` values containing the parameter being
   changed, for example `bus6141-g0-storage0` and
   `bus6141-g250-storage0`.
3. Add the candidates to a JSON list or to a manifest's `plans` array. The
   runner does not search directories or automatically discover new plan files.
4. Use a new `experiment_id` for a new study. Each candidate gets a new
   UUID-based run folder. Results are appended, not replaced.
5. Keep the JSON input under version control if it is part of the reproducible
   experiment. Review `git status` before committing because the default CSV
   database and log are persistent append targets.

For multi-site plans, capacity totals are validated across every site in the
candidate. Reusing the same bus for several sites results in their capacities
being aggregated by bus in the run database, while the generated submission
still has one row per site.

## Run Database

`analysis/run_database.csv` is the row-per-candidate summary. The repository
file is a header-only schema until runs are performed. The runner checks the
existing header against its expected schema before appending, but does not
deduplicate records, lock the file against simultaneous processes, or make
the append transactional. Do not run multiple experiment-runner processes
against the same database/log at once. If a column is added or reordered, the
runner will reject the mismatched file rather than silently writing shifted
values.

All 59 columns are described below. JSON-suffixed columns contain compact JSON
text inside a CSV cell.

| Column | Meaning |
|---|---|
| `record_id` | Unique ID for this database row. |
| `experiment_id` | Experiment grouping label. |
| `run_id` | UUID for this candidate's run folder. |
| `timestamp_utc` | UTC time the summary row was created. |
| `plan_name` | Candidate's display name. |
| `plan_source` | Candidate source metadata; defaults to `candidate-list`. |
| `team_id` | Team ID in the generated candidate CSV. |
| `week` | Week number, 1–3. |
| `submission` | Submission number, 1 or 2. |
| `scenario_id` | Candidate-provided scenario label; blank if omitted. |
| `scenario_sha256` | Hash of the scenario directory's relative file names and file hashes. |
| `rules_sha256` | SHA-256 hash of the selected scoring-rules file. |
| `release_sha256` | SHA-256 hash of the selected release-configuration file. |
| `base_load_sha256` | Hash of the supplied base-load directory; blank when not provided. |
| `seed` | Candidate-provided integer metadata; it is recorded but not used to randomize the preview. |
| `mode` | Always `preview` for this runner. |
| `status` | Summary state such as `success`, `invalid_plan`, or `evaluator_failure`. |
| `valid` | `true` or `false` from CSV validation. Invalid candidates do not reach preview. |
| `allocation_triggered` | Whether the preview used its allocation projection. |
| `evaluation_status` | Preview state, such as valid preview, not run, or evaluator failure. |
| `candidate_csv_path` | Path to generated `candidate.csv`. |
| `validation_output_path` | Path to `validation.json`. |
| `preview_output_path` | Path to `preview.json`, if it exists. |
| `official_output_path` | Reserved for official evaluation; currently blank. |
| `git_revision` | Git `HEAD` revision when it can be read; otherwise blank. |
| `buses_used_json` | Sorted bus IDs present in the plan. |
| `connection_capacity_mw_by_bus_json` | Sum of connection capacity at each bus, in MW. |
| `generator_capacity_mw_by_bus_json` | Sum of generator capacity at each bus, in MW. |
| `storage_power_mw_by_bus_json` | Sum of storage power at each bus, in MW. |
| `storage_energy_mwh_by_bus_json` | Sum of storage energy at each bus, in MWh. |
| `total_connection_capacity_mw` | Total requested connection capacity across sites, MW. |
| `total_generator_capacity_mw` | Total generator nameplate capacity across sites, MW. |
| `total_storage_power_mw` | Total storage power across sites, MW. |
| `total_storage_energy_mwh` | Total storage energy across sites, MWh. |
| `requested_capacity_mw` | Requested capacity used by the preview scoring/allocation result. |
| `allocated_capacity_mw` | Requested capacity multiplied by the returned team service fraction. |
| `score_usd` | Preview team score in USD. Blank when the preview did not provide a score. |
| `served_load_mwh` | Preview team served-load metric in MWh. Blank when unavailable. |
| `served_fraction` | Preview's team-level service fraction. This is not a per-site alpha series. |
| `it_value_usd` | Preview IT value, USD. |
| `energy_cost_usd` | Preview grid-energy cost, USD. |
| `generator_operating_cost_usd` | Preview private-generator operating cost, USD. |
| `generator_capital_cost_usd` | Preview generator capital charge, USD. |
| `storage_capital_cost_usd` | Preview storage capital charge, USD. It may be nonzero even though storage is idle in the preview. |
| `site_cost_usd` | Preview site/connection capital charge, USD. |
| `alpha_min` | Reserved per-site allocation statistic; currently blank. |
| `alpha_mean` | Currently duplicates `served_fraction`; do not interpret as a true per-site mean. |
| `alpha_max` | Reserved per-site allocation statistic; currently blank. |
| `curtailment_mw` | Requested connection capacity times one minus the team service fraction, MW. |
| `cpu_runtime_seconds` | Wall-clock time spent running the preview. |
| `peak_memory_gib` | Reserved memory metric; currently blank. |
| `binding_period_indices_json` | Reserved binding-period detail; currently `[]`. |
| `binding_branches_json` | Reserved binding-branch detail; currently `[]`. |
| `congestion_indicators_json` | Projection and preview metadata, including storage-not-dispatched and allocation-triggered indicators. It is not a full congestion report. |
| `maximum_branch_loading_pct` | Reserved branch-loading metric; currently blank. |
| `maximum_generator_utilization_pct` | Reserved generator-utilization metric; currently blank. |
| `warning_text` | Warning text returned by the preview, if any. |
| `issues_json` | JSON array of CSV-validation issues and any rejected-submission messages. |
| `raw_output_sha256` | Hash of the raw preview output JSON, when present. |

Do not treat blank score/cost fields as zero: blanks mean the preview did not
provide a scored value. Also do not interpret empty `binding_*` fields as
evidence that no constraints bound; the runner currently does not extract
those diagnostics into the summary row.

## Experiment Log

`analysis/experiment_log.csv` records events during generation, validation,
preview, and database append. One candidate normally creates multiple event
rows. It is intended for tracing workflow failures, not for ranking strategies.

| Column | Meaning |
|---|---|
| `event_id` | Unique event UUID. |
| `timestamp_utc` | UTC time of the event. |
| `experiment_id` | Experiment grouping label. |
| `run_id` | Candidate run UUID. |
| `plan_name` | Candidate name. |
| `phase` | Workflow phase, such as generate, validate, preview, or database. |
| `event_type` | Specific event name, such as preview started or validation completed. |
| `status` | Event result, such as started, success, or failure. |
| `elapsed_seconds` | Elapsed time recorded for that event; zero when not applicable. |
| `candidate_csv_path` | Candidate CSV path when relevant. |
| `validation_output_path` | Validation JSON path when relevant. |
| `preview_output_path` | Preview JSON path when relevant. |
| `official_output_path` | Reserved for an official result; currently blank. |
| `details_path` | Optional detailed-output path; currently not populated by the runner. |
| `message` | Human-readable event status or error detail. |
| `git_revision` | Git `HEAD` revision when available. |
| `scenario_sha256` | Scenario directory hash for the run. |
| `rules_sha256` | Rules-file hash for the run. |
| `base_load_sha256` | Base-load-directory hash, or blank when none was supplied. |

## Reproducing Existing Studies

### Hosting-capacity studies

Hosting capacity is an optimization result, not a candidate-plan preview. Use
the separate `ercot-game-hosting-capacity` command and a new output directory.
For example, to calculate one bus across the 120-period representative package:

```powershell
ercot-game-hosting-capacity `
  --artifact-dir .\ercot-connection-game\data\processed\activsg2000_representative_v1 `
  --bus-id 6141 `
  --period-count 120 `
  --output-dir .\runs\hosting-capacity-6141
```

Repeat `--bus-id` for additional buses or omit it to request the full network.
The full matrix is a substantially larger optimization run; do not use it as a
shortcut for a few plan previews. Existing results and methodology are in
[`analysis/carter_week1_material/hosting_capacity_all_buses.csv`](../analysis/carter_week1_material/hosting_capacity_all_buses.csv),
[`analysis/carter_week1_material/bus_screening_metrics.csv`](../analysis/carter_week1_material/bus_screening_metrics.csv),
and [`analysis/headroom_interaction_report.md`](../analysis/headroom_interaction_report.md).
The experiment runner does not import these HC outputs into its database.

### Site-size sweeps

Create one candidate per site size in a JSON list, as shown in
[Running Multiple Candidate Plans](#running-multiple-candidate-plans), while
holding bus, week, generation, storage, and scenario constant. Run the
experiment runner, then compare valid rows by `plan_name`, `score_usd`,
`served_fraction`, `served_load_mwh`, and cost columns.

Keep all candidate totals within the active capacity cap. Invalid oversized
candidates will be recorded but will have no preview score. The existing
site-size study and its assumptions/results are in
[`notes/carter_week1_notes/site_size_and_competition_study.md`](../notes/carter_week1_notes/site_size_and_competition_study.md)
and
[`analysis/carter_week1_material/site_size_sweep/`](../analysis/carter_week1_material/site_size_sweep/).

### Competition sweeps

Competition sweeps are **not supported by `experiment_runner.py`**. The runner
never includes more than one candidate CSV in a preview, so a list of five
candidates means five separate solo previews, not five candidates competing
against one another.

For joint competition, create a fresh submissions directory with one canonical
CSV for each team (our candidate plus one CSV per mock opponent), then use the
course batch evaluator. A typical full joint-evaluation command is:

```powershell
ercot-game-batch run `
  --submissions-dir .\runs\competition-01\inputs `
  --artifact-dir .\ercot-connection-game\data\processed\activsg2000_representative_v1 `
  --rules .\configs\scoring\dispatch_scoring_rules_500mw.json `
  --week 2 `
  --submission-number 1 `
  --solver-backend highs `
  --workers 1 `
  --output-mode compact `
  --output-dir .\runs\competition-01\results
```

Use distinct team IDs in all CSVs, and keep each scenario's inputs and results
in separate directories. To make a comparison fair, vary one factor at a time
and keep opponent plans, scoring rules, week, and base load fixed. The previous
competition and crowding assumptions/results are documented in the site-size
study and
[`notes/carter_week1_notes/crowding_study.md`](../notes/carter_week1_notes/crowding_study.md).
These joint results are not automatically appended to the runner's database.

### Generator studies

Generator capacity is a candidate-plan input. Create otherwise-identical
candidates with generator capacity values ranging from zero to the permitted
limit (`G <= C` in the finalized release), then run them through the runner
for an initial solo-preview comparison. Inspect served fraction and
`generator_operating_cost_usd`, `generator_capital_cost_usd`, and `score_usd`.
Keep each plan's connection capacity, site, week, and scenario unchanged.

The preview generator has no daily energy budget. Confirm any promising
generator plan with a full `ercot-game-batch run` using the finalized rules,
before drawing conclusions. See
[`configs/strategies/full_generation.json`](../configs/strategies/full_generation.json)
for an existing team strategy configuration and
[`docs/STRATEGY_DEVELOPMENT.md`](STRATEGY_DEVELOPMENT.md) for the team strategy
generation/evaluation workflow.

### Battery studies

You can generate candidate plans with different storage power and energy
capacities, but the runner's student preview leaves storage idle. It will
validate the selected battery and may include storage capital charges, but
will not capture charge/discharge value, storage dispatch, or the battery's
effect on served load. Therefore this runner cannot provide a meaningful
performance comparison of battery operating strategies.

For battery analysis, use the full course batch evaluator with the intended
joint submission set and full 120-period horizon. Compare its dispatch and
score outputs, not the runner's `preview.json`. The repository strategy guide
also recommends full-horizon evaluation for storage; see
[`docs/STRATEGY_DEVELOPMENT.md`](STRATEGY_DEVELOPMENT.md#9-evaluate-the-candidate-with-the-instructor-tools).

## Best Practices

- Use a descriptive `experiment_id` and `plan_name`, with one parameter change
  at a time.
- Keep candidate JSON, assumptions, and external opponent CSVs in a
  study-specific directory. Keep generated files under `runs/`.
- Use a new experiment ID for each distinct set of assumptions; never edit a
  candidate CSV after a run and treat it as the original input.
- Compare runs only when their scenario/rules hashes, week, stride, and base
  load are compatible.
- Use `--preview-stride 1` for conclusions. A larger stride samples fewer
  periods and can miss the limiting period.
- Confirm every candidate's `valid` status before comparing score. Keep invalid
  plans as validation evidence, but do not treat their blank score as zero.
- Preview is useful for screening only. Validate final candidates with the
  official batch evaluator, especially under competition, Submission 2, Week 3
  energy charges, or storage dispatch.
- Do not run concurrent processes against the same master CSV files. The
  append implementation validates headers but does not lock or transactionally
  coordinate writes.
- Preserve the generated CSV, normalized `plan.json`, validation JSON, raw
  preview output, and input hashes for a reproducible result.

## Troubleshooting

| Symptom | Likely cause | What to check |
|---|---|---|
| `--help` works but importing `ercot_game` fails | The course package is not installed into the active Python environment. | Run `python -m pip install -e .\ercot-connection-game` using the same `python` executable. |
| JSON parse error | Missing comma/quote, invalid JSON syntax, or passing a path that does not exist (the argument is then treated as inline JSON). | Validate the file with a JSON-aware editor and confirm the path from the current working directory. |
| No runs, or fewer rows than expected | A candidate list item was not a JSON object and was filtered out; or the JSON list is empty. | Check list item types and confirm the final `Appended N preview runs` count. |
| `plan requires plan_name` / `sites must be a list` | Candidate structure does not match the input schema. | Use `plan_name` (or `name`) and a non-empty `sites` array (or `site_list`). |
| `bus_id` missing or validation says bus is unknown | A site has no `bus_id`/`bus`, or the bus is not present in the selected scenario package. | Check bus IDs against the exact scenario package being used. |
| Numeric capacity error | Value cannot be converted to a finite, non-negative number. | Use JSON numbers; avoid strings such as `"250 MW"`, `null`, negative numbers, and NaN/Infinity. |
| Validation says generator exceeds connection | `generator_capacity_mw > connection_capacity_mw`, or a stricter active release limit applies. | Reduce generator capacity or increase connection capacity within team cap. |
| Validation says team cap exceeded | Sum of connection capacity across sites is above the selected rules/release maximum. | Reduce connection capacity. Do not assume the installed course subtree default matches finalized team rules. |
| Storage validation failure | Storage energy/power does not satisfy release limits (typically four-hour storage), or a capacity is inconsistent. | Set both power and energy explicitly, usually `energy = 4 × power`, and check the active rules. |
| Preview command fails after CSV validation | Scenario/rules mismatch, missing package data, evaluator/solver issue, or preview timeout. | Read `preview/preview.stderr.txt`, `preview/preview.stdout.txt`, and `preview/preview.json` warning; verify paths and package installation. |
| Preview has a warning or allocation was triggered | Full requests could not be served in the preview's joint dispatch/projection. | Read the raw preview JSON. `allocation_triggered` is a significant result, not necessarily a CSV validation failure. |
| Storage plan gets no operating benefit | Expected behavior of student preview. | Use the official full evaluator for battery dispatch; do not use the runner to rank battery value. |
| Database append fails with a schema mismatch | Existing CSV header differs from the runner's expected column order. | Back up the file and reconcile the schema deliberately. Do not delete historical rows to force an append. |
| Duplicate rows appear | Runs are append-only and there is no duplicate detection. | Give each run a unique experiment ID and check the database before rerunning. |
| Paths in a manifest do not resolve | Manifest paths are resolved relative to the working directory. | Run from the repository root or use absolute paths. |
| Submission 2 base load is rejected or seems inconsistent | `--base-load-from` does not point to a compatible evaluator output, or the base load was applied twice. | Point to the S1 evaluator output containing `site_net_withdrawal.csv` and use the original scenario package. |

If a preview fails, retain the failure artifacts and log rows. Do not replace
missing outputs with zero or silently reuse another run's result.
