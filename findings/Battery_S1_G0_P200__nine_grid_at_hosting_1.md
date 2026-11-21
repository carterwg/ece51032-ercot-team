# 500 MW at bus 6141, S1 generator 0 MW and battery 200 MW / 800 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,224.332082 | 17.429647 | 30.763287 | 0.553640 | 0.000000 | 0.000000 | 0.280000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 326,029.340 | 326,029.340 | 0.000 | 2,008.499 | 1,924.726 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 400.000 | 400.000 | 0.000 | 800.000 | 927.087 | 927.087 |
| 2 | 400.000 | 400.000 | 0.000 | 800.000 | 838.326 | 838.326 |
| 3 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |
| 4 | 400.000 | 400.000 | 0.000 | 800.000 | 1,000.000 | 1,000.000 |
| 5 | 400.000 | 400.000 | -0.000 | 800.000 | 814.884 | 814.884 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 700.000000 | 0.000000 | 200.000000 | 0.000000 | 600.000000 | 16,298.291385 | none |
| 12 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 475.913797 | 8,919.589075 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 2,784.676058 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 1,813.548276 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 979.621940 | none |
| 107 | 391.652260 | 0.000000 | 0.000000 | 108.347740 | 691.652260 | 448.075479 | none |
| 108 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 491.652260 | 137.473430 | none |
| 109 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 291.652260 | 0.271977 | none |
| 110 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 91.652260 | 137.473430 | none |
| 111 | 408.347740 | 0.000000 | 0.000000 | 91.652260 | -0.000000 | 431.380000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 979.621940 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,813.548276 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,784.676058 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p200/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p200/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
