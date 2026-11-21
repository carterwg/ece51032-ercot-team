# Ten-team comparison at 500 MW per submission

| Our layout and policy | Sites | S1 / S2 G MW | Fields complete | Mean score $B | Worst score $B | Minimum S1 admitted MW | Minimum S2 admitted MW | Max S1 required h/year | Max S2 required h/year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bottleneck_ptdf_1_s1_125_s2_cg | 1 | 125 / 500 | 4/4 | 69.026138 | 68.273092 | 500.000 | 500.000 | 3.000 | 302.195 |
| bottleneck_ptdf_5_s1_125_s2_cg | 5 | 125 / 500 | 4/4 | 68.871609 | 67.857092 | 500.000 | 500.000 | 1.000 | 302.195 |
| bottleneck_ptdf_1_s1_250_s2_cg | 1 | 250 / 500 | 4/4 | 68.521914 | 67.772941 | 500.000 | 500.000 | 3.000 | 302.195 |
| bottleneck_ptdf_5_s1_250_s2_cg | 5 | 250 / 500 | 4/4 | 68.364165 | 67.356993 | 500.000 | 500.000 | 3.000 | 302.195 |
| bottleneck_ptdf_1_s1_375_s2_cg | 1 | 375 / 500 | 4/4 | 68.012663 | 67.272844 | 500.000 | 500.000 | 3.000 | 302.195 |
| bottleneck_ptdf_5_s1_375_s2_cg | 5 | 375 / 500 | 4/4 | 67.842993 | 66.856907 | 500.000 | 500.000 | 3.000 | 302.195 |
| bottleneck_ptdf_1_both_cg | 1 | 500 / 500 | 4/4 | 67.501032 | 66.772785 | 500.000 | 500.000 | 5.000 | 302.195 |
| bottleneck_ptdf_2_both_cg | 2 | 500 / 500 | 4/4 | 67.403892 | 66.714537 | 500.000 | 500.000 | 3.000 | 302.195 |
| bottleneck_ptdf_5_both_cg | 5 | 500 / 500 | 4/4 | 67.332209 | 66.356833 | 500.000 | 500.000 | 3.000 | 302.195 |
| hosting_1_both_cg | 1 | 500 / 500 | 4/4 | 67.102372 | 66.015041 | 500.000 | 500.000 | 5.000 | 302.195 |
| hosting_5_both_cg | 5 | 500 / 500 | 4/4 | 67.022151 | 65.624985 | 500.000 | 500.000 | 5.000 | 302.195 |
| hosting_2_both_cg | 2 | 500 / 500 | 4/4 | 66.817041 | 64.841068 | 500.000 | 500.000 | 5.000 | 302.195 |
| bottleneck_ptdf_1_s2_cg | 1 | 0 / 500 | 4/4 | 58.840883 | 55.286670 | 300.419 | 500.000 | 0.000 | 302.195 |
| bottleneck_ptdf_5_s2_cg | 5 | 0 / 500 | 4/4 | 58.720722 | 55.078367 | 302.430 | 500.000 | 0.000 | 302.195 |
| bottleneck_ptdf_2_s2_cg | 2 | 0 / 500 | 4/4 | 58.790531 | 55.000269 | 302.430 | 500.000 | 0.000 | 302.195 |
| hosting_1_s2_cg | 1 | 0 / 500 | 4/4 | 58.573209 | 54.302629 | 302.430 | 500.000 | 0.000 | 302.195 |
| hosting_5_s2_cg | 5 | 0 / 500 | 4/4 | 58.500093 | 53.940626 | 302.430 | 500.000 | 0.000 | 302.195 |
| hosting_2_s2_cg | 2 | 0 / 500 | 4/4 | 58.406409 | 53.602205 | 302.430 | 500.000 | 0.000 | 302.195 |
| bottleneck_ptdf_5_grid | 5 | 0 / 0 | 4/4 | 25.311305 | 21.759196 | 302.430 | 0.000 | 0.000 | 0.000 |
| bottleneck_ptdf_2_grid | 2 | 0 / 0 | 4/4 | 25.311789 | 21.758985 | 302.430 | 0.000 | 0.000 | 0.000 |
| hosting_1_grid | 1 | 0 / 0 | 4/4 | 25.310837 | 21.757672 | 302.430 | 0.000 | 0.000 | 0.000 |
| hosting_5_grid | 5 | 0 / 0 | 4/4 | 25.310693 | 21.757567 | 302.430 | 0.000 | 0.000 | 0.000 |
| hosting_2_grid | 2 | 0 / 0 | 4/4 | 25.310642 | 21.757553 | 302.430 | 0.000 | 0.000 | 0.000 |
| bottleneck_ptdf_1_grid | 1 | 0 / 0 | 4/4 | 25.276302 | 21.615073 | 300.419 | 0.000 | 0.000 | 0.000 |

