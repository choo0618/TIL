import sys
sys.stdin = open('bj17244.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<M and -1<x<N
def BFS(i):
    V=[[0]*N for _ in range(M)]
    V[i[0]][i[1]]=1
    Que=deque([i])
    while Que:
        y,x,t,c=Que.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and Arr[Y][X]!='#' and not V[Y][X]:
                if Arr[Y][X]!='.':
                    Map[t][Arr[Y][X]]=c+1
                    Map[Arr[Y][X]][t]=c+1
                V[Y][X]=1
                Que.append((Y,X,t,c+1))
def DFS(x,c,r):
    global R
    if c==tmp-2:
        R=min(R,r+Map[x][tmp-1])
        return
    if r>=R:return
    for i in range(tmp-1):
        if V[i]:continue
        V[i]=1
        DFS(i,c+1,r+Map[x][i])
        V[i]=0
N,M=map(int,input().split())
Arr=[list(map(str,input()))for _ in range(M)]
List,tmp=[],1
for i in range(M):
    for j in range(N):
        if Arr[i][j]=='S':Arr[i][j]=0;List.append((i,j,0,0))
        elif Arr[i][j]=='E':E=(i,j);continue
        elif Arr[i][j]=='X':Arr[i][j]=tmp;List.append((i,j,tmp,0));tmp+=1
Arr[E[0]][E[1]]=tmp;List.append((E[0],E[1],tmp,0));tmp+=1
Map=[[0]*(tmp)for _ in range(tmp)]
for i in List:BFS(i)
R=10**9
V=[1]+[0]*(tmp-1)
DFS(0,0,0)
print(R)
