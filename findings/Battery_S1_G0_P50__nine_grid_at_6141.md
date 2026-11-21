# 500 MW at bus 6141, S1 generator 0 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,054.242274 | 17.638175 | 30.763287 | 0.555112 | 0.000000 | 0.000000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 98,990.818 | 98,990.818 | 0.000 | 1,992.540 | 2,457.260 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 343.003 | 343.003 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 5 | 100.000 | 100.000 | -0.000 | 200.000 | 200.000 | 200.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 16,618.381193 | none |
| 4 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 15,676.232687 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 2,954.765866 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,983.638084 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,149.711748 | none |
| 107 | 467.916186 | 0.000000 | 0.000000 | 32.083814 | 167.916186 | 541.901362 | b02136:lower |
| 108 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 117.916186 | 157.563238 | b02136:lower |
| 109 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 67.916186 | 20.361785 | b02136:lower |
| 110 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 17.916186 | 157.563238 | b02136:lower |
| 111 | 482.083814 | 0.000000 | 0.000000 | 17.916186 | -0.000000 | 527.733735 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,149.711748 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,983.638084 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,954.765866 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p50/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p50/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
