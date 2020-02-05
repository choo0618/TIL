import sys
sys.stdin = open('bj1944.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(q):
    Map=[[0]*N for _ in range(N)]
    Map[q[0]][q[1]]=1
    Q=deque([q])
    while Q:
        y,x,dis,t=Q.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and Arr[Y][X]!='1' and not Map[Y][X]:
                if Arr[Y][X]=='S' or Arr[Y][X]=='K':
                    if not Dis[t][Dic[(Y,X)]]:
                        L.append((dis+1,t,Dic[(Y,X)]))
                    Dis[t][Dic[(Y,X)]]=dis+1
                    Dis[Dic[(Y,X)]][t]=dis+1
                Map[Y][X]=1
                Q.append((Y,X,dis+1,t))
def MST():
    P=list(range(tmp))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R,k=0,0
    for l in L:
        if k==tmp-1:break
        c,a,b=l
        if find(a)!=find(b):R+=c;union(a,b);k+=1
    if k==tmp-1:return R
    return -1
N,M=map(int,input().split())
Arr=[input()for _ in range(N)]
Dic,tmp,Que={},1,[]
for i in range(N):
    for j in range(N):
        if Arr[i][j]=='S':Dic[(i,j)]=0;Que.append((i,j,0,0))
        elif Arr[i][j]=='K':Dic[(i,j)]=tmp;Que.append((i,j,0,tmp));tmp+=1
Dis=[[0]*tmp for _ in range(tmp)]
L=[]
for q in Que:BFS(q)
L.sort()
print(MST())