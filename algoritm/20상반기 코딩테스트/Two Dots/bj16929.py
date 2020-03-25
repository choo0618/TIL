import sys
sys.stdin = open('bj16929.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def DFS(y,x,D,S):
    global R
    if Map[y][x]:R=1;return
    Map[y][x]=1
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and A[Y][X]==S and (d+2)%4!=D:
            DFS(Y,X,d,S)
            if R:return
N,M=map(int,input().split())
A=[input()for _ in range(N)]
Map=[[0]*M for _ in range(N)]
R=0
for i in range(N):
    for j in range(M):
        if not Map[i][j]:DFS(i,j,0,A[i][j])
        if R:break
    if R:break
print('Yes' if R else 'No')