import sys
sys.stdin = open('1949.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<N
def DFS(y,x,r,c):
    global R
    R=max(R,r)
    V[y][x]=1
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X) and V[Y][X]==0:
            if A[Y][X]>=A[y][x] and c:
                for k in range(1,K+1):
                    if A[Y][X]-k>=A[y][x]:continue
                    A[Y][X]-=k
                    DFS(Y,X,r+1,0)
                    A[Y][X]+=k
            elif A[Y][X]<A[y][x]:DFS(Y,X,r+1,c)
    V[y][x]=0
for t in range(int(input())):
    N,K=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    M=max(max(a)for a in A)
    R=1
    V=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j]==M:DFS(i,j,1,1)
    print('#%d %d'%(t+1,R))