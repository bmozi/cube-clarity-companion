import unittest,random
from cube_clarity.cube import apply
from cube_clarity.pocket import CORNERS,solve,SWAP
class PocketTests(unittest.TestCase):
 def test_complete_beginner_route_on_1000_legal_scrambles(self):
  r=random.Random(20261113)
  for _ in range(1000):
   scramble=' '.join(r.choice('URFDLB')+r.choice(['',"'",'2']) for _ in range(25))
   start=apply(CORNERS,scramble);end,goal,trace=solve(start)
   self.assertEqual(end,goal,scramble)
   replay=start
   for step in trace:replay=apply(replay,step['moves']);self.assertEqual(replay,step['state'])
 def test_all_24_oriented_top_corner_permutations(self):
  encode=lambda s:tuple(s[k] for k in CORNERS)
  seen={encode(CORNERS):CORNERS};queue=[CORNERS]
  while queue:
   s=queue.pop()
   for a in ['U',SWAP]:
    t=apply(s,a);k=encode(t)
    if k not in seen:seen[k]=t;queue.append(t)
  self.assertEqual(len(seen),24)
  for s in seen.values():
   end,goal,_=solve(s);self.assertEqual(end,goal)
