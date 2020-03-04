import sys
sys.stdin = open('bj2589.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]=='L'
def BFS(y,x):
    V=[[0]*M for _ in range(N)]
    Q=deque([(y,x,0)])
    V[y][x],r=1,0
    while Q:
        y,x,t=Q.popleft()
        r=max(r,t)
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X)and not V[Y][X]:
                V[Y][X]=1
                Q.append((Y,X,t+1))
    return r
N,M=map(int,input().split())
A=[input()for _ in range(N)]
R=0
for i in range(N):
    for j in range(M):
        if A[i][j]=='L':R=max(R,BFS(i,j))
print(R)
