# Ten-team evaluator controls

| Round | Unmodified evaluation score $B | Week reuse score delta USD | Hourly separation score delta USD | Week reuse admission difference MW | Hourly separation admission difference MW |
| --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 11.046738201 | 0.000000 | -0.048679 | 0.0000000000 | 0.0000000013 |
| week-2-submission-2 | 16.899418107 | 0.000000 | 0.000000 | 0.0000000000 | 0.0000000000 |
| week-3-submission-1 | 10.708733637 | 0.000000 | -0.047188 | 0.0000000000 | 0.0000000013 |
| week-3-submission-2 | 15.647739364 | 0.000000 | 0.000000 | 0.0000000000 | 0.0000000000 |

The controls use bus 1079 for our 500 MW site, grid only in S1 and C = G in S2. Each of the nine rivals requests 250 MW at each of buses 1079 and 2054 under the same generation schedule. All variants use the same rules and 120 representative periods.

Week reuse gave identical scores in this control. Splitting the independent hours of the no-storage allocation into separate solves changed scores by less than $0.05 in each round. Both retain the instructor objective and final joint dispatch. The comparison counts the original campaign once.

[Unmodified evaluator evidence](<../runs/ten-teams-500mw/campaigns/hosting_1_s2_cg/nine_s2_cg_hosting_2/attempt-01/cell.json>) · [Week reuse evidence](<../runs/ten-team-parity-control/week-reuse.json>) · [Hourly separation evidence](<../runs/ten-team-allocation-control/hour-separation.json>)

## Personal notes

<!-- USER_NOTES -->