Accepted 96 of 96 campaigns (384 scored rounds). Mean scores weight the tested fields equally. Each campaign evaluates four 120-period graded submissions. W2 and W3 start from the same base. Actual S1 grid withdrawals from all ten teams carry into S2.

## Evaluation checks

Every accepted result uses the instructor allocation, joint dispatch, and scoring rules. Fixed plans with identical physical inputs can reuse the physical solve between weeks while the evaluator recomputes the score for each week. Later runs solve no-storage feasibility one hour at a time, with the same allocation objectives and checks across all 120 periods. Each case links any numerical retry and its audit.

`bottleneck_ptdf_1_s1_125_s2_cg` leads on worst-case score at **$68.273092B**. `bottleneck_ptdf_1_s1_125_s2_cg` leads on equal-weight mean at **$69.026138B**.

| Generation policy | Best mean layout | Mean $B | Worst $B for that layout | Lowest S1 MW across complete layouts | Lowest S2 MW across complete layouts |
| --- | --- | --- | --- | --- | --- |
| both_cg | bottleneck_ptdf_1_both_cg | 67.501032 | 66.772785 | 500.000 | 500.000 |
| grid | bottleneck_ptdf_2_grid | 25.311789 | 21.758985 | 300.419 | 0.000 |
| s1_125_s2_cg | bottleneck_ptdf_1_s1_125_s2_cg | 69.026138 | 68.273092 | 500.000 | 500.000 |
| s1_250_s2_cg | bottleneck_ptdf_1_s1_250_s2_cg | 68.521914 | 67.772941 | 500.000 | 500.000 |
| s1_375_s2_cg | bottleneck_ptdf_1_s1_375_s2_cg | 68.012663 | 67.272844 | 500.000 | 500.000 |
| s2_cg | bottleneck_ptdf_1_s2_cg | 58.840883 | 55.286670 | 300.419 | 500.000 |

## Opponent plans and site selection

| Field | Identical layout for each of nine rivals | S1 / S2 G MW per rival |
| --- | --- | --- |
| nine_grid_at_6141 | 6141 | 0 / 0 |
| nine_grid_at_hosting_1 | 1079 | 0 / 0 |
| nine_s2_cg_hosting_2 | 1079, 2054 | 0 / 500 |
| nine_both_cg_ptdf_5 | 6141, 5395, 6342, 5451, 6004 | 500 / 500 |

The hosting-capacity layouts take the first 1, 2, or 5 buses in standalone hosting rank. The electrical layouts start with the best composite-ranked bus that retained at least 500 MW across the Part 1 stress screens. They add buses by minimizing worst signed bottleneck overlap, then maximizing minimum PTDF distance. Loads are equally split within each layout.

| Layout | Buses | Per-site MW |
| --- | --- | --- |
| hosting_1 | 1079 | 500.000 |
| hosting_2 | 1079, 2054 | 250.000 |
| hosting_5 | 1079, 2054, 2127, 3046, 3048 | 100.000 |
| bottleneck_ptdf_1 | 6141 | 500.000 |
| bottleneck_ptdf_2 | 6141, 5395 | 250.000 |
| bottleneck_ptdf_5 | 6141, 5395, 6342, 5451, 6004 | 100.000 |

## Why S1 can need generation

At the tightest native hour, aggregate generation has **3,024.604 MW** of spare supply. For the full **5,000 MW** S1 field to be admitted at zero storage, at least **1,975.396 MW** must come from new private generation in that hour. Local transmission limits can tighten the result. The game admits one firm capacity per site for the entire modeled horizon, so the limiting hour can reduce IT value across the year.

The partial S1 tests hold S2 at 500 MW of generation. They bracket the tested cost and admission trade-off at 0, 125, 250, 375, and 500 MW of S1 generation for the one-site and five-site electrical layouts.

| Electrical layout | S1 G MW | Mean score $B | Worst score $B | Minimum S1 admitted MW | Fields complete |
| --- | --- | --- | --- | --- | --- |
| bottleneck_ptdf_1 | 0 | 58.840883 | 55.286670 | 300.419 | 4/4 |
| bottleneck_ptdf_1 | 125 | 69.026138 | 68.273092 | 500.000 | 4/4 |
| bottleneck_ptdf_1 | 250 | 68.521914 | 67.772941 | 500.000 | 4/4 |
| bottleneck_ptdf_1 | 375 | 68.012663 | 67.272844 | 500.000 | 4/4 |
| bottleneck_ptdf_1 | 500 | 67.501032 | 66.772785 | 500.000 | 4/4 |
| bottleneck_ptdf_5 | 0 | 58.720722 | 55.078367 | 302.430 | 4/4 |
| bottleneck_ptdf_5 | 125 | 68.871609 | 67.857092 | 500.000 | 4/4 |
| bottleneck_ptdf_5 | 250 | 68.364165 | 67.356993 | 500.000 | 4/4 |
| bottleneck_ptdf_5 | 375 | 67.842993 | 66.856907 | 500.000 | 4/4 |
| bottleneck_ptdf_5 | 500 | 67.332209 | 66.356833 | 500.000 | 4/4 |

