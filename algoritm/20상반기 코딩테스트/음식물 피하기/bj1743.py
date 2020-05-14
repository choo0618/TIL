import sys
sys.stdin = open('bj1743.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x):
    Q=deque([(y,x)])
    V[y][x]=1
    r=1
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X] and not V[Y][X]:
                Q.append((Y,X))
                V[Y][X]=1
                r+=1
    return r
N,M,K=map(int,input().split())
A=[[0]*M for _ in range(N)]
V=[[0]*M for _ in range(N)]
L=[]
R=0
for i in range(K):
    y,x=map(int,input().split())
    A[y-1][x-1]=1
    L.append((y-1,x-1))
for i,j in L:
    if A[i][j] and not V[i][j]:R=max(R,BFS(i,j))
# for i in range(N):
#     for j in range(M):
#         if A[i][j] and not V[i][j]:R=max(R,BFS(i,j))
print(R)