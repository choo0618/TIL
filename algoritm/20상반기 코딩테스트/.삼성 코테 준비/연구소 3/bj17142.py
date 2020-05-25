import sys
sys.stdin = open('bj17142.txt','r')

from collections import deque
import itertools
def BFS(l,b):
    r=0
    V=[[-1]*N for _ in range(N)]
    Q=deque()
    for y,x in l:V[y][x]=0;Q.append((y,x,0))
    while Q:
        y,x,t=Q.popleft()
        if A[y][x]==0:b-=1;r=t
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if -1<Y<N and -1<X<N and A[Y][X]!=1 and V[Y][X]==-1:
                V[Y][X]=t+1
                Q.append((Y,X,t+1))
    if b:return 10**9
    return r
N,M=map(int,input().split())
R,V,B=10**9,[],0
A=[]
for i in range(N):
    l=[int(x)for x in input().split()]
    for j in range(N):
        if l[j]==2:V.append((i,j))
        elif l[j]==0:B+=1
    A.append(l)
for C in itertools.combinations(V,M):R=min(R,BFS(C,B))
if R!=10**9:print(R)
else:print(-1)