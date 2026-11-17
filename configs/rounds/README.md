# Finalized round settings

`finalized_release_500mw.json` is the default team profile. It applies the
user-confirmed finalized limit of **500 MW per team per submission** and points
to the corresponding scoring-rules copy under `configs/scoring/`. The imported
instructor subtree remains unchanged; its bundled release predates finalization.

Submission 2 still requires a compatible carried-base-load package and our actual
S1 CSV. Each week resets; Week 3 charges grid energy at joint-dispatch LMPs.
The team context rejects budgets above 500 MW even with a different release.
