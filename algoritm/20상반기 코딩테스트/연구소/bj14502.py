import sys
sys.stdin = open('bj14502.txt','r')

import itertools
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(r):
    Q=V[:]
    while Q:
        y,x=Q.pop()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and Map[Y][X]==0:
                Q.append((Y,X))
                Map[Y][X]=2
                r-=1
    return r
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
V,B,b,=[],[],-3
for i in range(N):
    for j in range(M):
        if A[i][j]==2:V.append((i,j))
        elif A[i][j]==0:B.append((i,j));b+=1
R=0
for Comb in itertools.combinations(B,3):
    Map=[a[:]for a in A]
    for y,x in Comb:Map[y][x]=1
    R=max(R,BFS(b))
print(R)