import sys
sys.stdin = open('1249.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<N and -1<x<N:return True
    return False
def DFS(y,x,r):
    global R
    if y==x==N-1:
        if R>r:R=r;return
    if r>=R:return
    for dir in range(4):
        nY=y+dy[dir]
        nX=x+dx[dir]
        if IS(nY,nX) and M[nY][nX]>r:
            M[nY][nX]=r
            DFS(nY,nX,r+A[nY][nX])
T=int(input())
for n in range(T):
    N=int(input())
    A=[list(map(int,input()))for y in range(N)]
    M=[[999]*N for _ in range(N)]
    R=987654321
    DFS(0,0,0)
    print('#%d %d'%(n+1,M[N-1][N-1]))
