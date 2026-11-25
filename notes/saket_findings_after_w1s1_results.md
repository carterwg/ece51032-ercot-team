# Saket findings after W1S1 results

Prepared November 23, 2026. Week 1 is practice. These are local, full-horizon
course-evaluator runs conditioned on a reconstruction of the **nine** teams that
submitted in Week 1, Submission 1 (W1S1). They are not the instructor's hidden
team submissions or forecasts of what rivals will submit next.

## Public result and calibration

Nine of ten teams each requested 500 MW, for 4,500 MW total. The instructor
reported 4,355.4 MW allocated. Our team ranked **3 of 9**, scored **$17.930B**,
and received its full 500 MW at bus `6141` with 97 MW generation and a
99 MW / 396 MWh battery. The public [installation CSV](../analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv)
reports **allocated totals per bus across teams**, with no team or site IDs.
The [interactive map](../analysis/w1s1_public_reconstruction/grid_map_w1s1.svg)
shows bus and line summaries, including LMPs; it also does not identify owners.

One set of nine 500 MW requests, reconstructed from repeated CSV patterns, is:

| Inferred team plan in S1 | Model allocation | Model S1 score |
| --- | ---: | ---: |
| 25 × 20 MW, each with 1 MW generation | 499.941 MW | $18.211040B |
| 5 × 100 MW, each with 20 MW generation | 500.000 MW | $18.062859B |
| **Ours:** 500 MW at `6141`, G97, P99 / B396 | **500.000 MW** | **$17.930236B** |
| 5 × 100 MW, mixed generation: 25, 10, 50, 100, 0 MW | 490.967 MW | $17.562475B |
| 500 MW, 350 MW generation | 500.000 MW | $17.561990B |
| 2 × 250 MW, each G175 and P62.5 / B250 | 500.000 MW | $17.386914B |
| 2 × 250 MW, grid-only | 454.834 MW | $16.613531B |
| 5 × 100 MW, grid-only | 454.834 MW | $16.613529B |
| 100 × 5 MW, grid-only | 454.832 MW | $16.613450B |

The reconstruction explains the overlap rows exactly at the CSV's precision:
`1079: 115.513 = 90.967 + 19.998 + 4.548 MW`,
`3048: 247.415 = 227.417 + 19.998 MW`, and
`6197: 940.967 = 500 + 250 + 100 + 90.967 MW`. Its allocations total
**4,355.408 MW**; the largest difference at any published bus is **0.00035 MW**.
It reproduces the reported best, median, lowest, and our score at their published
three-decimal-billion precision, and puts us third. See the
[S1 results](../analysis/w1s1_public_reconstruction/results/s1_baseline.json)
and [per-team awards](../analysis/w1s1_public_reconstruction/results/s1_baseline_allocations.json).

This is strong calibration, not unique identification. The instructor's feedback
lists our generator operating cost as **$0.41M**; this reconstruction gives
**$0.451M**, so the original hidden rival inputs are not established exactly.
The 25-site team is the most likely first-place plan, but the public CSV alone
cannot prove ownership.

## Retrospective audit of the 36 earlier fields

The earlier 36-case study **succeeded at its stated admission test**: our
G97/P99 single site received at least 499.9 MW in all 36 modeled fields, and
the real W1S1 feedback awarded the full 500 MW. The ranking gap came from what
that test did not optimize. Each earlier field had **ten teams total**, with
**nine rivals using the same plan** within that field, spread over at most
five buses. The actual round had **nine teams total**, with a heterogeneous
mix that includes an inferred 25-site plan and a 100-site plan. The equipment
search kept our 500 MW at bus `6141`, then minimized its capital cost subject
to at least **499.9 MW in every stress field**. The final 1 MW refinement only
searched G85–105/P95–115. It did not compare the cost of failing that hard
threshold slightly against the much larger score benefit of buying less
equipment in the realized field. See the [36-field awards](../findings/Battery_S1_1MW_local_search.md)
and [search definition](../src/team_strategy/experiments/battery_s1_optimization.py).

