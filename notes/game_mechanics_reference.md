# ERCOT Connection Game: Mechanics Reference

This is the complete mechanics reference for a new team member. It combines the attached project tutorial, the checked-in course repository, the implementation, and the active scoring rules. It does not assume you have read [main (1).pdf](../../Downloads/main%20(1).pdf).

## 1. Scope and the important version boundary

The repository contains three nearby descriptions of the submission limit:

| Description | Connection limit |
|---|---:|
| Attached `main (1).pdf` tutorial | 500 MW per team per submission |
| `ercot-connection-game/` checked-in release and rules | 1,000 MW per team per submission |
| This team repository's finalized 500 MW team profile | 500 MW per team per submission |

The active numbers for the public course repository are defined by `ercot-connection-game/data/teaching/game_release_representative_v1.json` and `dispatch_scoring_rules_representative_v1.json`:

- 1,000 MW team connection cap
- G <= C
- storage B = 4P
- 120 periods
- 7% discount rate
- 10-year planning horizon

This team repository also has a separate root policy finalized at 500 MW for its team workflow. A team's actual submission must follow the current classroom rules announced for the round. The 500 MW tutorial text and this team's 500 MW configuration do not change the public repository's checked-in 1,000 MW release on their own.

For all examples below, `C`, `G`, `P`, and `B` mean the requested values unless the text explicitly says allocated values under alpha.

## 2. Repository structure and what to use

### Public course implementation

- `ercot-connection-game/README.md`: repository overview and commands.
- `ercot-connection-game/docs/REPOSITORY_GUIDE.md`: file layout and end-to-end workflow.
- `ercot-connection-game/docs/ACTIVSG2000_SCENARIO_PACKAGE.md`: representative-day data and provenance.
- `ercot-connection-game/docs/HYPERPARAMETERS.md`: active parameter values.
- `ercot-connection-game/docs/OFFICIAL_EVALUATION.md`: authoritative batch evaluation workflow.
- `ercot-connection-game/docs/student_tutorial/`: tutorial LaTeX source, PDF, figures, notebooks, and AI walkthrough.
- `ercot-connection-game/data/processed/activsg2000_representative_v1/`: 2,000-bus network, five representative days, and 120 periods.
- `ercot-connection-game/data/teaching/`: official release, rules, layouts, and demo data.
- `ercot-connection-game/src/ercot_game/csv_submission.py`: canonical parser and semantic validation.
- `ercot-connection-game/src/ercot_game/csv_validator.py`: student-facing checker.
- `ercot-connection-game/src/ercot_game/batch_evaluation.py`: batch collection, dispatch scoring, and team scoring.
- `ercot-connection-game/src/ercot_game/base_load.py`: Submission 2 carried base-load construction.
- `ercot-connection-game/tools/activsg2000/dcopf.py`: DCOPF and storage dispatch implementation.
- `ercot-connection-game/tools/activsg2000/allocation.py`: utilitarian site allocation.
- `ercot-connection-game/tools/hosting_capacity.py`: hosting-capacity calculation.
- `ercot-connection-game/examples/eight_team_round/`: complete worked eight-team example.

The public repository's Python evaluator, selected scenario block, and selected rules JSON are authoritative. A README or hand calculation is not a substitute for them.

### Canonical data

The production package has:

- 2,000 buses
- 3,206 branches
- 544 generator catalog records
- 432 active generators in the representative package
- five representative days
- 24 one-hour periods per day
- 120 hourly periods total
- period indices 0--119

The representative days are:

| Day | Date | Weight | Periods |
|---|---|---:|---|
| 0 | 2028-01-03 | 83.77 | 0--23 |
| 1 | 2028-05-10 | 99.73 | 24--47 |
| 2 | 2028-07-12 | 82.77 | 48--71 |
| 3 | 2028-09-10 | 97.73 | 72--95 |
| 4 | 2028-09-15 | 1.00 | 96--119 |

The weights sum to 365. Period 109 is the peak-load hour. The weights stand for one year, and the game evaluates the result over ten discounted years.

The system is a synthetic ACTIVSg2000 planning model, not historical ERCOT telemetry or an official ERCOT operating tariff.

## 3. Submission format

One submission is a UTF-8 CSV with exactly this header:

```text
team_id,site_id,bus_id,connection_capacity_mw,generator_capacity_mw,storage_power_mw,storage_energy_mwh
```

