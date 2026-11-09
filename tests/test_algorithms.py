from pathlib import Path
import sys,json,unittest,random
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'src'))
from cube_clarity.cube import sol,key,apply,inv,A
class ModelTests(unittest.TestCase):
 def test_quarter_turns(self):
  ident={k:i for i,k in enumerate(sol)}
  for f in 'UDFBRL':
   self.assertEqual(apply(ident,' '.join([f]*4)),ident)
   self.assertEqual(apply(ident,f+' '+f+"'"),ident)
   self.assertEqual(len(set(apply(ident,f).values())),54)
  # Independently stated physical destinations, beyond inverse self-consistency.
  self.assertEqual(apply({key('F',1,2):'marker'},'R'),{key('U',1,2):'marker'})
  self.assertEqual(apply({key('U',2,1):'marker'},'F2'),{key('D',0,1):'marker'})
 def test_generated_routes_and_protection(self):
  ident={k:i for i,k in enumerate(sol)}
  for family,count in [('f2l',41),('oll',57),('pll',21)]:
   rows=json.loads((R/'data'/f'{family}_working_cases.json').read_text());self.assertEqual(len(rows),count)
   self.assertEqual(len({tuple(z['canonical_key']) for z in rows}),count)
   for row in rows:
    s=apply(ident,row['setup']);self.assertEqual(apply(s,row['algorithm']),ident,row['id'])
    protected=[k for k in sol if k[0][1]<1 and (family!='f2l' or k[0] not in [(1,-1,1),(1,0,1)])]
    self.assertTrue(all(s[k]==ident[k] for k in protected),row['id'])
    self.assertEqual(row['human_ergonomics_review'],'pending')
 def test_named_final_edge_actions_fix_every_corner(self):
  ident={k:i for i,k in enumerate(sol)}
  for name in ['Ua','Ub','H edges','Z edges']:
   s=apply(ident,A[name]);self.assertTrue(all(s[k]==v for k,v in ident.items() if sum(x*x for x in k[0])==3),name)
 def test_trigger_returns_after_six_groups(self):
  self.assertEqual(apply(sol,' '.join(["R U R' U'"]*6)),sol)
if __name__=='__main__':unittest.main()
