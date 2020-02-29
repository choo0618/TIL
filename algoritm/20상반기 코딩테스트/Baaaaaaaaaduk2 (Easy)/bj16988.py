import sys
sys.stdin = open('bj16988.txt','r')

import itertools,collections
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def Check(i,j):
    for d in range(4):
        I,J=i+dy[d],j+dx[d]
        if IS(I,J) and A[I][J]==2:return True
    return False
def BFS(i,j):
    Map[i][j]=1
    r,c=1,1
    Q=collections.deque([(i,j)])
    while Q:
        y,x=Q.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and not Map[Y][X] and A[Y][X]!=1:
                if not A[Y][X]:c=0
                Map[Y][X]=1
                r+=1
                Q.append((Y,X))
    return r if c else 0
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
L=[]
for i in range(N):
    for j in range(M):
        if not A[i][j] and Check(i,j):L.append((i,j))
Re=0
for (y1,x1),(y2,x2) in itertools.combinations(L,2):
    A[y1][x1],A[y2][x2]=1,1
    Map=[[0]*M for _ in range(N)]
    R=0
    for i in range(N):
        for j in range(M):
            if A[i][j]==2 and not Map[i][j]:R+=BFS(i,j)
    Re=max(Re,R)
    A[y1][x1],A[y2][x2]=0,0
print(Re)
