# 500 MW at bus 6141, S1 generator 125 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 468.412923 | 4,968.412923 | 16.202679 | 28.819843 | 0.605909 | 0.001146 | 0.234206 | 0.065578 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,101,730.028 | 1,567.179 | 138,915.951 | 138,915.951 | 302.195 | 3,480.455 | 3,395.688 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 93.683 | 93.683 | 0.000 | 187.365 | 328.034 | 328.034 |
| 2 | 93.683 | 93.683 | 0.000 | 187.365 | 416.054 | 416.054 |
| 3 | 93.683 | 93.683 | 0.000 | 187.365 | 374.730 | 374.730 |
| 4 | 93.683 | 93.683 | 0.000 | 187.365 | 395.571 | 395.571 |
| 5 | 93.683 | 93.683 | 0.000 | 187.365 | 267.967 | 267.967 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 515.254215 | 0.000000 | 46.841292 | 0.000000 | 140.523877 | 14,707.369252 | b01921:upper, b02355:lower |
| 5 | 421.571631 | 0.000000 | 0.000000 | 46.841292 | 140.523877 | 12,924.976981 | b01921:upper |
| 104 | 468.412923 | 0.000000 | 0.000000 | 0.000000 | 187.365169 | 1,040.595217 | b02136:lower |
| 105 | 453.914802 | 14.498121 | 0.000000 | 0.000000 | 187.365169 | 306.816946 | b02136:lower |
| 106 | 410.229888 | 58.183036 | 0.000000 | 0.000000 | 187.365169 | 188.058673 | b02136:lower |
| 107 | 376.709274 | 91.703649 | 0.000000 | 0.000000 | 187.365169 | 96.932230 | b02136:lower |
| 108 | 311.657270 | 109.914361 | 0.000000 | 46.841292 | 140.523877 | 39.647743 | b02136:lower |
| 109 | 304.470023 | 117.101608 | 0.000000 | 46.841292 | 93.682585 | 20.109085 | b02136:lower |
| 110 | 311.657270 | 109.914361 | 0.000000 | 46.841292 | 46.841292 | 39.647743 | b02136:lower |
| 111 | 332.729208 | 88.842423 | 0.000000 | 46.841292 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 410.229888 | 58.183036 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 453.914802 | 14.498121 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 468.412923 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,040.595217 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p50/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p50/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
