import sys
sys.stdin = open('bj1103.txt','r')

import sys
sys.setrecursionlimit(10**9)
def IS(y,x):
    return -1<y<N and -1<x<M
def DFS(y,x):
    if not IS(y,x) or A[y][x]=='H':return 0
    if V[y][x]:return -1
    if DP[y][x]:return DP[y][x]
    V[y][x]=1
    n=int(A[y][x])
    for Y,X in (y,x+n),(y+n,x),(y,x-n),(y-n,x):
        c=DFS(Y,X)
        if c==-1:return -1
        DP[y][x]=max(DP[y][x],c+1)
    V[y][x]=0
    return DP[y][x]
N,M=map(int,input().split())
A=[list(map(str,input()))for _ in range(N)]
DP=[[0]*M for __ in range(N)]
V=[[0]*M for __ in range(N)]
print(DFS(0,0))