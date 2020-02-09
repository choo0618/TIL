import sys
sys.stdin = open('bj4485.txt','r')

import heapq
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
t=0
while True:
    t+=1
    N=int(input())
    if not N:break
    A=[[int(x) for x in input().split()]for y in range(N)]
    Q=[(A[0][0],0,0)]
    Map=[[0]*N for _ in range(N)]
    Map[0][0]=A[0][0]
    while Q:
        c,y,x=heapq.heappop(Q)
        if (y,x)==(N-1,N-1):print('Problem %d: %d'%(t,c));break
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and not Map[Y][X]:
                nC=c+A[Y][X]
                Map[Y][X]=1
                heapq.heappush(Q,(nC,Y,X))