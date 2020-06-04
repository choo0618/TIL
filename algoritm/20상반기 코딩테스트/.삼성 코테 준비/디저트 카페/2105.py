import sys
sys.stdin = open('2105.txt','r')

dx=[1,-1,-1,1]
dy=[1,1,-1,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def DFS(y,x,d,r):
    global R
    if not IS(y,x) or d>3:return
    if d==3 and (y,x)==(i,j):
        R=max(r,R)
        return
    if D[A[y][x]]:return
    D[A[y][x]]=1
    Y,X=y+dy[d],x+dx[d]
    DFS(Y,X,d,r+1)
    DFS(Y,X,d+1,r+1)
    D[A[y][x]]=0
for t in range(int(input())):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R=-1
    D=[0]*101
    for i in range(N-2):
        for j in range(1,N-1):
            DFS(i,j,0,0)
    print('#%d %d'%(t+1,R))

