import sys
sys.stdin = open('bj16197.txt','r')

from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def IS(y,x):
    return -1<y<N and -1<x<M
N,M=map(int,input().split())
A=[input()for _ in range(N)]
Map=[[[[0]*M for _ in range(N)]for __ in range(M)]for ___ in range(N)]
C=[0]
for i in range(N):
    for j in range(M):
        if A[i][j]=='o':
            C.append(i)
            C.append(j)
Q=deque([C])
Map[C[1]][C[2]][C[3]][C[4]]=1
R=-1
while Q and R==-1:
    cnt,y1,x1,y2,x2=Q.popleft()
    for d in range(4):
        Cnt,Y1,X1,Y2,X2=cnt+1,y1+dy[d],x1+dx[d],y2+dy[d],x2+dx[d]
        r=IS(Y1,X1)+IS(Y2,X2)
        if r==1:R=Cnt;break
        elif not r:continue
        if A[Y1][X1]=='#':Y1,X1=y1,x1
        if A[Y2][X2]=='#':Y2,X2=y2,x2
        if not Map[Y1][X1][Y2][X2] and Cnt<10:
            Map[Y1][X1][Y2][X2]=1
            Q.append((Cnt,Y1,X1,Y2,X2))
print(R)
