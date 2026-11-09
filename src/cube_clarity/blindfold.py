"""Verified beginner buffer-swap teaching system with explicit collateral swaps.
Routes derived from original coordinate model; no external algorithm tables copied.
"""
from pathlib import Path
import json
from .cube import sol,key,apply,norm
KEYS=list(sol)
IDENTITY={k:i for i,k in enumerate(KEYS)}
T="R U R' U' R' F R2 U' R' U' R U R' F'"
PARITY=T+" U2 R U' R U R U R U' R' U' R2 U2"
def sticker_name(k):
 return next(f for f,n in norm.items() if n==k[1])+''.join(f for f in 'UDLRFB' if norm[f]!=k[1] and sum(k[0][i]*norm[f][i] for i in range(3))==1)
NAME_TO_KEY={sticker_name(k):k for k in KEYS}
def load_routes():
 return json.loads((Path(__file__).resolve().parents[2]/'data/blindfold_routes.json').read_text())
def memo(state,family):
 """Simulate only the selected cubie type; other type uses its original memo."""
 rows=load_routes()[family];buf=key('U',1,2) if family=='edge' else key('U',0,0)
 dimension=2 if family=='edge' else 3
 selected=[k for k in KEYS if sum(t*t for t in k[0])==dimension]
 working=state.copy();targets=[];breaks=[]
 for _ in range(80):
  wrong=[k for k in selected if working[k]!=IDENTITY[k]]
  if not wrong:return {'targets':targets,'cycle_breaks':breaks}
  target=KEYS[working[buf]]
  if target[0]==buf[0]:
   target=next(k for k in wrong if k[0]!=buf[0]);breaks.append(len(targets))
  name=sticker_name(target);targets.append(name)
  moved=apply(working,rows[name]['algorithm'])
  for k in selected:working[k]=moved[k]
 raise RuntimeError('Memo did not terminate')
def plan(state):
 edges=memo(state,'edge');corners=memo(state,'corner')
 assert len(edges['targets'])%2==len(corners['targets'])%2
 return {'edges':edges,'corners':corners,'parity':bool(len(edges['targets'])%2)}
def execute(state,record):
 rows=load_routes();s=state
 for target in record['edges']['targets']:s=apply(s,rows['edge'][target]['algorithm'])
 if record['parity']:s=apply(s,PARITY)
 for target in record['corners']['targets']:s=apply(s,rows['corner'][target]['algorithm'])
 return s
