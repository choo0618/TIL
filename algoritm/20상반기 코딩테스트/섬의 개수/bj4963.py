import sys
sys.stdin = open('bj4963.txt','r')

from collections import deque
dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]
def IS(y,x):
    return -1<y<H and -1<x<W
def BFS(y,x,t):
    Que=deque([(y,x)])
    Map[y][x]=t
    while Que:
        Y,X=Que.popleft()
        for d in range(8):
            nY,nX=Y+dy[d],X+dx[d]
            if IS(nY,nX) and not Map[nY][nX] and A[nY][nX]:
                Map[nY][nX]=t
                Que.append((nY,nX))
while True:
    W,H=map(int,input().split())
    if not W+H:break
    A=[[int(x)for x in input().split()]for y in range(H)]
    Map=[[0]*W for _ in range(H)]
    tmp=0
    for i in range(H):
        for j in range(W):
            if A[i][j] and not Map[i][j]:tmp+=1;BFS(i,j,tmp)
    print(tmp)
