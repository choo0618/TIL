import sys
sys.stdin = open('1953.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
P=[[0,0,0,0],[1,1,1,1],[0,1,0,1],[1,0,1,0],[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
for t in range(int(input())):
    N,M,R,C,L=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    V=[[0]*M for _ in range(N)]
    V[R][C]=1
    Q=deque([(R,C,L,A[R][C])])
    r=0
    while Q:
        y,x,l,p=Q.popleft()
        if not l:break
        r+=1
        for d in range(4):
            if not P[p][d]:continue
            Y,X=y+dy[d],x+dx[d]
            if (-1<Y<N and -1<X<M) and not V[Y][X] and P[A[Y][X]][(d+2)%4]:
                V[Y][X]=1
                Q.append((Y,X,l-1,A[Y][X]))
    print('#%d %d'%(t+1,r))