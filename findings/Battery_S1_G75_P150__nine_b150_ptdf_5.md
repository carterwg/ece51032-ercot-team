# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,380.517817 | 17.340176 | 30.763287 | 0.562534 | 0.000577 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,477.239 | 522.761 | 242,469.476 | 242,469.476 | 7.000 | 1,937.693 | 1,825.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,164.155 | 1,961,282.523 | 1,961,282.523 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 711.192 | 711.192 |
| 3 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 4 | 300.000 | 300.000 | -0.000 | 600.000 | 725.146 | 725.146 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 877.550446 | 232.831069 | 14,547.386273 | none |
| 12 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 450.000000 | 0.000000 | 1,013.226660 | 8,726.630000 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,628.490323 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 657.362541 | none |
| 106 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 101.563795 | 0.000000 | none |
| 107 | 407.905330 | 75.000000 | 0.000000 | 17.094670 | 582.905330 | 0.000000 | 724.363326 | 0.000000 | none |
| 108 | 292.094670 | 75.000000 | 0.000000 | 132.905330 | 450.000000 | 0.000000 | 1,010.806975 | -0.000000 | none |
| 109 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 300.000000 | 7.371468 | 1,138.285226 | 0.000000 | none |
| 110 | 277.239431 | 72.760569 | 0.000000 | 150.000000 | 150.000000 | 23.953439 | 1,019.905175 | 0.000000 | none |
| 111 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 0.000000 | 0.000000 | 591.457995 | 0.000000 | none |
| 112 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 101.563795 | -0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 657.362541 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,628.490323 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_b150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_b150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
