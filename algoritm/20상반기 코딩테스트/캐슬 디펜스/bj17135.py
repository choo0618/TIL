import sys
sys.stdin = open('bj17135.txt','r')

import itertools
def DFS(y,x,c,m):
    if y<0 or not -1<x<M:return
    if A[y][x]:C[m]=1;A[y][x]=0;L.append((y,x));return
    if c==D:return
    for Y,X in (y,x-1),(y-1,x),(y,x+1):
        DFS(Y,X,c+1,m)
        if C[m]:return
N,M,D=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for a,b,c in itertools.combinations(range(M),3):
    L,now,r=[],N-1,0
    while now>=0:
        C=[0,0,0]
        DFS(now,a,1,0);DFS(now,b,1,1);DFS(now,c,1,2)
        r+=sum(C)
        now-=1
    for i,j in L:A[i][j]=1
    R=max(R,r)
print(R)

