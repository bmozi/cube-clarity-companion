import unittest,random,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cube_clarity.blindfold import *
from cube_clarity.cube import inv
class BlindfoldTests(unittest.TestCase):
 def test_all_directed_routes_and_collateral(self):
  r=load_routes()
  for family,buf,dimension,engine in [('edge',key('U',1,2),2,T),('corner',key('U',0,0),3,r['corner_engine'])]:
   collateral=apply(IDENTITY,engine)
   self.assertEqual(len(r[family]),22 if family=='edge' else 21)
   for name,row in r[family].items():
    k=NAME_TO_KEY[name];s=apply(IDENTITY,row['algorithm'])
    self.assertEqual(s[k],IDENTITY[buf]);self.assertEqual(s[buf],IDENTITY[k])
    self.assertTrue(all(s[j]==collateral[j] for j in KEYS if sum(t*t for t in j[0])!=dimension))
    self.assertEqual(apply(s,row['algorithm']),IDENTITY)
 def test_parity_contract(self):
  t=apply(IDENTITY,T);c=apply(IDENTITY,load_routes()['corner_engine']);s=apply(IDENTITY,PARITY)
  self.assertTrue(all(s[k]==(t[k] if sum(v*v for v in k[0])==3 else c[k] if sum(v*v for v in k[0])==2 else IDENTITY[k]) for k in KEYS))
 def test_complete_solves_with_breaks_and_orientation(self):
  rng=random.Random(8675309);counts={'odd':0,'even':0,'breaks':0,'flips':0,'twists':0}
  for _ in range(500):
   alg=' '.join(rng.choice('U D F B R L'.split())+rng.choice(['',"'",'2']) for _ in range(25));s=apply(IDENTITY,alg);p=plan(s)
   self.assertEqual(execute(s,p),IDENTITY,alg)
   # Independently follow the printed worksheet exchanges, not the move engine.
   routes=load_routes()
   for family,plural,dim in [('edge','edges',2),('corner','corners',3)]:
    names=routes['letter_map'][family]
    sheet={names[sticker_name(k)]:names[sticker_name(KEYS[s[k]])] for k in KEYS if sum(v*v for v in k[0])==dim}
    for target in p[plural]['targets']:
     for a,b in routes[family][target]['virtual_exchanges']:sheet[a],sheet[b]=sheet[b],sheet[a]
    self.assertTrue(all(k==v for k,v in sheet.items()),(alg,family))
   counts['odd' if p['parity'] else 'even']+=1
   counts['breaks']+=bool(p['edges']['cycle_breaks'] or p['corners']['cycle_breaks'])
   for k in KEYS:
    if s[k]!=IDENTITY[k] and KEYS[s[k]][0]==k[0]:counts['flips' if sum(t*t for t in k[0])==2 else 'twists']+=1
  self.assertTrue(all(counts.values()),counts)
 def test_dwide_physical_definition(self):
  self.assertEqual(apply(IDENTITY,'d d d d'),IDENTITY)
  self.assertEqual(apply({key('F',1,1):'marker'},'d'),{key('R',1,1):'marker'})
if __name__=='__main__':unittest.main()
