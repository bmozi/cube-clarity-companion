"""Print checked buffer-system target lists for an eyes-open practice scramble."""
from pathlib import Path
import argparse
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cube_clarity.blindfold import IDENTITY,load_routes,plan,execute
from cube_clarity.cube import apply

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scramble',default='F',help='outside face turns only; apply from solved')
    args=p.parse_args()
    if any(not re.fullmatch(r"[URFDLB](?:2|')?",t) for t in args.scramble.split()):p.error('Use U R F D L B, optionally followed by 2 or an apostrophe.')
    routes=load_routes();start=apply(IDENTITY,args.scramble);record=plan(start)
    if execute(start,record)!=IDENTITY:raise RuntimeError('Full replay failed; do not execute this record.')
    print('Start SOLVED, yellow up and green front. Scramble:',args.scramble or '(none)')
    print('Use docs/blindfold-course.md for the exact map, engines, setups and undo rows.')
    for family,plural in [('edge','edges'),('corner','corners')]:
        part=record[plural];letters=[routes['letter_map'][family][name] for name in part['targets']]
        print(f'{plural.title()} targets:', ' '.join(letters) or '(none)')
        print('Cycle-break target numbers (counting from 1):',', '.join(str(i+1) for i in part['cycle_breaks']) or '(none)')
        for i,name in enumerate(part['targets'],1):print(f'  {i}. {routes[family][name]["letter"]} ({name}): {routes[family][name]["algorithm"]}')
    print('EXECUTION ORDER: edges; '+('parity bridge; ' if record['parity'] else '')+'corners.')
    if record['parity']:print('PARITY BRIDGE:',routes['parity_algorithm'])
    print('Checked: all 54 stickers restored. Practise eyes open before adding memory.')
if __name__=='__main__':main()
