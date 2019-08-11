import sys
sys.stdin = open('1949.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    global M
    if -1<y<L[0] and -1<x<L[0]:return True
    return False
def DFS(y,x,c):
    global R
    if c>R:R=c
    for dir in range(4):
        nY=y+dy[dir]
        nX=x+dx[dir]
        if IS(nY,nX):
            if not M[nY][nX]and A[y][x]>A[nY][nX]:
                M[nY][nX]=1
                DFS(nY,nX,c+1)
                M[nY][nX]=0
T=int(input())
for t in range(T):
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[0])]
    R,m,Q=1,0,[]
    for _ in range(L[0]):
        if max(A[_])>m:m=max(A[_])
    for y in range(L[0]):
        for x in range(L[0]):
            if A[y][x]==m:Q.append([y,x])
    for i in range(L[0]):
        for j in range(L[0]):
            for d in range(L[1]):
                A[i][j]-=d+1
                for l in Q:
                    M=[[0]*L[0]for _ in range(L[0])]
                    M[l[0]][l[1]]=1
                    DFS(l[0],l[1],1)
                A[i][j]+=d+1
    print('#%d %d'%(t+1,R))