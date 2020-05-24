import sys
sys.stdin = open('bj16959.txt','r')

from collections import deque
dx=[[1,2,2,1,-1,-2,-2,-1],[1,1,-1,-1],[1,0,-1,0]]
dy=[[2,1,-1,-2,-2,-1,1,2],[-1,1,1,-1],[0,1,0,-1]]
def IS(y,x):
    return -1<y<N and -1<x<N
def Knight(y,x,n,t):
    for d in range(8):
        Y,X=y+dy[0][d],x+dx[0][d]
        if IS(Y,X):
            N=n
            if A[Y][X]==n+1:N+=1
            if t<V[Y][X][N][0]:
                V[Y][X][N][0]=t
                Q.append((Y,X,N,0,t))
def BL(y,x,n,t,s):
    for d in range(4):
        Y,X=y+dy[s][d],x+dx[s][d]
        while IS(Y,X):
            N=n
            if A[Y][X]==n+1:N+=1
            if t<V[Y][X][N][s]:
                V[Y][X][N][s]=t
                Q.append((Y,X,N,s,t))
            Y,X=Y+dy[s][d],X+dx[s][d]
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[[[[10**9]*3 for _ in range(N*N+1)]for __ in range(N)]for ___ in range(N)]
Q=deque()
for i in range(N):
    for j in range(N):
        if A[i][j]==1:
            for x in range(3):Q.append((i,j,1,x,0));V[i][j][1][x]=0
while Q:
    y,x,now,s,t=Q.popleft()
    if now==N*N:print(t);break
    for S in range(3):
        if S!=s and t+1<V[y][x][now][S]:Q.append((y,x,now,S,t+1))
    if s==0:Knight(y,x,now,t+1)
    else:BL(y,x,now,t+1,s)