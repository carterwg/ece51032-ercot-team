# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 4,860.927725 | 17.861689 | 30.763287 | 0.000000 | 0.001598 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 17.134953 | 30.763287 | 0.000000 | 0.128335 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 4,860.927725 | 17.295189 | 30.763287 | 0.566501 | 0.001598 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 16.140403 | 30.763287 | 0.994550 | 0.128335 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,504.112 | 1,495.888 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-2-submission-2 | 4,155,957.001 | 224,042.999 | 0.000 | 0.000 | 1,866.918 | 0.000 | 0.000 |
| week-3-submission-1 | 4,378,504.112 | 1,495.888 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-3-submission-2 | 4,155,957.001 | 224,042.999 | 0.000 | 0.000 | 1,866.918 | 0.000 | 0.000 |

Four-round score **$68.432234B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 1079, 2054, with 50 MW of S1 generation and 145 MW / 580 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-2-submission-1 | 18 | 1,264.669 | 2,250,067.689 | 2,250,067.689 |
| week-2-submission-2 | 0 | 0.000 | 0.000 | 0.000 |
| week-3-submission-1 | 18 | 1,264.669 | 2,250,067.689 | 2,250,067.689 |
| week-3-submission-2 | 0 | 0.000 | 0.000 | 0.000 |

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,148.080415 | b02579:lower |
| 105 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 405.135065 | b02579:lower |
| 106 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 204.305682 | 183.424751 | b02579:lower |
| 107 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 107.404182 | 768.179313 | -0.000000 | none |
| 108 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 68.027099 | 1,131.056540 | -0.000000 | none |
| 109 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,200.230894 | 0.000000 | none |
| 110 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 68.027099 | 1,131.056540 | -0.000000 | none |
| 111 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 33.765244 | 694.540375 | -0.000000 | none |
| 112 | 304.112252 | 195.887748 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 206.530444 | 181.537262 | b02579:lower |
| 113 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 405.135065 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,148.080415 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 554.189797 | b02579:lower |
| 105 | 0.662912 | 499.337088 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 404.472153 | b02579:lower |
| 106 | 0.000001 | 499.999999 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 183.424751 | b02579:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 0.000001 | 499.999999 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 181.537261 | b02579:lower |
| 113 | 0.662912 | 499.337088 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 404.472153 | b02579:lower |
| 114 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 554.189797 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,148.080415 | b02579:lower |
| 105 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 405.135065 | b02579:lower |
| 106 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 204.305682 | 183.424751 | b02579:lower |
| 107 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 107.404182 | 768.179313 | -0.000000 | none |
| 108 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 68.027099 | 1,131.056540 | -0.000000 | none |
| 109 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,200.230894 | 0.000000 | none |
| 110 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 68.027099 | 1,131.056540 | -0.000000 | none |
| 111 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 33.765244 | 694.540375 | -0.000000 | none |
| 112 | 304.112252 | 195.887748 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 206.530444 | 181.537262 | b02579:lower |
| 113 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 405.135065 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,148.080415 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 554.189797 | b02579:lower |
| 105 | 0.662912 | 499.337088 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 404.472153 | b02579:lower |
| 106 | 0.000001 | 499.999999 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 183.424751 | b02579:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 0.000001 | 499.999999 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 181.537261 | b02579:lower |
| 113 | 0.662912 | 499.337088 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 404.472153 | b02579:lower |
| 114 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 554.189797 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_07/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_07/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
