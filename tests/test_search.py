import sys,random,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'src'))
from cube_clarity.cube import sol,apply
from cube_clarity.search import *
class SearchTests(unittest.TestCase):
 def test_geometry_and_cubie_models_agree(self):
  rng=random.Random(411);stickers=sol;s=SOLVED
  for i in range(500):
   m=rng.choice(MOVES);stickers=apply(stickers,m);s=move(s,m);self.assertEqual(decode(stickers),s);s.validate()
 def test_reject_impossible_states(self):
  for s in [Cubie(co=(1,)+(0,)*7),Cubie(eo=(1,)+(0,)*11),Cubie(ep=(1,0)+tuple(range(2,12)))]:
   with self.assertRaises(ValueError):s.validate()
 def test_short_solutions(self):
  for a in ['', 'R', 'F2 U', "R U F2", "R U F2 L'", "F R U R' U'"]:
   s=sequence(SOLVED,a);res=solve_ida(s,max_depth=len(a.split()),node_budget=250000)
   self.assertEqual(res.status,'solved',a);self.assertEqual(sequence(s,' '.join(res.moves)),SOLVED)
 def test_depth_two_optimality_and_bound(self):
  q=deque([SOLVED]);dist={SOLVED:0}
  while q:
   s=q.popleft()
   if dist[s]==2:continue
   for m in MOVES:
    child=move(s,m)
    if child not in dist:dist[child]=dist[s]+1;q.append(child)
  for s,d in dist.items():
   self.assertLessEqual(lower_bound(s),d)
  for s,d in list(dist.items())[::11]:self.assertEqual(len(solve_ida(s,2,10000).moves),d)
 def test_budget_is_not_impossible(self):
  s=sequence(SOLVED,"R U F L D B")
  self.assertEqual(solve_ida(s,8,1).status,'budget-exhausted')
  self.assertEqual(solve_ida(s,0,100).status,'depth-limit')
 def test_phase_two_contract(self):
  s=sequence(SOLVED,'U R2 F2 D L2 B2')
  self.assertTrue(in_phase_two_group(s));self.assertNotEqual(s,SOLVED)
  for m in PHASE_TWO_MOVES:self.assertTrue(in_phase_two_group(move(s,m)))
  self.assertFalse(in_phase_two_group(move(s,'F')))
 def test_projected_databases(self):
  self.assertEqual(len(build_orientation_database('corners')),2187)
  self.assertEqual(len(build_orientation_database('edges')),2048)
if __name__=='__main__':unittest.main()
