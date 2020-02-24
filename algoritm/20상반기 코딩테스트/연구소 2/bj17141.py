import sys
sys.stdin = open('bj17141.txt','r')

import itertools
from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[]
Tmp,R=N**2,10**9
for i in range(N):
    for j in range(N):
        if A[i][j]==2:V.append((i,j,0))
        elif A[i][j]:Tmp-=1
for C in itertools.combinations(V,M):
    C=list(C)
    tmp,r=Tmp,0
    Map=[[-1]*N for _ in range(N)]
    for c in C:Map[c[0]][c[1]]=0
    Q=deque(C)
    while Q:
        y,x,c=Q.popleft()
        tmp-=1
        r=c
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and A[Y][X]!=1 and Map[Y][X]==-1:
                Map[Y][X]=c+1
                Q.append((Y,X,c+1))
    if not tmp:R=min(R,r)
print(R if R!=10**9 else -1)

