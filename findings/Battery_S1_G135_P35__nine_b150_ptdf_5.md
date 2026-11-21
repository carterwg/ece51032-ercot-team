# 500 MW at bus 6141, S1 generator 135 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.942389 | 4,348.998992 | 17.378084 | 30.759743 | 0.563345 | 0.000791 | 0.269969 | 0.048994 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,695.431 | 799.898 | 58,039.326 | 58,039.326 | 7.000 | 1,658.458 | 1,658.458 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,154.717 | 1,959,755.957 | 1,959,755.957 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 69.992 | 69.992 | -0.000 | 139.984 | 139.984 | 139.984 |
| 2 | 69.992 | 69.992 | -0.000 | 139.984 | 174.980 | 174.980 |
| 3 | 69.992 | 69.992 | -0.000 | 139.984 | 139.984 | 139.984 |
| 4 | 69.992 | 69.992 | -0.000 | 139.984 | 174.980 | 174.980 |
| 5 | 69.992 | 69.992 | -0.000 | 139.984 | 174.980 | 174.980 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 534.938356 | 0.000000 | 34.995967 | 0.000000 | 104.987902 | 866.451904 | 230.943396 | 14,703.120000 | none |
| 12 | 464.946422 | 0.000000 | 0.000000 | 34.995967 | 104.987902 | 0.000000 | 1,096.711867 | 8,726.630000 | none |
| 104 | 499.942389 | 0.000000 | 0.000000 | 0.000000 | 139.983869 | 0.000000 | 0.000000 | 1,660.009148 | none |
| 105 | 499.942389 | 0.000000 | 0.000000 | 0.000000 | 139.983869 | 0.000000 | 0.000000 | 688.881366 | none |
| 106 | 364.957944 | 134.984445 | 0.000000 | 0.000000 | 139.983869 | 0.000000 | 10.060525 | -0.000000 | none |
| 107 | 398.704055 | 101.238334 | 0.000000 | 0.000000 | 139.983869 | 0.000000 | 683.700836 | -0.000000 | none |
| 108 | 339.667808 | 125.278614 | 0.000000 | 34.995967 | 104.987902 | 0.000000 | 1,026.918899 | 0.000000 | none |
| 109 | 330.264437 | 134.681985 | 0.000000 | 34.995967 | 69.991934 | 0.000000 | 1,154.716981 | -0.000000 | none |
| 110 | 363.708088 | 101.238334 | 0.000000 | 34.995967 | 34.995967 | 0.000000 | 1,050.959179 | -0.000000 | none |
| 111 | 363.708088 | 101.238334 | 0.000000 | 34.995967 | -0.000000 | 0.000000 | 648.704869 | -0.000000 | none |
| 112 | 398.704055 | 101.238334 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 43.806636 | -0.000000 | none |
| 113 | 499.942389 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 688.881366 | none |
| 114 | 499.942389 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,660.009148 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g135_p35/nine_b150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g135_p35/nine_b150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
