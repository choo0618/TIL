import sys
sys.stdin = open('bj17090.txt','r')

import sys
sys.setrecursionlimit(10**9)
def DFS(y,x):
    if not (-1<y<N and -1<x<M):return 1
    if Map[y][x]!=-1:return Map[y][x]
    Map[y][x]=0
    Y,X=y,x
    if A[y][x]=='U':Y-=1
    elif A[y][x]=='R':X+=1
    elif A[y][x]=='D':Y+=1
    else:X-=1
    Map[y][x]=DFS(Y,X)
    return Map[y][x]
N,M=map(int,input().split())
A=[input() for y in range(N)]
Map=[[-1]*M for _ in range(N)]
R=0
for i in range(N):
    for j in range(M):R+=DFS(i,j)
print(R)
