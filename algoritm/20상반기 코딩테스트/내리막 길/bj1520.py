import sys
sys.stdin = open('bj1520.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<M
def DFS(y,x):
    # if (y,x)==(N-1,M-1):return 1
    if V[y][x]!=-1:return V[y][x]
    V[y][x]=0
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        Y,X=y+d[0],x+d[1]
        if IS(Y,X) and A[Y][X]<A[y][x]:
            V[y][x]+=DFS(Y,X)
    return V[y][x]
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[[-1]*M for _ in range(N)]
V[N-1][M-1]=1
print(DFS(0,0))