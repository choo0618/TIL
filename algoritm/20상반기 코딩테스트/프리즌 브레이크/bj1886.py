# import sys
# sys.stdin = open('bj1886.txt','r')
#
# from collections import deque
# def IS(y,x):
#     return -1<y<N and -1<x<M and A[y][x]!='X' and A[y][x]!='D'
# def BFS(y,x,i):
#     dis=[]
#     Map=[[0]*M for _ in range(N)]
#     Q=deque([(y,x,0)])
#     while Q:
#         y,x,c=Q.popleft()
#         for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
#             if IS(Y,X) and not Map[Y][X]:
#                 Map[Y][X]=1
#                 Q.append((Y,X,c+1))
#                 Set.add(A[Y][X])
#                 if not c:C[A[Y][X]]=1;continue
#                 dis.append((c+1,A[Y][X]))
#     dis.sort()
#     D[i]=deque(dis)
# N,M=map(int,input().split())
# A=[list(map(str,input()))for _ in range(N)]
# D,d,t=[],0,0
# for i in range(N):
#     for j in range(M):
#         if A[i][j]=='D':d+=1;D.append((i,j))
#         elif A[i][j]=='.':A[i][j]=t;t+=1
# i,Set,C=0,set(),[0]*t
# for y,x in D:BFS(y,x,i);i+=1
# T=1 if len(Set)==t else -1
# while not all(C) and T!=-1:
#     T+=1
#     for i in range(d):
#         if not D[i]:continue
#         while D[i] and D[i][0][0]<=T:
#             c,s=D[i].popleft()
#             if C[s]:continue
#             C[s]=1
#             break
#         if all(C):break
# print(T if T!=-1 else 'impossible')


import sys
sys.stdin = open('bj1886.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!='X' and A[y][x]!='D'
def BFS(y,x,i):
    dis=[]
    Map=[[0]*M for _ in range(N)]
    Q=deque([(y,x,0)])
    while Q:
        y,x,c=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and not Map[Y][X]:
                Map[Y][X]=1
                Q.append((Y,X,c+1))
                Set.add(A[Y][X])
                dis.append((c+1,A[Y][X]))
    dis.sort()
    D[i]=dis
def DFS(x,T):
    V[x]=1
    for c,s in D[x]:
        if c>T:break
        if not C[s] and (b[s]==-1 or (not V[b[s]] or DFS(b[s],T))):
            a[x]=s
            b[s]=x
            C[s]=1
            return 1
    return 0
N,M=map(int,input().split())
A=[list(map(str,input()))for _ in range(N)]
D,d,t=[],0,0
for i in range(N):
    for j in range(M):
        if A[i][j]=='D':d+=1;D.append((i,j))
        elif A[i][j]=='.':A[i][j]=t;t+=1
i,Set,C=0,set(),[0]*t
for y,x in D:BFS(y,x,i);i+=1
r,T=0,0 if len(Set)==t else -1
while r!=t and T!=-1:
    T+=1
    a=[-1]*d
    b=[-1]*t
    for i in range(d):
        V=[0]*d
        r+=DFS(i,T)
print(T if T!=-1 else 'impossible')