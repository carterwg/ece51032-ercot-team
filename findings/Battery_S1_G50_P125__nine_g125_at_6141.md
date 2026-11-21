# 500 MW at bus 6141, S1 generator 50 MW and battery 125 MW / 500 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,072.305347 | 17.420978 | 30.763287 | 0.567114 | 0.000196 | 0.100000 | 0.175000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,798.994 | 201.006 | 264,635.589 | 264,635.589 | 7.000 | 3,231.140 | 3,300.962 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 250.000 | 250.000 | 0.000 | 500.000 | 531.559 | 531.559 |
| 2 | 250.000 | 250.000 | -0.000 | 500.000 | 715.018 | 715.018 |
| 3 | 250.000 | 250.000 | 0.000 | 500.000 | 801.964 | 801.964 |
| 4 | 250.000 | 250.000 | 0.000 | 500.000 | 837.129 | 837.129 |
| 5 | 250.000 | 250.000 | 0.000 | 500.000 | 606.498 | 606.498 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 375.000000 | 0.000000 | 0.000000 | 125.000000 | 345.209122 | 7,996.615810 | b01921:upper |
| 22 | 625.000000 | 0.000000 | 125.000000 | 0.000000 | 156.559315 | 14,483.169614 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 500.000000 | 1,936.702793 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 500.000000 | 965.575011 | b02136:lower |
| 106 | 497.009256 | 2.990744 | 0.000000 | 0.000000 | 500.000000 | 188.058673 | b02136:lower |
| 107 | 467.914699 | 32.085301 | 0.000000 | 0.000000 | 500.000000 | 96.932230 | b02136:lower |
| 108 | 331.252344 | 43.747656 | 0.000000 | 125.000000 | 375.000000 | 39.647743 | b02136:lower |
| 109 | 325.014101 | 49.985899 | 0.000000 | 125.000000 | 250.000000 | 20.109084 | b02136:lower |
| 110 | 331.252344 | 43.747656 | 0.000000 | 125.000000 | 125.000000 | 39.647743 | b02136:lower |
| 111 | 349.541947 | 25.458053 | 0.000000 | 125.000000 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 497.009256 | 2.990744 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 965.575011 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,936.702793 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p125/nine_g125_at_6141/attempt-02/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p125/nine_g125_at_6141/attempt-02/execution.json>)

| Earlier attempt | Evidence |
| --- | --- |
| timeout after 360s | [Evaluation log](<../runs/battery-s1-500mw/sweep/g50_p125/nine_g125_at_6141/attempt-01/evaluation.log>) |

## Personal notes

<!-- USER_NOTES -->
