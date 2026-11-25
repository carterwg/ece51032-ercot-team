# Reproduce the Week 1 Submission 2 site ID sensitivity

This package runs four controlled versions of the same nine-team hypothetical
Submission 2 scenario with the course's `ercot-game` evaluator. It asks whether
changing arbitrary site IDs, while keeping each team's physical load and
equipment at the same buses, changes private scores.

## What is in the package

- `s2-base/`: the exact 120-hour prepared network used in the test. It includes
  fixed hourly net withdrawals from a **reconstructed** Submission 1 field.
- `s1-output/.../site_net_withdrawal.csv`: reconstructed Submission 1
  withdrawals, used by the evaluator to reserve prior site IDs.
- `inputs/team-000.csv` through `team-008.csv`: the nine exact Submission 2
  submissions. All nine request 500 MW of load and 500 MW of co-located
  generation, with no new storage. Only `team-008.csv` is modified by the runner.
- `rules.json`: the finalized 500 MW scoring rules.
- `reproduce.py`: the four-case evaluator script.
- `expected_results.csv`: the observed outputs from Python 3.14.3, HiGHS
  1.16.0, and `ercot-game` 0.3.0.

The reconstructed first submission was calibrated against the public
installation CSV and reported aggregate allocation. It is **not** the
instructor's hidden set of actual team submissions. This package tests a
behavior of the local evaluator on one specified input, not an official
Submission 2 outcome.

## Run

You need the course evaluator source at `ercot-connection-game/` inside the
`ece51032-ercot-team` repository and a Python environment at `.venv/`.
From the repository root, install dependencies if needed:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e ./ercot-connection-game
```

Unzip this package, then run:

```bash
./site_id_repro_bundle/run.sh /absolute/path/to/ece51032-ercot-team /absolute/path/to/new-results
```

Use a fresh `new-results` directory. The run evaluates 120 hours for all nine
teams in each of four cases and writes a `result.json` per case. Compare them
with `expected_results.csv`. Solver versions may change the selected dispatch
within an equal-cost tie; the observed dollar values are version-specific.

## The controlled change

The focal submission is `rival-100mw-mixed` in `team-008.csv`. The name refers
to its inferred Submission 1 plan; in this Submission 2 test it has five
identical 100 MW load / 100 MW generator sites, no storage:

| Bus | Original site ID | Reassigned site ID |
| --- | --- | --- |
| 7098 | `w1-s2-0001` | `w1-s2-0005` |
| 5047 | `w1-s2-0002` | `w1-s2-0004` |
| 7042 | `w1-s2-0003` | `w1-s2-0003` |
| 6141 | `w1-s2-0004` | `w1-s2-0002` |
| 6197 | `w1-s2-0005` | `w1-s2-0001` |

The runner compares `original`, `reverse_rows_only` (same ID-to-bus pairs),
`reverse_ids_only` (same bus row order), and `reverse_both` (restores the
original ID-to-bus pairs). The eight other team CSVs and the network base are
byte-for-byte identical in all cases.

## Observed result

All nine teams receive their full 500 MW in all four cases. The focal team's
score is $17,063,653,290.748 in the original, row-only, and reverse-both
cases. It is $17,032,448,127.354 when only site IDs are reassigned: a
$31,205,163.394 decrease. Its private generator operating cost rises by the
same amount. The sum of all nine team scores changes by about $0.002, and the
sum of the 120 unweighted hourly market dispatch objectives changes by about
$0.00003, both numerical noise at this scale.

The course parser uses site IDs to connect equipment to locations and embeds
them in generator IDs (`csv_submission.py`). The adapter sorts generators by
ID before handing them to the DCOPF (`plan_adapter.py`), and the DCOPF adds LP
columns in that order (`dcopf.py`). Site ID itself is not a cost or network
coefficient. The result is consistent with different equal-cost optimal
dispatches being selected after the variable order changes. The adapter has
an explicit proportional tie-break for generators at the **same** bus; it does
not resolve ties across different buses.
