# 500 MW at bus 6141, S1 generator 75 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.468962 | 30.763287 | 0.574246 | 0.000079 | 0.150000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,872.543 | 127.457 | 100,828.437 | 100,828.437 | 6.000 | 2,021.460 | 2,270.775 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 300.000 | 300.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 300.000 | 300.000 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 297.497 | 297.497 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 180.496533 | 14,809.824912 | none |
| 11 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 7,396.175489 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | none |
| 107 | 431.250000 | 18.750000 | 0.000000 | 50.000000 | 150.000000 | 0.000000 | none |
| 108 | 416.292732 | 33.707268 | 0.000000 | 50.000000 | 100.000000 | -0.000000 | none |
| 109 | 431.250000 | 18.750000 | 0.000000 | 50.000000 | 50.000000 | -0.000000 | none |
| 110 | 431.250000 | 18.750000 | 0.000000 | 50.000000 | 0.000000 | 0.000000 | none |
| 111 | 481.250000 | 18.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 481.250000 | 18.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p50/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p50/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
