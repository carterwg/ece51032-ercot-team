# 500 MW at bus 6141, S1 generator 150 MW and battery 5 MW / 20 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.944943 | 4,045.588296 | 17.386773 | 30.759900 | 0.567065 | 0.000472 | 0.299967 | 0.006999 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,979.080 | 538.621 | 11,023.567 | 11,023.567 | 7.000 | 2,288.726 | 2,288.726 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 886.411 | 1,949,493.495 | 1,949,493.495 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 9.999 | 9.999 | 0.000 | 19.998 | 24.997 | 24.997 |
| 2 | 9.999 | 9.999 | 0.000 | 19.998 | 34.996 | 34.996 |
| 3 | 9.999 | 9.999 | 0.000 | 19.998 | 29.997 | 29.997 |
| 4 | 9.999 | 9.999 | 0.000 | 19.998 | 29.997 | 29.997 |
| 5 | 9.999 | 9.999 | 0.000 | 19.998 | 24.997 | 24.997 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 504.944392 | 0.000000 | 4.999449 | 0.000000 | 14.998348 | 517.532561 | 295.470279 | 15,449.973441 | b01921:upper, b02355:lower |
| 12 | 494.945494 | 0.000000 | 0.000000 | 4.999449 | 14.998348 | 74.655280 | 680.952969 | 8,509.630000 | none |
| 104 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | 19.997798 | 0.000000 | 0.000000 | 1,963.419844 | none |
| 105 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | 19.997798 | 0.000000 | 0.000000 | 992.292062 | b02136:lower |
| 106 | 470.251996 | 29.692947 | 0.000000 | 0.000000 | 19.997798 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 432.864440 | 67.080503 | 0.000000 | 0.000000 | 19.997798 | 0.000000 | 511.380201 | 96.932230 | b02136:lower |
| 108 | 382.457881 | 112.487612 | 0.000000 | 4.999449 | 14.998348 | 0.000000 | 805.943465 | 39.647743 | b02136:lower |
| 109 | 345.262460 | 149.683033 | 0.000000 | 4.999449 | 9.998899 | 0.000000 | 886.410838 | 20.109084 | b02136:lower |
| 110 | 382.457881 | 112.487612 | 0.000000 | 4.999449 | 4.999449 | 0.000000 | 805.943465 | 39.647743 | b02136:lower |
| 111 | 457.449623 | 37.495871 | 0.000000 | 4.999449 | 0.000000 | 0.000000 | 535.965384 | 96.932230 | b02136:lower |
| 112 | 470.251996 | 29.692947 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 992.292062 | b02136:lower |
| 114 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,963.419844 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p5/nine_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p5/nine_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
