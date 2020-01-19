import sys
sys.stdin = open('bj2583.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<M and -1<x<N and not Map[y][x]

def BFS(y,x,tmp):
    Que=[[y,x]]
    Map[y][x]=tmp
    r=1
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX):
                    Map[nY][nX]=tmp
                    Q.append([nY,nX])
        r+=len(Q)
        Que=Q
    return r
M,N,K=map(int,input().split())
Map = [[0]*N for _ in range(M)]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            Map[y][x]=-1
tmp=0
R=[]
for i in range(M):
    for j in range(N):
        if not Map[i][j]:tmp+=1;R.append(BFS(i,j,tmp))
print(tmp)
R.sort()
for p in R:print(p,end=' ')