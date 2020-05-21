import sys
sys.stdin = open('bj16932.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    r,V[y][x]=1,t
    Q=deque([(i,j)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and V[Y][X]==0 and A[Y][X]:
                V[Y][X]=t
                r+=1
                Q.append((Y,X))
    return r
def Re(y,x):
    r,Set=1,set()
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X):Set.add(V[Y][X])
    for n in Set:r+=Size[n]
    return r
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[[0] * M for _ in range(N)]
R,tmp,Size=0,1,[0]
for i in range(N):
    for j in range(M):
        if A[i][j] and V[i][j]==0:Size.append(BFS(i,j,tmp));tmp+=1
for i in range(N):
    for j in range(M):
        if not A[i][j]:R=max(R,Re(i,j))
print(R)