# 500 MW at bus 6141, S1 generator 75 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 432.043086 | 4,320.430855 | 15.075007 | 26.582131 | 0.485447 | 0.000259 | 0.129613 | 0.090729 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,784,434.628 | 262.801 | 111,873.355 | 111,873.355 | 6.000 | 1,809.041 | 1,825.995 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 129.613 | 129.613 | 0.000 | 259.226 | 324.032 | 324.032 |
| 2 | 129.613 | 129.613 | 0.000 | 259.226 | 324.032 | 324.032 |
| 3 | 129.613 | 129.613 | 0.000 | 259.226 | 324.032 | 324.032 |
| 4 | 129.613 | 129.613 | 0.000 | 259.226 | 259.226 | 259.226 |
| 5 | 129.613 | 129.613 | 0.000 | 259.226 | 259.226 | 259.226 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 367.236623 | 0.000000 | 0.000000 | 64.806463 | 64.806463 | 15,466.999075 | none |
| 1 | 496.849548 | 0.000000 | 64.806463 | 0.000000 | 129.612926 | 15,474.587594 | none |
| 104 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 259.225851 | 1,688.577285 | none |
| 105 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 259.225851 | 717.449503 | none |
| 106 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 259.225851 | 0.000000 | none |
| 107 | 318.631776 | 48.604847 | 0.000000 | 64.806463 | 194.419388 | -0.000000 | none |
| 108 | 306.963264 | 60.273358 | 0.000000 | 64.806463 | 129.612926 | 0.000000 | none |
| 109 | 302.430160 | 64.806463 | 0.000000 | 64.806463 | 64.806463 | 0.000000 | none |
| 110 | 306.963264 | 60.273358 | 0.000000 | 64.806463 | 0.000000 | 0.000000 | none |
| 111 | 415.841470 | 16.201616 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 419.401560 | 12.641525 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 717.449503 | none |
| 114 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,688.577285 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p75/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p75/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
