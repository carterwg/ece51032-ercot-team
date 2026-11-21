# 500 MW at bus 6141, S1 generator 100 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,104.235767 | 17.506879 | 30.763287 | 0.556298 | 0.000110 | 0.200000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,900.259 | 99.741 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,904.772373 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,933.644591 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,099.718255 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 459.824055 | b02136:lower |
| 108 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 57.569745 | b02136:lower |
| 109 | 400.259208 | 99.740792 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 57.569745 | b02136:lower |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 459.824055 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,099.718255 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,933.644591 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,904.772373 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p0/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p0/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
