# 500 MW at bus 6141, S1 generator 150 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 432.043086 | 4,320.430855 | 15.035403 | 26.582131 | 0.485785 | 0.000641 | 0.259226 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,784,004.721 | 692.708 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,166.516 | 1,970,965.990 | 1,970,965.990 |

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,688.577285 | none |
| 105 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 717.449503 | none |
| 106 | 334.833391 | 97.209694 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 19.267139 | -0.000000 | none |
| 107 | 354.694131 | 77.348955 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 679.022078 | -0.000000 | none |
| 108 | 334.833391 | 97.209694 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,061.415649 | 0.000000 | none |
| 109 | 302.732611 | 129.310474 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,166.516331 | 0.000009 | none |
| 110 | 334.833391 | 97.209694 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,061.415649 | 0.000000 | none |
| 111 | 334.833391 | 97.209694 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 659.161339 | 0.000000 | none |
| 112 | 334.833391 | 97.209694 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 19.267139 | -0.000000 | none |
| 113 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 717.449503 | none |
| 114 | 432.043086 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,688.577285 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p0/nine_b150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p0/nine_b150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
