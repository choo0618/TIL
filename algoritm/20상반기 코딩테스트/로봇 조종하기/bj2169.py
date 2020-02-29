import sys
sys.stdin = open('bj2169.txt','r')

dx=[0,1,-1]
dy=[1,0,0]
def IS(y,x):
    return -1<y<N and -1<x<M
def DFS(y,x,d):
    if (y,x)==(N-1,M-1):return A[y][x]
    tmp=DP[y][x][d]
    if tmp!=-1000000:return tmp
    for i in range(3):
        Y,X=y+dy[i],x+dx[i]
        if IS(Y,X) and not V[Y][X]:
            V[Y][X]=1
            tmp=max(tmp,DFS(Y,X,i)+A[y][x])
            V[Y][X]=0
    return tmp
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
DP=[[[0,0,0]for _ in range(N)]for __ in range(M)]
V=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        DP[i][j][0]=DP[i][j][1]=DP[i][j][2]=A[i][j]
V[0][0]=1
print(DFS(0,0,0))