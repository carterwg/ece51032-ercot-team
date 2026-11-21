# 500 MW at bus 6141, S1 generator 0 MW and battery 200 MW / 800 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.415252 | 30.763287 | 0.568035 | 0.000000 | 0.000000 | 0.280000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 337,850.316 | 337,850.316 | 0.000 | 1,987.551 | 2,271.775 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |
| 2 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |
| 3 | 400.000 | 400.000 | -0.000 | 800.000 | 1,117.786 | 1,117.786 |
| 4 | 400.000 | 400.000 | -0.000 | 800.000 | 1,000.000 | 1,000.000 |
| 5 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 700.000000 | 0.000000 | 200.000000 | 0.000000 | 600.000000 | 14,522.623467 | none |
| 12 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 468.331841 | 7,143.921157 | b01854:lower, b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 0.000000 | none |
| 107 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 600.000000 | 0.000000 | none |
| 108 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 400.000000 | 0.000000 | none |
| 109 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 200.000000 | 0.000000 | none |
| 110 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 0.000000 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p200/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p200/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
