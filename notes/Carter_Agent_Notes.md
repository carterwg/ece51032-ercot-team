Prompt:
Using the ACTIVSg2000 dataset and the hosting-capacity results:

1. Identify the top 100 buses by minimum hosting capacity.
2. Group them into electrically connected regions.
3. Determine whether these buses share common transmission bottlenecks.
4. Produce a shortlist of 20 buses that are both:
   - high hosting capacity
   - geographically/electrically diverse

Save results to:
analysis/bus_rankings/diversified_top20.csv


Output:
Saved and validated the 20-bus shortlist in diversified_top20.csv. It includes each bus’s minimum hosting capacity, binding period, electrical-neighborhood ID and members, and binding branch IDs.

I grouped the top 100 into 22 local electrical neighborhoods, defined as candidate buses within two active-branch hops of each neighborhood’s highest-ranked center. The shortlist takes one center from each of the 20 strongest neighborhoods, avoiding multiple picks from the same local area. The two remaining top-100 neighborhoods are singletons: buses 6004 and 6342. The dataset has no geographic coordinates, so this is topology-based rather than geographic diversity.

The selected buses are 1079, 2054, 3088, 5131, 6021, 6038, 6197, 8155, 5413, 5317, 6062, 5015, 8043, 5384, 5295, 2002, 7095, 7414, 8126, and 6298. Their minimum hosting capacities range from 2,513.833 to 3,024.604 MW, and all bind at period 109.

Shared transmission constraints: At each candidate’s individual hosting limit, LP duals show binding branch constraints for 71 of the top 100. Branch b02579 (8004–7150, 647 MVA) was binding for 37 candidates; b02136 (6294–6293, 217.8 MVA) for 16. This identifies recurring constraints in individual-bus tests—not a joint evaluation of all 100 loads. No source files were changed.







Prompt:
Using diversified_top20.csv and the ACTIVSg2000 dataset:

1. For each shortlisted bus, identify the full set of binding constraints at minimum hosting capacity.

2. Group buses by shared bottlenecks.

3. Produce a table showing:
   - bus_id
   - minimum_hosting_capacity
   - binding branch
   - number of shortlisted buses sharing that branch

4. Rank buses according to uniqueness of their bottlenecks.

5. Highlight buses that appear to rely on transmission corridors not shared by other shortlisted buses.

Save as:
analysis/bus_rankings/bottleneck_diversity_analysis.csv


Output:
Saved the report to bottleneck_diversity_analysis.csv and validated its 20 unique bus rows.

At their individual hosting limits, 12 buses are transmission-limited across four binding branches: b02579 is shared by 8 shortlisted buses, b02136 by 2, while b01773 and b01758 are unique corridors for buses 6062 and 6298. Those two rank highest for corridor uniqueness. The other 8 buses have no binding branch in their hosting-limit solution; their limit is system generation capacity.

The CSV includes binding branch details and sharing counts, uniqueness ranks, and the full lists of generator Pmin/Pmax bounds active at each solution. No source files were changed; the existing untracked test.py was left untouched.