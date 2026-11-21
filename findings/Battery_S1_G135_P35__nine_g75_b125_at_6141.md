# 500 MW at bus 6141, S1 generator 135 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.929773 | 4,903.520501 | 17.356958 | 30.758966 | 0.583731 | 0.001077 | 0.269962 | 0.048993 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,381.831 | 1,002.980 | 89,167.170 | 89,167.170 | 9.000 | 2,642.759 | 2,739.490 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,100.898 | 2,456,513.750 | 2,456,513.750 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 69.990 | 69.990 | 0.000 | 139.980 | 279.961 | 279.961 |
| 2 | 69.990 | 69.990 | 0.000 | 139.980 | 290.236 | 290.236 |
| 3 | 69.990 | 69.990 | -0.000 | 139.980 | 235.105 | 235.105 |
| 4 | 69.990 | 69.990 | 0.000 | 139.980 | 174.975 | 174.975 |
| 5 | 69.990 | 69.990 | 0.000 | 139.980 | 209.971 | 209.971 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 534.924857 | 0.000000 | 34.995084 | 0.000000 | 104.985252 | 721.761508 | 366.965894 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 464.934689 | 0.000000 | 0.000000 | 34.995084 | 104.985252 | 504.586096 | 122.321965 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.929773 | 0.000000 | 0.000000 | 0.000000 | 139.980336 | 0.000000 | 0.000000 | 1,105.487639 | b02136:lower |
| 105 | 470.667847 | 29.261926 | 0.000000 | 0.000000 | 139.980336 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 364.948734 | 134.981039 | 0.000000 | 0.000000 | 139.980336 | 0.000000 | 92.105504 | 188.058673 | b02136:lower |
| 107 | 329.953650 | 134.981039 | 0.000000 | 34.995084 | 104.985252 | 0.000000 | 605.878177 | 96.932230 | b02136:lower |
| 108 | 329.953650 | 134.981039 | 0.000000 | 34.995084 | 69.990168 | 0.000000 | 950.848000 | 39.647743 | b02136:lower |
| 109 | 362.340538 | 134.981039 | 0.000000 | 2.608197 | 67.381972 | 0.000000 | 1,100.897682 | 20.109084 | b02136:lower |
| 110 | 332.561847 | 134.981039 | 0.000000 | 32.386887 | 34.995084 | 0.000000 | 953.456197 | 39.647743 | b02136:lower |
| 111 | 330.364520 | 134.570169 | 0.000000 | 34.995084 | 0.000000 | 0.000000 | 608.299663 | 96.932230 | b02136:lower |
| 112 | 364.948734 | 134.981039 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 92.105504 | 188.058673 | b02136:lower |
| 113 | 470.667847 | 29.261926 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.929773 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,105.487639 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g135_p35/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g135_p35/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
