# 500 MW at bus 6141, S1 generator 0 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943942 | 3,029.191722 | 17.671071 | 30.759838 | 0.555173 | 0.000000 | 0.000000 | 0.034996 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,508.929 | 0.000 | 52,142.424 | 52,142.424 | 0.000 | 2,092.266 | 2,091.266 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 49.994 | 49.994 | -0.000 | 99.989 | 174.980 | 174.980 |
| 2 | 49.994 | 49.994 | -0.000 | 99.989 | 148.646 | 148.646 |
| 3 | 49.994 | 49.994 | -0.000 | 99.989 | 124.986 | 124.986 |
| 4 | 49.994 | 49.994 | -0.000 | 99.989 | 124.986 | 124.986 |
| 5 | 49.994 | 49.994 | -0.000 | 99.989 | 99.989 | 99.989 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 474.946745 | 0.000000 | 0.000000 | 24.997197 | 24.997197 | 16,718.428942 | none |
| 1 | 524.941139 | 0.000000 | 24.997197 | 0.000000 | 49.994394 | 16,805.635993 | none |
| 104 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 99.988788 | 2,979.816418 | none |
| 105 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 99.988788 | 2,008.688636 | none |
| 106 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 99.988788 | 1,174.762300 | none |
| 107 | 481.980006 | 0.000000 | 0.000000 | 17.963935 | 82.024853 | 552.832035 | b02136:lower |
| 108 | 474.946745 | 0.000000 | 0.000000 | 24.997197 | 57.027656 | 157.610987 | b02136:lower |
| 109 | 474.946745 | 0.000000 | 0.000000 | 24.997197 | 32.030459 | 20.409534 | b02136:lower |
| 110 | 474.946745 | 0.000000 | 0.000000 | 24.997197 | 7.033262 | 157.610987 | b02136:lower |
| 111 | 492.910680 | 0.000000 | 0.000000 | 7.033262 | -0.000000 | 541.901362 | b02136:lower |
| 112 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,174.762300 | none |
| 113 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,008.688636 | none |
| 114 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,979.816418 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p25/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p25/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
