import sys
sys.stdin = open('bj1938.txt','r')

dx=[0,0,-1,1]
dy=[-1,1,0,0]
from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N and A[y][x]!='1'
def Start():
    q=deque()
    for i in range(N):
        for j in range(N):
            if A[i][j]=='B':
                if A[i+1][j]=='B':t, y1,x1,y2,x2,y3,x3=0,i,j,i+1,j,i+2,j
                else:t, y1,x1,y2,x2,y3,x3=1,i,j,i,j+1,i,j+2
                q.append((0,t,y1,x1,y2,x2,y3,x3))
                V[y2][x2][t]=1
                return q
def T(y,x):
    for Y,X in (y-1,x),(y+1,x),(y,x-1),(y,x+1),(y-1,x+1),(y-1,x-1),(y+1,x+1),(y+1,x-1):
        if not IS(Y,X) or A[Y][X]=='1':return 1
    return 0
N=int(input())
A=[input()for _ in range(N)]
V=[[[0,0]for _ in range(N)] for _ in range(N)]
Q=Start()
R=0
while Q:
    c,t,y1,x1,y2,x2,y3,x3=Q.popleft()
    if A[y1][x1]==A[y2][x2]==A[y3][x3]=='E':R=c;break
    for d in range(4):
        Y1,X1,Y2,X2,Y3,X3=y1+dy[d],x1+dx[d],y2+dy[d],x2+dx[d],y3+dy[d],x3+dx[d]
        if IS(Y1,X1) and IS(Y2,X2) and IS(Y3,X3) and V[Y2][X2][t]==0:
            V[Y2][X2][t]=1
            Q.append((c+1,t,Y1,X1,Y2,X2,Y3,X3))
    t=(t+1)%2
    if V[y2][x2][t] or T(y2,x2):continue
    if t:Y1,X1,Y3,X3=y1+1,x1-1,y3-1,x3+1
    else:Y1,X1,Y3,X3=y1-1,x1+1,y3+1,x3-1
    V[y2][x2][t]=1
    Q.append((c+1,t,Y1,X1,y2,x2,Y3,X3))
print(R)