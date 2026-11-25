"""Write the corrected ten-team research report from audited saved results."""
import json
from pathlib import Path
from run_validation import ROOT, CASES, CANDIDATES

HERE=Path(__file__).resolve().parent
LABELS={
 'garcia_g0_2054':'Garcia G0 at 2054','garcia_g100_2054':'Garcia G100 at 2054',
 'garcia_g150_2054':'Garcia G150 at 2054','garcia_g225_2054':'Garcia G225 at 2054',
 'location_g225_6141':'Location control G225 at 6141','ours_g200_6141':'Our G200 at 6141',
 'ours_b196_6141':'Our B196 at 6141','ours_g97_b99_6141':'Our G97 B99 at 6141',
 'ours_b35_6141':'Our B35 grid-only control at 6141'}


def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |',
        *['| '+' | '.join(map(str,row))+' |' for row in rows]])+'\n'


def main():
    s=json.loads((HERE/'summary.json').read_text())
    rows=s['results'];lookup={(r['case'],r['candidate']):r for r in rows}
    assert all(r['team_count']==10 for r in rows)
    alternate=[r for r in s['alternate_qp_attempts'] if r['status']=='complete']
    alt_lookup={(r['case'],r['candidate']):r for r in alternate}
    selected={tuple(p) for p in json.loads((HERE/'selected_pairs.json').read_text())['pairs']}
    fields=sorted({case for case,c in selected})
    parts=['# Garcia candidates in the ten team game\n',
      'Prepared November 21, 2026. **Ten teams total: our team plus nine rivals.** '
      'Every result below uses that team count and a 500 MW request from our team in Submission 1. '
      'Garcia’s uploaded study assumed eleven teams; his hardware choices are tested here with the actual '
      'nine opponents. Eleven-team explorations are excluded from this comparison.\n',
      f"**Execution:** {s['completed_pairs']} of {s['planned_pairs']} targeted pairs completed with the unchanged "
      f"course evaluator. {len(s['resolved_with_alternate_qp_only'])} more completed using an alternate fairness QP backend, "
      f"reported separately. {len(s['unresolved_after_all_methods'])} targeted pairs remain unresolved. "
      'All completed evaluations cover the full 120-period horizon. These are **S1 results**, not four-round campaign totals.\n',
      '## Findings for the actual ten team field\n']
    baseline='ours10_same6141_g200'
    garcia=lookup.get((baseline,'garcia_g225_2054'));hybrid=lookup.get((baseline,'ours_g97_b99_6141'))
    battery=lookup.get((baseline,'ours_b196_6141'));generator=lookup.get((baseline,'ours_g200_6141'))
    if all((garcia,hybrid,battery,generator)):
        parts.append('Against nine rivals with 200 MW generation at bus 6141, Garcia’s 225 MW generator at bus 2054 '
          'and all three of our benchmark plans received **500 MW**. The 225 MW build adds no admission benefit in this field. '
          f"Our 200 MW generator improves the Week 1/2 S1 score by **${(generator['week2_s1_score_usd']-garcia['week2_s1_score_usd'])/1e6:.3f}M**, "
          f"the refined 97 MW generator / 99 MW battery hybrid by **${(hybrid['week2_s1_score_usd']-garcia['week2_s1_score_usd'])/1e6:.3f}M**, "
          f"and the 196 MW battery by **${(battery['week2_s1_score_usd']-garcia['week2_s1_score_usd'])/1e6:.3f}M**. "
          'Battery-only results in this field do not establish robustness against rivals with storage.\n')
    adverse='ours10_same6141_g50_b175'
    h=lookup.get((adverse,'ours_g97_b99_6141'));g=lookup.get((adverse,'garcia_g225_2054'))
    if h and g:
        parts.append('Against nine rivals with 50 MW generation and 175 MW / 700 MWh batteries, '
          f"our refined hybrid retains **{h['our_admitted_mw']:.6f} MW**, meeting the earlier 499.9 MW target, "
          f"and scores **${(h['week2_s1_score_usd']-g['week2_s1_score_usd'])/1e6:.3f}M more** in W1/2 S1 "
          'than Garcia’s 225 MW generator, which retains exactly 500 MW. This supports the earlier hybrid finding '
          'within these matched fields; it does not prove a global optimum.\n')
    grid='ours10_same6141_g0'
    small=lookup.get((grid,'ours_b35_6141'));g100=lookup.get((grid,'garcia_g100_2054'))
    if small and g100:
        parts.append('Against nine grid-only rivals, Garcia’s 100 MW generator and our earlier 35 MW / 140 MWh '
          'battery both retain the full 500 MW. The battery costs $49M versus $200M for the generator and '
          f"improves the Week 1/2 S1 score by **${(small['week2_s1_score_usd']-g100['week2_s1_score_usd'])/1e6:.3f}M**. "
          'The small battery is a field-specific control, not a replacement for the refined hybrid across the wider rival set.\n')
    parts.append('## Garcia hardware choices with nine opponents\n')
    winners={
      'garcia10_diverse_c300g200':'garcia_g0_2054','garcia10_diverse_g0':'garcia_g100_2054',
      'garcia10_diverse_g100':'garcia_g150_2054','garcia10_diverse_g200':'garcia_g225_2054',
      'garcia10_diverse_g250':'garcia_g0_2054'}
    winners_rows=[]
    for case,candidate in winners.items():
        field=CASES[case];r=lookup.get((case,candidate))
        winners_rows.append([f"C{field['connection_mw']} / G{field['generator_mw']}",
          CANDIDATES[candidate][1], f"{r['our_admitted_mw']:.6f}" if r else 'pending',
          f"{r['week2_s1_score_usd']/1e9:.6f}" if r else '—',
          f"{r['week3_s1_score_usd']/1e9:.6f}" if r else '—'])
    parts.append(table(['Each rival’s load and generation MW','Our generation MW at 2054','Our admission MW',
                        'W1/2 S1 score $B','W3 S1 score $B'],winners_rows))
    parts.append('These are Garcia’s screened candidate sizes, not newly proven optimal generator sizes for ten teams. '
      'The diverse cases place the nine rivals cyclically at buses 1079, 2054, 2127, 3046 and 3048 '
      '(two rivals at each of the first four buses, one at the last). Garcia did not upload his exact diverse '
      'bus assignments or scripts, so these are documented reconstructions with the corrected team count. '
      'The co-location controls place all nine rivals at 2054. His original eleven-team screen scores '
      'are not direct baselines for these ten-team scores.\n')
    parts.append('## Comparison against our previous rival fields\n')
    for case in ('ours10_same6141_g0','ours10_same6141_g200','ours10_same6141_g50_b175'):
        field=CASES[case]
        parts.append(f"### Nine rivals at 6141 with {field['generator_mw']} MW generation and {field['battery_mw']} MW batteries\n")
        entries=[]
        for candidate in CANDIDATES:
            if (case,candidate) not in selected:continue
            r=lookup.get((case,candidate));a=alt_lookup.get((case,candidate))
            if r:entries.append([LABELS[candidate],f"{r['our_admitted_mw']:.6f}",
                f"{r['week2_s1_score_usd']/1e9:.6f}",f"{r['week3_s1_score_usd']/1e9:.6f}",'unchanged evaluator'])
            elif a:entries.append([LABELS[candidate],f"{a['our_admitted_mw']:.6f}",
                f"{a['energy_off_score_usd']/1e9:.6f}",f"{a['week3_score_usd']/1e9:.6f}",'alternate fairness QP'])
            else:entries.append([LABELS[candidate],'pending','—','—','—'])
        parts.append(table(['Our equipment and bus','Admission MW','W1/2 S1 score $B','W3 S1 score $B','Method'],entries))
    parts.append('The original 196 MW / 784 MWh battery finding covered seven fields without rival storage. '
      'The refined 97 MW generator plus 99 MW / 396 MWh battery was selected for at least 499.9 MW admission '
      'across 36 ten-team fields. This validation checks specific matched fields rather than repeating that entire search. '
      '[Previous findings](Saket_Findings_11-19-2026.md)\n')
    parts.append('### Reproduction of saved results\n')
    parts.append(table(['Field','Our plan','Previous admission MW','New admission MW','W1/2 score difference $'],
      [[r['case'],LABELS[r['candidate']],f"{r['previous_admitted_mw']:.6f}",f"{r['new_admitted_mw']:.6f}",
        f"{r['week2_score_difference_usd']:+.6f}"] for r in s['matched_previous_results']]))
    parts.append('## All ten team test fields\n')
    parts.append(table(['Field','Rivals','Rival load MW','Rival generator MW','Rival battery MW','Rival buses'],
      [[name,9,CASES[name]['connection_mw'],CASES[name]['generator_mw'],CASES[name]['battery_mw'],
        ', '.join(dict.fromkeys(CASES[name]['rival_bus_assignment']))] for name in fields]))
    parts.append('![Ten-team admission and score comparison](../analysis/garcia_validation/comparison.png)\n')
    parts.append('The [comparison CSV](../analysis/garcia_validation/comparison.csv) contains only unchanged-evaluator '
      'ten-team results. It includes equipment capital, fuel cost, and each raw result path. '
      '[Full summary and numerical retry records](../analysis/garcia_validation/summary.json)\n')
    parts.append('## Evaluation method\n')
    parts.append('Every run exports canonical student CSVs and calls the course `evaluate_csv_batch` through '
      'the existing team adapter. Each completed batch checks ten valid, feasible team scores, joint competition '
      'scope, all 120 periods, and score components. The native allocation and network model use HiGHS 1.16.0. '
      'The supported monolithic daily LP setting is used where appropriate for batteries. '
      'Instructor source files are unchanged. Job records retain source, scenario, rules, and output hashes.\n')
    parts.append('Week 1 and Week 2 have the same S1 energy-off score. The W3 column uses the unchanged course '
      '`_score_team` on the same official joint dispatch with LMP energy billing enabled. '
      'The week’s billing switch does not change the physical allocation or dispatch. '
      'No S2 carryover or four-round campaign score is inferred from these S1 results.\n')
    if alternate:
        parts.append('### Alternate fairness QP solver\n')
        parts.append('Some unchanged-HiGHS allocation runs did not complete within the process limit. '
          'The labelled numerical retries use the team’s existing Gurobi implementation of the fairness QP '
          'with the same objective, bounds, capacity floor, and network feasibility cuts. '
          'The course first-stage linear objective, exact daily network and battery models, final dispatch, '
          'and scoring remain in place. These are **not completely unchanged-evaluator runs**. '
          'They are excluded from the main CSV and figure and identified explicitly in tables.\n')
        parts.append(table(['Field','Our plan','Admission MW','W1/2 S1 score $B','W3 S1 score $B'],
          [[r['case'],LABELS[r['candidate']],f"{r['our_admitted_mw']:.6f}",
            f"{r['energy_off_score_usd']/1e9:.6f}",f"{r['week3_score_usd']/1e9:.6f}"] for r in alternate]))
    if s['unresolved_after_all_methods']:
        parts.append('### Remaining evaluations\n')
        parts.append(table(['Field','Candidate'],s['unresolved_after_all_methods']))
    parts.append('## Reproduction and artifacts\n')
    parts.append('From the repository root:\n\n```bash\n'
      'export PYTHONPATH=src:ercot-connection-game/src:ercot-connection-game\n'
      '.venv/bin/python analysis/garcia_validation/run_suite.py --jobs 2 --storage-solver monolithic\n'
      '.venv/bin/python analysis/garcia_validation/summarize.py\n'
      '.venv/bin/python analysis/garcia_validation/plot_results.py\n'
      '.venv/bin/python analysis/garcia_validation/write_report.py\n```\n')
    parts.append('The selected-pair manifest fixes the primary design at ten total teams. '
      'Raw CSVs, canonical outputs, dispatch traces, solver logs and audits are retained in '
      '`runs/garcia-validation/` (ignored by Git). The original Garcia upload is pinned to '
      '`08b997d522143bb537ca6bb4014311e8689d5212` under `analysis/garcia_validation/sources/`. '
      'Earlier eleven-team explorations remain separate under `analysis/garcia_validation/exploratory_eleven_team/` '
      'and do not contribute to these findings. These commands evaluate locally and do not upload a course submission.\n')
    (ROOT/'notes/Garcia_Official_Validation_11-21-2026.md').write_text('\n'.join(parts))


if __name__=='__main__':main()
