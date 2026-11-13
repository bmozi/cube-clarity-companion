"""Reproduce the book's complete 2x2 teaching route without extra packages."""
from pathlib import Path
import sys,argparse,re
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cube_clarity.cube import apply
from cube_clarity.pocket import CORNERS,solve
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--scramble',default='R U F2');a=p.parse_args()
 if any(not re.fullmatch(r"[URFDLB](?:2|')?",t) for t in a.scramble.split()):p.error('Use face turns U R F D L B, optionally followed by 2 or an apostrophe.')
 start=apply(CORNERS,a.scramble);end,goal,steps=solve(start)
 print('Start solved, yellow up and green front. Scramble:',a.scramble)
 for i,step in enumerate(steps,1):print(f'{i:2}. {step["stage"]:29} {step["moves"]}')
 print('Checked: all 24 corner stickers solved in the final rotated frame:',end==goal)
 print('y turns the entire puzzle; other letters turn the named face. This is a learning route, not a shortest or speed solution.')
