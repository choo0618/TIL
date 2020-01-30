import sys
sys.stdin=open('bj1261.txt','r')

import heapq
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
M,N=map(int,input().split())
Arr=[list(map(int,input()))for _ in range(N)]
Map=[[0]*M for _ in range(N)]
Map[0][0]=1
Que=[(1,0,0)]
while Que:
    c,y,x=heapq.heappop(Que)
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and not Map[Y][X]:
            if Arr[Y][X]==0:
                Map[Y][X]=c
                heapq.heappush(Que,(c,Y,X))
            else:
                Map[Y][X]=c+1
                heapq.heappush(Que,(c+1,Y,X))
print(Map[N-1][M-1]-1)

# from collections import deque
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# def IS(y,x):
#     return -1<y<N and -1<x<M
# def BFS(y,x,tmp):
#     Que=deque([(y,x)])
#     Map[y][x]=tmp
#     Dic[tmp]=[(y,x,0)]
#     while Que:
#         Y,X=Que.popleft()
#         for d in range(4):
#             nY,nX=Y+dy[d],X+dx[d]
#             if IS(nY,nX) and not Map[nY][nX] and not Arr[nY][nX]:
#                 Map[nY][nX]=tmp
#                 Dic[tmp].append((nY,nX,0))
#                 Que.append((nY,nX))
# def DBFS(now,Q):
#     Map1=[[0]*M for _ in range(N)]
#     Que=deque(Q)
#     while Que:
#         y,x,dis=Que.popleft()
#         for d in range(4):
#             Y,X=y+dy[d],x+dx[d]
#             if IS(Y,X) and Map[Y][X]!=now and not Map1[Y][X]:
#                 if Arr[Y][X]==1:
#                     Map1[Y][X]=1
#                     Que.append((Y,X,dis+1))
#                 elif Arr[Y][X]!=now and (Dis[now][Map[Y][X]]>dis or Dis[now][Map[Y][X]]==-1):
#                     Dis[now][Map[Y][X]]=dis
#                     Dis[Map[Y][X]][now]=dis
# M,N=map(int,input().split())
# Arr=[list(map(int,input()))for _ in range(N)]
# Map=[[0]*M for _ in range(N)]
# tmp,Dic=0,{}
# for i in range(N):
#     for j in range(M):
#         if Arr[i][j]==0 and not Map[i][j]:tmp+=1;BFS(i,j,tmp)
# Dis=[[-1]*(tmp+1) for _ in range(tmp+1)]
# for d in Dic.items():
#     DBFS(d[0],d[1])
#     Dis[d[0]][d[0]]=0
# Re=[987654321]*(tmp+1)
# Re[1]=0
# Que=deque([(1,0)])
# while Que:
#     n,dis=Que.popleft()
#     for d in range(tmp+1):
#         if not d or n==d or Dis[n][d]==-1:continue
#         nD=Dis[n][d]+dis
#         if nD<Re[d]:
#             Re[d]=Dis[n][d]+dis
#             Que.append((d,nD))
# print(Re[Map[N-1][M-1]])