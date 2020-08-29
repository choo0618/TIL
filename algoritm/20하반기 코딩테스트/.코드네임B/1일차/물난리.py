import sys
sys.stdin = open('물난리.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(i,j):
    Visit=[[0]*N for _ in range(N)]
    Visit[i][j]=1
    Visit[0][0]=1
    Q=deque([(0,0)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X]==0 and Visit[Y][X]==0:
                Visit[Y][X]=1
                Q.append((Y,X))
    r=0
    for i in range(N):
        for j in range(N):
            if A[i][j]==Visit[i][j]==0:r+=1
    return r
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Result=0
Map=[[[-1,-1]for _ in range(N)]for __ in range(N)]
Q=deque([(0,0,0,0),(N-1,N-1,1,0)])
Map[0][0][0]=0
Map[N-1][N-1][1]=0
while Q:
    y,x,tmp,d=Q.popleft()
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X) and A[Y][X]==0 and Map[Y][X][tmp]==-1:
            Map[Y][X][tmp]=d+1
            Q.append((Y,X,tmp,d+1))
for i in range(N):
    for j in range(N):
        if i==j==0 or i==j==N-1 or A[i][j]==1 or Map[i][j][0]==-1 or Map[i][j][1]==-1 or Map[i][j][0]<=Map[i][j][1]:continue
        Result=max(Result,BFS(i,j))
if Result==0:Result=max(Result,BFS(0,0))
print(Result)