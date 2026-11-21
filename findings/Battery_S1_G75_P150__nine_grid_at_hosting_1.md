# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,249.329496 | 17.348544 | 30.763287 | 0.554661 | 0.000082 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,925.275 | 74.725 | 219,000.864 | 219,000.864 | 1.000 | 1,645.496 | 1,643.499 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 3 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 5 | 300.000 | 300.000 | -0.000 | 600.000 | 600.864 | 600.864 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 16,460.495416 | none |
| 12 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 424.924375 | 8,844.591661 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 2,759.678644 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 1,788.550862 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 954.624526 | none |
| 107 | 383.350326 | 0.000000 | 0.000000 | 116.649674 | 483.350326 | 431.380000 | none |
| 108 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 333.350326 | 62.476016 | none |
| 109 | 275.274563 | 74.725437 | 0.000000 | 150.000000 | 183.350326 | -0.000000 | none |
| 110 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 33.350326 | 62.476016 | none |
| 111 | 466.649674 | 0.000000 | 0.000000 | 33.350326 | -0.000000 | 348.080653 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 954.624526 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,788.550862 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,759.678644 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
