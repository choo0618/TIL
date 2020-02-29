import sys
sys.stdin = open('bj1937.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def DFS(y,x):
    if DP[y][x]:return DP[y][x]
    DP[y][x]=1
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and A[Y][X]>A[y][x]:
            DP[y][x]=max(DP[y][x],DFS(Y,X)+1)
    return DP[y][x]
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
DP=[[0]*N for _ in range(N)]
R=0
for i in range(N):
    for j in range(N):
        R=max(R,DFS(i,j))
print(R)


import heapq
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[[1]*N for _ in range(N)]
Q=[]
for i in range(N):
    for j in range(N):
        heapq.heappush(Q,(A[i][j],i,j))
while Q:
    c,y,x=heapq.heappop(Q)
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and A[Y][X]<A[y][x] and Map[Y][X]+1>Map[y][x]:Map[y][x]=Map[Y][X]+1
print(max(max(x)for x in Map))