Each data row is one site. The active schema has no period rows, hourly profiles, submission number, public generator ID, or storage ID.

Example:

```text
team_id,site_id,bus_id,connection_capacity_mw,generator_capacity_mw,storage_power_mw,storage_energy_mwh
team-blue,north,1001,40,20,10,40
team-blue,south,1002,15,0,0,0
```

CSV names and uploads normally follow a team/week/submission convention, but the checker validates the file content rather than its filename. The exact filename and submission deadline remain classroom administrative requirements.

## 4. Every decision variable

These are the only team-controlled numerical decisions in the canonical CSV: bus, connection capacity, generator capacity, and storage power/energy. A team may create multiple rows/sites.

### `team_id`

- **Definition:** stable identifier for the submitting team.
- **Units:** text identifier.
- **Format:** letters, digits, `_`, `.`, `:`, or `-`; no whitespace; at most 128 characters.
- **Allowable range:** one nonempty ID, identical on every row in the file.
- **Score impact:** it associates sites, assets, allocations, and results with the team. It does not directly enter the physics or scoring formula.
- **Allocation impact:** it controls team-level accounting and the rule that private generators and storage serve only that team's own load at a bus.
- **Interactions:** every row must use the same team ID. The evaluator assigns internal generator and storage IDs deterministically from team and site identity.
- **Submission 2 interaction:** a team ID used in Submission 2 must correspond to the same team; the batch process also uses the team's reserved Submission 1 site IDs.

### `site_id`

- **Definition:** a team-defined label for one row/site.
- **Units:** text identifier.
- **Format:** letters, digits, `_`, `.`, `:`, or `-`; no whitespace; at most 128 characters.
- **Allowable range:** unique within the file.
- **Score impact:** it is bookkeeping; it does not have a direct economic coefficient. It determines the internal asset IDs and which capital costs belong to which build.
- **Allocation impact:** allocation is calculated at the site level. Therefore, multiple rows at the same bus are not necessarily treated as one invisible site.
- **Interactions:** paired with `team_id` to form the persistent site identity. It must not repeat an existing Submission 1 site ID in that team's Submission 2 file.
- **Submission 2 interaction:** an S1 row remains a base-load asset. The S2 CSV may contain only new site IDs.

### `bus_id`

- **Definition:** the source-network bus at which the site's connection, generation, and storage reside.
- **Units:** bus catalog identifier.
- **Allowable range:** it must exist in the selected scenario block's `bus.csv`; for the production package it is a source bus between the valid catalog values. The checker does not infer a bus from a name or region.
- **Score impact:** location changes served load, network price, and congestion. It does not itself change the IT-value or capital coefficients.
- **Allocation impact:** location is central. The allocation rule values sites that use less of scarce network capacity and sites whose private resources reduce grid withdrawal.
- **Interactions:**
  - multiple teams at the same bus compete for that location
  - generator and battery effects are attached to the site's bus
  - a bus is affected by PTDF/shift factors on bottleneck branches
  - LMP settlement is bus-specific in Week 3
  - distinct sites at the same bus may receive potentially different allocations only under the general site algorithm
- **No direct team choice:** the grid operator, not the team, selects dispatch at the bus.

### `connection_capacity_mw`, C

- **Definition:** the IT-load capacity requested at a site. The evaluator expands it as a constant load over all 120 periods, subject to allocation.
- **Units:** MW.
- **Allowable range:** finite and nonnegative. C must be greater than zero for a row to be a valid site. If C = 0, the row is rejected unless every other capacity is also zero; a row with G or P while C = 0 is also rejected.
- **Team limit:** all site C values in one submission sum to at most 1,000 MW in the checked-in public release. This can be 500 MW under an announced classroom override.
- **Score impact:**
  - requested C determines the scale of potential IT value
  - full service is worth $1,000/MWh times the weighted served MWh
  - site cost is $25M/MW of allocated connection capacity
  - in Week 3, grid withdrawal tied to C can create energy cost
- **Allocation impact:** C is scaled by the site's alpha. Stage 1 maximizes sum(alpha_s C_s), while stage 2 minimizes sum(C_s (1-alpha_s)^2).
- **Interactions:**
  - G <= C
  - larger C increases grid need only insofar as G/P/B do not cover it
  - C determines requested load and thus allocation/capital
  - at G = C, on-site generator capacity can eliminate grid withdrawal

