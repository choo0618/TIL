import sys
sys.stdin = open('bj14497.txt','r')

import heapq
def IS(y,x):
    return -1<y<N and -1<x<M
N,M=map(int,input().split())
y1,x1,y2,x2=map(int,input().split())
A=[input()for _ in range(N)]
V=[[0]*M for _ in range(N)]
V[y1-1][x1-1]=1
Q=[(1,y1-1,x1-1)]
while Q:
    d,y,x=heapq.heappop(Q)
    if A[y][x]=='#':print(d);break
    for D,Y,X in (d,y,x+1),(d,y+1,x),(d,y,x-1),(d,y-1,x):
        if IS(Y,X) and not V[Y][X]:
            if A[Y][X]=='1':D+=1
            V[Y][X]=1
            heapq.heappush(Q,(D,Y,X))