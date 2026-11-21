# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,371.898240 | 17.367012 | 30.763287 | 0.562927 | 0.000747 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,323.233 | 676.767 | 158,460.720 | 158,460.720 | 7.000 | 1,658.458 | 1,658.458 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,161.569 | 1,967,684.621 | 1,967,684.621 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 436.405 | 436.405 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 826.004958 | 258.126549 | 14,683.846818 | none |
| 12 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 1,055.607083 | 8,726.630000 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,637.109900 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 665.982118 | none |
| 106 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 70.944218 | -0.000000 | none |
| 107 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 710.838418 | -0.000000 | none |
| 108 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 1,014.092728 | -0.000000 | none |
| 109 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,151.294181 | 0.000000 | none |
| 110 | 306.232979 | 94.767021 | 0.000000 | 99.000000 | 99.000000 | 34.856272 | 1,051.181979 | 0.000001 | none |
| 111 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 0.000000 | 0.000000 | 611.838418 | 0.000000 | none |
| 112 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 70.944218 | -0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 665.982118 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,637.109900 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_b150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_b150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
