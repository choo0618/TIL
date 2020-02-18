import sys
sys.stdin=open('bj16933.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
N,M,K=map(int,input().split())
A=[list(map(int,input()))for y in range(N)]
Map=[[[0]*M for _ in range(N)]for __ in range(K+1)]
Map[0][0][0]=1
Q=deque([(0,0,0,1)])
R=-1
while Q:
    y,x,k,Day=Q.popleft()
    if (y,x)==(N-1,M-1):R=Day;break
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and A[Y][X]:
            if k==K:continue
            if not Map[k+1][Y][X]:
                if not Day%2:
                    Q.append((y,x,k,Day+1))
                else:
                    Map[k+1][Y][X]=1
                    Q.append((Y,X,k+1,Day+1))
        elif IS(Y,X) and not A[Y][X]:
            if not Map[k][Y][X]:
                Map[k][Y][X]=1
                Q.append((Y,X,k,Day+1))
print(R)