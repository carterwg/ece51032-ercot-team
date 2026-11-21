# 500 MW at bus 6141, S1 generator 96 MW and battery 100 MW / 400 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.894922 | 4,945.802099 | 17.342055 | 30.756822 | 0.584665 | 0.000799 | 0.191960 | 0.139971 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,331.831 | 747.684 | 277,701.491 | 277,701.491 | 9.000 | 2,922.989 | 2,992.797 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,556.068 | 3,813,760.111 | 3,813,760.111 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 199.958 | 199.958 | 0.000 | 399.916 | 744.038 | 744.038 |
| 2 | 199.958 | 199.958 | 0.000 | 399.916 | 999.790 | 999.790 |
| 3 | 199.958 | 199.958 | 99.979 | 399.916 | 799.832 | 799.832 |
| 4 | 199.958 | 199.958 | 0.000 | 399.916 | 499.895 | 499.895 |
| 5 | 199.958 | 199.958 | 0.000 | 399.916 | 608.798 | 608.798 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.873906 | 0.000000 | 99.978984 | 0.000000 | 299.936953 | 766.219287 | 518.689171 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 399.915937 | 0.000000 | 0.000000 | 99.978984 | 291.742396 | 750.759215 | 345.792780 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.894922 | 0.000000 | 0.000000 | 0.000000 | 399.915937 | 0.000000 | 0.000000 | 1,063.206041 | b02136:lower |
| 105 | 461.767462 | 38.127460 | 0.000000 | 0.000000 | 399.915937 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 360.371670 | 95.979825 | 0.000000 | 43.543427 | 356.372510 | 0.000000 | 345.792780 | 188.058673 | b02136:lower |
| 107 | 303.936112 | 95.979825 | 0.000000 | 99.978984 | 256.393526 | 0.000000 | 838.124980 | 96.932230 | b02136:lower |
| 108 | 303.936112 | 95.979825 | 0.000000 | 99.978984 | 156.414542 | 0.000000 | 1,183.094803 | 39.647743 | b02136:lower |
| 109 | 447.458524 | 95.979825 | 43.543427 | 0.000000 | 199.957969 | 0.000000 | 1,444.280009 | 20.109084 | b02136:lower |
| 110 | 303.936112 | 95.979825 | 0.000000 | 99.978984 | 99.978984 | 0.000000 | 1,183.094803 | 39.647743 | b02136:lower |
| 111 | 304.366054 | 95.549883 | 0.000000 | 99.978984 | 0.000000 | 43.543427 | 884.089893 | 96.932230 | b02136:lower |
| 112 | 403.915097 | 95.979825 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 389.336207 | 188.058673 | b02136:lower |
| 113 | 461.767462 | 38.127460 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.894922 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,063.206041 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

Full result (local solver artifact) · Solver audit (local solver artifact)

## Personal notes

<!-- USER_NOTES -->
