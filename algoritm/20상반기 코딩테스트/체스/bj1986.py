import sys
sys.stdin = open('bj1986.txt','r')

from collections import deque
kd = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
def IS(y,x):
    return -1<y<N and -1<x<M and not Map[y][x]
def Queen(y,x):
    for d in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
        nY, nX = y+d[0], x+d[1]
        while IS(nY,nX) and not Map[nY][nX]:
            RM[nY][nX]=0
            nY+=d[0]
            nX+=d[1]

N,M=map(int,input().split())
Map = [[0]*M for _ in range(N)]
RM = [[1]*M for _ in range(N)]
Q = [int(x)for x in input().split()]
K = [int(x)for x in input().split()]
P = [int(x)for x in input().split()]
Que=deque()
for q in range(1,2*Q[0]+1,2):
    Map[Q[q]-1][Q[q+1]-1]=1
    Que.append([Q[q]-1,Q[q+1]-1,'Q'])
for k in range(1,2*K[0]+1,2):
    Map[K[k]-1][K[k+1]-1]=1
    Que.append([K[k]-1,K[k+1]-1,'K'])
for p in range(1,2*P[0]+1,2):Map[P[p]-1][P[p+1]-1]=1
while Que:
    y,x,s=Que.popleft()
    if s=='Q':Queen(y,x)
    else:
        for d in kd:
            nY = y+d[0]
            nX = x+d[1]
            if IS(nY,nX):RM[nY][nX]=0
R = 0
for m in RM:
    R+=sum(m)
print(R-Q[0]-K[0]-P[0])