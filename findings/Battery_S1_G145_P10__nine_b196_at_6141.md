# 500 MW at bus 6141, S1 generator 145 MW and battery 10 MW / 40 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,507.308818 | 17.381563 | 30.763287 | 0.576605 | 0.001119 | 0.290000 | 0.014000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,987.155 | 1,012.845 | 21,473.316 | 21,473.316 | 7.000 | 2,174.041 | 2,174.041 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 196 MW / 784 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,570.865 | 3,609,550.394 | 3,609,550.394 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 20.000 | 20.000 | 0.000 | 40.000 | 60.000 | 60.000 |
| 2 | 20.000 | 20.000 | 0.000 | 40.000 | 57.322 | 57.322 |
| 3 | 20.000 | 20.000 | 0.000 | 40.000 | 70.000 | 70.000 |
| 4 | 20.000 | 20.000 | 0.000 | 40.000 | 50.000 | 50.000 |
| 5 | 20.000 | 20.000 | 0.000 | 40.000 | 50.000 | 50.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 510.000000 | 0.000000 | 10.000000 | 0.000000 | 30.000000 | 1,047.243371 | 458.808583 | 14,616.879862 | b01921:upper, b02355:lower |
| 9 | 490.000000 | 0.000000 | 0.000000 | 10.000000 | 30.000000 | 0.000000 | 322.165784 | 9,644.852975 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 40.000000 | 0.000000 | 0.000000 | 1,501.699322 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 40.000000 | 0.000000 | 0.000000 | 530.571540 | b02136:lower |
| 106 | 355.000000 | 145.000000 | 0.000000 | 0.000000 | 40.000000 | 0.000000 | 346.413469 | 188.058673 | b02136:lower |
| 107 | 355.000000 | 145.000000 | 0.000000 | 0.000000 | 40.000000 | 0.000000 | 895.181226 | 96.932230 | b02136:lower |
| 108 | 345.000000 | 145.000000 | 0.000000 | 10.000000 | 30.000000 | 0.000000 | 1,230.151049 | 39.647743 | b02136:lower |
| 109 | 345.000000 | 145.000000 | 0.000000 | 10.000000 | 20.000000 | 0.000000 | 1,347.813843 | 20.109084 | b02136:lower |
| 110 | 347.154896 | 142.845104 | 0.000000 | 10.000000 | 10.000000 | 0.000000 | 1,232.305945 | 39.647743 | b02136:lower |
| 111 | 355.000000 | 145.000000 | 0.000000 | 0.000000 | 10.000000 | 0.000000 | 895.181226 | 96.932230 | b02136:lower |
| 112 | 345.000000 | 145.000000 | 0.000000 | 10.000000 | 0.000000 | 0.000000 | 336.413469 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 530.571540 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,501.699322 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g145_p10/nine_b196_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g145_p10/nine_b196_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
