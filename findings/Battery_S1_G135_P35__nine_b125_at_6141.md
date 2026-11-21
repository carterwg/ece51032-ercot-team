# 500 MW at bus 6141, S1 generator 135 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,065.639681 | 17.375982 | 30.763287 | 0.567830 | 0.000475 | 0.270000 | 0.049000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,461.018 | 538.982 | 77,036.619 | 77,036.619 | 7.000 | 2,303.688 | 2,303.688 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 891.410 | 1,937,504.651 | 1,937,504.651 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 2 | 70.000 | 70.000 | 0.000 | 140.000 | 245.000 | 245.000 |
| 3 | 70.000 | 70.000 | 0.000 | 140.000 | 208.544 | 208.544 |
| 4 | 70.000 | 70.000 | 0.000 | 140.000 | 209.689 | 209.689 |
| 5 | 70.000 | 70.000 | 0.000 | 140.000 | 189.072 | 189.072 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 535.000000 | 0.000000 | 35.000000 | 0.000000 | 105.000000 | 533.187047 | 297.136640 | 15,385.933378 | b01921:upper, b02355:lower |
| 9 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 105.000000 | 0.000000 | 111.493452 | 9,900.849780 | b01921:upper |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 0.000000 | 1,943.368459 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 0.000000 | 972.240677 | b02136:lower |
| 106 | 466.250000 | 33.750000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 15.994333 | 188.058673 | b02136:lower |
| 107 | 399.503091 | 100.496909 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | 498.015181 | 96.932230 | b02136:lower |
| 108 | 363.750000 | 101.250000 | 0.000000 | 35.000000 | 105.000000 | 0.000000 | 807.231913 | 39.647743 | b02136:lower |
| 109 | 330.265213 | 134.734787 | 0.000000 | 35.000000 | 70.000000 | 0.000000 | 891.409920 | 20.109084 | b02136:lower |
| 110 | 363.750000 | 101.250000 | 0.000000 | 35.000000 | 35.000000 | 0.000000 | 807.231913 | 39.647743 | b02136:lower |
| 111 | 431.250000 | 33.750000 | 0.000000 | 35.000000 | 0.000000 | 0.000000 | 529.762090 | 96.932230 | b02136:lower |
| 112 | 466.250000 | 33.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 15.994333 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 972.240677 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,943.368459 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g135_p35/nine_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g135_p35/nine_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
