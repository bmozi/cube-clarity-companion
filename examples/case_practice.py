"""Inspect one exact 3x3 reference case, then reveal its complete route."""
from pathlib import Path
import argparse
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cube_clarity.cube import sol,key,apply
ROOT=Path(__file__).resolve().parents[1]
COLORS={'U':'Y','D':'W','F':'G','B':'B','R':'O','L':'R'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list',action='store_true',help='list IDs and mapped conventional names')
    parser.add_argument('--family',choices=['f2l','oll','pll'])
    parser.add_argument('--case',help='stable case ID, such as F2L-026')
    parser.add_argument('--hide-answer',action='store_true',help='show pattern without moves')
    parser.add_argument('--show-setup',action='store_true',help='show practice setup; use only from solved')
    args=parser.parse_args()
    if args.hide_answer and args.show_setup:parser.error('Hide the answer or show the practice setup, not both.')
    rows=[row for family in ['f2l','oll','pll'] for row in json.loads((ROOT/'data'/f'{family}_working_cases.json').read_text()) if not args.family or family==args.family]
    if args.list:
        if args.case:parser.error('Choose --list or --case.')
        for row in rows:print(row['id'],row.get('standard_label',''))
        return
    if not args.case:parser.error('Choose --list or provide --case.')
    row=next((r for r in rows if r['id']==args.case.upper()),None)
    if row is None:parser.error('Unknown case ID for the selected family. Use --list.')
    state=apply(sol,row['setup'])
    if apply(state,row['algorithm'])!=sol:raise RuntimeError('Route replay failed; do not execute it.')
    print('HOLD: yellow up, green front, orange right. Read each face from its outside.')
    print('Colors: W white; Y yellow; G green; B blue; O orange; R red.')
    print('CASE:',row['id'])
    for face in ['U','F','R','B','L','D']:
        print(face+' face:')
        for r in range(3):print(' '.join(COLORS[state[key(face,r,c)]] for c in range(3)))
    if args.hide_answer:
        print('Name the remaining job and distinguish the pattern before revealing its route.')
        return
    if row.get('standard_label'):print('Mapped name:',row['standard_label'])
    if args.show_setup:print('PRACTICE ONLY: start SOLVED in the stated grip, then apply:',row['setup'])
    print('DO:',row['algorithm'])
    print('CHECK: '+('Chosen pair home; cross and previously solved neighboring slots restored.' if row['family']=='f2l' else 'All nine top stickers yellow; both lower layers restored. Side permutation may remain.' if row['family']=='oll' else 'All six faces uniform and aligned with their centers.'))
    print('Model replay passed. This does not establish comfortable grips or human speed.')
if __name__=='__main__':main()
