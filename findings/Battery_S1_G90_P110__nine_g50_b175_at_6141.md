# 500 MW at bus 6141, S1 generator 90 MW and battery 110 MW / 440 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.889419 | 4,945.393976 | 17.340045 | 30.756483 | 0.584527 | 0.000750 | 0.179960 | 0.153966 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,329.698 | 701.612 | 309,533.462 | 309,533.462 | 9.000 | 3,006.759 | 3,105.485 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,555.927 | 3,829,735.480 | 3,829,735.480 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 219.951 | 219.951 | -0.000 | 439.903 | 769.830 | 769.830 |
| 2 | 219.951 | 219.951 | -0.000 | 439.903 | 1,079.246 | 1,079.246 |
| 3 | 219.951 | 219.951 | 219.951 | 439.903 | 879.805 | 879.805 |
| 4 | 219.951 | 219.951 | -0.000 | 439.903 | 654.624 | 654.624 |
| 5 | 219.951 | 219.951 | 0.000 | 439.903 | 614.783 | 614.783 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 609.865091 | 0.000000 | 109.975672 | 0.000000 | 329.927016 | 756.583749 | 518.642198 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 389.913747 | 0.000000 | 0.000000 | 109.975672 | 303.827017 | 827.802369 | 412.431124 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.889419 | 0.000000 | 0.000000 | 0.000000 | 439.902689 | 0.000000 | 0.000000 | 1,063.614164 | b02136:lower |
| 105 | 463.810125 | 36.079293 | 0.000000 | 0.000000 | 439.902689 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 409.909324 | 89.980095 | 0.000000 | 0.000000 | 439.902689 | 0.000000 | 394.968077 | 188.058673 | b02136:lower |
| 107 | 299.933651 | 89.980095 | 0.000000 | 109.975672 | 329.927016 | 0.000000 | 833.760161 | 96.932230 | b02136:lower |
| 108 | 299.933651 | 89.980095 | 0.000000 | 109.975672 | 219.951344 | 0.000000 | 1,178.729984 | 39.647743 | b02136:lower |
| 109 | 365.602141 | 89.980095 | 0.000000 | 44.307182 | 175.644162 | 0.000000 | 1,362.061268 | 20.109084 | b02136:lower |
| 110 | 344.240834 | 89.980095 | 0.000000 | 65.668490 | 109.975672 | 49.206611 | 1,272.243778 | 39.647743 | b02136:lower |
| 111 | 300.341272 | 89.572475 | 0.000000 | 109.975672 | 0.000000 | 172.880733 | 1,009.062380 | 96.932230 | b02136:lower |
| 112 | 409.909324 | 89.980095 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 394.968077 | 188.058673 | b02136:lower |
| 113 | 463.810125 | 36.079293 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.889419 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,063.614164 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g90_p110/nine_g50_b175_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g90_p110/nine_g50_b175_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
