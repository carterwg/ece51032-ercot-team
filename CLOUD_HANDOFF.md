# ERCOT team project: cloud handoff

**State recorded:** November 25, 2026. Update this note when new official feedback or a selected submission changes the state below. This document is for a fresh Codex Cloud workspace; it does not assume access to the previous local chat, Mac, `Downloads/`, or uncommitted solver outputs.

## Where to start

- GitHub repository: `carterwg/ece51032-ercot-team`, working branch **`Saket`**. Check the branch and pull its latest commits before running an analysis. The course code in `ercot-connection-game/` is already tracked in this repository.
- Read [README.md](README.md) for setup, [the post-W1S1 findings](notes/saket_findings_after_w1s1_results.md) for the current analysis, and [the finalized release](configs/rounds/finalized_release_500mw.json) plus [matching rules](configs/scoring/dispatch_scoring_rules_500mw.json) for the team-specific 500 MW cap.
- [The official evaluation guide](notes/OFFICIAL_EVALUATION.md) explains the carryover, dispatch, and scoring process. Its imported course example still says **1,000 MW**; use our finalized 500 MW release for this project. [The older project-state note](notes/current_state_of_project.md) also contains pre-result and 1,000 MW claims and should not guide a new submission.
- Treat public results, reconstructed rivals, and modeled counterfactuals as three different evidence levels. A numerical match to public bus totals does not reveal the original private CSVs.

## Actual result and current task

Week 1 is practice and excluded from the final game score. The four scored rounds are Week 2 Submissions 1 and 2 and Week 3 Submissions 1 and 2. Weeks 1–2 do not charge for grid energy; Week 3 does. Within each week, Submission 1 sites become fixed **hourly net grid withdrawal** in the Submission 2 base. They are not scored again in Submission 2; each new submission may request up to 500 MW and must use new site IDs. The system resets to the representative base between weeks.

The instructor's Week 1 Submission 1 (W1S1) announcement says **9 of 10 teams submitted**, every submitting team requested 500 MW, and 4,355.4 of 4,500 MW was allocated. Our private feedback: **rank 3/9**, **$17.930B**, and **500/500 MW** allocated. Our actual site was 500 MW at bus `6141`, generator 97 MW, storage 99 MW / 396 MWh. The original submitted CSV is archived at [our W1S1 CSV](submissions/week1/team07_week1_sub1.csv). Preserve this archive; its historical `team_id` format differs from the `team07` label used by the local reconstruction.

The next immediate decision is **Week 1 Submission 2 (W1S2)**. The class announcement gave **Sunday, November 29, 2026, 11:59 p.m.** as its deadline; verify the live course portal before upload. Submit **only new sites**, with site IDs not used in W1S1. A new site may use the same bus as an earlier one. The announcement says to run `ercot-game-check-csv` on the exact file and confirm `VALID`, then have one team member upload one UTF-8 CSV named `teamXX_week1_sub2.csv`, using `teamXX` in every `team_id` cell. Confirm the exact team ID and portal requirements against the current course instructions; the archived W1S1 CSV is not a template for that ID format.

No final W1S2 CSV is identified in this handoff. Do not mistake a modeled candidate for a selected or uploaded plan.

## What our W1S1 analysis established

The instructor's [public installation CSV](analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv) and [interactive map](analysis/w1s1_public_reconstruction/grid_map_w1s1.svg) are committed here. The CSV has **post-allocation totals at each bus across all teams**. It contains no team or site IDs. Our [reconstruction](analysis/w1s1_public_reconstruction/results/s1_baseline.json) uses eight inferred rival plans plus ours. It matches the published 4,355.4 MW class total, bus totals to rounding, and the published score order/precision. It is a strong **working hypothesis**, not a unique identification of rival bids. Its modeled generator operating cost for us also differs slightly from the private feedback.

The inferred first-place plan is 25 sites of 20 MW, each with 1 MW local generation. Its modeled score is $18.211B. Our submitted site scored $17.930B. In that reconstructed field, a **500 MW grid-only** request at bus `6141` would have received only **418.914 MW** and scored $15.301B. A C500/G1/no-storage request would have received **499.742 MW** and scored $18.252B. These are jointly reallocated model counterfactuals, not alternate historical results. The [36-case retrospective](analysis/w1s1_public_reconstruction/results/s1_36_case_audit.json) explains why the earlier equipment sizing protected full admission yet spent too much capital for this realized field.

The editable [ten-team S1 runner](analysis/w1s1_public_reconstruction/run_my_ten_team_s1.py) models eight inferred rivals, an imaginary tenth team that copies the 25 × 20 MW inferred leader, and an editable `OUR_SUBMISSION_CSV` string for `team07`. It prints the score, rank, and allocated MW for all ten teams. It is a scenario tool, not a prediction that the absent team will choose that plan.

For W1S2, one conditional simulation carries the **reconstructed** S1 hourly net withdrawals into the base and lets rivals repeat their S1 methods. In that field, only about **99 MW** of new class load is admitted; repeating our G97/P99 S1 plan receives zero. A new single C500/G500/no-storage site at `6141` receives **500 MW** and scores **$17.259B**. See the [repeat field](analysis/w1s1_public_reconstruction/results/s2_repeat.json) and [G500 candidate](analysis/w1s1_public_reconstruction/results/s2_g500_6141.json). This is the strongest completed candidate in that specific repeat-rival field, **not** a proved optimum or guaranteed real W1S2 award. Other later S2 sweeps use different rival assumptions. The [five-site study](analysis/w1s1_public_reconstruction/results/s2_five_site_location_report.md) also found score sensitivity to which site ID is assigned to which bus, so retain the exact CSV mapping when comparing a result.

