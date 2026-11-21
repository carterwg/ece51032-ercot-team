# S1 sizing at bus 6141 in 1 MW increments

| G MW | P MW | B MWh | Capital $M | Minimum S1 MW | Exact 500 MW | At least 499.9 MW |
| --- | --- | --- | --- | --- | --- | --- |
| 97 | 99 | 396 | 332.6 | 499.901525136 | 32/36 | 36/36 |
| 95 | 105 | 420 | 337.0 | 499.915360813 | 32/36 | 36/36 |

The 1 MW screen covered generators from 85 to 105 MW and battery power from 95 to 115 MW. Of these, 219 pairs cost less than $337M. The same-bus analysis checked 27 fields and screened out all 173 pairs cheaper than $332.6M. Exact S1 runs checked the selected build over all 36 fields using 120 modeled periods, four-hour batteries, and a daily half-full state-of-charge requirement. The campaign study supplies the baseline values. Each campaign week used the same S1 dispatch inputs.

The minimum award for the selected build was 499.901525136 MW in nine_g50_b175_at_6141. The strongest cheaper pair in the same-bus screen cost $332M and received 499.894921744 MW in the exact check of its limiting field. [Cheaper-pair dispatch](<Battery_S1_G96_P100__nine_g50_b175_at_6141.md>) · [Selected build in its limiting field](<Battery_S1_G97_P99__nine_g50_b175_at_6141.md>)

## Exact S1 allocations by field

