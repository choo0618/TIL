import sys
sys.stdin = open('bj11967.txt','r')

from collections import deque
def IS(x,y):
    return -1<y<N and -1<x<N
N,M=map(int,input().split())
S=[[[]for _ in range(N)]for __ in range(N)]
for i in range(M):
    x,y,X,Y=map(int,input().split())
    S[x-1][y-1].append((X-1,Y-1))
R=0
light=[[0]*N for _ in range(N)]
light[0][0]=1
while True:
    C=1
    Q=deque([(0,0)])
    V=[[0]*N for _ in range(N)]
    V[0][0]=1
    while Q:
        x,y=Q.popleft()
        for X,Y in S[x][y]:
            if not light[X][Y]:light[X][Y]=1;C=0
        for X,Y in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
            if IS(X,Y) and light[X][Y] and not V[X][Y]:
                V[X][Y]=1
                Q.append((X,Y))
    if C:break
print(sum(sum(l)for l in light))



