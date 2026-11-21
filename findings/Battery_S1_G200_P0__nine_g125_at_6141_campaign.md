# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 4,105.634342 | 17.862485 | 30.763287 | 0.000000 | 0.000802 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 15.398494 | 30.763287 | 0.000000 | 1.864793 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 4,105.634342 | 17.292475 | 30.763287 | 0.570010 | 0.000802 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 13.126124 | 30.763287 | 2.272371 | 1.864793 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,178.400 | 821.600 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-2-submission-2 | 2,112,532.630 | 2,267,467.370 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |
| week-3-submission-1 | 4,379,178.400 | 821.600 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-3-submission-2 | 2,112,532.630 | 2,267,467.370 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |

Four-round score **$63.679578B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 106 | 483.704686 | 16.295314 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 384.056333 | 115.943667 | 0.000000 | 0.000000 | 0.000000 | 96.932230 | b02136:lower |
| 108 | 321.414762 | 178.585238 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 300.048886 | 199.951114 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 321.414762 | 178.585238 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 384.056333 | 115.943667 | 0.000000 | 0.000000 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 483.704686 | 16.295314 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 106 | 483.704686 | 16.295314 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 384.056333 | 115.943667 | 0.000000 | 0.000000 | 0.000000 | 96.932230 | b02136:lower |
| 108 | 321.414762 | 178.585238 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 300.048886 | 199.951114 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 321.414762 | 178.585238 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 384.056333 | 115.943667 | 0.000000 | 0.000000 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 483.704686 | 16.295314 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
