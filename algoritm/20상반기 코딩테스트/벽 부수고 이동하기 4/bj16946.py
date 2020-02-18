import sys
sys.stdin=open('bj16946.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x):
    Map=[[0]*M for _ in range(N)]
    Map[y][x]=1
    Q=deque([(y,x)])
    List=[(y,x)]
    while Q:
        hy,hx=Q.popleft()
        for d in range(4):
            Y,X=hy+dy[d],hx+dx[d]
            if IS(Y,X) and not A[Y][X] and not Map[Y][X]:
                List.append((Y,X))
                Map[Y][X]=1
                Q.append((Y,X))
    return List,len(List)
def Check(y,x):
    r=1
    check=[0]*(n+1)
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and not check[IN[Y][X]]:r+=IL[Y][X];check[IN[Y][X]]=1
    return r
N,M=map(int,input().split())
A=[list(map(int,input()))for _ in range(N)]
IL=[[0]*M for _ in range(N)]
IN=[[0]*M for _ in range(N)]
R=[[0]*M for _ in range(N)]
n=0
for i in range(N):
    for j in range(M):
        if not A[i][j] and not IL[i][j]:
            n+=1
            l,tmp=BFS(i,j)
            for ti,tj in l:IL[ti][tj]=tmp;IN[ti][tj]=n
for i in range(N):
    for j in range(M):
        if A[i][j]:
            tmp=Check(i,j)
            R[i][j]=tmp
for p in R:print(''.join(map(str,p)))


# from collections import deque
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# def IS(y,x):
#     return -1<y<N and -1<x<M
# def BFS(y,x):
#     Map=[[0]*M for _ in range(N)]
#     Map[y][x]=1
#     Q=deque([(y,x)])
#     List=[(y,x)]
#     while Q:
#         hy,hx=Q.popleft()
#         for d in range(4):
#             Y,X=hy+dy[d],hx+dx[d]
#             if IS(Y,X) and not A[Y][X] and not Map[Y][X]:
#                 List.append((Y,X))
#                 Map[Y][X]=1
#                 Q.append((Y,X))
#     return len(List)
# N,M=map(int,input().split())
# A=[list(map(int,input()))for _ in range(N)]
# R=[[0]*M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if A[i][j]:R[i][j]=BFS(i,j)
# for p in R:print(''.join(map(str,p)))