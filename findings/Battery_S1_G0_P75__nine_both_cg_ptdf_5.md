# 500 MW at bus 6141, S1 generator 0 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.584782 | 30.763287 | 0.573505 | 0.000000 | 0.000000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 129,263.864 | 129,263.864 | 0.000 | 1,724.277 | 1,973.592 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 3 | 150.000 | 150.000 | 0.000 | 300.000 | 450.000 | 450.000 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 5 | 150.000 | 150.000 | 0.000 | 300.000 | 318.110 | 318.110 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 280.496533 | 14,784.824912 | none |
| 11 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 7,421.175489 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 0.000000 | none |
| 107 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 0.000000 | none |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 150.000000 | 0.000000 | none |
| 109 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 75.000000 | -0.000000 | none |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 0.000000 | 0.000000 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p75/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p75/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
