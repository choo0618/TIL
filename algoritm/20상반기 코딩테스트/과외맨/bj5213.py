import sys
sys.stdin = open('bj5213.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<2*N and nMap[y][x]!=-1
def Find(y,x):
    for Y,X in (y,x+1),(y,x-1):
        if tMap[Y][X]==tMap[y][x]:return Y,X
def Check(i):
    L=[]
    while i!=R[i]:
        L.append(i)
        i=R[i]
    return L[::-1]
N=int(input())
nMap,tMap,T,I=[],[],1,0
for i in range(N):
    nl,tl=[],[]
    Len=N
    if i%2:Len-=1;nl.append(-1);tl.append(-1)
    for j in range(Len):
        x,y=map(int,input().split())
        nl.append(x);nl.append(y)
        tl.append(T);tl.append(T)
        T+=1
    if i%2:nl.append(-1);tl.append(-1)
    nMap.append(nl);tMap.append(tl)
R=[int(x)for x in range(T)]
V=[[0]*(2*N)for _ in range(N)]
R[1]=0
Q=deque([(0,1)])
V[0][0]=V[0][1]=1
while Q:
    y,x=Q.popleft()
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if not IS(Y,X) or V[Y][X]:continue
        t,nt=tMap[y][x],tMap[Y][X]
        if t!=nt and nMap[y][x]!=nMap[Y][X]:continue
        if nt!=t:R[nt]=t
        I=max(I,nt)
        i,j=Find(Y,X)
        V[Y][X]=V[i][j]=1
        Q+=[(Y,X),(i,j)]
L=Check(I)
print(len(L))
print(*L)
