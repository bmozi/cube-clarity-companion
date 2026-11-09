"""Educational cubie model and bounded IDA* solver, in half-turn metric.

Correctness-first teaching implementation. It has no large pattern database and
is not a practical fast solver for arbitrary full-length scrambles. A budget
exhaustion is an incomplete search, never proof of an impossible cube.
"""
from dataclasses import dataclass
from collections import Counter,deque
from math import ceil,inf
from .cube import sol,apply,norm
CORNERS=('URF','UFL','ULB','UBR','DFR','DLF','DBL','DRB')
EDGES=('UR','UF','UL','UB','DR','DF','DL','DB','FR','FL','BL','BR')
MOVES=tuple(f+s for f in 'UDFBRL' for s in ('',"'",'2'))
def position(name):return tuple(sum(norm[f][i] for f in name) for i in range(3))
def parity(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
@dataclass(frozen=True)
class Cubie:
 cp:tuple=tuple(range(8))
 co:tuple=(0,)*8
 ep:tuple=tuple(range(12))
 eo:tuple=(0,)*12
 def validate(self):
  if sorted(self.cp)!=list(range(8)) or sorted(self.ep)!=list(range(12)):raise ValueError('Each cubie must appear exactly once')
  if len(self.co)!=8 or any(x not in (0,1,2) for x in self.co) or sum(self.co)%3:raise ValueError('Corner orientations must sum to zero modulo three')
  if len(self.eo)!=12 or any(x not in (0,1) for x in self.eo) or sum(self.eo)%2:raise ValueError('Edge orientations must sum to zero modulo two')
  if parity(self.cp)!=parity(self.ep):raise ValueError('Corner and edge permutation parities must agree')
  return self
SOLVED=Cubie()
def decode(stickers):
 if set(stickers)!=set(sol) or Counter(stickers.values())!=Counter(sol.values()):raise ValueError('Need 54 stickers with exactly nine of each face color')
 if any(stickers[(norm[f],norm[f])]!=f for f in norm):raise ValueError('Centers must match the declared reference frame')
 cp=[];co=[];ep=[];eo=[]
 for name in CORNERS:
  colors=tuple(stickers[(position(name),norm[f])] for f in name)
  ori=next((i for i,col in enumerate(colors) if col in 'UD'),None)
  if ori is None:raise ValueError('Corner lacks its U or D color')
  aligned=colors[ori:]+colors[:ori]
  try:piece=CORNERS.index(''.join(aligned))
  except ValueError:raise ValueError('Unknown or reflected corner color order') from None
  cp.append(piece);co.append(ori)
 for name in EDGES:
  colors=''.join(stickers[(position(name),norm[f])] for f in name)
  if colors in EDGES:ep.append(EDGES.index(colors));eo.append(0)
  elif colors[::-1] in EDGES:ep.append(EDGES.index(colors[::-1]));eo.append(1)
  else:raise ValueError('Unknown edge color pair')
 return Cubie(tuple(cp),tuple(co),tuple(ep),tuple(eo)).validate()
# Move tables are derived from the independent 54-sticker geometry.
TABLES={m:decode(apply(sol,m)) for m in MOVES}
def move(s,m):
 t=TABLES[m]
 return Cubie(tuple(s.cp[t.cp[i]] for i in range(8)),tuple((s.co[t.cp[i]]+t.co[i])%3 for i in range(8)),tuple(s.ep[t.ep[i]] for i in range(12)),tuple(s.eo[t.ep[i]]^t.eo[i] for i in range(12)))
def sequence(s,text):
 for m in text.split():s=move(s,m)
 return s

def lower_bound(s):
 """Each face turn touches at most four corners and four edges; use max."""
 return max(ceil(sum(x!=i for i,x in enumerate(s.cp))/4),ceil(sum(x!=i for i,x in enumerate(s.ep))/4),ceil(sum(x!=0 for x in s.co)/4),ceil(sum(x!=0 for x in s.eo)/4))
def in_phase_two_group(s):
 return not any(s.co) and not any(s.eo) and set(s.ep[8:])==set(range(8,12))
PHASE_TWO_MOVES=('U',"U'",'U2','D',"D'",'D2','R2','L2','F2','B2')
@dataclass(frozen=True)
class Result:
 status:str
 moves:tuple=()
 expanded:int=0
 bound:int=0
class Exhausted(Exception):pass

def solve_ida(start,max_depth=8,node_budget=200_000):
 """A found path is HTM-optimal; incomplete results do not claim solvability.

The bound is g+h. All 18 moves cost one. Consecutive same-face moves can
always be merged or cancelled, so removing them cannot remove every optimum.
"""
 start.validate()
 if max_depth<0 or node_budget<1:raise ValueError('Need nonnegative depth and positive node budget')
 expanded=0;path=[];active={start};answer=None
 def visit(s,g,bound,last_face):
  nonlocal expanded,answer
  estimate=g+lower_bound(s)
  if estimate>bound:return estimate
  if s==SOLVED:answer=tuple(path);return -1
  if expanded>=node_budget:raise Exhausted
  expanded+=1;next_bound=inf
  for m in MOVES:
   if m[0]==last_face:continue
   child=move(s,m)
   if child in active:continue
   path.append(m);active.add(child)
   t=visit(child,g+1,bound,m[0])
   active.remove(child);path.pop()
   if t==-1:return -1
   next_bound=min(next_bound,t)
  return next_bound
 bound=lower_bound(start)
 try:
  while bound<=max_depth:
   t=visit(start,0,bound,None)
   if t==-1:return Result('solved',answer,expanded,bound)
   if t==inf:return Result('no-path',(),expanded,bound)
   bound=int(t)
 except Exhausted:return Result('budget-exhausted',(),expanded,bound)
 return Result('depth-limit',(),expanded,bound)

def build_orientation_database(kind='corners'):
 """Exact projected distances: 2187 corner or 2048 edge orientations.

This database is deliberately separate from solve_ida's simpler heuristic so
readers can measure the effect of adding it rather than hiding that change.
"""
 if kind not in ['corners','edges']:raise ValueError('Choose corners or edges')
 start=(0,)*(8 if kind=='corners' else 12);dist={start:0};q=deque([start])
 while q:
  a=q.popleft()
  for t in TABLES.values():
   b=tuple((a[t.cp[i]]+t.co[i])%3 for i in range(8)) if kind=='corners' else tuple(a[t.ep[i]]^t.eo[i] for i in range(12))
   if b not in dist:dist[b]=dist[a]+1;q.append(b)
 return dist

def main():
 import argparse
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--scramble',default="R U F2");ap.add_argument('--max-depth',type=int,default=8);ap.add_argument('--node-budget',type=int,default=200000);args=ap.parse_args()
 s=sequence(SOLVED,args.scramble);result=solve_ida(s,args.max_depth,args.node_budget)
 print('Status:',result.status);print('Expanded nodes:',result.expanded);print('Moves:',' '.join(result.moves))
 if result.status=='solved':assert sequence(s,' '.join(result.moves))==SOLVED
if __name__=='__main__':main()
