# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.319364 | 30.763287 | 0.583685 | 0.000238 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,700.794 | 299.206 | 349,640.270 | 349,640.270 | 9.000 | 3,004.762 | 3,074.573 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 170 MW of S1 generation and 120 MW / 480 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,080.000 | 2,487,960.830 | 2,487,960.830 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 1,116.689 | 1,116.689 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 927.884 | 927.884 |
| 3 | 300.000 | 300.000 | -0.000 | 600.000 | 1,083.166 | 1,083.166 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 606.088 | 606.088 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 503.311199 | 360.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 383.311199 | 600.000000 | 199.210451 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 487.432870 | 12.567130 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 454.013801 | 45.986199 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 450.000000 | 0.000000 | 981.622408 | 96.932230 | b02136:lower |
| 108 | 319.726999 | 30.273001 | 0.000000 | 150.000000 | 300.000000 | 0.000000 | 1,080.000000 | 39.647743 | b02136:lower |
| 109 | 350.372566 | 56.250000 | 0.000000 | 93.377434 | 206.622566 | 0.000000 | 698.377592 | 20.109084 | b02136:lower |
| 110 | 319.726999 | 30.273001 | 0.000000 | 150.000000 | 56.622566 | 0.000000 | 1,080.000000 | 39.647743 | b02136:lower |
| 111 | 396.823703 | 46.553731 | 0.000000 | 56.622566 | 0.000000 | 0.000000 | 480.000000 | 96.932230 | b02136:lower |
| 112 | 454.013801 | 45.986199 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 487.432870 | 12.567130 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_05/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_05/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
