"""Corner-only 2x2 teaching model and deterministic beginner lesson checks.

The coordinate frame is a teaching aid, not visible center pieces on a 2x2.
Face moves are projected from the independently tested 3x3 sticker geometry.
"""
from .cube import sol,apply,inv,key,A
CORNERS={k:v for k,v in sol.items() if all(abs(x)==1 for x in k[0])}
INSERT="R U R' U'"
TWIST="R' D' R D"
SWAP=A['T corners']
UFR=(1,1,1);DFR=(1,-1,1)
def colors(s,pos):return frozenset(v for (p,n),v in s.items() if p==pos)
def at_home(s,goal,pos):return all(s[k]==v for k,v in goal.items() if k[0]==pos)
def layer(s,goal):return all(s[k]==v for k,v in goal.items() if k[0][1]==-1)
def oriented(s):return all(v=='U' for (p,n),v in s.items() if n==(0,1,0))
def solve(start):
 s=dict(start);goal=dict(CORNERS);steps=[]
 def move(alg,stage):
  nonlocal s,goal
  s=apply(s,alg)
  if any(t[0] in 'xyz' for t in alg.split()):goal=apply(goal,alg)
  steps.append({'stage':stage,'moves':alg,'state':dict(s)})
 # Frames keep yellow up / white down; y rotates only the chosen side frame.
 for _ in range(4):
  if layer(s,goal):break
  for _ in range(4):
   if not at_home(s,goal,DFR):break
   move('y','choose home')
  wanted=colors(goal,DFR)
  pos=next(p for p,n in s if colors(s,p)==wanted)
  if pos[1]==-1:
   for _ in range(4):
    if colors(s,DFR)==wanted:break
    move('y','reach trapped corner')
   move(INSERT,'eject')
   for _ in range(4):
    if colors(goal,DFR)==wanted:break
    move('y','restore target home')
  for _ in range(4):
   if colors(s,UFR)==wanted:break
   move('U','place above home')
  for count in range(1,7):
   move(INSERT,'insert')
   if at_home(s,goal,DFR):break
  assert count in [1,3,5],count
 assert layer(s,goal)
 for _ in range(4):
  if oriented(s):break
  for _ in range(4):
   if s[(UFR,(0,1,0))]!='U':break
   move('U','next yellow corner')
  for count in range(1,7):
   move(TWIST,'orient')
   if s[(UFR,(0,1,0))]=='U':break
  assert count in [2,4],count
 assert oriented(s) and layer(s,goal)
 def finish():
  for n in range(4):
   a=apply(s,' '.join(['U']*n))
   if a==goal:
    if n:move({1:'U',2:'U2',3:"U'"}[n],'final alignment')
    return True
  return False
 if finish():return s,goal,steps
 def pair(face):return s[key(face,0,0)]==s[key(face,0,2)]
 if not any(pair(f) for f in 'FRBL'):move(SWAP,'create a matching pair')
 for _ in range(4):
  if pair('L'):break
  move('y','matching pair to left')
 assert pair('L')
 move(SWAP,'swap the other two corners')
 assert finish(), 'Permutation lesson did not finish'
 return s,goal,steps
