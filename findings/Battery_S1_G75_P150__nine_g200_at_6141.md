# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.291506 | 30.763287 | 0.611255 | 0.000526 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,365.207 | 634.793 | 323,654.735 | 323,654.735 | 106.732 | 3,201.225 | 3,943.186 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | -0.000 | 600.000 | 689.754 | 689.754 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 907.105 | 907.105 |
| 3 | 300.000 | 300.000 | -0.000 | 600.000 | 993.984 | 993.984 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 945.297 | 945.297 |
| 5 | 300.000 | 300.000 | -0.000 | 600.000 | 752.173 | 752.173 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 347.891446 | 7,093.921157 | b01921:upper, b02090:lower, b02355:lower |
| 23 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 300.000000 | 14,170.369176 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 1,009.008140 | b02136:lower |
| 105 | 489.242536 | 10.757464 | 0.000000 | 0.000000 | 600.000000 | 306.816946 | b02136:lower |
| 106 | 460.635814 | 39.364186 | 0.000000 | 0.000000 | 600.000000 | 188.058673 | b02136:lower |
| 107 | 416.242616 | 60.379793 | 0.000000 | 23.377592 | 576.622408 | 96.932230 | b02136:lower |
| 108 | 280.886311 | 69.113689 | 0.000000 | 150.000000 | 426.622408 | 39.647743 | b02136:lower |
| 109 | 276.179799 | 73.820201 | 0.000000 | 150.000000 | 276.622408 | 20.109084 | b02136:lower |
| 110 | 280.886311 | 69.113689 | 0.000000 | 150.000000 | 126.622408 | 39.647743 | b02136:lower |
| 111 | 317.127592 | 56.250000 | 0.000000 | 126.622408 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 460.635814 | 39.364186 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 489.242536 | 10.757464 | 0.000000 | 0.000000 | -0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
