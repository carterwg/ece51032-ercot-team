# 500 MW at bus 6141, S1 generator 0 MW and battery 196 MW / 784 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.380142 | 30.763287 | 0.608745 | 0.000000 | 0.000000 | 0.274400 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 406,702.326 | 406,702.326 | 0.000 | 3,481.458 | 4,126.685 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 392.000 | 392.000 | 0.000 | 784.000 | 875.277 | 875.277 |
| 2 | 392.000 | 392.000 | -0.000 | 784.000 | 1,132.194 | 1,132.194 |
| 3 | 392.000 | 392.000 | -0.000 | 784.000 | 1,222.266 | 1,222.266 |
| 4 | 392.000 | 392.000 | 0.000 | 784.000 | 1,210.446 | 1,210.446 |
| 5 | 392.000 | 392.000 | 0.000 | 784.000 | 1,002.468 | 1,002.468 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 304.000000 | 0.000000 | 0.000000 | 196.000000 | 485.891446 | 7,139.921157 | b01921:upper, b02090:lower, b02355:lower |
| 45 | 696.000000 | 0.000000 | 196.000000 | 0.000000 | 337.019340 | 15,825.202668 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 784.000000 | 1,009.008140 | b02136:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 784.000000 | 306.816946 | b02136:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 784.000000 | 188.058673 | b02136:lower |
| 107 | 317.127592 | 0.000000 | 0.000000 | 182.872408 | 601.127592 | 96.932230 | b02136:lower |
| 108 | 304.000000 | 0.000000 | 0.000000 | 196.000000 | 405.127592 | 39.647743 | b02136:lower |
| 109 | 304.000000 | 0.000000 | 0.000000 | 196.000000 | 209.127592 | 20.109084 | b02136:lower |
| 110 | 422.157769 | 0.000000 | 0.000000 | 77.842231 | 131.285361 | 39.647743 | b02136:lower |
| 111 | 368.714639 | 0.000000 | 0.000000 | 131.285361 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p196/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p196/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