To isolate this, we replaced only our S1 plan in the calibrated **eight-rival**
field. All other teams were jointly reallocated and rescored with the unchanged
120-period course evaluator:

| Our 500 MW site at `6141` | Our allocation | Our score | Rank |
| --- | ---: | ---: | ---: |
| Submitted G97/P99/B396 | 500.000 MW | $17.930236B | 3/9 |
| G0/P0 | 418.914 MW | $15.301488B | 6/9 |
| G1/P0 | 499.742 MW | **$18.251860B** | **1/9** |
| G25/P0 | 500.000 MW | $18.213186B | 2/9, within about $1,400 of first |
| G100/P0 | 500.000 MW | $18.062838B | 3/9 |

The [counterfactual summary](../analysis/w1s1_public_reconstruction/results/s1_36_case_audit.json)
and [runner](../analysis/w1s1_public_reconstruction/audit_single_site_no_storage.py)
preserve these checks. G1 misses the old 499.9 MW cutoff by just **0.158 MW**,
but its $2M generator and lack of storage more than offset the 0.258 MW of
curtailment relative to full allocation. It scores **$321.625M** above our
submitted plan in this reconstructed field. G25 obtains all 500 MW at our
original bus without a battery, so a 25-bus layout was **not necessary** for
the near-winning score in this particular reconstructed field.

The inferred first-place plan's G25 total costs about **$50M** in generator
capital, compared with our **$194M** generator and **$138.6M** storage capital.
In the calibrated S1 result, the first-place score exceeds ours by
**$280.804M**. Approximately **$282.606M** of the difference is equipment
capital; its slightly lower allocated load and differences in site and
operating terms nearly offset the rest. The lesson is to optimize expected
score and rank across plausible mixed fields, while treating minimum admission
as a tradeoff, rather than requiring near-perfect admission in every extreme
homogeneous field. These counterfactual ranks remain conditional on the
reconstructed rivals, not proven historical outcomes.

## One MW of generation at each grid-only site

In two separate W1S1 counterfactuals, we changed only one inferred grid-only
team at a time. Every site in that team's plan received a **1 MW generator**;
our submitted G97/P99 plan and the other seven rival plans remained fixed.
The unchanged 120-period evaluator reallocated and rescored all nine teams.

| Changed team | Added generation | Team award before → after | Rank before → after | Score before → after |
| --- | ---: | ---: | ---: | ---: |
| 5 × 100 MW grid-only sites | 5 MW total | 454.834 → **499.906 MW** | 8 → **1** | $16.613529B → **$18.249850B** |
| 100 × 5 MW grid-only sites | 100 MW total | 454.832 → **500.000 MW** | 9 → **3** | $16.613450B → **$18.062887B** |

For the five-site team, its own award rose **45.072 MW** while the class award
rose only **5.049 MW**; most of its gain came from a change in *which team*
received scarce grid capacity. The 100-site change is much larger in equipment:
1 MW **per site** means 100 MW of generators and about **$200M** of generator
capital at full allocation. These results make small local generation a
valuable candidate to test in the reconstructed field, but do not establish
that G1 improves allocation or score in every possible opponent field. The
[original per-team awards](../analysis/w1s1_public_reconstruction/results/s1_baseline_allocations.json)
provide the before values; each counterfactual was an independent joint run.

## Imaginary tenth team: duplicate the inferred leader

To isolate one concrete ten-team scenario, we added a tenth 500 MW applicant
that exactly copies the inferred 25 × 20 MW plan, including 1 MW generation at
each of the same 25 buses. The original eight rivals remain; the evaluator
jointly reallocates and rescores all ten teams over all 120 periods. Both
complete evaluations report ten valid, feasible teams.

| Our S1 plan | Our award | Our score | Our rank | Class award |
| --- | ---: | ---: | ---: | ---: |
| Submitted G97/P99 | 500.000 MW | $17.930329B | **4/10** | 4,380.514 MW |
| G1/P0 counterfactual | 499.741 MW | $18.251814B | **1/10** | 4,185.475 MW |

