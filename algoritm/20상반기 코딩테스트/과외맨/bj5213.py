import sys
sys.stdin = open('bj5213.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<2*N
def Check(i):
    L=[]
    while i!=R[i]:
        L.append(i)
        i=R[i]
    return L
N=int(input())
nMap,tMap,t=[],[],1
for i in range(N):
    nl,tl=[],[]
    Len=N
    if i%2:Len-=1;nl.append(-1);tl.append(-1)
    for j in range(Len):
        x,y=map(int,input().split())
        nl.append(x);nl.append(y)
        tl.append(t);tl.append(t)
        t+=1
    if i%2:nl.append(-1);tl.append(-1)
    nMap.append(nl);tMap.append(tl)
R=[int(x)for x in range(t)]
V=[[0]*(2*N)for _ in range(N)]
R[1],V[0][0]=0,1
Q=deque([(0,0)])
while Q:
    y,x=Q.popleft()
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X) and nMap[Y][X]!=-1 and not V[Y][X]:
            n,nn,t,nt=nMap[y][x],nMap[Y][X],tMap[y][x],tMap[Y][X]
            if t!=nt:
                if n!=nn:continue
                else:R[nt]=t
            V[Y][X]=1
            Q.append((Y,X))
for r in range(t,0,-1):
    if R[r]!=r:
        L=Check(r)
        if L[-1]!=1:continue
        L.reverse()
        print(len(L))
        print(*L)
        break
