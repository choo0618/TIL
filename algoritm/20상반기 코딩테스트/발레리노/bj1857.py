import sys
sys.stdin = open('bj1857.txt','r')

# import heapq
# dx=[1,2,2,1,-1,-2,-2,-1]
# dy=[-2,-1,1,2,2,1,-1,-2]
# def IS(y,x):
#     return -1<y<M and -1<x<N
# M,N=map(int,input().split())
# A=[[int(x)for x in input().split()]for y in range(M)]
# for i in range(M):
#     for j in range(N):
#         if A[i][j]==3:S=(0,i,j)
#         elif A[i][j]==4:E=(i,j)
# Que=[S]
# Map=[[[0]*8 for _ in range(N)]for __ in range(M)]
# Map[Que[0][0]][Que[0][1]]=[0]*8
# Min=987654321
# R=0
# while Que:
#     C,Y,X=heapq.heappop(Que)
#     if C>Min+1:continue
#     if A[Y][X]==4:Min=min(Min,C);R+=1;continue
#     for d in range(8):
#         nY,nX,nC=Y+dy[d],X+dx[d],C
#         if IS(nY,nX) and A[nY][nX]!=2 and not Map[nY][nX][d]:
#             if not A[nY][nX]:nC+=1
#             Map[nY][nX][d]=1
#             heapq.heappush(Que,(nC,nY,nX))
# print(Min)
# print(R)

# Que=[S]
# Map=[[[0]*8 for _ in range(N)]for __ in range(M)]
# Map[Que[0][0]][Que[0][1]]=[1]*8
# R=0
# while Que:
#     C,Y,X=heapq.heappop(Que)
#     for d in range(8):
#         nY,nX,nC=Y+dy[d],X+dx[d],C
#         if IS(nY,nX) and A[nY][nX]!=2:
#             if q[2]==Min and A[q[0]][q[1]]==4:R+=1;print(R);break
#             if not A[nY][nX]:nC+=1
#             Q.append((nY,nX,nC))
#     Que=Q
# print(Min)
# print(R)
#

from collections import deque
import heapq
dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
def IS(y,x):
    return -1<y<M and -1<x<N
def BFS(s,t):
    global Min,R
    que=[s]
    Map1=[[0]*N for _ in range(M)]
    Map2=[[0]*N for _ in range(M)]
    Map1[s[1]][s[2]]=1
    Map2[s[1]][s[2]]=1
    while que:
        c,y,x=heapq.heappop(que)
        if c>=Min:continue
        for d in range(8):
            Y,X,nC=y+dy[d],x+dx[d],c
            if IS(Y,X) and A[Y][X]!=2:
                if t:
                    if Map1[Y][X]:continue
                    if A[Y][X]==4:
                        Min = min(c+1,Min)
                        return
                else:
                    if A[Y][X]==4:R+=1;continue
                    if Map2[Y][X]:continue
                if A[Y][X]==0:
                    nC+=1
                if nC<Min:
                    if not A[Y][X]:Map2[Y][X]=1
                    Map1[Y][X]+=Map1[y][x]
                    heapq.heappush(que,(nC,Y,X))
    print(Map1)

M,N=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(M)]
for i in range(M):
    for j in range(N):
        if A[i][j]==3:S=(0,i,j)
        elif A[i][j]==4:E=(i,j)
Map=[[0]*N for _ in range(M)]
Que=[S]
Min,R=987654321,0
# while Que:
# s=heapq.heappop(Que)
# Map[S[1]][S[2]]=1
BFS(S,1)
BFS(S,0)
print(Min)
print(R)