| Opponent field | Rival buses | G per rival MW | P per rival MW | Our S1 MW |
| --- | --- | --- | --- | --- |
| [nine_grid_at_6141](<Battery_S1_G97_P99__nine_grid_at_6141.md>) | 6141 | 0 | 0 | 500.000000000 |
| [nine_grid_at_hosting_1](<Battery_S1_G97_P99__nine_grid_at_hosting_1.md>) | 1079 | 0 | 0 | 500.000000000 |
| [nine_s2_cg_hosting_2](<Battery_S1_G97_P99__nine_s2_cg_hosting_2.md>) | 1079, 2054 | 0 | 0 | 500.000000000 |
| [nine_both_cg_ptdf_5](<Battery_S1_G97_P99__nine_both_cg_ptdf_5.md>) | 6141, 5395, 6342, 5451, 6004 | 500 | 0 | 500.000000000 |
| [nine_g125_at_6141](<Battery_S1_G97_P99__nine_g125_at_6141.md>) | 6141 | 125 | 0 | 500.000000000 |
| [nine_g150_ptdf_5](<Battery_S1_G97_P99__nine_g150_ptdf_5.md>) | 6141, 5395, 6342, 5451, 6004 | 150 | 0 | 500.000000000 |
| [nine_g200_at_6141](<Battery_S1_G97_P99__nine_g200_at_6141.md>) | 6141 | 200 | 0 | 500.000000000 |
| [nine_b125_at_6141](<Battery_S1_G97_P99__nine_b125_at_6141.md>) | 6141 | 0 | 125 | 500.000000000 |
| [nine_b196_at_6141](<Battery_S1_G97_P99__nine_b196_at_6141.md>) | 6141 | 0 | 196 | 500.000000000 |
| [nine_b150_ptdf_5](<Battery_S1_G97_P99__nine_b150_ptdf_5.md>) | 6141, 5395, 6342, 5451, 6004 | 0 | 150 | 500.000000000 |
| [nine_g75_b125_at_6141](<Battery_S1_G97_P99__nine_g75_b125_at_6141.md>) | 6141 | 75 | 125 | 499.925737570 |
| [nine_random_storage_01](<Battery_S1_G97_P99__nine_random_storage_01.md>) | 6141 | 55 | 70 | 500.000000000 |
| [nine_random_storage_02](<Battery_S1_G97_P99__nine_random_storage_02.md>) | 6141 | 70 | 195 | 500.000000000 |
| [nine_random_storage_03](<Battery_S1_G97_P99__nine_random_storage_03.md>) | 6141 | 85 | 155 | 500.000000000 |
| [nine_random_storage_04](<Battery_S1_G97_P99__nine_random_storage_04.md>) | 6141 | 145 | 80 | 500.000000000 |
| [nine_random_storage_05](<Battery_S1_G97_P99__nine_random_storage_05.md>) | 6141 | 170 | 120 | 500.000000000 |
| [nine_random_storage_06](<Battery_S1_G97_P99__nine_random_storage_06.md>) | 6141 | 165 | 185 | 500.000000000 |
| [nine_random_storage_07](<Battery_S1_G97_P99__nine_random_storage_07.md>) | 1079, 2054 | 50 | 145 | 500.000000000 |
| [nine_random_storage_08](<Battery_S1_G97_P99__nine_random_storage_08.md>) | 1079, 2054 | 160 | 145 | 500.000000000 |
| [nine_random_storage_09](<Battery_S1_G97_P99__nine_random_storage_09.md>) | 6141, 5395, 6342, 5451, 6004 | 35 | 190 | 500.000000000 |
| [nine_random_storage_10](<Battery_S1_G97_P99__nine_random_storage_10.md>) | 6141, 5395, 6342, 5451, 6004 | 145 | 110 | 500.000000000 |
| [nine_g50_b125_at_6141](<Battery_S1_G97_P99__nine_g50_b125_at_6141.md>) | 6141 | 50 | 125 | 499.944569464 |
| [nine_g50_b150_at_6141](<Battery_S1_G97_P99__nine_g50_b150_at_6141.md>) | 6141 | 50 | 150 | 499.940265031 |
| [nine_g50_b175_at_6141](<Battery_S1_G97_P99__nine_g50_b175_at_6141.md>) | 6141 | 50 | 175 | 499.901525136 |
| [nine_g50_b200_at_6141](<Battery_S1_G97_P99__nine_g50_b200_at_6141.md>) | 6141 | 50 | 200 | 500.000000000 |
| [nine_g75_b150_at_6141](<Battery_S1_G97_P99__nine_g75_b150_at_6141.md>) | 6141 | 75 | 150 | 500.000000000 |
| [nine_g75_b175_at_6141](<Battery_S1_G97_P99__nine_g75_b175_at_6141.md>) | 6141 | 75 | 175 | 500.000000000 |
| [nine_g75_b200_at_6141](<Battery_S1_G97_P99__nine_g75_b200_at_6141.md>) | 6141 | 75 | 200 | 500.000000000 |
| [nine_g100_b125_at_6141](<Battery_S1_G97_P99__nine_g100_b125_at_6141.md>) | 6141 | 100 | 125 | 500.000000000 |
| [nine_g100_b150_at_6141](<Battery_S1_G97_P99__nine_g100_b150_at_6141.md>) | 6141 | 100 | 150 | 500.000000000 |
| [nine_g100_b175_at_6141](<Battery_S1_G97_P99__nine_g100_b175_at_6141.md>) | 6141 | 100 | 175 | 500.000000000 |
| [nine_g100_b200_at_6141](<Battery_S1_G97_P99__nine_g100_b200_at_6141.md>) | 6141 | 100 | 200 | 500.000000000 |
| [nine_g125_b125_at_6141](<Battery_S1_G97_P99__nine_g125_b125_at_6141.md>) | 6141 | 125 | 125 | 500.000000000 |
| [nine_g125_b150_at_6141](<Battery_S1_G97_P99__nine_g125_b150_at_6141.md>) | 6141 | 125 | 150 | 500.000000000 |
| [nine_g125_b175_at_6141](<Battery_S1_G97_P99__nine_g125_b175_at_6141.md>) | 6141 | 125 | 175 | 500.000000000 |
| [nine_g125_b200_at_6141](<Battery_S1_G97_P99__nine_g125_b200_at_6141.md>) | 6141 | 125 | 200 | 500.000000000 |

## Personal notes

<!-- USER_NOTES -->
