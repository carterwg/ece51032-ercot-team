# 500 MW at bus 6141, S1 generator 75 MW and battery 125 MW / 500 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.324672 | 30.763287 | 0.613027 | 0.000588 | 0.150000 | 0.175000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,263.476 | 736.524 | 284,029.786 | 284,029.786 | 106.732 | 3,299.951 | 3,843.460 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 250.000 | 250.000 | -0.000 | 500.000 | 614.754 | 614.754 |
| 2 | 250.000 | 250.000 | 0.000 | 500.000 | 823.306 | 823.306 |
| 3 | 250.000 | 250.000 | -0.000 | 500.000 | 868.984 | 868.984 |
| 4 | 250.000 | 250.000 | 0.000 | 500.000 | 796.791 | 796.791 |
| 5 | 250.000 | 250.000 | -0.000 | 500.000 | 627.173 | 627.173 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 375.000000 | 0.000000 | 0.000000 | 125.000000 | 272.891446 | 7,068.921157 | b01921:upper, b02090:lower, b02355:lower |
| 23 | 625.000000 | 0.000000 | 125.000000 | 0.000000 | 250.000000 | 14,195.369176 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 500.000000 | 1,009.008140 | b02136:lower |
| 105 | 489.242536 | 10.757464 | 0.000000 | 0.000000 | 500.000000 | 306.816946 | b02136:lower |
| 106 | 460.635814 | 39.364186 | 0.000000 | 0.000000 | 500.000000 | 188.058673 | b02136:lower |
| 107 | 438.685104 | 61.314896 | 0.000000 | 0.000000 | 500.000000 | 96.932230 | b02136:lower |
| 108 | 304.886311 | 70.113689 | 0.000000 | 125.000000 | 375.000000 | 39.647743 | b02136:lower |
| 109 | 300.179799 | 74.820201 | 0.000000 | 125.000000 | 250.000000 | 20.109084 | b02136:lower |
| 110 | 304.886311 | 70.113689 | 0.000000 | 125.000000 | 125.000000 | 39.647743 | b02136:lower |
| 111 | 318.685104 | 56.314896 | 0.000000 | 125.000000 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 460.635814 | 39.364186 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 489.242536 | 10.757464 | 0.000000 | 0.000000 | -0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p125/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p125/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
