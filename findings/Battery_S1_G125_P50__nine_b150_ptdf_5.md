# 500 MW at bus 6141, S1 generator 125 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943901 | 4,356.141134 | 17.377166 | 30.759836 | 0.563305 | 0.000804 | 0.249972 | 0.069992 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,727.245 | 781.331 | 81,760.986 | 81,760.986 | 7.000 | 1,659.458 | 1,658.458 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,156.859 | 1,967,279.420 | 1,967,279.420 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 99.989 | 99.989 | -0.000 | 199.978 | 199.978 | 199.978 |
| 2 | 99.989 | 99.989 | -0.000 | 199.978 | 249.972 | 249.972 |
| 3 | 99.989 | 99.989 | -0.000 | 199.978 | 199.978 | 199.978 |
| 4 | 99.989 | 99.989 | -0.000 | 199.978 | 238.179 | 238.179 |
| 5 | 99.989 | 99.989 | -0.000 | 199.978 | 249.972 | 249.972 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 549.938292 | 0.000000 | 49.994390 | 0.000000 | 149.983170 | 844.739777 | 231.371834 | 14,703.120000 | none |
| 12 | 449.949511 | 0.000000 | 0.000000 | 49.994390 | 149.983170 | 0.000000 | 1,088.855587 | 8,726.630000 | none |
| 104 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 199.977561 | 0.000000 | 0.000000 | 1,652.867006 | none |
| 105 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 199.977561 | 0.000000 | 0.000000 | 681.739224 | none |
| 106 | 374.957926 | 124.985975 | 0.000000 | 0.000000 | 199.977561 | 0.000000 | 27.201136 | -0.000000 | none |
| 107 | 401.978091 | 94.210522 | 0.000000 | 3.755288 | 196.222273 | 0.000000 | 694.115502 | -0.000000 | none |
| 108 | 328.718824 | 124.985975 | 0.000000 | 46.239102 | 149.983170 | 0.000000 | 1,023.110544 | -0.000000 | none |
| 109 | 325.265996 | 124.683515 | 0.000000 | 49.994390 | 99.988780 | 0.000000 | 1,156.859170 | -0.000000 | none |
| 110 | 356.210030 | 93.739482 | 0.000000 | 49.994390 | 49.994390 | 0.000000 | 1,050.601750 | 0.000000 | none |
| 111 | 356.210030 | 93.739482 | 0.000000 | 49.994390 | -0.000000 | 0.000000 | 648.347440 | -0.000000 | none |
| 112 | 374.957926 | 124.985975 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 27.201136 | -0.000000 | none |
| 113 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 681.739224 | none |
| 114 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,652.867006 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p50/nine_b150_ptdf_5/attempt-02/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p50/nine_b150_ptdf_5/attempt-02/execution.json>)

## Personal notes

<!-- USER_NOTES -->
