# 500 MW at bus 6141, S1 generator 75 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,124.342848 | 17.522412 | 30.763287 | 0.555793 | 0.000083 | 0.150000 | 0.035000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,925.261 | 74.739 | 42,262.373 | 42,262.373 | 1.000 | 1,710.312 | 1,794.082 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 50.000 | 50.000 | 0.000 | 100.000 | 144.086 | 144.086 |
| 2 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |
| 3 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |
| 4 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |
| 5 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 525.000000 | 0.000000 | 25.000000 | 0.000000 | 75.000000 | 16,710.482064 | none |
| 10 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 9,886.726816 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 2,884.665292 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,913.537510 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,079.611174 | none |
| 107 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 464.716974 | none |
| 108 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 50.000000 | 62.462664 | none |
| 109 | 400.261211 | 74.738789 | 0.000000 | 25.000000 | 25.000000 | 0.000000 | none |
| 110 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 0.000000 | 62.462664 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 439.716974 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,079.611174 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,913.537510 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,884.665292 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p25/nine_grid_at_hosting_1/attempt-02/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p25/nine_grid_at_hosting_1/attempt-02/execution.json>)

| Earlier attempt | Evidence |
| --- | --- |
| timeout after 360s | [Evaluation log](<../runs/battery-s1-500mw/sweep/g75_p25/nine_grid_at_hosting_1/attempt-01/evaluation.log>) |

## Personal notes

<!-- USER_NOTES -->