In the submitted-plan run, the original 25-site rival and its copy each get
500 MW and the same $18.213187B score; evaluator ranks them first and second.
The 5 × 100 MW, G20-per-site rival is third at $18.062885B, ahead of us in
fourth. In the G1 run, we remain ahead of both 25-site rivals, which each score
$18.213188B. See the [complete ten-team rankings](../analysis/w1s1_public_reconstruction/results/s1_tenth_team_duplicate_winner.json)
and [runner](../analysis/w1s1_public_reconstruction/audit_tenth_team.py).
This chosen tenth team is one possible plan, not a forecast of the absent
team's submission. The public CSV still does not uniquely identify the
original eight rivals.

## Our grid-only S1 counterfactual

Replacing only our S1 row with **500 MW load, zero generator, zero battery** at
bus `6141`, while retaining the eight reconstructed rivals, gives a valid joint
evaluation but only **418.914 MW allocated** (83.78%), a **$15.301488B** score,
and rank **6 of 9**. Relative to the calibrated submitted plan, that loses
81.086 MW and **$2.629B** of score. The saved
[counterfactual](../analysis/w1s1_public_reconstruction/results/s1_grid_only.json)
reallocates all nine teams rather than freezing rival awards.

## If all nine repeat their S1 method in S2

For this conditional W1S2 run, all 146 reconstructed S1 sites become fixed
hourly **net grid withdrawal** in the S2 base. Every team requests 500 MW of
*new* sites at the same buses with the same equipment ratios as S1; new S2
site IDs avoid reuse. The derived base passes the course network validation,
and all nine S2 submissions are valid and feasible.

The course allocation admits only about **99.000 MW of new class load**. The
mixed 5 × 100 MW team receives 99 MW at its `8126` site, where its new
100 MW connection has 100 MW generation; it scores **$3.417364B** and wins
S2. The S1 first-place 25 × 20 MW team and our repeated G97/P99 plan receive
**0 MW** and score $0 in S2. The mixed team's hypothetical S1+S2 total is
**$20.979839B**, ahead of the S1 winner's **$18.211040B**. See the
[repeat-S2 result](../analysis/w1s1_public_reconstruction/results/s2_repeat.json).

The carried base is already near the grid's constrained-hour limit. A new
site with generation smaller than its load still needs additional grid power;
the mixed team's C100/G100 site can self-supply in those hours. Original S1
sites are not scored again in S2.

## Tested S2 alternatives for our team

All entries below use the reconstructed S1 carryover and eight rivals repeating
their S1 method. They request **500 MW of new load** with new site IDs. Week 1
does not charge grid-energy cost.

| Our new S2 request | New award | S2 score |
| --- | ---: | ---: |
| One site at `6141`, G500, no storage | **500 MW** | **$17.259415B** |
| One site at `6197`, G500, no storage | 500 MW | $17.259415B |
| Two sites: C250/G250 at `6141` and `6197` | 495 MW | $17.086820B |
| One site at `6141`, G450 and P50 / B200 | effectively 0 | effectively $0 |
| One site at `6141`, P500 / B2000 and no generation | 0 | $0 |

At `6141`, the G500 score consists of $30.763287B IT value minus $12.500B
site cost, $1.000B generator capital, and about $3.872M generator operation.
The [single-site run](../analysis/w1s1_public_reconstruction/results/s2_g500_6141.json)
and [split run](../analysis/w1s1_public_reconstruction/results/s2_split_cg_6141_6197.json)
support **one new C500/G500/P0/B0 site at `6141`** as the strongest completed
candidate in this repeat-rival field. Same-bus siting is allowed with a new
site ID. A G499 test near the boundary did not finish promptly and was
interrupted; this menu is not a proof of a global optimum.

## Hourly-LMP sensitivity

