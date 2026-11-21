# 500 MW at bus 6141, S1 generator 135 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,512.830647 | 17.366637 | 30.763287 | 0.576609 | 0.001042 | 0.270000 | 0.049000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,057.160 | 942.840 | 73,847.664 | 73,847.664 | 7.000 | 2,372.499 | 2,174.041 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 196 MW / 784 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,573.030 | 3,657,111.492 | 3,657,111.492 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 70.000 | 70.000 | 0.000 | 140.000 | 210.000 | 210.000 |
| 2 | 70.000 | 70.000 | 0.000 | 140.000 | 187.603 | 187.603 |
| 3 | 70.000 | 70.000 | 0.000 | 140.000 | 245.000 | 245.000 |
| 4 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 5 | 70.000 | 70.000 | -0.000 | 140.000 | 164.786 | 164.786 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 535.000000 | 0.000000 | 35.000000 | 0.000000 | 105.000000 | 1,048.686409 | 490.773451 | 14,616.879862 | b01921:upper, b02355:lower |
| 9 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 105.000000 | 0.000000 | 302.687613 | 9,644.852975 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 0.000000 | 1,496.177493 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 0.000000 | 525.049711 | b02136:lower |
| 106 | 365.000000 | 135.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 361.935298 | 188.058673 | b02136:lower |
| 107 | 365.000000 | 135.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 910.703055 | 96.932230 | b02136:lower |
| 108 | 330.000000 | 135.000000 | 0.000000 | 35.000000 | 105.000000 | 0.000000 | 1,220.672878 | 39.647743 | b02136:lower |
| 109 | 330.000000 | 135.000000 | 0.000000 | 35.000000 | 70.000000 | 0.000000 | 1,338.335673 | 20.109084 | b02136:lower |
| 110 | 332.160318 | 132.839682 | 0.000000 | 35.000000 | 35.000000 | 0.000000 | 1,222.833196 | 39.647743 | b02136:lower |
| 111 | 342.373162 | 135.000000 | 0.000000 | 22.626838 | 12.373162 | 0.000000 | 888.076218 | 96.932230 | b02136:lower |
| 112 | 352.626838 | 135.000000 | 0.000000 | 12.373162 | -0.000000 | 0.000000 | 349.562136 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 525.049711 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,496.177493 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g135_p35/nine_b196_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g135_p35/nine_b196_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