### `generator_capacity_mw`, G

- **Definition:** maximum private-generator capacity colocated with the site.
- **Units:** MW.
- **Allowable range:** finite and nonnegative, and G <= C using the release ratio 1.0. A rules override could change the G/C ratio, but the active release uses G <= C.
- **No run-hour limit:** the team generator may run in every period. There is no restriction to a number of hours per day.
- **No generator asset registry:** the generator is attached to the submitted site. Students do not choose public generator IDs.
- **Dispatch:** the grid operator chooses generator output from 0 through G. It serves the team's own load only and cannot export to the grid or another team.
- **Score impact:**
  - generator operating cost is piecewise: 25% of G at $80/MWh, next 50% at $150/MWh, last 25% at $250/MWh
  - generator capital is $2.0M/MW of allocated G
  - replacing grid purchase can reduce Week-3 LMP energy cost
  - private generation does not create IT value beyond the IT value earned for served load
- **Allocation impact:** G reduces network withdrawal and is rewarded by the allocation objective. G = C can make the site independent of grid delivery and is never cut by the allocation rule.
- **Interactions:**
  - G is scaled by alpha with C
  - G cannot exceed C
  - if G is too small to cover C, the remaining load is grid or storage supplied
  - G and P/B can be combined on one site
  - grid LMP is not itself controlled; the centralized dispatch uses it to decide whether it is cheaper to generate or buy
- **G/C behavior:** G = C is the reference off-grid construction, but the official joint dispatch is still an optimizer. The absolute-points reference analytically assumes the 1,000 MW site runs at full private output.

### `storage_power_mw`, P

- **Definition:** maximum signed battery power. Positive means discharge; negative means charge.
- **Units:** MW.
- **Allowable range:** finite and nonnegative. P must be zero with B = 0, or positive with B = 4P.
- **Active relation:** B = 4P. P itself has no explicit published maximum separate from the team C cap. It is possible to submit P without a P <= C rule in the current validator.
- **Dispatch:** -P <= p[t] <= P.
- **Score impact:**
  - no storage operating cost
  - storage capital = $400k/MW for P plus $250k/MWh for B
  - equivalent 4-hour cost = $1.4M/MW
  - storage can reduce peak grid withdrawal or relieve a tight dispatch period
- **Allocation impact:** P and B scale with alpha. Storage can reduce the network need of a site and shift withdrawal toward slack periods.
- **Interactions:**
  - exact four-hour relation: B = 4P
  - SOC and power are coupled over 24 hours
  - battery discharge cannot exceed the owning team's load at the bus
  - storage cannot export to the grid or another team
  - storage and generation can be combined
- **Preview caveat:** the student preview reports storage capital but leaves storage idle. It therefore does not show the official storage benefit.

### `storage_energy_mwh`, B

- **Definition:** battery energy capacity.
- **Units:** MWh.
- **Allowable range:** finite and nonnegative. Active rule: B = 4P; P = 0 requires B = 0.
- **Dispatch relation:**
  - state of charge at start/end of every representative day = B/2
  - 0 <= SOC[t] <= B
  - SOC[t] = SOC[t-1] - 1h * p[t]
  - no state of charge carries between days
- **Score impact:** capital cost is $250k/MWh of allocated B.
- **Allocation impact:** B scales with P and C under alpha. It permits the grid operator to couple 24 hours while seeking a feasible dispatch.
- **Interactions:** P controls power but B controls usable energy. Together they define a four-hour battery.

### Other user choices

The team can choose:

- the number of site rows
- the team/week/submission timing
- bus choices
- C, G, P, and B per site
- whether and how to diversify locations
- whether to react to Week 1 feedback in Week 2 or later

The team does not choose:

- generator operating schedule
- battery operating schedule
- storage state of charge
- hourly load profile
- public LMP
- alpha
- private generator split across teams
- dispatch-period schedules
- existing public-generator dispatch

## 5. Exact scoring process

For each submission, the evaluator computes:

```text
score =
  IT value
  - Week-3 grid energy cost
  - team-generator operating cost
  - generator capital cost
  - storage capital cost
  - connection-site cost
```

Invalid submissions use score zero. The score is for one submission, not the whole campaign.

### 5.1 Present-value weights

The rules give:

