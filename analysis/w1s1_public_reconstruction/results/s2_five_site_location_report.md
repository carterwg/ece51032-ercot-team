# Week 1 Submission 2: five-site location and ID sensitivity

## Question and fixed assumptions

This local experiment varies only the **five bus IDs** of the inferred
`rival-100mw-mixed` team's new Submission 2 sites. Each site requests 100 MW of
connection and 100 MW of local generation, with no storage. The team label,
site IDs, capacities, and order of sites are fixed across the main comparison;
bus IDs are sorted ascending in every case. All eight other team labels and
their new Submission 2 plans are unchanged. Team `team07` requests one new
500 MW load / 500 MW generator site at bus `6141`. Every other rival requests
500 MW of new load on its inferred Submission 1 buses, with `G=C` at each site.

The Submission 2 base is the **reconstructed** joint Submission 1 hourly net
withdrawal of nine teams, not an instructor-issued base or the rivals' private
files. Each portfolio is a separate fixed ten-year site plan; sites do not move
between hours. Week 1 grid purchases are not billed.

We tested 54 distinct five-bus sets: the inferred original layout, high-hosting
and screening layouts, concentrated and spread layouts, five one-site
substitutions, and 40 seeded random layouts. Every selected bus had at least
2,500 MW of standalone hosting capacity in the original base. This screen is
not itself a guarantee of Submission 2 admission; the full joint evaluation
checks admission directly.

## Results

| Sorted-order case | Five buses | Focal allocated MW | Focal score | Focal rank |
| --- | --- | ---: | ---: | ---: |
| Best tested (`random_spread_05`) | 2017, 3048, 5385, 6349, 8155 | 500 | $17.063980B | 1/9 |
| Inferred original | 2101, 6066, 6197, 7099, 8126 | 500 | $17.052200B | 1/9 |
| Worst tested (`random_high_hosting_12`) | 5295, 5304, 5380, 5388, 5395 | 500 | $16.952141B | 9/9 |

The best-to-worst difference is **$111.839M**, or **0.660%** of the worst
score. The median across the 54 sets is **$17.006900B**. Focal ranks range
from first to ninth. All nine teams are valid, feasible, and receive their full
500 MW in every case; the evaluator covers all 120 periods. The only changed
CSV fields across these 54 cases are the focal team's five `bus_id` values.
The reconstructed base and scoring-rule hashes match across all cases.

Because load value, site capital, and generator capital are identical, focal
score changes equal its generator operating-cost changes: **$199.307M** in the
best case and **$311.146M** in the worst. However, the sum of all nine teams'
scores changes by only **$2.118M** across all 54 cases. Most of the focal
score movement is a redistribution of generator dispatch cost among teams,
not a large change in total served load or combined team value. The fixed
`team07` plan's own score ranges by **$139.350M** across these focal-bus cases.

## Site-ID control and interpretation

The initial controls reordered the five-bus list. Because the CSV exporter
assigns site IDs `w1-s2-0001` through `w1-s2-0005` by list position, those
controls changed **both row order and which site ID belonged to each bus**.
Calling this a row-order effect alone was incorrect. For one fixed five-bus
set, the four generated ID-to-bus assignments spanned **$31.205M** in the
focal team's score, while the nine-team total score stayed constant to less
than one cent.

A separate two-factor test on that same physical set isolated the inputs:

| Change from original CSV | Focal score | Nine-team total score |
| --- | ---: | ---: |
| None | $17.063653B | $153.097433B |
| Reverse rows, retaining each ID-to-bus pair | $17.063653B | $153.097433B |
| Reverse site IDs, retaining bus row order | $17.032448B | $153.097433B |
| Reverse both, restoring original ID-to-bus pairs | $17.063653B | $153.097433B |

The sum of all 120 hourly dispatch objectives also matches to solver precision.
The affected team's generator operating cost rises by **$31.205M** when its
site IDs are reassigned. Four modeled hours on the heavily weighted September
10 representative day account for nearly all of that change. The course
optimizer is selecting different equal-cost generator dispatches and assigning
different private operating costs, even though the physical plans and market
objective are the same.

The main 54-case comparison uses a consistent ascending-bus-to-ID convention,
but this does **not** isolate a purely physical location effect: changing the
bus set also changes the ID-to-bus mapping. The firm 500 MW admission result is
robust across the tested layouts. The **$111.839M score range and ranks 1–9
belong to these generated bus-to-ID assignments**, not a proven intrinsic
advantage of the best bus set over the worst. The extrema are only among the
tested portfolios, not global optima or forecasts of private rival bids.

## Evidence

- [All 54 sorted-order cases](s2_five_site_location_sweep.csv)
- [Reproducible runner](../w1s2_five_site_location_sweep.py)
- [Site-ID and row-order diagnostic](../w1s2_row_id_order_diagnostic.py)
- [Four-case diagnostic results](s2_row_id_order_diagnostic.csv)
- `runs/w1s2-five-site-location-sorted/candidate_manifest.json` lists every
  candidate and each case directory contains `case.json`, the generated CSVs,
  the evaluator leaderboard, and the canonical evaluation output.
- `runs/w1s2-five-site-location-sweep/` contains the initial mixed controls.
- `runs/w1s2-row-id-order-diagnostic/` contains the separate row and ID tests.
