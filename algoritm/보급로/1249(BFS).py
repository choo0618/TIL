import sys
sys.stdin = open('1249.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<N and -1<x<N:return True
    return False
T=int(input())
for n in range(T):
    N=int(input())
    A=[list(map(int,input()))for y in range(N)]
    M=[[-1]*N for _ in range(N)]
    Q=deque()
    Q.append([0,0,0])
    M[0][0]=0
    while Q:
        hY,hX,r=Q.popleft()
        for dir in range(4):
            if IS(hY+dy[dir],hX+dx[dir]):
                nY=hY+dy[dir]
                nX=hX+dx[dir]
                nR=r+A[nY][nX]
                if M[nY][nX]==-1 or M[nY][nX]>nR:
                    M[nY][nX]=nR
                    Q.append([nY,nX,nR])
    print('#%d %d'%(n+1,M[N-1][N-1]))
