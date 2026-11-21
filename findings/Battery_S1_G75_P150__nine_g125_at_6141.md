# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,138.963838 | 17.335668 | 30.763287 | 0.567314 | 0.000305 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,683.326 | 316.674 | 299,938.851 | 299,938.851 | 7.000 | 3,409.649 | 3,414.649 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 639.280 | 639.280 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 854.570 | 854.570 |
| 3 | 300.000 | 300.000 | 0.000 | 600.000 | 826.183 | 826.183 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 942.320 | 942.320 |
| 5 | 300.000 | 300.000 | -0.000 | 600.000 | 683.931 | 683.931 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 456.299574 | 15,570.861074 | b01921:upper, b02355:lower |
| 12 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 353.550631 | 7,954.957319 | b01921:upper |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 1,870.044302 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 898.916520 | b02136:lower |
| 106 | 490.626838 | 9.373162 | 0.000000 | 0.000000 | 600.000000 | 188.058673 | b02136:lower |
| 107 | 448.831499 | 51.168501 | 0.000000 | 0.000000 | 600.000000 | 96.932230 | b02136:lower |
| 108 | 283.982176 | 66.017824 | 0.000000 | 150.000000 | 450.000000 | 39.647743 | b02136:lower |
| 109 | 275.020723 | 74.979277 | 0.000000 | 150.000000 | 300.000000 | 20.109084 | b02136:lower |
| 110 | 283.982176 | 66.017824 | 0.000000 | 150.000000 | 150.000000 | 39.647743 | b02136:lower |
| 111 | 310.255824 | 39.744176 | 0.000000 | 150.000000 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 490.626838 | 9.373162 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 898.916520 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,870.044302 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
