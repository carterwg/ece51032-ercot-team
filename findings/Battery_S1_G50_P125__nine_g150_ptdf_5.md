# 500 MW at bus 6141, S1 generator 50 MW and battery 125 MW / 500 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943901 | 4,356.141134 | 17.424886 | 30.759836 | 0.561183 | 0.000200 | 0.099989 | 0.174980 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,303.854 | 204.723 | 215,426.131 | 215,426.131 | 6.000 | 1,893.811 | 1,726.268 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 249.972 | 249.972 | 0.000 | 499.944 | 624.930 | 624.930 |
| 2 | 249.972 | 249.972 | -0.000 | 499.944 | 621.589 | 621.589 |
| 3 | 249.972 | 249.972 | -0.000 | 499.944 | 624.930 | 624.930 |
| 4 | 249.972 | 249.972 | -0.000 | 499.944 | 499.944 | 499.944 |
| 5 | 249.972 | 249.972 | -0.000 | 499.944 | 499.944 | 499.944 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 374.957926 | 0.000000 | 0.000000 | 124.985975 | 124.985975 | 15,491.468309 | none |
| 1 | 624.929877 | 0.000000 | 124.985975 | 0.000000 | 249.971951 | 15,378.697803 | none |
| 104 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 499.943901 | 1,652.867006 | none |
| 105 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 499.943901 | 681.739224 | none |
| 106 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 499.943901 | 0.000000 | none |
| 107 | 365.086387 | 37.495793 | 0.000000 | 97.361721 | 402.582180 | 0.000000 | none |
| 108 | 328.840254 | 46.117672 | 0.000000 | 124.985975 | 277.596205 | 0.000000 | none |
| 109 | 324.963536 | 49.994390 | 0.000000 | 124.985975 | 152.610229 | -0.000000 | none |
| 110 | 328.840254 | 46.117672 | 0.000000 | 124.985975 | 27.624254 | 0.000000 | none |
| 111 | 459.821050 | 12.498598 | 0.000000 | 27.624254 | -0.000000 | 0.000000 | none |
| 112 | 487.445304 | 12.498598 | 0.000000 | 0.000000 | -0.000000 | -0.000000 | none |
| 113 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 681.739224 | none |
| 114 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,652.867006 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p125/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p125/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
