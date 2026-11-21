# 500 MW at bus 6141, S1 generator 0 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943901 | 3,049.298794 | 17.671512 | 30.759836 | 0.554730 | 0.000000 | 0.000000 | 0.034996 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,508.576 | 0.000 | 47,668.513 | 47,668.513 | 0.000 | 1,976.584 | 1,976.584 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 49.994 | 49.994 | -0.000 | 99.989 | 179.200 | 179.200 |
| 2 | 49.994 | 49.994 | -0.000 | 99.989 | 99.989 | 99.989 |
| 3 | 49.994 | 49.994 | -0.000 | 99.989 | 124.986 | 124.986 |
| 4 | 49.994 | 49.994 | -0.000 | 99.989 | 124.986 | 124.986 |
| 5 | 49.994 | 49.994 | -0.000 | 99.989 | 124.986 | 124.986 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 474.946706 | 0.000000 | 0.000000 | 24.997195 | 24.997195 | 16,698.321868 | none |
| 1 | 524.941096 | 0.000000 | 24.997195 | 0.000000 | 49.994390 | 16,785.528923 | none |
| 104 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 99.988780 | 2,959.709346 | b02579:lower |
| 105 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 99.988780 | 1,988.581564 | b02579:lower |
| 106 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 99.988780 | 1,154.655228 | none |
| 107 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 99.988780 | 514.761028 | none |
| 108 | 474.946706 | 0.000000 | 0.000000 | 24.997195 | 74.991585 | 137.503913 | none |
| 109 | 474.946706 | 0.000000 | 0.000000 | 24.997195 | 49.994390 | 0.302460 | none |
| 110 | 474.946706 | 0.000000 | 0.000000 | 24.997195 | 24.997195 | 137.503913 | none |
| 111 | 474.946706 | 0.000000 | 0.000000 | 24.997195 | -0.000000 | 539.758223 | none |
| 112 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,154.655228 | none |
| 113 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,988.581564 | b02579:lower |
| 114 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,959.709346 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p25/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p25/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
