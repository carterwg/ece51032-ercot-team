# 500 MW at bus 6141, S1 generator 0 MW and battery 195 MW / 780 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.152164 | 4,999.152164 | 17.351995 | 30.711123 | 0.607787 | 0.000000 | 0.000000 | 0.272537 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,372,572.959 | 0.000 | 405,416.993 | 405,416.993 | 0.000 | 3,481.458 | 4,126.685 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 389.339 | 389.339 | 0.000 | 778.677 | 872.497 | 872.497 |
| 2 | 389.339 | 389.339 | 0.000 | 778.677 | 1,125.175 | 1,125.175 |
| 3 | 389.339 | 389.339 | 0.000 | 778.677 | 1,214.765 | 1,214.765 |
| 4 | 389.339 | 389.339 | 0.000 | 778.677 | 1,213.237 | 1,213.237 |
| 5 | 389.339 | 389.339 | -0.000 | 778.677 | 997.993 | 997.993 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 304.482820 | 0.000000 | 0.000000 | 194.669344 | 482.747314 | 7,139.438337 | b01921:upper, b02090:lower, b02355:lower |
| 45 | 693.821508 | 0.000000 | 194.669344 | 0.000000 | 336.536520 | 15,827.381160 | b01921:upper, b02355:lower |
| 104 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | 778.677376 | 1,009.855976 | b02136:lower |
| 105 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | 778.677376 | 306.816946 | b02136:lower |
| 106 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | 778.677376 | 188.058673 | b02136:lower |
| 107 | 317.127592 | 0.000000 | 0.000000 | 182.024573 | 596.652804 | 96.932230 | b02136:lower |
| 108 | 304.482820 | 0.000000 | 0.000000 | 194.669344 | 401.983460 | 39.647743 | b02136:lower |
| 109 | 304.482820 | 0.000000 | 0.000000 | 194.669344 | 207.314116 | 20.109084 | b02136:lower |
| 110 | 422.157769 | 0.000000 | 0.000000 | 76.994395 | 130.319720 | 39.647743 | b02136:lower |
| 111 | 368.832444 | 0.000000 | 0.000000 | 130.319720 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 306.816946 | b02136:lower |
| 114 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,009.855976 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p195/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p195/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
