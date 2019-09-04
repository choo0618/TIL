import sys
sys.stdin = open('2105.txt','r')

dx=[1,-1,-1,1]
dy=[1,1,-1,-1]
def IS(y,x):
    if -1<y<N and -1<x<N:return True
    return False
def DFS(y,x,dir,l):
    global R
    if dir>3:return
    nY=y+dy[dir]
    nX=x+dx[dir]
    if not IS(nY,nX):return
    if (nY,nX)==(i,j):
        if len(l)>R:R=len(l);return
    if A[nY][nX] in l:return
    l.append(A[nY][nX])
    DFS(nY,nX,dir,l)
    DFS(nY,nX,dir+1,l)
    l.pop()
T=int(input())
for t in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R=-1
    for i in range(0,N-2):
        for j in range(1,N-1):
            DFS(i,j,0,[A[i][j]])
    print('#%d %d'%(t+1,R))