- 10-year discount rate: 7%
- annuity factor:

```text
A = sum(y=1..10) 1/1.07^y = 7.023581540933
```

- period weight:

```text
w_t = 1 hour x representative-day weight x A
```

The 120 weights sum to 61,526.57 equivalent hours. This weighting is applied to IT value, Week-3 energy purchases, and team-generator operating cost.

The active period weights are 588.3645 hours for each winter day hour, 700.4339 for spring, 581.3601 for summer, 686.4252 for late summer, and 7.0236 for each peak-day hour.

### 5.2 IT value

IT value is:

```text
IT value = $1,000/MWh
           x sum over period t and site s of
             w_t x served_load_t,s_MW
```

For a fully served site, C MW earns:

```text
C x 61,526.57 x $1,000/MWh
```

One fully served MW therefore earns about $61.526 million present value.

If a site is allocated as alpha C, the dispatch uses alpha C (and alpha G/P/B), and IT value is calculated from the dispatched allocated load. The output reports represented-year served MWh separately from present-value IT dollars.

### 5.3 Generator operating cost

The team-generator curve is convex:

| Portion of G | Cost |
|---|---:|
| first 25% | $80/MWh |
| next 50% | $150/MWh |
| last 25% | $250/MWh |

For dispatch amount g in a period:

```text
cost = sum(segment_amount x segment_marginal_cost)
```

where segment amounts are limited to 25%, 50%, and 25% of G. The cost is weighted by `w_t`.

Example for G = 100 MW:

- first 25 MW is charged at $80/MWh
- next 50 MW at $150/MWh
- final 25 MW at $250/MWh

If G runs at 100 MW every weighted hour, average variable cost on that full-output point is:

```text
25% x $80 + 50% x $150 + 25% x $250 = $157.50/MWh
```

### 5.4 Week-3 energy cost

In Weeks 1 and 2, energy cost is zero.

In Week 3, energy cost is:

```text
energy cost =
  sum over period t and bus n
    w_t x grid_purchase_t,n_MW x lambda_t,n
```

where `lambda_t,n` is the bus LMP in that period, clipped at zero.

The LMP is a dual of the joint-dispatch bus balance. It is not a student-selected electricity price.

Before the teams add congestion, LMPs are approximately $18/MWh in the tutorial's baseline discussion. Grid congestion can raise or lower bus prices. Grid withdrawal is:

```text
grid purchase = allocated connection load
                - private generation
                - battery net discharge
```

At a site, positive battery discharge reduces withdrawal; battery charging can increase grid purchase.

### 5.5 Capital charges

Capital is one-time and undiscounted:

| Asset | Rate | Allocated basis |
|---|---:|---|
| connection site | $25M/MW | alpha C |
| team generator | $2M/MW | alpha G |
| storage power | $400k/MW | alpha P |
| storage energy | $250k/MWh | alpha B |

For a 4-hour battery:

```text
storage capital = $400k x P + $250k x (4P)
                = $1.4M x P
```

No storage operating cost is charged.

Under normal full allocation alpha = 1:

- 1 MW of C costs $25M
- 1 MW of G costs $2M
- 1 MW of P plus 4 MWh costs $1.4M

### 5.6 Allocation factor alpha

If the combined valid request is infeasible, the evaluator assigns a separate:

```text
alpha_s in [0, 1]
```

for every site.

The site is treated as if it submitted:

```text
C' = alpha_s C
G' = alpha_s G
P' = alpha_s P
B' = alpha_s B
```

Stage 1:

```text
maximize sum_s(alpha_s C_s)
subject to the joint DCOPF in all 120 periods
```

Stage 2:

```text
among allocations reaching that maximum,
minimize sum_s C_s (1-alpha_s)^2
```

The tie-break is strictly convex, so the allocation is unique. It does not depend on the submission-file order or solver.

The rule rewards:

- more served MW per MW of network use
- private generation that reduces grid withdrawal
- storage that shifts withdrawal away from bottleneck periods
- locations with favorable shift factors on congested branches
- identical treatment of identical sites

A site with G = C needs no network withdrawal and is never cut. There is no minimum allocation: a small but positive alpha can be served.

Capital is charged on alpha-scaled values, and IT value is earned on the resulting served load.

### 5.7 Storage treatment

The official storage model is exact and dispatches P/B jointly with the network:

