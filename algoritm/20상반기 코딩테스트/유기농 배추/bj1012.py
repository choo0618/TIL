import sys
sys.stdin = open('bj1012.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M and Map[y][x]==-1

def BFS(y,x,t):
    Map[y][x]=t
    Que=[[y,x]]
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX):
                    Map[nY][nX]=t
                    Q.append([nY,nX])
        Que=Q
T=int(input())
for t in range(T):
    M,N,K=map(int,input().split())
    Map = [[0]*M for _ in range(N)]
    for i in range(K):
        x,y=map(int,input().split())
        Map[y][x]=-1
    tmp=1
    for i in range(N):
        for j in range(M):
            if Map[i][j]==-1:BFS(i,j,tmp);tmp+=1
    print(tmp-1)


