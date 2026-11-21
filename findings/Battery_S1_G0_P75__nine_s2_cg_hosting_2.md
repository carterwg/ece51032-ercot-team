# 500 MW at bus 6141, S1 generator 0 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,099.345855 | 17.603877 | 30.763287 | 0.554410 | 0.000000 | 0.000000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 128,603.882 | 128,603.882 | 0.000 | 2,075.315 | 2,160.079 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 433.457 | 433.457 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 3 | 150.000 | 150.000 | 0.000 | 300.000 | 306.274 | 306.274 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 5 | 150.000 | 150.000 | -0.000 | 300.000 | 375.000 | 375.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 225.000000 | 16,548.277612 | none |
| 10 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 181.363380 | 9,961.723809 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 2,909.662285 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,938.534503 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,104.608167 | none |
| 107 | 462.773967 | 0.000000 | 0.000000 | 37.226033 | 262.773967 | 501.940000 | none |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 187.773967 | 137.459657 | none |
| 109 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 112.773967 | 0.258204 | none |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 37.773967 | 137.459657 | none |
| 111 | 462.226033 | 0.000000 | 0.000000 | 37.773967 | -0.000000 | 502.487934 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,104.608167 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,938.534503 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,909.662285 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p75/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p75/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
