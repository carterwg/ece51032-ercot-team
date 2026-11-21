# 500 MW at bus 6141, S1 generator 75 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,104.235767 | 17.522119 | 30.763287 | 0.556085 | 0.000083 | 0.150000 | 0.035000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,925.259 | 74.741 | 54,675.137 | 54,675.137 | 1.000 | 2,187.005 | 2,187.005 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 50.000 | 50.000 | 0.000 | 100.000 | 150.000 | 150.000 |
| 2 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |
| 3 | 50.000 | 50.000 | 0.000 | 100.000 | 150.000 | 150.000 |
| 4 | 50.000 | 50.000 | 0.000 | 100.000 | 175.000 | 175.000 |
| 5 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 525.000000 | 0.000000 | 25.000000 | 0.000000 | 75.000000 | 16,730.589145 | none |
| 4 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 15,601.239194 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 2,904.772373 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,933.644591 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,099.718255 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 459.824055 | b02136:lower |
| 108 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 82.569745 | b02136:lower |
| 109 | 400.259208 | 74.740792 | 0.000000 | 25.000000 | 50.000000 | 20.109084 | b02136:lower |
| 110 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 25.000000 | 82.569745 | b02136:lower |
| 111 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 0.000000 | 484.824055 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,099.718255 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,933.644591 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,904.772373 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p25/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p25/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
