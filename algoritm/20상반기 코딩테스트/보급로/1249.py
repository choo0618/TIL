import sys
sys.stdin = open('1249.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
for t in range(int(input())):
    N=int(input())
    A=[list(map(int,input()))for y in range(N)]
    Map=[[10**9]*N for _ in range(N)]
    Q=deque([(0,0,0)])
    while Q:
        c,y,x=Q.popleft()
        if Map[y][x]<c:continue
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if not IS(Y,X) or Map[Y][X]<=c+A[Y][X]:continue
            Map[Y][X]=c+A[Y][X]
            Q.append((c+A[Y][X],Y,X))
    print('#%d %d'%(t+1,Map[N-1][N-1]))