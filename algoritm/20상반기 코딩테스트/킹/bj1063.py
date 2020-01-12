import sys
sys.stdin = open('bj1063.txt','r')

def IS(x,y):
    return 0<y<9 and 0<x<9

D = {'R':(1,0),'L':(-1,0),'B':(0,-1),'T':(0,1),'RT':(1,1),'LT':(-1,1),'RB':(1,-1),'LB':(-1,-1)}
Al={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
K,S,N = map(str,input().split())
K,S = [Al[K[0]],abs(int(K[1]))],[Al[S[0]],abs(int(S[1]))]
L = [input()for _ in range(int(N))]
for l in L:
    dx,dy = D[l]
    nX = K[0]+dx
    nY = K[1]+dy
    if not IS(nX,nY):continue
    if [nX,nY]==S:
        sX = S[0]+dx
        sY = S[1]+dy
        if not IS(sX,sY):continue
        S=[sX,sY]
    K=[nX,nY]
for r in [K,S]:
    R = [Al[r[0]],str(r[1])]
    print(''.join(R))
