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