- one signed power variable per battery and hour
- positive discharge, negative charge
- 100% efficiency
- dt = 1 hour
- start/end of each day at B/2
- SOC between zero and B
- power between -P and P
- no discharge above prior-hour stored energy
- no discharge greater than the owning team's load at the bus
- no SOC carryover between representative days

The grid operator chooses storage dispatch to make the DCOPF feasible and cost-efficient. Storage has no operating cost.

### 5.8 Reference and grading values

The attached tutorial defines B = $24.84B as the final score of a team that runs 1,000 MW off-grid:

- W2S1: about $24.836B
- W2S2: $0
- W3S1: about $24.836B
- W3S2: $0
- total B: about $49.672B

The absolute grading point is:

```text
5 x min(1, max(0, S/(2B)))
```

where S is the sum of the four graded submissions.

At a 500 MW finalized team profile, only the team-specific scenario differs; the grade and relative formulas still depend on the announced classroom configuration.

## 6. Exact evaluation workflow

### 6.1 Submission collection

The batch evaluator:

1. reads every CSV in the submission directory
2. rejects malformed or invalid files independently
3. records the team ID and SHA-256 input hash
4. validates the canonical header and exactly seven fields
5. validates each row and team total
6. continues with valid teams if a malformed team is rejected
7. optionally checks Submission 2 reserved site IDs

Rejected files do not participate in the joint dispatch and score zero.

### 6.2 CSV and catalog validation

Validation checks:

- file decodes as UTF-8
- exact header
- exactly seven fields per row
- at least one site row
- nonempty well-formed team and site IDs
- no duplicate site ID
- one team ID in the file
- bus ID exists in the selected artifact
- C finite and nonnegative
- G finite and nonnegative
- P finite and nonnegative
- B finite and nonnegative
- C > 0 unless every row capacity is zero
- G <= C
- sum(C) <= team limit
- P and B are both zero or both positive
- B = 4P
- no row with C = 0 and G or P > 0
- Submission 2 no reuse of a team's old S1 site ID

IDs allow only letters, digits, `_`, `.`, `:`, and `-`, with no spaces and at most 128 characters.

Exit behavior:

- checker 0: valid
- checker 1: invalid
- checker 2: command/configuration problem

The checker is convenience validation. The batch evaluator is authoritative.

### 6.3 Submission 1

For a Week or submission one:

1. the representative base load is loaded
2. all teams' submitted site plans are represented
3. each team's private assets are attached to their sites
4. all 120 periods are checked through joint dispatch
5. if full dispatch is feasible, alpha = 1 for every site
6. if infeasible, site allocation is run
7. exact dispatch is computed
8. team scores are calculated
9. the Submission 1 site hourly net withdrawals are recorded

For each site, the net grid withdrawal is the site's allocated load minus private generation and battery discharge.

### 6.4 Dispatch

The evaluator solves the DCOPF for all 120 periods and all teams together.

For each period:

- existing public generator output respects p_min/p_max and marginal cost
- team-generator output respects 0 <= g <= alpha G
- team generators serve only the submitting team's load
- battery signed power respects P and SOC
- battery discharge serves only its team
- bus net injections satisfy network balance
- branch flows satisfy thermal limits
- DC line injections are included
- storage boundaries couple 24 periods inside a day

The objective is generation and dispatch cost. Grid purchases are not a separate objective term within the DCOPF; Week-3 energy cost is later computed from actual joint-dispatch LMPs.

The production storage dispatch uses exact daily-cycle methods. When plans fit, storage-aware Benders decomposition couples each 24-hour day and is exact to the configured tolerance. An allocation-backed dispatch is solved with exact monolithic daily LPs.

### 6.5 Allocation

If the full request is infeasible:

1. allocation maximizes total feasible served connection capacity
2. every site receives alpha in [0,1]
3. every site, generator, and battery is scaled together
4. fractions are coupled across all periods
5. stage 2 resolves ties by closeness to full service
6. the allocation is dispatched exactly
7. marginal safety backoffs may be applied to keep the final dispatch strictly inside limits

Identical sites at the same bus receive the same fraction. The result does not use first-come-first-served priority.

### 6.6 Scoring

For every team:

1. served load is taken from the joint dispatch
2. IT value is calculated using weighted served MWh
3. Week-3 energy cost is calculated from each bus LMP and net grid purchase
4. private-generator segment cost is summed over all periods
5. allocated generator, storage, and site capital is added
6. invalid/evaluation-failed teams receive the configured fallback score

