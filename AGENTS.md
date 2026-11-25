# Repository guidance for Codex

- Read [CLOUD_HANDOFF.md](CLOUD_HANDOFF.md) before changing the game strategy or preparing a submission. It records the current state and points to the evidence.
- Work from the root of this repository. The instructor game under `ercot-connection-game/` is a tracked subtree, not a submodule.
- Use the finalized 500 MW per-team, per-submission release in `configs/rounds/finalized_release_500mw.json` and the matching scoring rules in `configs/scoring/dispatch_scoring_rules_500mw.json`. Some older notes and imported course documentation still describe a 1,000 MW limit.
- Distinguish observed instructor results from our inferred rival plans and conditional simulations. The public W1S1 bus CSV contains allocated bus totals, not private team submissions.
- For Submission 2, list only new sites with site IDs unused by our Submission 1. The prior submission's net withdrawals are part of the new base load.
- Keep candidate outputs in `runs/` and commit the selected CSV plus compact evidence when a result must be available in another workspace. Run the exact submission CSV through the appropriate checker before upload.
