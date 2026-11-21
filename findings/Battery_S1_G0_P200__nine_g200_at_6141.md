# 500 MW at bus 6141, S1 generator 0 MW and battery 200 MW / 800 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.374679 | 30.763287 | 0.608609 | 0.000000 | 0.000000 | 0.280000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 412,482.490 | 412,482.490 | 0.000 | 3,481.458 | 4,210.455 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 400.000 | 400.000 | -0.000 | 800.000 | 891.277 | 891.277 |
| 2 | 400.000 | 400.000 | 0.000 | 800.000 | 1,148.194 | 1,148.194 |
| 3 | 400.000 | 400.000 | -0.000 | 800.000 | 1,242.266 | 1,242.266 |
| 4 | 400.000 | 400.000 | 0.000 | 800.000 | 1,222.446 | 1,222.446 |
| 5 | 400.000 | 400.000 | 0.000 | 800.000 | 1,018.468 | 1,018.468 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 497.891446 | 7,143.921157 | b01921:upper, b02090:lower, b02355:lower |
| 45 | 700.000000 | 0.000000 | 200.000000 | 0.000000 | 341.019340 | 15,821.202668 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 1,009.008140 | b02136:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 306.816946 | b02136:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 188.058673 | b02136:lower |
| 107 | 317.127592 | 0.000000 | 0.000000 | 182.872408 | 617.127592 | 96.932230 | b02136:lower |
| 108 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 417.127592 | 39.647743 | b02136:lower |
| 109 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 217.127592 | 20.109084 | b02136:lower |
| 110 | 422.157769 | 0.000000 | 0.000000 | 77.842231 | 139.285361 | 39.647743 | b02136:lower |
| 111 | 360.714639 | 0.000000 | 0.000000 | 139.285361 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p200/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p200/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