| Layout | Rival field | S1 sizes tested | Smallest tested G for full S1 MW | Highest scoring tested S1 G MW | S1 MW at highest score | Score $B |
| --- | --- | --- | --- | --- | --- | --- |
| bottleneck_ptdf_1 | nine_grid_at_6141 | 5 | 125 | 125 | 500.000000 | 69.433216 |
| bottleneck_ptdf_1 | nine_grid_at_hosting_1 | 5 | 125 | 125 | 500.000000 | 69.436247 |
| bottleneck_ptdf_1 | nine_s2_cg_hosting_2 | 5 | 125 | 125 | 500.000000 | 68.961998 |
| bottleneck_ptdf_1 | nine_both_cg_ptdf_5 | 5 | 0 | 0 | 500.000000 | 68.773317 |
| bottleneck_ptdf_5 | nine_grid_at_6141 | 5 | 125 | 125 | 500.000000 | 69.435357 |
| bottleneck_ptdf_5 | nine_grid_at_hosting_1 | 5 | 125 | 125 | 500.000000 | 69.433503 |
| bottleneck_ptdf_5 | nine_s2_cg_hosting_2 | 5 | 125 | 125 | 500.000000 | 68.760483 |
| bottleneck_ptdf_5 | nine_both_cg_ptdf_5 | 5 | 0 | 0 | 500.000000 | 68.357206 |

## Matched scores by field

| Our strategy | nine_grid_at_6141 | nine_grid_at_hosting_1 | nine_s2_cg_hosting_2 | nine_both_cg_ptdf_5 |
| --- | --- | --- | --- | --- |
| bottleneck_ptdf_1_s1_125_s2_cg | 69.433216 | 69.436247 | 68.961998 | 68.273092 |
| bottleneck_ptdf_5_s1_125_s2_cg | 69.435357 | 69.433503 | 68.760483 | 67.857092 |
| bottleneck_ptdf_1_s1_250_s2_cg | 68.930090 | 68.933638 | 68.450986 | 67.772941 |
| bottleneck_ptdf_5_s1_250_s2_cg | 68.932741 | 68.930462 | 68.236462 | 67.356993 |
| bottleneck_ptdf_1_s1_375_s2_cg | 68.426944 | 68.432698 | 67.918165 | 67.272844 |
| bottleneck_ptdf_5_s1_375_s2_cg | 68.431481 | 68.428893 | 67.654691 | 66.856907 |
| bottleneck_ptdf_1_both_cg | 67.922103 | 67.930719 | 67.378522 | 66.772785 |
| bottleneck_ptdf_2_both_cg | 67.929030 | 67.925797 | 67.046206 | 66.714537 |
| bottleneck_ptdf_5_both_cg | 67.930030 | 67.926632 | 67.115340 | 66.356833 |
| hosting_1_both_cg | 67.930062 | 67.916901 | 66.015041 | 66.547483 |
| hosting_5_both_cg | 67.930064 | 67.915756 | 65.624985 | 66.617798 |
| hosting_2_both_cg | 67.930064 | 67.915654 | 64.841068 | 66.581377 |
| bottleneck_ptdf_1_s2_cg | 55.578471 | 55.725075 | 55.286670 | 68.773317 |
| bottleneck_ptdf_5_s2_cg | 55.724435 | 55.722880 | 55.078367 | 68.357206 |
| bottleneck_ptdf_2_s2_cg | 55.724392 | 55.722334 | 55.000269 | 68.715131 |
| hosting_1_s2_cg | 55.724277 | 55.717709 | 54.302629 | 68.548222 |
| hosting_5_s2_cg | 55.724267 | 55.716999 | 53.940626 | 68.618481 |
| hosting_2_s2_cg | 55.724269 | 55.716941 | 53.602205 | 68.582220 |
| bottleneck_ptdf_5_grid | 21.759715 | 21.759196 | 21.778401 | 35.947906 |
| bottleneck_ptdf_2_grid | 21.759697 | 21.758985 | 21.778091 | 35.950383 |
| hosting_1_grid | 21.759731 | 21.757672 | 21.776725 | 35.949219 |
| hosting_5_grid | 21.759728 | 21.757567 | 21.776339 | 35.949139 |
| hosting_2_grid | 21.759732 | 21.757553 | 21.776173 | 35.949109 |
| bottleneck_ptdf_1_grid | 21.615073 | 21.760020 | 21.779491 | 35.950624 |

### nine_grid_at_6141

