# 500 MW at bus 6141, S1 generator 0 MW and battery 200 MW / 800 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,391.904919 | 17.422762 | 30.763287 | 0.560525 | 0.000000 | 0.000000 | 0.280000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 336,336.194 | 336,336.194 | 0.000 | 1,909.767 | 1,922.729 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |
| 2 | 400.000 | 400.000 | 0.000 | 800.000 | 1,078.580 | 1,078.580 |
| 3 | 400.000 | 400.000 | 0.000 | 800.000 | 1,000.000 | 1,000.000 |
| 4 | 400.000 | 400.000 | -0.000 | 800.000 | 800.000 | 800.000 |
| 5 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 700.000000 | 0.000000 | 200.000000 | 0.000000 | 600.000000 | 15,267.919993 | none |
| 12 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 531.090933 | 7,752.016238 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 1,617.103221 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 645.975439 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | -0.000000 | none |
| 107 | 368.923638 | 0.000000 | 0.000000 | 131.076362 | 668.923638 | -0.000000 | none |
| 108 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 468.923638 | -0.000000 | none |
| 109 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 268.923638 | -0.000000 | none |
| 110 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 68.923638 | 0.000000 | none |
| 111 | 431.076362 | 0.000000 | 0.000000 | 68.923638 | 0.000000 | -0.000000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 645.975439 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,617.103221 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p200/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p200/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
