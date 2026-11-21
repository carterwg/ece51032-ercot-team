# 500 MW at bus 6141, S1 generator 25 MW and battery 175 MW / 700 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.358072 | 30.763287 | 0.610054 | 0.000161 | 0.050000 | 0.245000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,817.445 | 182.555 | 364,796.715 | 364,796.715 | 106.732 | 3,019.723 | 4,222.419 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 350.000 | 350.000 | -0.000 | 700.000 | 782.781 | 782.781 |
| 2 | 350.000 | 350.000 | 0.000 | 700.000 | 1,007.105 | 1,007.105 |
| 3 | 350.000 | 350.000 | -0.000 | 700.000 | 1,118.984 | 1,118.984 |
| 4 | 350.000 | 350.000 | 0.000 | 700.000 | 1,077.342 | 1,077.342 |
| 5 | 350.000 | 350.000 | 0.000 | 700.000 | 877.173 | 877.173 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 325.000000 | 0.000000 | 0.000000 | 175.000000 | 422.891446 | 7,118.921157 | b01921:upper, b02090:lower, b02355:lower |
| 23 | 675.000000 | 0.000000 | 175.000000 | 0.000000 | 350.000000 | 14,145.369176 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 700.000000 | 1,009.008140 | b02136:lower |
| 105 | 496.315937 | 3.684063 | 0.000000 | 0.000000 | 700.000000 | 306.816946 | b02136:lower |
| 106 | 486.519114 | 13.480886 | 0.000000 | 0.000000 | 700.000000 | 188.058673 | b02136:lower |
| 107 | 468.273164 | 20.849244 | 0.000000 | 10.877592 | 689.122408 | 96.932230 | b02136:lower |
| 108 | 301.673394 | 23.326606 | 0.000000 | 175.000000 | 514.122408 | 39.647743 | b02136:lower |
| 109 | 300.061575 | 24.938425 | 0.000000 | 175.000000 | 339.122408 | 20.109084 | b02136:lower |
| 110 | 301.673394 | 23.326606 | 0.000000 | 175.000000 | 164.122408 | 39.647743 | b02136:lower |
| 111 | 317.127592 | 18.750000 | 0.000000 | 164.122408 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 486.519114 | 13.480886 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 496.315937 | 3.684063 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g25_p175/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g25_p175/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
