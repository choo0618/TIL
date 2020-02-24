import sys
sys.stdin = open('bj18405.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
N,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
S,X,Y=map(int,input().split())
Q=[]
for i in range(N):
    for j in range(N):
        if A[i][j]:Q.append((A[i][j],i,j))
Q.sort()
for _ in range(S):
    q=[]
    for t,y,x in Q:
        for d in range(4):
            nY,nX=y+dy[d],x+dx[d]
            if IS(nY,nX) and not A[nY][nX]:
                A[nY][nX]=t
                q.append((t,nY,nX))
    Q=q
print(A[X-1][Y-1])

