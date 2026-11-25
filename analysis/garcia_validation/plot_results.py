"""Render full-horizon official S1 results as a standalone comparison figure."""
import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'garcia-validation-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from run_validation import CASES,CANDIDATES

HERE=Path(__file__).resolve().parent


def main():
    summary=json.loads((HERE/'summary.json').read_text())
    results={(r['case'],r['candidate']):r for r in summary['results']}
    candidates=list(CANDIDATES)
    cases=sorted({r['case'] for r in summary['results']}|{p[0] for p in summary['missing_pairs']})
    labels=['G0\n2054','G100\n2054','G150\n2054','G225\n2054',
            'G225\n6141','G200\n6141','B196\n6141','G97+B99\n6141','B35\n6141']
    case_labels=[]
    for case in cases:
        f=CASES[case]
        assert f['rival_count']==9
        place='diverse*' if 'diverse' in case else 'at '+f['rival_bus_assignment'][0]
        equipment=f"G{f['generator_mw']}"+(f"/B{f['battery_mw']}" if f['battery_mw'] else '')
        if f['connection_mw']!=500:equipment=f"C{f['connection_mw']}/"+equipment
        case_labels.append(f'9 rivals · {equipment} {place}')
    fig,axes=plt.subplots(1,2,figsize=(19,8.8),layout='constrained')
    fig.suptitle('Garcia candidates and our plans — ten teams total',fontsize=19,fontweight='bold')
    for ax,key,title,scale,limits in zip(axes,('our_admitted_mw','week2_s1_score_usd'),
        ('Firm S1 admission (MW)','Week 1/2 S1 score ($B)'),(1,1e9),((0,500),(0,19))):
        values=np.full((len(cases),len(candidates)),np.nan)
        for i,case in enumerate(cases):
            for j,candidate in enumerate(candidates):
                r=results.get((case,candidate))
                if r:values[i,j]=r[key]/scale
        cmap=plt.get_cmap('viridis').copy();cmap.set_bad('#e5e7eb')
        ax.imshow(values,cmap=cmap,vmin=limits[0],vmax=limits[1],aspect='auto')
        ax.set_xticks(range(len(candidates)),labels,fontsize=9)
        ax.set_yticks(range(len(cases)),case_labels if ax==axes[0] else [],fontsize=10)
        ax.set_title(title,fontsize=13,pad=14)
        for i in range(len(cases)):
            for j in range(len(candidates)):
                v=values[i,j]
                if np.isnan(v):
                    label=('QP retry' if [cases[i],candidates[j]] in summary['resolved_with_alternate_qp_only'] else
                           'unresolved' if [cases[i],candidates[j]] in summary['missing_pairs'] else 'not tested')
                else:label=f'{v:.3f}'
                color='#111827' if np.isnan(v) or v>(limits[0]+limits[1])*.64 else 'white'
                ax.text(j,i,label,ha='center',va='center',fontsize=8,color=color)
        ax.set_xticks(np.arange(-.5,len(candidates),1),minor=True)
        ax.set_yticks(np.arange(-.5,len(cases),1),minor=True)
        ax.grid(which='minor',color='white',linewidth=1.5)
        ax.tick_params(which='minor',bottom=False,left=False)
    fig.supxlabel('All our requests are 500 MW. G = generator MW; B = four-hour battery MW.\n'
                  'Every field has exactly nine rivals. * Explicit reconstructed diverse placements. '
                  'QP retry results appear separately in the report. S1 is not a four-round campaign.',fontsize=10)
    fig.savefig(HERE/'comparison.png',dpi=170)
    fig.savefig(HERE/'comparison.svg')
    plt.close(fig)


if __name__=='__main__':
    main()
