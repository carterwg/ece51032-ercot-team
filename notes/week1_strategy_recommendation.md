# Week 1 practice strategy recommendation

## Recommendation at a glance

Use the unscored practice week to measure the real joint-allocation behavior
before committing to a score-maximizing Week 2 plan:

1. **Week 1 Submission 1:** submit four 250 MW, grid-only sites at buses
   **2054, 6062, 6298, and 7414** (1,000 MW total).
2. Read the actual joint-evaluation results, especially site service/allocation,
   period of curtailment, generator dispatch, and binding branches.
3. **Week 1 Submission 2:** add two new 250 MW sites at the most informative
   bus from Submission 1: a no-resource control and one resource treatment.
   If a transmission branch binds while generation headroom remains, use a
   battery treatment (`P=62.5 MW`, `B=250 MWh`). If the system is generation-
   constrained instead, use a generator treatment (`G=125 MW`). Do not combine
   generator and battery in the treatment site; that would obscure which
   resource helped.

Each submission stays within the 1,000 MW team connection cap. Submission 2
must list only new sites; the Submission 1 sites remain in the base load, so
the second experiment measures residual headroom after the first build.
Week 1 is practice/feedback-only and does not count toward the final score.
See the [Week 1 schedule and within-week rules](../docs/OFFICIAL_EVALUATION.md#L40-L62)
and the [released cap](../data/teaching/game_release_representative_v1.json#L11-L12).

## Why these buses

| Bus | Evidence from the prior analysis | What it contributes to the experiment |
|---:|---|---|
| 2054 | 3,024.604 MW minimum hosting capacity; no binding branch at its individual hosting limit; generation-limited. Composite screening rank 32. | Strong grid-served reference and a generation-ceiling case. |
| 6062 | 2,958.841 MW; uniquely limited by b01773 (6075–6062, 2,020 MVA). | A distinct transmission-constrained corridor. |
| 6298 | 2,513.833 MW; uniquely limited by b01758 (6298–6056, 2,020 MVA). | A different unique corridor with lower headroom. |
| 7414 | 2,795.556 MW; b02136 binds and is shared with bus 7095 in the diverse shortlist. | A shared-corridor comparison, in a distinct electrical region. |

These are not four equally good individual locations: bus 6298 has less
individual headroom, and 6062/6298/7414 have line limits at their hosting
ceilings. Their value in Week 1 is diagnostic diversity. See the [diversified
top-20 results](../analysis/bus_rankings/diversified_top20.csv) and [bottleneck
analysis](../analysis/bus_rankings/bottleneck_diversity_analysis.csv).

## Specific Week 1 recommendations

The options below are designed to answer different questions. Do not stack
the standalone alternatives into one submission: each submission has a
1,000 MW connection-capacity cap. The primary sequence above is the
recommended use of the two practice submissions.

| Recommendation | Proposed buses and sizes | Generation? | Batteries? | Why the submission is valuable | Hypothesis being tested | Information learned |
|---|---|---|---|---|---|---|
| **Primary: spatial information screen (S1)** | 250 MW each at 2054, 6062, 6298, 7414; 1,000 MW total. | No (`G=0`). | No (`P=B=0`). | Holds total request and resource mix constant while sampling generation-limited, unique-corridor, and shared-corridor sites. | Geographic/electrical diversity can change allocation and line stress even when individual hosting capacities are all high. | Which sites are curtailed first, whether b01773/b01758/b02136 or a system-wide generation limit binds, and whether the model gives any location advantage under actual team submissions. |
| **Adaptive: matched resource diagnostic (S2)** | At the most informative S1 bus, two new 250 MW sites at the same bus: one control with no assets; one with either `G=125 MW` **or** `P=62.5 MW, B=250 MWh`. 500 MW total new capacity. | Choose generator only if S1 suggests a generation shortage; otherwise `G=0`. | Choose a battery only if S1 shows transmission congestion with generation headroom; otherwise `P=B=0`. Never add both resources to the treatment site. | Keeps bus and site size matched while testing one intervention. The old S1 load remains in the network, so it tests whether the resource helps under residual congestion. | A generator reduces grid withdrawal whenever generation headroom is scarce; a four-hour battery can shift withdrawal away from line-constrained periods. | Change in served share/allocation, generator dispatch or battery state-of-charge, grid withdrawal, and binding constraints attributable to that one treatment. Use the instructor evaluation for battery conclusions; the student preview does not dispatch storage. |
| **Score-first benchmark** | 1,000 MW at 2054. | No. | No. | Existing no-competition previews fully served 1,000 MW at all tested candidate buses with equal scores; 2054 combines maximum-class hosting capacity and a strong screening rank. | A full grid-served site at a high-headroom bus is the best simple benchmark, provided competition does not curtail it. | Actual score and allocation under the class's joint plan; the difference between solo potential and competition outcomes. |
| **Contrarian portfolio** | 500 MW at 6298 and 500 MW at 7414. | No. | No. | Avoids putting all capacity at the generation-limited plateau buses and tests two distinct corridors with lower top-20 crowding overlap. | Unique or less-shared corridors can preserve service when teams cluster at the most obvious high-HC sites. | Whether corridor diversity produces better allocation than a single popular-area site; whether b01758 and b02136 remain limiting when combined. |
| **High-risk / high-reward stress test** | 1,000 MW at 6298. | No. | No. | Uses the full cap at the candidate with the lowest minimum hosting capacity among these four and a unique binding corridor. | The apparently weaker individual bus may nevertheless benefit from being on a unique corridor when other teams crowd elsewhere. | Whether competitors' locations matter more than standalone hosting rank, and the downside in curtailed MW if b01758 becomes the limiting constraint. This is a deliberate test, not a proven higher-return choice. |

For the matched resource diagnostic, the two-site treatment can alternatively
be run in separate practice versions: one with the generator and one with the
battery. If there is a way to obtain additional practice evaluations, separate
runs are preferable to combining both resources, because they identify the
contribution of each resource independently.

## Strategy labels

### Highest expected score for a later scored submission

**1,000 MW at bus 2054, with no generator or battery**, is the strongest
simple score-first choice in the current evidence. At 1,000 MW, the
no-competition preview score was about **$36.53 billion** and full service was
observed. A grid-served MW also has greater modeled net value than a fully
off-grid MW before Week 3 energy charges. This is a benchmark, not a
guaranteed expected value: the preview studies found that competition can
curtail large requests, and Week 3 LMP charges may change site comparisons.
The [site-size study](../analysis/site_size_and_competition_study.md) found
equal solo scores across the five candidates, so the data do not establish
2054 as a uniquely superior score bus.

### Highest information gain

**Four 250 MW grid-only sites at 2054, 6062, 6298, and 7414** in Submission 1,
followed by the adaptive matched resource test in Submission 2. It spans
three transmission-bottleneck patterns and a generation-limited case, then
uses the observed binding constraint to choose a single intervention.
Week 1's purpose is to reveal how the actual joint evaluator allocates
capacity, not merely to repeat solo hosting calculations.

### Highest contrarian

**500 MW at 6298 plus 500 MW at 7414, grid-only.** Bus 6298's b01758 corridor
was unique in the shortlist; 7414 sits in a one-member electrical region in
the diversified top-20 study and binds on b02136, shared with only one other
shortlisted bus. This is a test of whether those less-obvious corridors avoid
crowding, not a claim that they beat the top-HC buses.

### Highest risk / highest reward

**A full 1,000 MW grid-only site at bus 6298** is the clearest deliberate
high-variance bet among these recommendations: it offers the same
full-service upside if the unique corridor has room, but has less standalone
hosting headroom and a known line bottleneck. The existing crowding
experiments did **not** show it outperforming other candidates under the
tested equal-size rival scenarios, so take this as a contrarian experiment,
not the expected-score recommendation.

## What the existing artifacts do and do not establish

- The all-bus hosting results show that 1,530 buses hit the same approximately
  3,024.604 MW system generation ceiling in period 109. The reserve-margin
  study confirms this equals aggregate generation headroom at the peak-load
  period. Bus-specific transmission limits reduce hosting capacity below
  that ceiling at some locations.
- The joint 1079/2054 test reaches the generation limit at 3,024.604 MW total;
  the 6062/6298 pair reaches 3,007.890 MW and binds on b02136. The
  four-location portfolio also tops out at about 3,024.604 MW. These results
  show that individual hosting capacities do not add.
- In the previous competition and concentrated-crowding previews, candidate
  service fractions were effectively identical (about 50.4% with five
  rivals, 27.5% with ten). These are allocation outcomes under equal 1,000 MW
  requests and the preview's fairness allocation, not evidence that buses
  are universally interchangeable or equally resilient.
- The site-screening composite is a screening heuristic, not the game score.
  For example, 2054 ranks 32nd and 6062 ranks 258th on that composite, but
  6062 is still useful as a corridor stress-test site. Low base-load buses
  can also tie on that part of the metric, so it should not be read as a
  precise siting recommendation.
- The 1,500 MW and 2,000 MW site-size requests were rejected by the released
  1,000 MW per-submission cap. Do not use those unscored counterfactual sizes
  to plan an actual Week 1 file.
- Preview scores are non-authoritative; in particular, the preview does not
  dispatch storage. Use the instructor's full Week 1 results to assess a
  battery, and check the reported binding constraints and allocation before
  deciding on Submission 2.

## Supporting artifacts

- [All-bus hosting capacity](../runs/analysis/hosting_capacity_all_buses.csv)
- [Bus screening metrics](../runs/analysis/bus_screening_metrics.csv)
- [Diversified top 20](../analysis/bus_rankings/diversified_top20.csv)
- [Bottleneck diversity analysis](../analysis/bus_rankings/bottleneck_diversity_analysis.csv)
- [1079/2054 joint test](../analysis/experiments/1079_2054_joint_test.md)
- [6062/6298 joint test](../analysis/experiments/6062_6298_joint_test.md)
- [Portfolio comparison](../analysis/experiments/portfolio_comparison.md)
- [Site-size and competition study](../analysis/site_size_and_competition_study.md)
- [Crowding study](../analysis/crowding_study.md)
- [System reserve-margin study](../analysis/system_reserve_margin_study.md)
