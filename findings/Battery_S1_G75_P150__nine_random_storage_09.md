# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.337699 | 30.763287 | 0.565044 | 0.000544 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,495.920 | 504.080 | 267,987.836 | 267,987.836 | 7.000 | 1,908.773 | 1,908.773 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 35 MW of S1 generation and 190 MW / 760 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,710.000 | 3,191,578.985 | 3,191,578.985 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | -0.000 | 600.000 | 600.000 | 600.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |
| 3 | 300.000 | 300.000 | 0.000 | 600.000 | 832.193 | 832.193 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 993.208719 | 612.565252 | 14,191.980000 | none |
| 13 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 306.070624 | 5.089711 | 1,558.000000 | 8,509.630000 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 106 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 406.045978 | -0.000000 | none |
| 107 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 1,045.940178 | -0.000000 | none |
| 108 | 382.805512 | 75.000000 | 0.000000 | 42.194488 | 557.805512 | 76.000000 | 1,482.000000 | -0.000000 | none |
| 109 | 293.750000 | 56.250000 | 0.000000 | 150.000000 | 407.805512 | 38.000000 | 1,507.895941 | 0.000000 | none |
| 110 | 277.169984 | 72.830016 | 0.000000 | 150.000000 | 257.805512 | 0.000000 | 1,302.187259 | -0.000000 | none |
| 111 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 107.805512 | 0.000000 | 895.940178 | -0.000000 | none |
| 112 | 317.194488 | 75.000000 | 0.000000 | 107.805512 | 0.000000 | 0.000000 | 313.990466 | -0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_09/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_09/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
