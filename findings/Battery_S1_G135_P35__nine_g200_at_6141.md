# 500 MW at bus 6141, S1 generator 135 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 461.314847 | 4,961.314847 | 15.956139 | 28.383122 | 0.598499 | 0.001294 | 0.249110 | 0.045209 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,039,316.592 | 1,801.470 | 98,131.876 | 98,131.876 | 302.195 | 3,480.455 | 3,395.688 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 64.584 | 64.584 | -0.000 | 129.168 | 240.047 | 240.047 |
| 2 | 64.584 | 64.584 | -0.000 | 129.168 | 285.464 | 285.464 |
| 3 | 64.584 | 64.584 | -0.000 | 129.168 | 258.336 | 258.336 |
| 4 | 64.584 | 64.584 | -0.000 | 129.168 | 286.275 | 286.275 |
| 5 | 64.584 | 64.584 | -0.000 | 129.168 | 193.752 | 193.752 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 493.606887 | 0.000000 | 32.292039 | 0.000000 | 96.876118 | 14,729.016580 | b01921:upper, b02355:lower |
| 5 | 429.022808 | 0.000000 | 0.000000 | 32.292039 | 96.876118 | 12,917.525804 | b01921:upper |
| 104 | 461.314847 | 0.000000 | 0.000000 | 0.000000 | 129.168157 | 1,047.693293 | b02136:lower |
| 105 | 446.413237 | 14.901611 | 0.000000 | 0.000000 | 129.168157 | 306.816946 | b02136:lower |
| 106 | 400.128374 | 61.186473 | 0.000000 | 0.000000 | 129.168157 | 188.058673 | b02136:lower |
| 107 | 364.612749 | 96.702098 | 0.000000 | 0.000000 | 129.168157 | 96.932230 | b02136:lower |
| 108 | 312.084560 | 116.938248 | 0.000000 | 32.292039 | 96.876118 | 39.647743 | b02136:lower |
| 109 | 304.469558 | 124.553250 | 0.000000 | 32.292039 | 64.584079 | 20.109085 | b02136:lower |
| 110 | 312.084560 | 116.938248 | 0.000000 | 32.292039 | 32.292039 | 39.647743 | b02136:lower |
| 111 | 334.410614 | 94.612194 | 0.000000 | 32.292039 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 400.128374 | 61.186473 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 446.413237 | 14.901611 | 0.000000 | 0.000000 | -0.000000 | 306.816946 | b02136:lower |
| 114 | 461.314847 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,047.693293 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g135_p35/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g135_p35/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
