import sys
sys.stdin = open('bj17472.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    island=[(y,x)]
    Que=deque([(y,x)])
    Map[y][x]=t
    while Que:
        Y,X=Que.pop()
        for d in range(4):
            nY,nX=Y+dy[d],X+dx[d]
            if IS(nY,nX) and Arr[nY][nX] and not Map[nY][nX]:
                Map[nY][nX]=t
                island.append((nY,nX))
                Que.append((nY,nX))
    return island
def Go(y,x,d,i):
    t=0
    while True:
        t+=1
        y+=dy[d]
        x+=dx[d]
        if not IS(y,x) or Map[y][x]==i:break
        if Map[y][x] and Map[y][x]!=i:return Map[y][x],t
    return -1,-1
def DIS(IL,i):
    Dis=[-1]*tmp
    Que=deque(IL)
    while Que:
        y,x=Que.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and not Map[Y][X]:
                a,dis=Go(Y,X,d,i+1)
                if a!=-1 and dis>=2 and (Dis[a-1]==-1 or Dis[a-1]>dis):Dis[a-1]=dis
    for d in range(i+1,tmp):
        if Dis[d]>=2:D.append((Dis[d],i,d))
def MST(Dis):
    P=list(range(tmp))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(b)]=find(a)
    R,mst=0,[]
    for dis in Dis:
        d,a,b=dis
        if find(a)!=find(b):R+=d;union(a,b);mst.append((a,b))
    if len(mst)==tmp-1:return R
    return -1
N,M=map(int,input().split())
Arr=[[int(x)for x in input().split()]for y in range(N)]
Map,tmp,IsLand=[[0]*M for _ in range(N)],0,[]
for i in range(N):
    for j in range(M):
        if Arr[i][j] and not Map[i][j]:tmp+=1;IsLand.append(BFS(i,j,tmp))
D=[]
for i in range(tmp):DIS(IsLand[i],i)
D.sort()
print(MST(D))
