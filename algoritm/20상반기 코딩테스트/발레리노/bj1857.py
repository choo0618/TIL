import sys
sys.stdin = open('bj1857.txt','r')

import heapq
dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
def IS(y,x):
    return -1<y<M and -1<x<N
M,N=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(M)]
for i in range(M):
    for j in range(N):
        if A[i][j]==3:S=(0,i,j)
        elif A[i][j]==4:E=(i,j)
Que=[S]
Map=[[[0]*8 for _ in range(N)]for __ in range(M)]
Map[Que[0][0]][Que[0][1]]=[0]*8
Min=987654321
R=0
while Que:
    C,Y,X=heapq.heappop(Que)
    if C>Min+1:continue
    if A[Y][X]==4:Min=min(Min,C);R+=1;continue
    for d in range(8):
        nY,nX,nC=Y+dy[d],X+dx[d],C
        if IS(nY,nX) and A[nY][nX]!=2 and not Map[nY][nX][d]:
            if not A[nY][nX]:nC+=1
            Map[nY][nX][d]=1
            heapq.heappush(Que,(nC,nY,nX))
print(Min)
print(R)

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



