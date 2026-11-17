# Strategy comparison and risk · finalized 500 MW case

The finalized limit is **500 MW per team per submission**. The team's comparison
scale is separate from the instructor's grade formula:

```text
S = W2S1 + W2S2 + W3S1 + W3S2, in billions of USD
Q(S) = 100 * (S - 49.67) / (73.0525 - 49.67)
```

Negative Q values and values above 100 remain visible. Normalize only complete
graded campaigns. Report inputs are numeric **USD**, converted to billions
internally. Missing scores and evaluator failures must not become zero.

## Meaning of the anchors

Both anchors assume one full new 500 MW budget in each of the four graded
submissions, with S1-to-S2 carryover and a reset between weeks.

- **Lower, $49.67B:** analytical C = G, with generators at full output throughout
  the weighted horizon and no batteries.
- **Upper, $73.0525B:** full allocation, all electricity from the grid at zero
  energy price, and no private generation or storage capital cost. This is an
  idealized scoring bound, not a guarantee of network feasibility. Actual Week 3
  prices come from joint-dispatch LMPs.

The measured `full_generation` strategy can buy cheaper grid electricity despite
C = G. Its actual score is recorded as observed; it is not forced to equal zero
on the normalized scale. The instructor's grading reference builds only in S1,
so it is distinct from this four-build comparison case.

The runtime retains the agreed rounding convention: the raw economics give
approximately $49.672277694B and $73.053148597B for the two analytical cases.
Comparison anchors remain $49.67B and $73.0525B. The profile is recorded in
[`finalized_500mw_reference.json`](../configs/scoring/finalized_500mw_reference.json).

## Active settings

Use [`finalized_release_500mw.json`](../configs/rounds/finalized_release_500mw.json)
and [`dispatch_scoring_rules_500mw.json`](../configs/scoring/dispatch_scoring_rules_500mw.json).
They apply the user-confirmed finalized cap while preserving the imported
instructor engine and the existing economic coefficients. The bundled course
release predates the capacity finalization.

The team context, CLI, and reporting scale reject budgets above 500 MW even if
an older release is supplied explicitly. Smaller budgets are supported for
smoke tests; their anchors scale by `budget_mw / 500`. Saved strategy campaigns
and notebooks contain only the finalized 500 MW case.

## Risk and frontier

For matched complete campaign scenarios j:

```text
mean_Q = mean(Q_j)
downside_risk = sqrt(mean(min(Q_j - mean_Q, 0)^2))
worst_Q = min(Q_j)
fraction_below_baseline = count(Q_j < 0) / scenario_count
```

Downside risk is lower semideviation around the strategy's own mean, in
normalized-score points. Its denominator includes every scenario. It describes
variability below the mean; worst-case and below-baseline statistics separately
expose losses against C = G. Scenarios are equally weighted. At least two matched
scenarios per strategy are required; a single solo run does not measure risk.

The Pareto frontier maximizes average Q and minimizes downside risk. A candidate
is dominated only if another is at least as good on both measures and strictly
better on one. Ties remain. There is no weighted composite score or automatic
winner selection. These summaries are not calibrated forecasts.

## Report input

Supply JSON with `capacity_per_submission_mw: 500`. Each strategy must have the
same campaign scenario IDs. Each scenario contains numeric USD scores for
exactly W2S1, W2S2, W3S1, and W3S2. This example shows the structure; replace
strings with actual numbers and add another matched scenario to calculate risk:

```json
{
  "capacity_per_submission_mw": 500,
  "strategies": {
    "full_generation": {
      "mixed-seed-1": {
        "week-2-submission-1": "numeric USD score",
        "week-2-submission-2": "numeric USD score",
        "week-3-submission-1": "numeric USD score",
        "week-3-submission-2": "numeric USD score"
      }
    }
  }
}
```

Explicit zero is valid for a genuinely scored zero or deliberately empty
new-build round. Practice scores, incomplete campaigns, and nonfinite values
are rejected.

```bash
team-strategy report --input campaign_scores.json --output-dir runs/comparison-001 --plot
```

Outputs are `input.json`, `comparison.json`, `comparison.csv`, and `frontier.png`.
