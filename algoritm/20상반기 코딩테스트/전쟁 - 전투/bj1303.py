import sys
sys.stdin = open('bj1303.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    global W,B
    c=1
    V[y][x]=1
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and V[Y][X]==0 and A[Y][X]==t:
                V[Y][X]=1
                c+=1
                Q.append((Y,X))
    if t=='W':W+=c*c
    else:B+=c*c
M,N=map(int,input().split())
A=[input()for _ in range(N)]
V=[[0]*M for _ in range(N)]
W,B=0,0
for i in range(N):
    for j in range(M):
        if V[i][j]==0:BFS(i,j,A[i][j])
print(W,B)