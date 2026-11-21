# 500 MW at bus 6141, S1 generator 0 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 432.043086 | 4,320.430855 | 15.114681 | 26.582131 | 0.484915 | 0.000000 | 0.000000 | 0.181458 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,784,697.429 | 0.000 | 219,052.938 | 219,052.938 | 0.000 | 1,825.997 | 1,842.951 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 259.226 | 259.226 | 0.000 | 518.452 | 518.452 | 518.452 |
| 2 | 259.226 | 259.226 | 0.000 | 518.452 | 709.873 | 709.873 |
| 3 | 259.226 | 259.226 | 0.000 | 518.452 | 648.065 | 648.065 |
| 4 | 259.226 | 259.226 | 0.000 | 518.452 | 518.452 | 518.452 |
| 5 | 259.226 | 259.226 | 0.000 | 518.452 | 518.452 | 518.452 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 561.656011 | 0.000000 | 129.612926 | 0.000000 | 388.838777 | 15,409.781131 | none |
| 12 | 302.430160 | 0.000000 | 0.000000 | 129.612926 | 388.838777 | 7,753.103228 | b01854:lower |
| 104 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 518.451703 | 1,688.577285 | none |
| 105 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 518.451703 | 717.449503 | none |
| 106 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 518.451703 | 0.000000 | none |
| 107 | 317.256034 | 0.000000 | 0.000000 | 114.787051 | 403.664651 | 0.000000 | none |
| 108 | 302.430160 | 0.000000 | 0.000000 | 129.612926 | 274.051726 | -0.000000 | none |
| 109 | 302.430160 | 0.000000 | 0.000000 | 129.612926 | 144.438800 | 0.000000 | none |
| 110 | 302.430160 | 0.000000 | 0.000000 | 129.612926 | 14.825874 | 0.000000 | none |
| 111 | 417.217211 | 0.000000 | 0.000000 | 14.825874 | 0.000000 | 0.000000 | none |
| 112 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 113 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 717.449503 | none |
| 114 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,688.577285 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p150/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p150/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
