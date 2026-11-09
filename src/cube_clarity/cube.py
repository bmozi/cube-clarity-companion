"""Exact 54-sticker model; x right, y up, z front. Original project implementation."""
norm={'U':(0,1,0),'D':(0,-1,0),'F':(0,0,1),'B':(0,0,-1),'R':(1,0,0),'L':(-1,0,0)}
def key(f,r,c):
 p={'U':(c-1,1,r-1),'D':(c-1,-1,1-r),'F':(c-1,1-r,1),'B':(1-c,1-r,-1),'R':(1,1-r,1-c),'L':(-1,1-r,c-1)}[f]
 return p,norm[f]
sol={key(f,r,c):f for f in norm for r in range(3) for c in range(3)}
def rot(v,axis,sgn):
 x,y,z=v
 if axis==0:return (x,-sgn*z,sgn*y)
 if axis==1:return (sgn*z,y,-sgn*x)
 return (-sgn*y,sgn*x,z)
def apply(s,alg):
 for t in alg.split():
  f=t[0]; n=2 if '2' in t else 3 if "'" in t else 1
  if f in 'xyz':
   axis='xyz'.index(f);layer=0;sgn=-1;pred=lambda p:True
  elif f=='u':axis,layer,sgn=1,1,-1;pred=lambda p:p[1]>=0
  elif f=='f':axis,layer,sgn=2,1,-1;pred=lambda p:p[2]>=0
  elif f=='b':axis,layer,sgn=2,-1,1;pred=lambda p:p[2]<=0
  elif f=='E':axis,layer,sgn=1,0,1;pred=lambda p:p[1]==0
  elif f=='S':axis,layer,sgn=2,0,-1;pred=lambda p:p[2]==0
  elif f=='l': axis,layer,sgn=0,-1,1; pred=lambda p:p[0]<=0
  elif f=='d': axis,layer,sgn=1,-1,1; pred=lambda p:p[1]<=0
  elif f=='M': axis,layer,sgn=0,0,1; pred=lambda p:p[0]==0
  elif f=='r':axis,layer,sgn=0,1,-1; pred=lambda p:p[0]>=0
  else:
   axis=next(i for i,v in enumerate(norm[f]) if v);layer=norm[f][axis];sgn=-layer;pred=lambda p:p[axis]==layer
  for _ in range(n): s={(rot(p,axis,sgn),rot(v,axis,sgn)) if pred(p) else (p,v):col for (p,v),col in s.items()}
 return s
def inv(a):return ' '.join(t if '2' in t else t[0] if "'" in t else t+"'" for t in a.split()[::-1])
def f2l(s):return all(s[k]==v for k,v in sol.items() if k[0][1]<1)
def yellow(s):return all(s[key('U',r,c)]=='U' for r,c in [(0,1),(1,0),(1,1),(1,2),(2,1)])
A={
'Right insert':"U R U' R' U' F' U F",'Left insert':"U' L' U L U F U' F'",
'Line':"F R U R' U' F'",'Elbow':"F U R U' R' F'",
'Dot':"F R U R' U' F' U2 F U R U' R' F'",
'Sune':"R U R' U R U2 R'",'Antisune':"R U2 R' U' R U' R'",
'Headlights':"R2 D R' U2 R D' R' U2 R'",'Chameleon':"r U R' U' r' F R F'",
'Bowtie':"F' r U R' U' r' F R",'Pi':"R U2 R2 U' R2 U' R2 U2 R",
'H corners':"R U R' U R U' R' U R U2 R'",
'T corners':"R U R' U' R' F R2 U' R' U' R U R' F'",
'Diagonal corners':"R' U L' U2 R U' L R' U L' U2 R U' L",
'Ua':"R U' R U R U R U' R' U' R2",
'Ub':"R2 U R U R' U' R' U' R' U R'",
'Z edges':"M2 U M2 U M' U2 M2 U2 M' U2",'H edges':"M2 U M2 U2 M2 U M2"}

