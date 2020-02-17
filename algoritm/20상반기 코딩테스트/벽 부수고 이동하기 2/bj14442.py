import sys
sys.stdin = open('bj14442.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
N,M,K=map(int,input().split())
A=[list(map(int,input()))for y in range(N)]
Map=[[[-1]*M for _ in range(N)]for __ in range(K+1)]
Q=deque([(0,0,0,1)])
R=0
while Q:
    b,y,x,l=Q.popleft()
    if (y,x)==(N-1,M-1):R=l;break
    for d in range(4):
        B,Y,X=b,y+dy[d],x+dx[d]
        if IS(Y,X):
            if A[Y][X]:B+=1
            if B<=K and Map[B][Y][X]==-1:
                Map[B][Y][X]=l+1
                Q.append((B,Y,X,l+1))
print(R if R else -1)
