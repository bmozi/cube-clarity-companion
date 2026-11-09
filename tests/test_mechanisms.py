import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cube_clarity.blindfold import IDENTITY,KEYS
from cube_clarity.cube import apply,inv
class MechanismTests(unittest.TestCase):
 def test_pure_three_cycles(self):
  for alg,positions in [("M U2 M' U2",{(0,1,1),(0,1,-1),(0,-1,-1)}),("R U R' D R U' R' D'",{(1,1,1),(1,-1,1),(-1,-1,1)})]:
   s=apply(IDENTITY,alg)
   self.assertEqual({k[0] for k in KEYS if s[k]!=IDENTITY[k]},positions)
   self.assertEqual(apply(s,inv(alg)),IDENTITY)
   self.assertEqual(apply(IDENTITY,' '.join([alg]*3)),IDENTITY)
 def test_disjoint_commutator(self):self.assertEqual(apply(IDENTITY,"R L R' L'"),IDENTITY)
