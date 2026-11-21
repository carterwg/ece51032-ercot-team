# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 3,224.332082 | 17.862984 | 30.763287 | 0.000000 | 0.000303 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 17.166521 | 30.763287 | 0.000000 | 0.096766 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 3,224.332082 | 17.306127 | 30.763287 | 0.556856 | 0.000303 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 16.314402 | 30.763287 | 0.852120 | 0.096766 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,675.219 | 324.781 | 0.000 | 0.000 | 3.000 | 0.000 | 0.000 |
| week-2-submission-2 | 4,210,496.989 | 169,503.011 | 0.000 | 0.000 | 1,338.364 | 0.000 | 0.000 |
| week-3-submission-1 | 4,379,675.219 | 324.781 | 0.000 | 0.000 | 3.000 | 0.000 | 0.000 |
| week-3-submission-2 | 4,210,496.989 | 169,503.011 | 0.000 | 0.000 | 1,338.364 | 0.000 | 0.000 |

Four-round score **$68.650034B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,784.676058 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,813.548276 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 979.621940 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 339.727740 | none |
| 108 | 437.473430 | 62.526570 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 300.271977 | 199.728023 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 110 | 437.473430 | 62.526570 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 339.727740 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 979.621940 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,813.548276 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,784.676058 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 547.161210 | b02579:lower |
| 105 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 214.933596 | b02579:lower |
| 106 | 208.768622 | 291.231378 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 208.768622 | 291.231378 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 214.933596 | b02579:lower |
| 114 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 547.161210 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,784.676058 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,813.548276 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 979.621940 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 339.727740 | none |
| 108 | 437.473430 | 62.526570 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 300.271977 | 199.728023 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 110 | 437.473430 | 62.526570 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 339.727740 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 979.621940 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,813.548276 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,784.676058 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 547.161210 | b02579:lower |
| 105 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 214.933596 | b02579:lower |
| 106 | 208.768622 | 291.231378 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 208.768622 | 291.231378 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | b02579:lower |
| 113 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 214.933596 | b02579:lower |
| 114 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 547.161210 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
