# 500 MW at bus 6141, S1 generator 0 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,039.245063 | 17.659057 | 30.763287 | 0.555230 | 0.000000 | 0.000000 | 0.049000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 70,780.814 | 70,780.814 | 0.000 | 2,092.266 | 2,273.764 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 70.000 | 70.000 | 0.000 | 140.000 | 245.000 | 245.000 |
| 2 | 70.000 | 70.000 | 0.000 | 140.000 | 185.799 | 185.799 |
| 3 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 4 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 5 | 70.000 | 70.000 | -0.000 | 140.000 | 140.000 | 140.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 35.000000 | 16,718.378404 | none |
| 1 | 535.000000 | 0.000000 | 35.000000 | 0.000000 | 70.000000 | 16,785.579849 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 2,969.763077 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 1,998.635295 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 1,164.708959 | none |
| 107 | 482.086603 | 0.000000 | 0.000000 | 17.913397 | 122.086603 | 542.728157 | b02136:lower |
| 108 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 87.086603 | 157.560449 | b02136:lower |
| 109 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 52.086603 | 20.358996 | b02136:lower |
| 110 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 17.086603 | 157.560449 | b02136:lower |
| 111 | 482.913397 | 0.000000 | 0.000000 | 17.086603 | -0.000000 | 541.901362 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,164.708959 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,998.635295 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,969.763077 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p35/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p35/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
