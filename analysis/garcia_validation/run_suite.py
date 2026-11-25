"""Run independent official evaluation jobs, preserving inputs, outputs and logs."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

from run_validation import ROOT, OUTPUT, CASES, CANDIDATES


def run_one(case, candidate, timeout, storage_solver='benders', allocation_solver='course'):
    suffix='' if allocation_solver=='course' else '-gurobi-allocation-qp'
    destination=OUTPUT/case/candidate/f'week-2-highs-{storage_solver}{suffix}'
    result_file=destination/'result.json'
    if result_file.exists():
        result=json.loads(result_file.read_text())
        return case,candidate,result['status'],result.get('our_admitted_mw'),result.get('elapsed_seconds')
    if destination.exists():
        return case,candidate,'already_started',None,None
    logs=OUTPUT/'logs';logs.mkdir(exist_ok=True,parents=True)
    log_path=logs/f'{case}__{candidate}{suffix}.log'
    command=[sys.executable,str(Path(__file__).with_name('run_validation.py')),
             '--case',case,'--candidate',candidate,'--workers','2',
             '--storage-solver',storage_solver,'--allocation-solver',allocation_solver]
    started=time.monotonic()
    with log_path.open('w') as log:
        process=subprocess.Popen(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:
            code=process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGTERM)
            process.wait()
            (destination/'timeout.json').write_text(json.dumps({'timeout_seconds':timeout,'log':str(log_path)}))
            return case,candidate,'timeout',None,time.monotonic()-started
    if result_file.exists():
        result=json.loads(result_file.read_text())
        return case,candidate,result['status'],result.get('our_admitted_mw'),result.get('elapsed_seconds')
    return case,candidate,f'exit_{code}',None,time.monotonic()-started


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--group',choices=('generators','storage','all'),default='all')
    parser.add_argument('--jobs',type=int,default=2)
    parser.add_argument('--timeout',type=int,default=480)
    parser.add_argument('--cases',nargs='+',choices=CASES)
    parser.add_argument('--candidates',nargs='+',choices=CANDIDATES)
    parser.add_argument('--storage-solver',choices=('benders','monolithic'),default='benders')
    parser.add_argument('--allocation-solver',choices=('course','gurobi'),default='course')
    args=parser.parse_args()
    design={'cases':CASES,'candidates':CANDIDATES,'horizon':120,'submission':1,
            'dispatch_and_allocation':'Unchanged instructor evaluator; no monkeypatches',
            'week2':'Independent full joint evaluation',
            'week3':'Official scorer called on same physical dispatch with energy charge enabled'}
    OUTPUT.mkdir(exist_ok=True,parents=True)
    (OUTPUT/'design.json').write_text(json.dumps(design,indent=2)+'\n')
    selection=ROOT/'analysis/garcia_validation/selected_pairs.json'
    selected={tuple(p) for p in json.loads(selection.read_text())['pairs']} if selection.exists() else None
    jobs=[(case,candidate) for case in (args.cases or CASES) for candidate,(_,_,battery) in CANDIDATES.items()
          if (args.group=='all' or (args.group=='storage')==bool(battery))
          and (not args.candidates or candidate in args.candidates)
          and (selected is None or (case,candidate) in selected)]
    print(f'{len(jobs)} {args.group} cases, {args.jobs} concurrent',flush=True)
    with ThreadPoolExecutor(args.jobs) as pool:
        futures=[pool.submit(run_one,*job,args.timeout,args.storage_solver,args.allocation_solver) for job in jobs]
        for index,future in enumerate(as_completed(futures),1):
            print(index,len(jobs),*future.result(),flush=True)


if __name__=='__main__':
    main()
