# 500 MW at bus 6141, S1 generator 145 MW and battery 10 MW / 40 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.944943 | 4,045.588295 | 17.389808 | 30.759900 | 0.567048 | 0.000453 | 0.289968 | 0.013998 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,999.078 | 518.623 | 22,575.785 | 22,575.785 | 7.000 | 2,390.447 | 2,390.447 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 886.411 | 1,941,358.674 | 1,941,358.674 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 19.998 | 19.998 | -0.000 | 39.996 | 58.113 | 58.113 |
| 2 | 19.998 | 19.998 | -0.000 | 39.996 | 78.272 | 78.272 |
| 3 | 19.998 | 19.998 | -0.000 | 39.996 | 59.993 | 59.993 |
| 4 | 19.998 | 19.998 | -0.000 | 39.996 | 49.994 | 49.994 |
| 5 | 19.998 | 19.998 | -0.000 | 39.996 | 49.994 | 49.994 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 509.943842 | 0.000000 | 9.998899 | 0.000000 | 29.996697 | 512.533111 | 295.470279 | 15,449.973441 | b01921:upper, b02355:lower |
| 7 | 489.946044 | 0.000000 | 0.000000 | 9.998899 | 29.996697 | 0.000000 | 39.851099 | 11,837.534011 | b01921:upper |
| 104 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | 39.995595 | 0.000000 | 0.000000 | 1,963.419845 | none |
| 105 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | 39.995595 | 0.000000 | 0.000000 | 992.292063 | b02136:lower |
| 106 | 470.251996 | 29.692947 | 0.000000 | 0.000000 | 39.995595 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 439.113752 | 60.831191 | 0.000000 | 0.000000 | 39.995595 | 0.000000 | 517.629513 | 96.932230 | b02136:lower |
| 108 | 381.208019 | 108.738025 | 0.000000 | 9.998899 | 29.996697 | 0.000000 | 804.693603 | 39.647743 | b02136:lower |
| 109 | 345.262460 | 144.683584 | 0.000000 | 9.998899 | 19.997798 | 0.000000 | 886.410838 | 20.109084 | b02136:lower |
| 110 | 381.208019 | 108.738025 | 0.000000 | 9.998899 | 9.998899 | 0.000000 | 804.693603 | 39.647743 | b02136:lower |
| 111 | 453.700036 | 36.246008 | 0.000000 | 9.998899 | -0.000000 | 0.000000 | 532.215797 | 96.932230 | b02136:lower |
| 112 | 470.251996 | 29.692947 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 992.292063 | b02136:lower |
| 114 | 499.944943 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,963.419845 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g145_p10/nine_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g145_p10/nine_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
