# 500 MW at bus 6141, S1 generator 0 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,074.349365 | 17.638395 | 30.763287 | 0.554892 | 0.000000 | 0.000000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 92,370.149 | 92,370.149 | 0.000 | 1,893.814 | 1,976.584 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 322.896 | 322.896 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 5 | 100.000 | 100.000 | -0.000 | 200.000 | 250.000 | 250.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 16,598.274102 | none |
| 4 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 15,656.125596 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 2,934.658775 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,963.530993 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,129.604657 | none |
| 107 | 487.770457 | 0.000000 | 0.000000 | 12.229543 | 187.770457 | 501.940000 | none |
| 108 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 137.770457 | 137.456147 | none |
| 109 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 87.770457 | 0.254694 | none |
| 110 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 37.770457 | 137.456147 | none |
| 111 | 462.229543 | 0.000000 | 0.000000 | 37.770457 | -0.000000 | 527.480913 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,129.604657 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,963.530993 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,934.658775 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p50/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p50/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