| Case | Score $B | Rank of 10 | Lead over best rival $B | Gross IT value $B | Grid MWh across build-years | Private MWh across build-years | Generator on h across build-years | Verified required h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [bottleneck_ptdf_5_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_6141.md>) | 69.435357 | 1 | 48.258438 | 123.053149 | 17,516,459.269 | 3,540.731 | 12.000 | 12.000 |
| [bottleneck_ptdf_1_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141__nine_grid_at_6141.md>) | 69.433216 | 1 | 48.417224 | 123.053149 | 17,516,073.802 | 3,926.198 | 16.000 | 16.000 |
| [bottleneck_ptdf_5_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_6141.md>) | 68.932741 | 1 | 46.757438 | 123.053149 | 17,515,209.400 | 4,790.600 | 16.000 | 16.000 |
| [bottleneck_ptdf_1_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141__nine_grid_at_6141.md>) | 68.930090 | 1 | 46.915488 | 123.053149 | 17,514,823.933 | 5,176.067 | 16.000 | 16.000 |
| [bottleneck_ptdf_5_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_6141.md>) | 68.431481 | 1 | 45.257462 | 123.053149 | 17,513,959.527 | 6,040.473 | 16.000 | 16.000 |
| [bottleneck_ptdf_1_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141__nine_grid_at_6141.md>) | 68.426944 | 1 | 45.413831 | 123.053149 | 17,513,574.060 | 6,425.940 | 16.000 | 16.000 |
| [hosting_2_both_cg](<C_eq_G_S1_S2_500_1079_2054__nine_grid_at_6141.md>) | 67.930064 | 1 | 43.918718 | 123.053149 | 17,512,871.093 | 7,128.907 | 16.000 | 16.000 |
| [hosting_5_both_cg](<C_eq_G_S1_S2_500_1079_2054_2127_3046_3048__nine_grid_at_6141.md>) | 67.930064 | 1 | 43.918717 | 123.053149 | 17,512,871.093 | 7,128.907 | 16.000 | 16.000 |
| [hosting_1_both_cg](<C_eq_G_S1_S2_500_1079__nine_grid_at_6141.md>) | 67.930062 | 1 | 43.918707 | 123.053149 | 17,512,871.083 | 7,128.917 | 16.000 | 16.000 |
| [bottleneck_ptdf_5_both_cg](<C_eq_G_S1_S2_500_6141_5395_6342_5451_6004__nine_grid_at_6141.md>) | 67.930030 | 1 | 43.918771 | 123.053149 | 17,512,871.173 | 7,128.827 | 16.000 | 16.000 |
| [bottleneck_ptdf_2_both_cg](<C_eq_G_S1_S2_500_6141_5395__nine_grid_at_6141.md>) | 67.929030 | 1 | 43.917809 | 123.053149 | 17,512,871.083 | 7,128.917 | 16.000 | 16.000 |
| [bottleneck_ptdf_1_both_cg](<C_eq_G_S1_S2_500_6141__nine_grid_at_6141.md>) | 67.922103 | 1 | 43.911330 | 123.053149 | 17,512,324.186 | 7,675.814 | 20.000 | 20.000 |
| [bottleneck_ptdf_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_6141.md>) | 55.724435 | 1 | 33.964525 | 98.741551 | 14,056,124.253 | 2,451.194 | 6.000 | 6.000 |
| [bottleneck_ptdf_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395__nine_grid_at_6141.md>) | 55.724392 | 1 | 33.964496 | 98.741556 | 14,056,124.968 | 2,451.194 | 6.000 | 6.000 |
| [hosting_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079__nine_grid_at_6141.md>) | 55.724277 | 1 | 33.964367 | 98.741558 | 14,056,125.206 | 2,451.194 | 6.000 | 6.000 |
| [hosting_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054__nine_grid_at_6141.md>) | 55.724269 | 1 | 33.964359 | 98.741556 | 14,056,124.968 | 2,451.194 | 6.000 | 6.000 |
| [hosting_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054_2127_3046_3048__nine_grid_at_6141.md>) | 55.724267 | 1 | 33.964357 | 98.741551 | 14,056,124.253 | 2,451.194 | 6.000 | 6.000 |
| [bottleneck_ptdf_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141__nine_grid_at_6141.md>) | 55.578471 | 1 | 33.963158 | 98.494134 | 14,020,669.989 | 2,678.818 | 10.000 | 10.000 |
| [hosting_2_grid](<G_eq_0_S1_S2_500_1079_2054__nine_grid_at_6141.md>) | 21.759732 | 1 | 0.000063 | 37.218703 | 5,299,106.021 | 0.000 | 0.000 | 0.000 |
| [hosting_1_grid](<G_eq_0_S1_S2_500_1079__nine_grid_at_6141.md>) | 21.759731 | 1 | 0.000063 | 37.218705 | 5,299,106.258 | 0.000 | 0.000 | 0.000 |
| [hosting_5_grid](<G_eq_0_S1_S2_500_1079_2054_2127_3046_3048__nine_grid_at_6141.md>) | 21.759728 | 1 | 0.000060 | 37.218698 | 5,299,105.306 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_5_grid](<G_eq_0_S1_S2_500_6141_5395_6342_5451_6004__nine_grid_at_6141.md>) | 21.759715 | 1 | 0.000047 | 37.218698 | 5,299,105.306 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_2_grid](<G_eq_0_S1_S2_500_6141_5395__nine_grid_at_6141.md>) | 21.759697 | 1 | 0.000043 | 37.218703 | 5,299,106.021 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_1_grid](<G_eq_0_S1_S2_500_6141__nine_grid_at_6141.md>) | 21.615073 | 1 | -0.000000 | 36.971256 | 5,263,875.142 | 0.000 | 0.000 | 0.000 |

