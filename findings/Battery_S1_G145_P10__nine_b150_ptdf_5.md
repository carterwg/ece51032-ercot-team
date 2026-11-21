# 500 MW at bus 6141, S1 generator 145 MW and battery 10 MW / 40 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.919707 | 4,327.572565 | 17.393646 | 30.758347 | 0.562039 | 0.000718 | 0.289953 | 0.013998 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,521.045 | 775.588 | 16,581.912 | 16,581.912 | 7.000 | 1,658.458 | 1,658.458 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 0 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 1,148.296 | 1,943,182.739 | 1,943,182.739 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 19.997 | 19.997 | -0.000 | 39.994 | 39.994 | 39.994 |
| 2 | 19.997 | 19.997 | -0.000 | 39.994 | 49.992 | 49.992 |
| 3 | 19.997 | 19.997 | -0.000 | 39.994 | 39.994 | 39.994 |
| 4 | 19.997 | 19.997 | -0.000 | 39.994 | 49.992 | 49.992 |
| 5 | 19.997 | 19.997 | -0.000 | 39.994 | 49.992 | 49.992 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 509.918101 | 0.000000 | 9.998394 | 0.000000 | 29.995182 | 911.591679 | 229.659171 | 14,703.120000 | none |
| 12 | 489.921313 | 0.000000 | 0.000000 | 9.998394 | 29.995182 | 0.000000 | 1,100.283014 | 8,726.630000 | none |
| 104 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | 39.993577 | 0.000000 | 0.000000 | 1,681.435575 | none |
| 105 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | 39.993577 | 0.000000 | 0.000000 | 710.307793 | none |
| 106 | 391.187171 | 108.732536 | 0.000000 | 0.000000 | 39.993577 | 0.000000 | 14.886007 | 0.000000 | none |
| 107 | 391.187171 | 108.732536 | 0.000000 | 0.000000 | 39.993577 | 0.000000 | 654.780207 | -0.000000 | none |
| 108 | 381.188777 | 108.732536 | 0.000000 | 9.998394 | 29.995182 | 0.000000 | 1,047.036123 | 0.000000 | none |
| 109 | 345.247058 | 144.674255 | 0.000000 | 9.998394 | 19.996788 | 0.000000 | 1,148.295857 | 0.000000 | none |
| 110 | 381.188777 | 108.732536 | 0.000000 | 9.998394 | 9.998394 | 0.000000 | 1,047.036123 | -0.000000 | none |
| 111 | 402.670070 | 87.251243 | 0.000000 | 9.998394 | -0.000000 | 0.000000 | 666.263106 | 0.000000 | none |
| 112 | 391.187171 | 108.732536 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 14.886007 | 0.000000 | none |
| 113 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 710.307793 | none |
| 114 | 499.919707 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,681.435575 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g145_p10/nine_b150_ptdf_5/attempt-02/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g145_p10/nine_b150_ptdf_5/attempt-02/execution.json>)

## Personal notes

<!-- USER_NOTES -->
