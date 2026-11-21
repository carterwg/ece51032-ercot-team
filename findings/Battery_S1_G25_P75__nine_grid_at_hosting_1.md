# 500 MW at bus 6141, S1 generator 25 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,124.342848 | 17.552877 | 30.763287 | 0.555383 | 0.000027 | 0.050000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,975.261 | 24.739 | 123,589.497 | 123,589.497 | 1.000 | 1,711.312 | 1,893.808 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 394.086 | 394.086 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 3 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 5 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 225.000000 | 16,660.482064 | none |
| 10 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 9,936.726816 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 2,884.665292 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,913.537510 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,079.611174 | none |
| 107 | 437.776974 | 0.000000 | 0.000000 | 62.223026 | 237.776974 | 501.940000 | none |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 162.776974 | 112.462664 | none |
| 109 | 400.261211 | 24.738789 | 0.000000 | 75.000000 | 87.776974 | 0.000000 | none |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 12.776974 | 112.462664 | none |
| 111 | 487.223026 | 0.000000 | 0.000000 | 12.776974 | 0.000000 | 452.493947 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,079.611174 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,913.537510 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,884.665292 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g25_p75/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g25_p75/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