### nine_grid_at_hosting_1

| Case | Score $B | Rank of 10 | Lead over best rival $B | Gross IT value $B | Grid MWh across build-years | Private MWh across build-years | Generator on h across build-years | Verified required h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [bottleneck_ptdf_1_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141__nine_grid_at_hosting_1.md>) | 69.436247 | 1 | 48.260636 | 123.053149 | 17,516,459.269 | 3,540.731 | 12.000 | 12.000 |
| [bottleneck_ptdf_5_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_hosting_1.md>) | 69.433503 | 1 | 48.258190 | 123.053149 | 17,516,459.269 | 3,540.731 | 12.000 | 12.000 |
| [bottleneck_ptdf_1_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141__nine_grid_at_hosting_1.md>) | 68.933638 | 1 | 46.760066 | 123.053149 | 17,515,209.400 | 4,790.600 | 16.000 | 16.000 |
| [bottleneck_ptdf_5_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_hosting_1.md>) | 68.930462 | 1 | 46.756999 | 123.053149 | 17,515,209.400 | 4,790.600 | 16.000 | 16.000 |
| [bottleneck_ptdf_1_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141__nine_grid_at_hosting_1.md>) | 68.432698 | 1 | 45.260387 | 123.053149 | 17,513,959.527 | 6,040.473 | 16.000 | 16.000 |
| [bottleneck_ptdf_5_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_hosting_1.md>) | 68.428893 | 1 | 45.257112 | 123.053149 | 17,513,959.527 | 6,040.473 | 16.000 | 16.000 |
| [bottleneck_ptdf_1_both_cg](<C_eq_G_S1_S2_500_6141__nine_grid_at_hosting_1.md>) | 67.930719 | 1 | 43.760176 | 123.053149 | 17,512,709.653 | 7,290.347 | 16.000 | 16.000 |
| [bottleneck_ptdf_5_both_cg](<C_eq_G_S1_S2_500_6141_5395_6342_5451_6004__nine_grid_at_hosting_1.md>) | 67.926632 | 1 | 43.756377 | 123.053149 | 17,512,709.653 | 7,290.347 | 16.000 | 16.000 |
| [bottleneck_ptdf_2_both_cg](<C_eq_G_S1_S2_500_6141_5395__nine_grid_at_hosting_1.md>) | 67.925797 | 1 | 43.755562 | 123.053149 | 17,512,709.653 | 7,290.347 | 16.000 | 16.000 |
| [hosting_1_both_cg](<C_eq_G_S1_S2_500_1079__nine_grid_at_hosting_1.md>) | 67.916901 | 1 | 43.747382 | 123.053149 | 17,512,343.975 | 7,656.025 | 20.000 | 20.000 |
| [hosting_5_both_cg](<C_eq_G_S1_S2_500_1079_2054_2127_3046_3048__nine_grid_at_hosting_1.md>) | 67.915756 | 1 | 43.746493 | 123.053149 | 17,512,240.561 | 7,759.439 | 24.000 | 24.000 |
| [hosting_2_both_cg](<C_eq_G_S1_S2_500_1079_2054__nine_grid_at_hosting_1.md>) | 67.915654 | 1 | 43.746392 | 123.053149 | 17,512,224.048 | 7,775.952 | 24.000 | 24.000 |
| [bottleneck_ptdf_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141__nine_grid_at_hosting_1.md>) | 55.725075 | 1 | 33.966702 | 98.741558 | 14,056,125.207 | 2,451.194 | 6.000 | 6.000 |
| [bottleneck_ptdf_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_grid_at_hosting_1.md>) | 55.722880 | 1 | 33.964616 | 98.741551 | 14,056,124.253 | 2,451.194 | 6.000 | 6.000 |
| [bottleneck_ptdf_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395__nine_grid_at_hosting_1.md>) | 55.722334 | 1 | 33.964118 | 98.741556 | 14,056,124.968 | 2,451.194 | 6.000 | 6.000 |
| [hosting_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079__nine_grid_at_hosting_1.md>) | 55.717709 | 1 | 33.959796 | 98.741558 | 14,056,125.207 | 2,451.194 | 6.000 | 6.000 |
| [hosting_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054_2127_3046_3048__nine_grid_at_hosting_1.md>) | 55.716999 | 1 | 33.959085 | 98.741551 | 14,056,097.844 | 2,477.603 | 10.000 | 10.000 |
| [hosting_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054__nine_grid_at_hosting_1.md>) | 55.716941 | 1 | 33.959028 | 98.741556 | 14,056,089.109 | 2,487.053 | 10.000 | 10.000 |
| [bottleneck_ptdf_1_grid](<G_eq_0_S1_S2_500_6141__nine_grid_at_hosting_1.md>) | 21.760020 | 1 | 0.001889 | 37.218705 | 5,299,106.258 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_5_grid](<G_eq_0_S1_S2_500_6141_5395_6342_5451_6004__nine_grid_at_hosting_1.md>) | 21.759196 | 1 | 0.001173 | 37.218698 | 5,299,105.306 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_2_grid](<G_eq_0_S1_S2_500_6141_5395__nine_grid_at_hosting_1.md>) | 21.758985 | 1 | 0.001011 | 37.218703 | 5,299,106.021 | 0.000 | 0.000 | 0.000 |
| [hosting_1_grid](<G_eq_0_S1_S2_500_1079__nine_grid_at_hosting_1.md>) | 21.757672 | 1 | -0.000000 | 37.218705 | 5,299,106.258 | 0.000 | 0.000 | 0.000 |
| [hosting_5_grid](<G_eq_0_S1_S2_500_1079_2054_2127_3046_3048__nine_grid_at_hosting_1.md>) | 21.757567 | 10 | -0.000105 | 37.218698 | 5,299,105.306 | 0.000 | 0.000 | 0.000 |
| [hosting_2_grid](<G_eq_0_S1_S2_500_1079_2054__nine_grid_at_hosting_1.md>) | 21.757553 | 10 | -0.000118 | 37.218703 | 5,299,106.021 | 0.000 | 0.000 | 0.000 |

