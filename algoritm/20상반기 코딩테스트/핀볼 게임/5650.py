import sys
sys.stdin = open('5650.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
Block=[0,[2,0,3,1],[2,3,1,0],[1,3,0,2],[3,2,0,1],[2,3,0,1]]
def IS(y,x):
    return -1<y<N and -1<x<N
def Check(y,x,t):
    for i,j in W[t]:
        if (i,j)!=(y,x):return (i,j)
def BFS(i,j,Dir):
    Q=deque([(i,j,Dir,0,0)])
    while Q:
        y,x,d,c,tmp=Q.popleft()
        if (tmp and (i,j)==(y,x)) or A[y][x]==-1:r=c;break
        if DP[y][x][d]:r=c+DP[y][x][d]+c;break
        if 0<A[y][x]<6:d,c=Block[A[y][x]][d],c+1
        Y,X=y+dy[d],x+dx[d]
        if not IS(Y,X):
            d=(d+2)%4
            c+=1
            Y,X=y,x
        if A[Y][X]>5:Y,X=Check(Y,X,A[Y][X])
        Q.append((Y,X,d,c,1))
    DP[i][j][Dir]=r
    return r
for t in range(int(input())):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    DP=[[[0]*4 for _ in range(N)] for __ in range(N)]
    R,S,W=0,[],{6:[],7:[],8:[],9:[],10:[]}
    for i in range(N):
        for j in range(N):
            if not A[i][j]:S.append((i,j))
            elif A[i][j]>5:W[A[i][j]].append((i,j))
    for i,j in S:
        for d in range(4):R=max(R,BFS(i,j,d))
    print('#%d %d'%(t+1,R))