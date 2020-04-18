import sys
sys.stdin = open('bj10711.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
N,M=map(int,input().split())
A=[list(map(lambda x: int(x) if x.isdigit() else 0, list(input()))) for r in range(N)]
Q=deque()
for i in range(N):
    for j in range(M):
        if not A[i][j]:Q.append((i,j,0))
c=0
while Q:
    y,x,c=Q.popleft()
    for Y,X in (y-1,x),(y-1,x+1),(y,x+1),(y+1,x+1),(y+1,x),(y+1,x-1),(y,x-1),(y-1,x-1):
        if IS(Y,X) and A[Y][X]:
            A[Y][X]-=1
            if not A[Y][X]:Q.append((Y,X,c+1))
print(c)