# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 4,105.634342 | 17.862505 | 30.763287 | 0.000000 | 0.000782 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 15.409492 | 30.763287 | 0.000000 | 1.853795 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 4,105.634342 | 17.294607 | 30.763287 | 0.567898 | 0.000782 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 13.151865 | 30.763287 | 2.257628 | 1.853795 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,160.125 | 839.875 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-2-submission-2 | 2,112,330.714 | 2,267,669.286 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |
| week-3-submission-1 | 4,379,160.125 | 839.875 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-3-submission-2 | 2,112,330.714 | 2,267,669.286 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |

Four-round score **$63.718469B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 55 MW of S1 generation and 70 MW / 280 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-2-submission-1 | 9 | 504.789 | 1,091,546.705 | 1,091,546.705 |
| week-2-submission-2 | 0 | 0.000 | 0.000 | 0.000 |
| week-3-submission-1 | 9 | 504.789 | 1,091,546.705 | 1,091,546.705 |
| week-3-submission-2 | 0 | 0.000 | 0.000 | 0.000 |

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 106 | 469.917527 | 30.082473 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058671 | b02136:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 191.041917 | 96.932230 | b02136:lower |
| 108 | 339.533390 | 160.466610 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 504.788808 | 39.647743 | b02136:lower |
| 109 | 300.090248 | 199.909752 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 504.788808 | 20.109084 | b02136:lower |
| 110 | 339.533390 | 160.466610 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 504.788808 | 39.647743 | b02136:lower |
| 111 | 391.133391 | 108.866609 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 313.746891 | 96.932230 | b02136:lower |
| 112 | 469.917526 | 30.082474 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000002 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109084 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 106 | 469.917527 | 30.082473 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058671 | b02136:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 191.041917 | 96.932230 | b02136:lower |
| 108 | 339.533390 | 160.466610 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 504.788808 | 39.647743 | b02136:lower |
| 109 | 300.090248 | 199.909752 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 504.788808 | 20.109084 | b02136:lower |
| 110 | 339.533390 | 160.466610 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 504.788808 | 39.647743 | b02136:lower |
| 111 | 391.133391 | 108.866609 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 313.746891 | 96.932230 | b02136:lower |
| 112 | 469.917526 | 30.082474 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000002 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109084 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 62.542907 | 437.457093 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 113.633130 | 386.366870 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_01/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_01/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
