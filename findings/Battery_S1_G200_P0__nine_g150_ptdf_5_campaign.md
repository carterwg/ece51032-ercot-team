# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 4,391.904919 | 17.862428 | 30.763287 | 0.000000 | 0.000859 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 16.980354 | 30.763287 | 0.000000 | 0.282933 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 4,391.904919 | 17.299597 | 30.763287 | 0.562831 | 0.000859 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 16.087522 | 30.763287 | 0.892832 | 0.282933 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,072.979 | 927.021 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-2-submission-2 | 4,046,092.225 | 333,907.775 | 0.000 | 0.000 | 1,338.364 | 0.000 | 0.000 |
| week-3-submission-1 | 4,379,072.979 | 927.021 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-3-submission-2 | 4,046,092.225 | 333,907.775 | 0.000 | 0.000 | 1,338.364 | 0.000 | 0.000 |

Four-round score **$68.229902B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,617.103221 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 645.975439 | none |
| 106 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 | 336.489452 | 163.510548 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 | 336.489452 | 163.510548 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 645.975439 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,617.103221 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 85 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 104 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | b01841:lower |
| 105 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 114 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | b01841:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,617.103221 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 645.975439 | none |
| 106 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 | 336.489452 | 163.510548 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 | 336.489452 | 163.510548 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 645.975439 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,617.103221 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 85 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 104 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | b01841:lower |
| 105 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 114 | 125.000000 | 375.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | b01841:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