The W1S1 map exposes average bus LMPs, but Weeks 1–2 do not bill energy. The [post-result note](notes/saket_findings_after_w1s1_results.md) contains a labeled Week-3-style hourly-LMP counterfactual; do not apply a simple map-average LMP as an actual Week 1 charge.

## Repository map

| Path | Purpose |
| --- | --- |
| [`analysis/w1s1_public_reconstruction/`](analysis/w1s1_public_reconstruction/) | Committed public files, reconstruction scripts, counterfactual runners, compact result JSON/CSV. |
| [`analysis/carter_week1_material/bus_screening_metrics.csv`](analysis/carter_week1_material/bus_screening_metrics.csv) | Earlier bus screening; a standalone screen, not a guarantee of multi-team admission or score. |
| [`analysis/carter_week1_material/hosting_capacity_all_buses.csv`](analysis/carter_week1_material/hosting_capacity_all_buses.csv) | Standalone hosting-capacity estimates on the earlier base. |
| [`notes/saket_findings_after_w1s1_results.md`](notes/saket_findings_after_w1s1_results.md) | Detailed interpretation, numeric results, caveats, and reproduction commands. |
| [`configs/rounds/finalized_release_500mw.json`](configs/rounds/finalized_release_500mw.json) | Active team release: 500 MW cap and carryover contract. |
| [`configs/scoring/dispatch_scoring_rules_500mw.json`](configs/scoring/dispatch_scoring_rules_500mw.json) | Matching score settings. |
| [`submissions/`](submissions/) | Deliberately selected/archived submission files; inspect before assuming a candidate was submitted. |
| [`ercot-connection-game/`](ercot-connection-game/) | Full imported instructor evaluator and synthetic scenario package. |
| [`runs/`](runs/) | Generated raw runs, ignored by Git and absent from a fresh Cloud checkout. |

## Fresh Cloud environment and reproducibility

Use **this GitHub repository and the `Saket` branch** in a Codex Cloud environment. A separate copy of the repo is unnecessary. A named, reusable Cloud environment is useful for work across desktop, web, and mobile; the existing desktop project may also work with the default environment when its GitHub repo is connected. The [official Cloud environment guide](https://learn.chatgpt.com/docs/environments/cloud-environments) describes the setup. During setup, have Codex use Python 3.11 or newer and run the commands below from the team repository root. The environment needs access to the private GitHub repo and Python package installation. It does not need the Mac's Box folder path.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ./ercot-connection-game
python -m pip install -e '.[test,plot]'
python -m pytest -q
```

To rerun the editable ten-team S1 scenario, edit only `OUR_SUBMISSION_CSV` in [the runner](analysis/w1s1_public_reconstruction/run_my_ten_team_s1.py), then run:

```bash
.venv/bin/python analysis/w1s1_public_reconstruction/run_my_ten_team_s1.py
```

The [post-result note](notes/saket_findings_after_w1s1_results.md#scope-and-reproduction) has the baseline and W1S2 commands. They regenerate data under ignored `runs/`, which can be compute-intensive. Prefer the committed compact result files for initial reading. The course engine evaluates 120 representative hourly periods (five weighted days), not a single-hour proxy.

For an actual submission, use the exact seven-column header:

```text
team_id,site_id,bus_id,connection_capacity_mw,generator_capacity_mw,storage_power_mw,storage_energy_mwh
```

For a four-hour battery, `storage_energy_mwh = 4 × storage_power_mw`; generator capacity cannot exceed connection capacity. The 500 MW limit is on the team's total connection capacity **in that submission**. Validate the final exported file with the course checker and the current team rules, and inspect the CSV itself before upload. Candidate generation or simulation does **not** upload anything to the course portal.

## Working across Cloud tasks

The durable state is Git, not a specific Cloud task's virtual machine. Commit and push any selected CSV, updated interpretation, and compact evidence to `Saket` (or a review branch agreed with the team); check for newer remote changes before pushing. `runs/` and `.venv/` are ignored. Local `Downloads/` files and this chat's screenshots are unavailable in a fresh Cloud task unless committed or reattached. The actual W1S1 feedback values and course announcement from those screenshots are recorded above, while the public CSV/SVG are in Git. Later private instructor feedback or a new official S2 base must be provided to the Cloud task when received. Revisit the original Cloud task to continue its uncommitted work; a new task has its own workspace. See [Using Codex Cloud](https://help.openai.com/en/articles/20001545-using-codex-cloud).

Suggested first Cloud prompt:

> Work in `carterwg/ece51032-ercot-team` on branch `Saket`. Read `AGENTS.md` and `CLOUD_HANDOFF.md`, check the latest commit and environment, and summarize the actual W1S1 result versus inferred rivals. Then help evaluate W1S2 candidates using the finalized 500 MW rules and new site IDs. Treat the reconstructed S2 base as conditional until official S2 base data is available. Show the exact CSV and validation result before recommending upload.
