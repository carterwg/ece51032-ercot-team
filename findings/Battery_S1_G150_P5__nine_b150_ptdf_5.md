# 500 MW at bus 6141, S1 generator 150 MW and battery 5 MW / 20 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.919707 | 4,327.572565 | 17.390598 | 30.758347 | 0.562070 | 0.000735 | 0.299952 | 0.006999 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,501.048 | 795.585 | 8,290.956 | 8,290.956 | 7.000 | 1,658.458 | 1,658.458 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,148.296 | 1,945,607.007 | 1,945,607.007 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 9.998 | 9.998 | -0.000 | 19.997 | 19.997 | 19.997 |
| 2 | 9.998 | 9.998 | -0.000 | 19.997 | 24.996 | 24.996 |
| 3 | 9.998 | 9.998 | -0.000 | 19.997 | 19.997 | 19.997 |
| 4 | 9.998 | 9.998 | -0.000 | 19.997 | 24.996 | 24.996 |
| 5 | 9.998 | 9.998 | -0.000 | 19.997 | 24.996 | 24.996 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 504.918904 | 0.000000 | 4.999197 | 0.000000 | 14.997591 | 916.590876 | 229.659171 | 14,703.120000 | none |
| 12 | 494.920510 | 0.000000 | 0.000000 | 4.999197 | 14.997591 | 0.000000 | 1,105.282211 | 8,726.630000 | none |
| 104 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | 19.996788 | 0.000000 | 0.000000 | 1,681.435575 | none |
| 105 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | 19.996788 | 0.000000 | 0.000000 | 710.307793 | none |
| 106 | 387.437773 | 112.481934 | 0.000000 | 0.000000 | 19.996788 | 0.000000 | 11.136609 | 0.000000 | none |
| 107 | 387.437773 | 112.481934 | 0.000000 | 0.000000 | 19.996788 | 0.000000 | 651.030809 | -0.000000 | none |
| 108 | 382.438576 | 112.481934 | 0.000000 | 4.999197 | 14.997591 | 0.000000 | 1,048.285922 | 0.000000 | none |
| 109 | 345.247058 | 149.673452 | 0.000000 | 4.999197 | 9.998394 | 0.000000 | 1,148.295857 | -0.000000 | none |
| 110 | 382.438576 | 112.481934 | 0.000000 | 4.999197 | 4.999197 | 0.000000 | 1,048.285922 | -0.000000 | none |
| 111 | 411.418664 | 83.501846 | 0.000000 | 4.999197 | -0.000000 | 0.000000 | 675.011700 | 0.000000 | none |
| 112 | 387.437773 | 112.481934 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 11.136609 | 0.000000 | none |
| 113 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 710.307793 | none |
| 114 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,681.435575 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p5/nine_b150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p5/nine_b150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