One valid team but infeasible/unavailable final dispatch is handled with the evaluator's deterministic fallback policy; it must not silently become a real scored result.

### 6.7 Submission 2

Within a week:

1. add every team's S1 hourly net grid withdrawal to the representative base load
2. validate the resulting 120-period scenario
3. fix S1 sites as base load
4. do not re-evaluate, re-score, re-project, or re-dispatch S1 sites
5. require only new sites in the S2 CSV
6. reject reuse of a team's prior S1 site IDs
7. dispatch S2 with that base load

The S2 base load is instructor-derived. Teams receive per-bus totals, not another team's plan.

S1 value is kept. Each S1 site earns its ten-year value once, in S1; S2 adds the value of the new S2 sites. S2 capital is charged only for new S2 assets.

### 6.8 Week reset and final score

Each week resets to the representative base load. No S1/S2 asset carries to a later week.

The final team score is:

```text
W2S1 + W2S2 + W3S1 + W3S2
```

W1 is practice and does not count.

### 6.9 Results and privacy

The instructor releases:

- private score breakdown
- team service/allocation fraction
- whether allocation was triggered
- privacy-safe aggregate grid map

The public grid map shows total served connection capacity at buses and branch loading; it does not reveal team identity or exact plans.

## 7. Limits and configuration

### Sites

No explicit maximum number of sites is enforced by the validator. The only structural limits are:

- one team ID per file
- unique site IDs
- C > 0 for submitted sites
- team C <= the released team cap
- valid bus IDs

Therefore, a team can split capacity across many rows, subject to readability and the team cap.

### Generator

- G finite and nonnegative
- G <= C
- no run-hour limit
- no explicit G daily-energy limit
- private generation cannot export
- private generation serves only the owning team
- operating cost uses a 25/50/25% segment curve
- $2M/MW allocated capital

The public repository implementation also proportionally splits each bus's solved private-generation total across colocated team generators after the network solve, with deterministic fallback handling. The bus-level total, flows, LMPs, and objective remain unchanged.

### Storage

- P finite and nonnegative
- B finite and nonnegative
- P = 0 and B = 0, or P > 0 and B = 4P
- no explicit P/B maximum other than rules, team capacity, and feasibility
- 100% efficiency
- exact daily cycle
- no operating cost
- no cross-team discharge
- no grid export
- $400k/MW P plus $250k/MWh B capital

### Team and submission

- one team per CSV
- all C in the file <= 1,000 MW in the public release
- 500 MW if a classroom override is announced and enforced
- no more than one canonical row schema
- no duplicated site ID
- S2 only new sites
- no S1 site ID reuse
- invalid or late submission scores zero

### Horizon and scoring

- 120 periods
- five 24-hour representative days
- 1-hour periods
- 10-year present-value horizon
- 7% discount rate
- no energy charge in Weeks 1/2
- dispatch LMP energy charge in Week 3

## 8. Section 7 of the tutorial in detail

Section 7 is the “Explore the Data / Hosting Capacity” strategy foundation.

### 8.1 Data to inspect

The tutorial points to:

- `bus.csv`: valid bus IDs
- `demand_bus.csv`: base load by bus and period
- `representative_days.csv`: day weights and period ranges
- `generator_catalog.csv`: existing generator records
- `generator_limits.csv`: active status and p-min/p-max
- `branch_limits.csv`: branches and thermal limits
- `manifest.json`: horizon and validation status

Start with system summary values:

- 2,000 buses
- 3,206 branches
- 544 generator records
- 432 active generators
- 120 periods
- peak system load in period 109

Good initial bus screening attributes are:

- direct and nearby generator headroom
- local and neighboring base load
- connected branch thermal capacity
- binding period
- electrical distance and bottleneck corridors
- whether top buses share the same limiting generation or transmission resource

The public tutorial warns that baseline LMPs are nearly flat at about $18/MWh without teams' plans. LMP should not be used alone to select location; network headroom and congestion matter more.

### 8.2 What hosting capacity means

At bus k and period t, hosting capacity is the maximum additional constant load L that can be served by the DCOPF:

```text
maximize L
subject to:
  extra load L at bus k
  generator limits
  system balance
  DC branch flows
  branch thermal limits
```

