# 500 MW at bus 6141, S1 generator 50 MW and battery 100 MW / 400 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 432.043086 | 4,320.430855 | 15.088235 | 26.582131 | 0.485266 | 0.000172 | 0.086409 | 0.120972 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,784,522.042 | 175.387 | 149,164.473 | 149,164.473 | 6.000 | 1,809.041 | 1,825.995 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 172.817 | 172.817 | -0.000 | 345.634 | 432.043 | 432.043 |
| 2 | 172.817 | 172.817 | -0.000 | 345.634 | 432.043 | 432.043 |
| 3 | 172.817 | 172.817 | -0.000 | 345.634 | 432.043 | 432.043 |
| 4 | 172.817 | 172.817 | -0.000 | 345.634 | 345.634 | 345.634 |
| 5 | 172.817 | 172.817 | -0.000 | 345.634 | 345.634 | 345.634 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 345.634468 | 0.000000 | 0.000000 | 86.408617 | 86.408617 | 15,488.601229 | none |
| 1 | 518.451703 | 0.000000 | 86.408617 | 0.000000 | 172.817234 | 15,452.985440 | none |
| 104 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 345.634468 | 1,688.577285 | none |
| 105 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 345.634468 | 717.449503 | none |
| 106 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 345.634468 | -0.000000 | none |
| 107 | 313.231237 | 32.403231 | 0.000000 | 86.408617 | 259.225851 | -0.000000 | none |
| 108 | 305.688329 | 39.946140 | 0.000000 | 86.408617 | 172.817234 | -0.000000 | none |
| 109 | 302.430160 | 43.204309 | 0.000000 | 86.408617 | 86.408617 | -0.000000 | none |
| 110 | 305.688329 | 39.946140 | 0.000000 | 86.408617 | -0.000000 | 0.000000 | none |
| 111 | 421.242008 | 10.801077 | 0.000000 | 0.000000 | -0.000000 | -0.000000 | none |
| 112 | 422.956989 | 9.086096 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | none |
| 113 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 717.449503 | none |
| 114 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,688.577285 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p100/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p100/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
