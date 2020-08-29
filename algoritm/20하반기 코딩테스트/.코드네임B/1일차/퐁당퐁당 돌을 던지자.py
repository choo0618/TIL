import sys
sys.stdin = open('퐁당퐁당 돌을 던지자.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(i,j):
    Visit=[[0]*N for _ in range(N)]
    r=1
    Visit[i][j]=1
    Q=deque([(i,j,0)])
    while Q:
        y,x,d=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X]==0 and Visit[Y][X]==0 and d+1<=M:
                Visit[Y][X]=1
                r+=1
                Q.append((Y,X,d+1))
    return r
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Result=0

for i in range(N):
    for j in range(N):
        if A[i][j]==0:Result=max(Result,BFS(i,j))
print(Result)