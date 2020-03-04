import sys
sys.stdin = open('1949.txt','r')

def DFS(y,x,r,c):
    global R
    R=max(R,r)
    V[y][x]=1
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if -1<Y<N and -1<X<N and not V[Y][X]:
            if A[Y][X]>=A[y][x] and c:
                for d in range(K,-1,-1):
                    if A[Y][X]-d<A[y][x]:
                        A[Y][X]-=d
                        DFS(Y,X,r+1,0)
                        V[Y][X]=0
                        A[Y][X]+=d
                    else:break
            elif A[Y][X]<A[y][x]:
                DFS(Y,X,r+1,c)
                V[Y][X]=0
for t in range(int(input())):
    N,K=map(int,input().split())
    A=[[int(x)for x in input().split()] for y in range(N)]
    M=max(max(x)for x in A)
    R=0
    for i in range(N):
        for j in range(N):
            if A[i][j]==M:
                V=[[0]*N for _ in range(N)]
                DFS(i,j,1,1)
    print('#%d %d'%(t+1,R))