The single-bus number for the whole horizon is:

```text
HC_k = min over t of HC_k,t
```

It represents the most load one can add at that bus alone while all 120-period or sampled-period network constraints remain feasible.

The tutorial gives examples:

- bus 1001: 391 MW in period 0 and 332 MW at peak period 109
- bus 1002: 129 MW and 123 MW
- bus 7419: 687 MW and 248 MW

These are illustrative numbers for the older/base dataset in the tutorial and are not a substitute for recomputing against the released and possibly carried-base package.

### 8.3 How to compute it

The safest general method is binary search:

1. call the prepared DCOPF at L = upper bound
2. if feasible, hosting capacity is at least that bound
3. otherwise, bisect the [0, upper bound] interval
4. keep bisection until the MW tolerance is reached
5. repeat for all 120 periods or an efficient peak-period shortlist

For many buses, use `ercot-game-hosting-capacity` rather than writing repeated LP checks.

Screening sequence:

1. rank buses using simple connected-load and generator/line attributes
2. calculate peak-period hosting capacity for a shortlist
3. calculate all 120 periods for the final bus list
4. recompute against Submission 2's released carried base

In the tutorial, screening 2,000 x 120 cases is computationally expensive, so it suggests peak-period filtering followed by a final all-period pass.

### 8.4 Why the number is incomplete

A one-bus number is a single axis of a feasible hosting-region polytope. It assumes no team is adding a competing load.

Consequences:

- two individual hosting capacities cannot be added
- a bus with 123 MW alone can have much less room when a neighboring 60 MW load is added
- multiple buses that share the same branch compete for that branch's capacity
- separate generation-limited buses can share a system generation ceiling
- a bus's one-bus bottleneck can change when another bus is loaded

Therefore, hosting capacity is a screening metric, not an official joint-allocation forecast.

### 8.5 Private generator hosting formula

For a site with connection load L and private generation G:

```text
grid withdrawal = L - g
0 <= g <= G
```

The tutorial gives the approximate exact relation:

```text
HC_G(k) = min_t HC_k,t + G
```

It is exact only when the generator is always available and the dispatch is ideal. This game is more complex because:

- generator cost is piecewise
- output is optimized against grid LMP and network feasibility
- G is scaled under allocation
- outages/ramp limits are not present in the same idealized model

Nevertheless, the formula shows why G expands useful load capacity at a constrained bus.

### 8.6 Storage hosting formula

For battery P and energy B over a day:

```text
grid withdrawal per period = L - u_t
```

The battery:

- discharges in tight periods
- charges in slack periods
- stays within P and B
- starts and ends the day at B/2

Because energy across a cycle balances:

```text
sum(u_t) = 0
```

The tutorial derives the upper bound:

```text
HCS_k <= average_t(HC_k,t)
```

Storage cannot make a system feasible above the average bus headroom by using a single daily cycle. It can raise a bus above its minimum headroom if slack periods provide enough charging.

In the real game, storage may allow it to serve a load in multiple tight periods that would otherwise limit the site. The preview does not dispatch storage, so the preview cannot validate this benefit.

### 8.7 Flexible-connection comparison

The appendix considers an extended case where load may be curtailed in K periods. Its mathematical order statistic is:

```text
flexible hosting capacity = K+1-th smallest period hosting capacity
```

This game does not implement flexible curtailment by the student. Curtailment happens through evaluator-wide site allocation only, not a student-chosen demand curve.

The generator/battery extension is a useful way to test how much capacity is needed during the K tightest periods.

### 8.8 Caveats

Hosting capacity should be interpreted with these limitations:

- plain DCOPF, not AC optimal power flow
- no N-1 contingency or reserve requirement
- no voltage or reactive-power limits
- no network losses
- no physical data-center ride-through dynamics
- no outages or ramp limits
- no competing-team loads
- no knowledge of hidden opponent plans

Single-bus, base-network numbers remain useful for:

- finding bottleneck corridors
- identifying generator-limited buses
- screening C and G choices
- choosing controlled experiments

They must not be used to claim an official joint allocation or final score.

## 9. Strategy design space

The central strategy tradeoffs are:

### Location

- low crowding
- high hosting headroom
- unique bottleneck
- shared corridor
- nearby generation
- remote/weak bus
- effect on other teams' allocation