### nine_s2_cg_hosting_2

| Case | Score $B | Rank of 10 | Lead over best rival $B | Gross IT value $B | Grid MWh across build-years | Private MWh across build-years | Generator on h across build-years | Verified required h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [bottleneck_ptdf_1_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141__nine_s2_cg_hosting_2.md>) | 68.961998 | 1 | 15.490884 | 123.053149 | 17,217,710.431 | 302,289.569 | 2,678.729 | 12.000 |
| [bottleneck_ptdf_5_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_s2_cg_hosting_2.md>) | 68.760483 | 1 | 15.391954 | 123.053149 | 17,113,143.040 | 406,856.960 | 3,739.836 | 12.000 |
| [bottleneck_ptdf_1_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141__nine_s2_cg_hosting_2.md>) | 68.450986 | 1 | 14.106281 | 123.053149 | 17,180,035.314 | 339,964.686 | 2,682.729 | 16.000 |
| [bottleneck_ptdf_5_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_s2_cg_hosting_2.md>) | 68.236462 | 1 | 14.018426 | 123.053149 | 17,092,512.931 | 427,487.069 | 3,743.836 | 16.000 |
| [bottleneck_ptdf_1_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141__nine_s2_cg_hosting_2.md>) | 67.918165 | 1 | 12.661836 | 123.053149 | 17,176,589.193 | 343,410.807 | 3,013.819 | 16.000 |
| [bottleneck_ptdf_5_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_s2_cg_hosting_2.md>) | 67.654691 | 1 | 12.543925 | 123.053149 | 17,009,263.670 | 510,736.330 | 4,465.852 | 16.000 |
| [bottleneck_ptdf_1_both_cg](<C_eq_G_S1_S2_500_6141__nine_s2_cg_hosting_2.md>) | 67.378522 | 1 | 11.196636 | 123.053149 | 17,137,134.829 | 382,865.171 | 3,013.819 | 16.000 |
| [bottleneck_ptdf_5_both_cg](<C_eq_G_S1_S2_500_6141_5395_6342_5451_6004__nine_s2_cg_hosting_2.md>) | 67.115340 | 1 | 11.108326 | 123.053149 | 16,984,154.374 | 535,845.626 | 4,465.852 | 16.000 |
| [bottleneck_ptdf_2_both_cg](<C_eq_G_S1_S2_500_6141_5395__nine_s2_cg_hosting_2.md>) | 67.046206 | 1 | 11.052167 | 123.053149 | 16,870,642.854 | 649,357.146 | 4,469.852 | 16.000 |
| [hosting_1_both_cg](<C_eq_G_S1_S2_500_1079__nine_s2_cg_hosting_2.md>) | 66.015041 | 1 | 10.311756 | 123.053149 | 16,034,374.892 | 1,485,625.108 | 8,073.978 | 24.000 |
| [hosting_5_both_cg](<C_eq_G_S1_S2_500_1079_2054_2127_3046_3048__nine_s2_cg_hosting_2.md>) | 65.624985 | 1 | 10.111986 | 123.053149 | 15,825,006.569 | 1,694,993.431 | 17,530.000 | 24.000 |
| [hosting_2_both_cg](<C_eq_G_S1_S2_500_1079_2054__nine_s2_cg_hosting_2.md>) | 64.841068 | 1 | 9.792139 | 123.053149 | 15,384,265.434 | 2,135,734.566 | 17,530.000 | 24.000 |
| [bottleneck_ptdf_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141__nine_s2_cg_hosting_2.md>) | 55.286670 | 1 | 1.290809 | 98.741559 | 13,761,621.845 | 296,954.795 | 2,345.638 | 6.000 |
| [bottleneck_ptdf_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_s2_cg_hosting_2.md>) | 55.078367 | 1 | 1.174808 | 98.741555 | 13,664,507.334 | 394,068.709 | 3,733.836 | 6.000 |
| [bottleneck_ptdf_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395__nine_s2_cg_hosting_2.md>) | 55.000269 | 1 | 1.106874 | 98.741558 | 13,522,012.425 | 536,563.976 | 3,737.836 | 6.000 |
| [hosting_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079__nine_s2_cg_hosting_2.md>) | 54.302629 | 1 | 0.637331 | 98.741559 | 13,069,130.645 | 989,445.994 | 6,085.414 | 10.000 |
| [hosting_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054_2127_3046_3048__nine_s2_cg_hosting_2.md>) | 53.940626 | 1 | 0.297073 | 98.741555 | 12,893,559.024 | 1,165,017.019 | 17,520.000 | 10.000 |
| [hosting_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054__nine_s2_cg_hosting_2.md>) | 53.602205 | 1 | -0.000000 | 98.741558 | 12,480,668.019 | 1,577,908.382 | 17,520.000 | 10.000 |
| [bottleneck_ptdf_1_grid](<G_eq_0_S1_S2_500_6141__nine_s2_cg_hosting_2.md>) | 21.779491 | 10 | -32.295971 | 37.252200 | 5,303,875.208 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_5_grid](<G_eq_0_S1_S2_500_6141_5395_6342_5451_6004__nine_s2_cg_hosting_2.md>) | 21.778401 | 10 | -32.223170 | 37.252196 | 5,303,874.595 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_2_grid](<G_eq_0_S1_S2_500_6141_5395__nine_s2_cg_hosting_2.md>) | 21.778091 | 10 | -32.224465 | 37.252198 | 5,303,874.988 | 0.000 | 0.000 | 0.000 |
| [hosting_1_grid](<G_eq_0_S1_S2_500_1079__nine_s2_cg_hosting_2.md>) | 21.776725 | 10 | -32.165497 | 37.252200 | 5,303,875.209 | 0.000 | 0.000 | 0.000 |
| [hosting_5_grid](<G_eq_0_S1_S2_500_1079_2054_2127_3046_3048__nine_s2_cg_hosting_2.md>) | 21.776339 | 10 | -32.126566 | 37.252196 | 5,303,874.630 | 0.000 | 0.000 | 0.000 |
| [hosting_2_grid](<G_eq_0_S1_S2_500_1079_2054__nine_s2_cg_hosting_2.md>) | 21.776173 | 10 | -32.105214 | 37.252198 | 5,303,874.988 | 0.000 | 0.000 | 0.000 |

