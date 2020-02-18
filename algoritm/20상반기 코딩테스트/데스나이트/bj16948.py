import sys
sys.stdin=open('bj16948.txt','r')

from collections import deque
dy=[-2,-2,0,0,2,2]
dx=[-1,1,-2,2,-1,1]
def IS(y,x):
    return -1<y<N and -1<x<N
N=int(input())
Y1,X1,Y2,X2=map(int,input().split())
Map=[[0]*N for _ in range(N)]
Map[Y1][X1]=1
Q=deque([(Y1,X1,0)])
R=-1
while Q:
    y,x,c=Q.popleft()
    if (y,x)==(Y2,X2):R=c;break
    for d in range(6):
        Y,X,C=y+dy[d],x+dx[d],c+1
        if IS(Y,X) and not Map[Y][X]:
            Map[Y][X]=1
            Q.append((Y,X,C))
print(R)