### Size

- larger C produces more IT value if served
- larger C costs more site capital
- larger C consumes more network and allocation room
- 500/1,000 MW team caps reduce the number of alternatives
- allocation may scale C down if the joint plan is infeasible

### Generator

- G reduces grid withdrawal
- G improves allocation value
- G costs capital and fuel
- G = C is the reference off-grid case
- G may run every hour
- grid power can be cheaper in uncongested periods
- G should be evaluated against actual binding periods

### Storage

- P/B is useful mainly in network/generation-tight periods
- B shifts withdrawal across a day
- no storage operating cost
- capital is $1.4M/MW for a four-hour battery
- the preview idle-storage model understates official storage behavior
- the correct scale is determined by binding-period duration, headroom, and LMP

### Timing

- Week 1: practice and feedback
- Week 2: no energy charge, first four graded submissions begin
- Week 3: energy charge
- Submission 1: first access to room
- Submission 2: reaction to observed crowding but only residual room
- weekly reset: means no learning carries physically across weeks

### Controlled experiment method

For each candidate, change one variable at a time:

- base case
- larger C
- alternate bus
- add G
- add P/B
- diversify sites
- change one bus from grid-only to G=C

Keep one candidate per preview folder because the preview dispatches every CSV in a folder jointly. Preserve:

- CSV
- command
- bus shortlist
- served load
- score
- binding periods/branches
- assumptions about rivals

## 10. Common planning formulas

### Full-service per-MW Week 1/2 value

Before energy and assets:

```text
IT value per MW  = $61.526M
site cost         = $25.0M
net grid value    = about $36.526M
```

### Full off-grid C = G = 1 MW

```text
IT value                         $61.526M
generator operating cost         -$9.690M
site capital                     -$25.000M
generator capital                -$2.000M
net value                        about $24.836M
```

The exact generator operating cost uses every weighted hour and the 25/50/25% segment curve.

### Storage 1 MW / 4 MWh

```text
power capital: 1 MW x $400k = $400k
energy capital: 4 MWh x $250k = $1M
total: $1.4M
```

### Break-even site service

Ignoring Week-3 energy and resource costs, full IT value less site cost yields a simple break-even service fraction:

```text
$25M / $61.526M = about 40.6%
```

This is not a final profit guarantee; it excludes generator/storage cost and Week-3 energy purchases.

## 11. The student preview

The preview command:

```bash
ercot-game-preview \
  --submissions-dir runs/candidate-a \
  --week 3 \
  --output runs/candidate-a.json
```

It:

- solves all 120 periods
- uses one team's or supplied teams' plans
- validates storage
- charges storage capital
- leaves storage idle
- can apply the same site-allocation fallback
- ignores unrepresented opponents
- is approximate and non-authoritative

The preview is useful for screening a bus, size, or generator. It is not an official forecast.

For Submission 2, use the instructor-released base-load artifact or `--base-load-from`.

Keep exactly one candidate CSV in each preview folder.

## 12. Important interpretation rules

- A low alpha means the joint plan needed allocation.
- Alpha is not a student-set fraction.
- A full standalone hosting capacity is not an expected score or a guaranteed allocation.
- Baseline LMP is not enough to select a location.
- A bus that is strong alone can be poor if many teams choose it.
- A generator reduces the grid resource a site needs.
- Storage does not get free operating revenue in this model.
- A battery's exact benefit depends on operating all 120 periods.
- Invalid files score zero and are omitted from the joint plan.
- Week-1 feedback is powerful but practice-only.
- Week-2 and Week-3 outcomes are not repeatable or added across weekly resets.

## 13. Quick checklist before submission

- [ ] Header is exactly the seven canonical columns
- [ ] UTF-8 CSV
- [ ] exactly one team_id
- [ ] all site_id values are unique
- [ ] bus_id values exist in the active artifact
- [ ] C > 0 for every site row
- [ ] G <= C
- [ ] sum(C) <= active team cap
- [ ] P and B are either both zero or satisfy B = 4P
- [ ] Submission 2 contains only new sites
- [ ] Submission 2 does not reuse a Submission 1 site_id
- [ ] the exact file is checked with `ercot-game-check-csv`
- [ ] each candidate is previewed in its own folder
- [ ] the team can explain each bus, C, G, and P/B choice
- [ ] the team has logged the command and assumptions
