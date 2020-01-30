import sys
sys.stdin=open('bj2665.txt','r')

import heapq
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
N=int(input())
A=[input()for _ in range(N)]
Map=[[0]*N for _ in range(N)]
Map[0][0]=1
Que=[(1,0,0)]
while Que:
    c,y,x=heapq.heappop(Que)
    for d in range(4):
        Y,X,C=y+dy[d],x+dx[d],c
        if IS(Y,X) and not Map[Y][X]:
            if A[Y][X]=='0':C+=1
            Map[Y][X]=C
            heapq.heappush(Que,(C,Y,X))
print(Map[N-1][N-1]-1)



