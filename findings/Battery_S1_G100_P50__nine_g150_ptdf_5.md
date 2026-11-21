# 500 MW at bus 6141, S1 generator 100 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 432.043086 | 4,320.430855 | 15.061811 | 26.582131 | 0.485594 | 0.000346 | 0.172817 | 0.060486 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,784,347.350 | 350.079 | 74,582.237 | 74,582.237 | 6.000 | 1,809.041 | 1,825.995 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 86.409 | 86.409 | 0.000 | 172.817 | 216.022 | 216.022 |
| 2 | 86.409 | 86.409 | 0.000 | 172.817 | 216.022 | 216.022 |
| 3 | 86.409 | 86.409 | -0.000 | 172.817 | 216.022 | 216.022 |
| 4 | 86.409 | 86.409 | 0.000 | 172.817 | 172.817 | 172.817 |
| 5 | 86.409 | 86.409 | 0.000 | 172.817 | 172.817 | 172.817 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 388.838777 | 0.000000 | 0.000000 | 43.204309 | 43.204309 | 15,445.396920 | none |
| 1 | 475.247394 | 0.000000 | 43.204309 | 0.000000 | 86.408617 | 15,496.189748 | none |
| 104 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 172.817234 | 1,688.577285 | none |
| 105 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 172.817234 | 717.449503 | none |
| 106 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 172.817234 | 0.000000 | none |
| 107 | 324.032314 | 64.806463 | 0.000000 | 43.204309 | 129.612926 | -0.000000 | none |
| 108 | 308.065911 | 80.772866 | 0.000000 | 43.204309 | 86.408617 | 0.000000 | none |
| 109 | 302.430160 | 86.408617 | 0.000000 | 43.204309 | 43.204309 | 0.000000 | none |
| 110 | 308.065911 | 80.772866 | 0.000000 | 43.204309 | 0.000000 | 0.000000 | none |
| 111 | 410.440931 | 21.602154 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 416.326595 | 15.716491 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 717.449503 | none |
| 114 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,688.577285 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p50/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p50/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
