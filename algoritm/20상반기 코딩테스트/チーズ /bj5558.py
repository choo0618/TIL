import sys
sys.stdin = open('bj5558.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<H and -1<x<W
def BFS(t):
    global S
    y,x=S
    Q=deque([(y,x,0)])
    V=[[0]*W for _ in range(H)]
    V[y][x]=1
    while Q:
        y,x,c=Q.popleft()
        if A[y][x]==str(t):S=(y,x);return c
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and not V[Y][X] and A[Y][X]!='X':
                V[Y][X]=1
                Q.append((Y,X,c+1))
H,W,N=map(int,input().split())
A=[input()for i in range(H)]
R,S=0,0
for i in range(H):
    for j in range(W):
        if A[i][j]=='S':S=(i,j)
for _ in range(N):R+=BFS(_+1)
print(R)