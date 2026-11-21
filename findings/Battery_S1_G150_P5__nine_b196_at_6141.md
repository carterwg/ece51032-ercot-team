# 500 MW at bus 6141, S1 generator 150 MW and battery 5 MW / 20 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,510.069721 | 17.378549 | 30.763287 | 0.576581 | 0.001158 | 0.300000 | 0.007000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,952.158 | 1,047.842 | 11,279.082 | 11,279.082 | 7.000 | 2,355.542 | 2,255.816 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 196 MW / 784 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,571.947 | 3,665,745.960 | 3,665,745.960 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 10.000 | 10.000 | 0.000 | 20.000 | 25.000 | 25.000 |
| 2 | 10.000 | 10.000 | 0.000 | 20.000 | 30.000 | 30.000 |
| 3 | 10.000 | 10.000 | 0.000 | 20.000 | 45.000 | 45.000 |
| 4 | 10.000 | 10.000 | 0.000 | 20.000 | 25.000 | 25.000 |
| 5 | 10.000 | 10.000 | 0.000 | 20.000 | 25.000 | 25.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 505.000000 | 0.000000 | 5.000000 | 0.000000 | 15.000000 | 1,047.964887 | 457.291002 | 14,616.879861 | b01921:upper, b02355:lower |
| 9 | 495.000000 | 0.000000 | 0.000000 | 5.000000 | 15.000000 | 0.000000 | 329.926687 | 9,644.852975 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 20.000000 | 0.000000 | 0.000000 | 1,498.938419 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 20.000000 | 0.000000 | 0.000000 | 527.810637 | b02136:lower |
| 106 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 20.000000 | 0.000000 | 344.174372 | 188.058673 | b02136:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 20.000000 | 0.000000 | 892.942129 | 96.932230 | b02136:lower |
| 108 | 345.000000 | 150.000000 | 0.000000 | 5.000000 | 15.000000 | 0.000000 | 1,232.911952 | 39.647743 | b02136:lower |
| 109 | 345.000000 | 150.000000 | 0.000000 | 5.000000 | 10.000000 | 0.000000 | 1,350.574746 | 20.109084 | b02136:lower |
| 110 | 347.157670 | 147.842330 | 0.000000 | 5.000000 | 5.000000 | 0.000000 | 1,235.069622 | 39.647743 | b02136:lower |
| 111 | 345.000000 | 150.000000 | 0.000000 | 5.000000 | 0.000000 | 0.000000 | 887.942129 | 96.932230 | b02136:lower |
| 112 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 344.174372 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 527.810637 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,498.938419 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p5/nine_b196_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p5/nine_b196_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
