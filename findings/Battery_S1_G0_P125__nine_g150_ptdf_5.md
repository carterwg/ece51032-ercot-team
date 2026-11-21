# 500 MW at bus 6141, S1 generator 0 MW and battery 125 MW / 500 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 0.006049 | 4,320.430423 | 0.000212 | 0.000372 | 0.000007 | 0.000000 | 0.000000 | 0.000002 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 52.986 | 0.000 | 2.635 | 2.635 | 0.000 | 1,742.225 | 1,742.225 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.003 | 0.003 | -0.000 | 0.006 | 0.006 | 0.006 |
| 2 | 0.003 | 0.003 | -0.000 | 0.006 | 0.009 | 0.009 |
| 3 | 0.003 | 0.003 | -0.000 | 0.006 | 0.008 | 0.008 |
| 4 | 0.003 | 0.003 | -0.000 | 0.006 | 0.006 | 0.006 |
| 5 | 0.003 | 0.003 | -0.000 | 0.006 | 0.006 | 0.006 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.007561 | 0.000000 | 0.001512 | 0.000000 | 0.004536 | 15,539.392977 | none |
| 11 | 0.004536 | 0.000000 | 0.000000 | 0.001512 | 0.004536 | 8,025.746578 | b01854:lower |
| 104 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | 0.006049 | 1,688.577717 | none |
| 105 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | 0.006049 | 717.449935 | none |
| 106 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | 0.006049 | 0.000000 | none |
| 107 | 0.004536 | 0.000000 | 0.000000 | 0.001512 | 0.004536 | -0.000000 | none |
| 108 | 0.004536 | 0.000000 | 0.000000 | 0.001512 | 0.003024 | -0.000000 | none |
| 109 | 0.004536 | 0.000000 | 0.000000 | 0.001512 | 0.001512 | -0.000000 | none |
| 110 | 0.004536 | 0.000000 | 0.000000 | 0.001512 | -0.000000 | -0.000000 | none |
| 111 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | none |
| 112 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | none |
| 113 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 717.449935 | none |
| 114 | 0.006049 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,688.577717 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p125/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p125/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
