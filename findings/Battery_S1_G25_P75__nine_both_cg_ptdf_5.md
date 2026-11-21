# 500 MW at bus 6141, S1 generator 25 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.534798 | 30.763287 | 0.573463 | 0.000026 | 0.050000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,957.583 | 42.417 | 148,921.656 | 148,921.656 | 6.000 | 2,104.233 | 2,270.775 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 450.000 | 450.000 |
| 3 | 150.000 | 150.000 | -0.000 | 300.000 | 450.000 | 450.000 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 422.497 | 422.497 |
| 5 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 280.496533 | 14,784.824912 | none |
| 11 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 7,421.175489 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 0.000000 | none |
| 107 | 418.750000 | 6.250000 | 0.000000 | 75.000000 | 225.000000 | 0.000000 | none |
| 108 | 413.832581 | 11.167419 | 0.000000 | 75.000000 | 150.000000 | 0.000000 | none |
| 109 | 418.750000 | 6.250000 | 0.000000 | 75.000000 | 75.000000 | -0.000000 | none |
| 110 | 418.750000 | 6.250000 | 0.000000 | 75.000000 | 0.000000 | 0.000000 | none |
| 111 | 493.750000 | 6.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 493.750000 | 6.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g25_p75/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g25_p75/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
