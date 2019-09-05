import sys
sys.stdin = open('bj7562.txt','r')

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
def IS(y,x):
    if -1<y<N and -1<x<N and not M[y][x]:return True
    return False
T=int(input())
for t in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(2)]
    M=[[0]*N for _ in range(N)]
    M[A[0][1]][A[0][0]]=1
    Q=[[A[0][1],A[0][0],1]]
    while Q:
        q=[]
        for n in Q:
            for dir in range(8):
                nY=n[0]+dy[dir]
                nX=n[1]+dx[dir]
                d=n[2]
                if IS(nY,nX):M[nY][nX]=d+1;q.append([nY,nX,d+1])
        Q=q
    print(M[A[1][1]][A[1][0]]-1)