# 500 MW at bus 6141, S1 generator 145 MW and battery 10 MW / 40 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.909596 | 4,897.460502 | 17.371262 | 30.757725 | 0.583622 | 0.001156 | 0.289948 | 0.013997 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,133.718 | 1,074.343 | 24,973.035 | 24,973.035 | 9.000 | 2,641.759 | 2,641.759 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,099.388 | 2,437,668.997 | 2,437,668.997 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 19.996 | 19.996 | 0.000 | 39.993 | 79.986 | 79.986 |
| 2 | 19.996 | 19.996 | 0.000 | 39.993 | 80.823 | 80.823 |
| 3 | 19.996 | 19.996 | 0.000 | 39.993 | 63.629 | 63.629 |
| 4 | 19.996 | 19.996 | 0.000 | 39.993 | 49.991 | 49.991 |
| 5 | 19.996 | 19.996 | 0.000 | 39.993 | 59.989 | 59.989 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 509.907788 | 0.000000 | 9.998192 | 0.000000 | 29.994576 | 732.925151 | 347.072645 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 489.911404 | 0.000000 | 0.000000 | 9.998192 | 29.994576 | 488.616767 | 125.289528 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.909596 | 0.000000 | 0.000000 | 0.000000 | 39.992768 | 0.000000 | 0.000000 | 1,111.547638 | b02136:lower |
| 105 | 469.928210 | 29.981386 | 0.000000 | 0.000000 | 39.992768 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 354.935813 | 144.973783 | 0.000000 | 0.000000 | 39.992768 | 0.000000 | 76.958734 | 188.058673 | b02136:lower |
| 107 | 344.937621 | 144.973783 | 0.000000 | 9.998192 | 29.994576 | 0.000000 | 615.728299 | 96.932230 | b02136:lower |
| 108 | 344.937621 | 144.973783 | 0.000000 | 9.998192 | 19.996384 | 0.000000 | 960.698122 | 39.647743 | b02136:lower |
| 109 | 344.937621 | 144.973783 | 0.000000 | 9.998192 | 9.998192 | 0.000000 | 1,078.360917 | 20.109084 | b02136:lower |
| 110 | 354.935813 | 144.973783 | 0.000000 | 0.000000 | 9.998192 | 0.000000 | 970.696314 | 39.647743 | b02136:lower |
| 111 | 345.373924 | 144.537480 | 0.000000 | 9.998192 | 0.000000 | 0.000000 | 618.149785 | 96.932230 | b02136:lower |
| 112 | 354.935813 | 144.973783 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 76.958734 | 188.058673 | b02136:lower |
| 113 | 469.928210 | 29.981386 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.909596 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,111.547638 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g145_p10/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g145_p10/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
