# 500 MW at bus 6141, S1 generator 0 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.639481 | 30.763287 | 0.574806 | 0.000000 | 0.000000 | 0.049000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 60,349.685 | 60,349.685 | 0.000 | 1,724.277 | 1,973.592 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 70.000 | 70.000 | 0.000 | 140.000 | 140.000 | 140.000 |
| 2 | 70.000 | 70.000 | 0.000 | 140.000 | 140.000 | 140.000 |
| 3 | 70.000 | 70.000 | 0.000 | 140.000 | 210.000 | 210.000 |
| 4 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 5 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 535.000000 | 0.000000 | 35.000000 | 0.000000 | 120.496533 | 14,824.824912 | none |
| 11 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 105.000000 | 7,381.175489 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 0.000000 | none |
| 107 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 105.000000 | 0.000000 | none |
| 108 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 70.000000 | 0.000000 | none |
| 109 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 35.000000 | 0.000000 | none |
| 110 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 0.000000 | 0.000000 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p35/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p35/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
