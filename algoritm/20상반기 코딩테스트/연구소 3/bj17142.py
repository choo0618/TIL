import sys
sys.stdin = open('bj17142.txt','r')

import itertools
from collections import deque
def BFS(s):
    r=0
    V=[[-1]*N for _ in range(N)]
    Q=deque(C)
    for i,j,c in Q:V[i][j]=c
    while Q:
        y,x,c=Q.popleft()
        if not A[y][x]:r=c;s-=1
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if (-1<Y<N and -1<X<N) and A[Y][X]!=1 and V[Y][X]==-1:
                V[Y][X]=c+1
                Q.append((Y,X,c+1))
    if s:return 10**9
    return r
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R,V,v,s=10**10,[],0,0
for i in range(N):
    for j in range(N):
        if A[i][j]==2:V.append((i,j,0));v+=1
        if not A[i][j]:s+=1
for C in itertools.combinations(V,M):R=min(R,BFS(s))
print(-1 if R==10**9 else R)