# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.364546 | 30.763287 | 0.565390 | 0.000751 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,321.000 | 679.000 | 179,185.099 | 179,185.099 | 7.000 | 1,908.773 | 1,824.003 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 35 MW of S1 generation and 190 MW / 760 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,710.000 | 3,196,828.948 | 3,196,828.948 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 396.000 | 396.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 577.193 | 577.193 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 1,039.643467 | 608.000000 | 14,191.980000 | none |
| 13 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 209.160336 | 0.000000 | 1,603.910289 | 8,509.630000 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 106 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 384.045978 | 0.000000 | none |
| 107 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 1,023.940178 | -0.000000 | none |
| 108 | 363.228927 | 97.000000 | 0.000000 | 39.771073 | 356.228927 | 73.940178 | 1,460.363593 | -0.000000 | none |
| 109 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 257.228927 | 16.363593 | 1,480.759534 | 0.000000 | none |
| 110 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 158.228927 | 0.000000 | 1,327.194488 | -0.000000 | none |
| 111 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 59.228927 | 0.000000 | 924.940178 | 0.000000 | none |
| 112 | 343.771073 | 97.000000 | 0.000000 | 59.228927 | 0.000000 | 0.000000 | 329.059822 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_09/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_09/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
