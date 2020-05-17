import sys
sys.stdin = open('bj16973.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def Check(i,j,d):
    if d==0:j+=W-1
    elif d==1:i+=H-1
    if not IS(i,j):return 0
    if d%2:
        for t in range(j,j+W):
            if A[i][t]:return 0
    else:
        for t in range(i,i+H):
            if A[t][j]:return 0
    return 1
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
H,W,sy,sx,ey,ex=map(int,input().split())
V=[[0]*M for _ in range(N)]
V[sy-1][sx-1]=1
Q=deque([(sy-1,sx-1,0)])
R=-1
while Q:
    y,x,c=Q.popleft()
    if (y,x)==(ey-1,ex-1):R=c;break
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and not V[Y][X] and Check(Y,X,d):V[Y][X]=1;Q.append((Y,X,c+1))
print(R)