### nine_both_cg_ptdf_5

| Case | Score $B | Rank of 10 | Lead over best rival $B | Gross IT value $B | Grid MWh across build-years | Private MWh across build-years | Generator on h across build-years | Verified required h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [bottleneck_ptdf_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141__nine_both_cg_ptdf_5.md>) | 68.773317 | 1 | 2.254344 | 123.053149 | 16,705,594.925 | 814,405.075 | 3,007.819 | 604.389 |
| [bottleneck_ptdf_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395__nine_both_cg_ptdf_5.md>) | 68.715131 | 1 | 2.222192 | 123.053149 | 16,656,362.453 | 863,637.547 | 3,733.836 | 604.389 |
| [hosting_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054_2127_3046_3048__nine_both_cg_ptdf_5.md>) | 68.618481 | 1 | 2.175039 | 123.053149 | 16,594,926.783 | 925,073.217 | 3,733.836 | 604.389 |
| [hosting_2_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079_2054__nine_both_cg_ptdf_5.md>) | 68.582220 | 1 | 2.134730 | 123.053149 | 16,549,676.052 | 970,323.948 | 3,733.836 | 604.389 |
| [hosting_1_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_1079__nine_both_cg_ptdf_5.md>) | 68.548222 | 1 | 2.096948 | 123.053149 | 16,482,500.416 | 1,037,499.584 | 3,733.836 | 604.389 |
| [bottleneck_ptdf_5_s2_cg](<G_eq_0_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_both_cg_ptdf_5.md>) | 68.357206 | 1 | 2.000483 | 123.053149 | 16,361,860.629 | 1,158,139.371 | 7,142.510 | 604.389 |
| [bottleneck_ptdf_1_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141__nine_both_cg_ptdf_5.md>) | 68.273092 | 1 | 1.754077 | 123.053149 | 16,704,817.812 | 815,182.188 | 3,021.819 | 604.389 |
| [bottleneck_ptdf_5_s1_125_s2_cg](<G_eq_125_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_both_cg_ptdf_5.md>) | 67.857092 | 1 | 1.500340 | 123.053149 | 16,361,313.831 | 1,158,686.169 | 7,156.510 | 604.389 |
| [bottleneck_ptdf_1_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141__nine_both_cg_ptdf_5.md>) | 67.772941 | 1 | 1.253893 | 123.053149 | 16,704,182.462 | 815,817.538 | 3,021.819 | 604.389 |
| [bottleneck_ptdf_5_s1_250_s2_cg](<G_eq_250_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_both_cg_ptdf_5.md>) | 67.356993 | 1 | 1.000212 | 123.053149 | 16,360,795.813 | 1,159,204.187 | 7,156.510 | 604.389 |
| [bottleneck_ptdf_1_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141__nine_both_cg_ptdf_5.md>) | 67.272844 | 1 | 0.753768 | 123.053149 | 16,703,647.181 | 816,352.819 | 3,021.819 | 604.389 |
| [bottleneck_ptdf_5_s1_375_s2_cg](<G_eq_375_S1_C_eq_G_S2_500_6141_5395_6342_5451_6004__nine_both_cg_ptdf_5.md>) | 66.856907 | 1 | 0.500100 | 123.053149 | 16,360,304.359 | 1,159,695.641 | 7,156.510 | 604.389 |
| [bottleneck_ptdf_1_both_cg](<C_eq_G_S1_S2_500_6141__nine_both_cg_ptdf_5.md>) | 66.772785 | 1 | 0.253685 | 123.053149 | 16,703,185.164 | 816,814.836 | 3,021.819 | 604.389 |
| [bottleneck_ptdf_2_both_cg](<C_eq_G_S1_S2_500_6141_5395__nine_both_cg_ptdf_5.md>) | 66.714537 | 1 | 0.221464 | 123.053149 | 16,653,950.766 | 866,049.234 | 3,747.836 | 604.389 |
| [hosting_5_both_cg](<C_eq_G_S1_S2_500_1079_2054_2127_3046_3048__nine_both_cg_ptdf_5.md>) | 66.617798 | 1 | 0.174212 | 123.053149 | 16,592,276.783 | 927,723.217 | 3,747.836 | 604.389 |
| [hosting_2_both_cg](<C_eq_G_S1_S2_500_1079_2054__nine_both_cg_ptdf_5.md>) | 66.581377 | 1 | 0.133725 | 123.053149 | 16,546,676.052 | 973,323.948 | 3,747.836 | 604.389 |
| [hosting_1_both_cg](<C_eq_G_S1_S2_500_1079__nine_both_cg_ptdf_5.md>) | 66.547483 | 1 | 0.096059 | 123.053149 | 16,479,697.638 | 1,040,302.362 | 3,747.836 | 604.389 |
| [bottleneck_ptdf_5_both_cg](<C_eq_G_S1_S2_500_6141_5395_6342_5451_6004__nine_both_cg_ptdf_5.md>) | 66.356833 | 1 | 0.000000 | 123.053149 | 16,359,837.478 | 1,160,162.522 | 7,156.510 | 604.389 |
| [bottleneck_ptdf_1_grid](<G_eq_0_S1_S2_500_6141__nine_both_cg_ptdf_5.md>) | 35.950624 | 10 | -30.723079 | 61.526574 | 8,760,000.000 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_2_grid](<G_eq_0_S1_S2_500_6141_5395__nine_both_cg_ptdf_5.md>) | 35.950383 | 10 | -30.694415 | 61.526574 | 8,760,000.000 | 0.000 | 0.000 | 0.000 |
| [hosting_1_grid](<G_eq_0_S1_S2_500_1079__nine_both_cg_ptdf_5.md>) | 35.949219 | 10 | -30.684322 | 61.526574 | 8,760,000.000 | 0.000 | 0.000 | 0.000 |
| [hosting_5_grid](<G_eq_0_S1_S2_500_1079_2054_2127_3046_3048__nine_both_cg_ptdf_5.md>) | 35.949139 | 10 | -30.684403 | 61.526574 | 8,760,000.000 | 0.000 | 0.000 | 0.000 |
| [hosting_2_grid](<G_eq_0_S1_S2_500_1079_2054__nine_both_cg_ptdf_5.md>) | 35.949109 | 10 | -30.684429 | 61.526574 | 8,760,000.000 | 0.000 | 0.000 | 0.000 |
| [bottleneck_ptdf_5_grid](<G_eq_0_S1_S2_500_6141_5395_6342_5451_6004__nine_both_cg_ptdf_5.md>) | 35.947906 | 10 | -30.629685 | 61.526574 | 8,760,000.000 | 0.000 | 0.000 | 0.000 |

## Personal notes

<!-- USER_NOTES -->
