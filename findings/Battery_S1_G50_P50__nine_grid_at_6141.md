# 500 MW at bus 6141, S1 generator 50 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,104.235767 | 17.537333 | 30.763287 | 0.555900 | 0.000055 | 0.100000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,950.259 | 49.741 | 107,769.423 | 107,769.423 | 1.000 | 2,369.504 | 2,270.775 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 289.193 | 289.193 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 291.935 | 291.935 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 350.000 | 350.000 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 242.056 | 242.056 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 16,705.589145 | none |
| 8 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 11,736.888041 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 2,904.772373 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,933.644591 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,099.718255 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 459.824055 | b02136:lower |
| 108 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 107.569745 | b02136:lower |
| 109 | 400.259208 | 49.740792 | 0.000000 | 50.000000 | 100.000000 | 20.109084 | b02136:lower |
| 110 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 50.000000 | 107.569745 | b02136:lower |
| 111 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 0.000000 | 509.824055 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,099.718255 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,933.644591 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,904.772373 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p50/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p50/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
