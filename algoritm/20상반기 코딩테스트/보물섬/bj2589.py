import sys
sys.stdin = open('bj2589.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]=='L'
def BFS(y,x):
    V=[[0]*M for _ in range(N)]
    Que=[[y,x]]
    V[y][x],tmp=1,0
    while Que:
        tmp+=1
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX) and not V[nY][nX]:
                    V[nY][nX]=tmp
                    Q.append([nY,nX])
        Que=Q
    return tmp-1
N,M=map(int,input().split())
A=[input()for _ in range(N)]
R=0
for i in range(N):
    for j in range(M):
        if A[i][j]=='L':
            r=BFS(i,j)
            if r>R:R=r
print(R)