Under the released rules, **Weeks 1 and 2 do not bill grid energy**; Week 3
does. The following is a Week 3-style **billing counterfactual** on the same
reconstructed physical field. The evaluator settles hourly grid purchases at
hourly dispatch LMPs. Applying the public map's simple average LMP to all
energy would misstate the charge.

With hourly billing, the S1 25 × 20 MW team remains first at **$17.647550B**,
and we remain third at **$17.368913B**. In the repeated S2 field, the mixed
team still wins, now at **$3.306354B**; our repeated G97/P99 plan and the
S1 winner still have no meaningful S2 award. See the
[priced S1](../analysis/w1s1_public_reconstruction/results/s1_priced.json)
and [priced repeat-S2](../analysis/w1s1_public_reconstruction/results/s2_repeat_priced.json)
results.

For our **C500/G500/P0/B0** S2 candidate, all tested buses receive 500 MW and
score the same $17.259415B before energy billing:

| Bus | Hourly-LMP grid bill | Price-adjusted S2 score |
| --- | ---: | ---: |
| `7150` | $566.592M | **$16.692823B** |
| `6141` | $566.808M | $16.692607B |
| `6197` | $566.827M | $16.692588B |
| `5131` | $567.746M | $16.691670B |

Bus `7150` is best of these **four** priced sites by only **$0.216M** over
`6141`, about 0.0013% of the score. The priced
[7150](../analysis/w1s1_public_reconstruction/results/s2_priced_g500_7150.json)
and [6141](../analysis/w1s1_public_reconstruction/results/s2_priced_g500_6141.json)
runs preserve the full award. The map's W1S1 average at `6141` is
$27.34/MWh. Multiplying that by the modeled present-value grid purchases
estimates an **$840.396M** bill, versus the hourly settlement's **$566.808M**.
The generator covers some high-price hours, so the purchase-weighted price
(about $18.44/MWh) matters more than the simple mean. The Week 1 S2 choice
stays at `6141` because energy is not billed this week and the priced location
differences in this field are small.

## Scope and reproduction

- The eight original rival CSVs are private. The inferred team grouping is one
  exact match to rounded public bus totals and published score precision, not
  proof of the original bids. Another grouping or rival adaptation could
  change S2 outcomes.
- The absent tenth team did not submit W1S1; it may participate later. These
  simulations have nine teams throughout.
- The derived S2 base uses the reconstructed S1 hourly dispatch, not an
  instructor-issued post-S1 base package. All reported score and allocation
  numbers are conditional on that base.
- The Week 3-style LMP test changes billing only. The physical allocation and
  dispatch match the energy-off runs in this model; actual later-week bids and
  congestion may differ.

The [analysis directory](../analysis/w1s1_public_reconstruction/) preserves
the public source files, three local runner scripts, and compact result JSONs.
From the repository root, run in a fresh output directory:

```bash
export PYTHONPATH=analysis/w1s1_public_reconstruction:src:ercot-connection-game/src:ercot-connection-game
.venv/bin/python analysis/w1s1_public_reconstruction/week1_public_reconstruction.py \
  --repo . --public-csv analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv \
  --output runs/w1s1-reconstruction-baseline
.venv/bin/python analysis/w1s1_public_reconstruction/week1_s2_repeat.py \
  --repo . --public-csv analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv \
  --s1-output runs/w1s1-reconstruction-baseline --output runs/w1s1-reconstruction-repeat-s2
.venv/bin/python analysis/w1s1_public_reconstruction/week1_s2_candidate.py \
  --repo . --public-csv analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv \
  --s1-output runs/w1s1-reconstruction-baseline \
  --s2-base runs/w1s1-reconstruction-repeat-s2/s2-base \
  --output runs/w1s1-candidate-g500-6141 --site 6141 500 500 0
```

Add `--energy-price` to a runner for the hourly-LMP counterfactual. These
commands use the unchanged course allocation, dispatch, and score engine over
all 120 represented periods. They do not upload a course submission.
