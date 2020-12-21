import sys
sys.stdin = open('bj20058.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def Ro(y,x,l):
    # tmp=[[A[i][j]for j in range(x,x+l)]for i in range(y,y+l)]
    # tmp=list(map(list,zip(*tmp[::-1])))
    # for i in range(y,y+l):
    #     for j in range(x,x+l):
    #         A[i][j]=tmp[i%l][j%l]
    #         if A[i][j]==0:tMap[i][j]=0
    for i in range(y,y+l):
        for j in range(x,x+l):
            Map[j+y-x][l-i-1+y+x]=A[i][j]
            if A[i][j]==0:tMap[j+y-x][l-i-1+y+x]=0
def Chk(y,x):
    c=0
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X):c+=tMap[Y][X]
    return c
def BFS(y,x):
    r=1
    V[y][x]=1
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X] and V[Y][X]==0:
                Q.append((Y,X))
                V[Y][X]=1
                r+=1
    return r
N,Q=map(int,input().split())
N=2**N
A=[[int(x)for x in input().split()]for y in range(N)]
R1,R2=sum(sum(a)for a in A),0
for L in map(int,input().split()):
    L=2**L
    Map=[[0]*N for _ in range(N)]
    tMap=[[1]*N for _ in range(N)]
    for i in range(0,N,L):
        for j in range(0,N,L):
            Ro(i,j,L)
    A=Map
    for i in range(N):
        for j in range(N):
            if A[i][j] and Chk(i,j)<3:A[i][j]-=1;R1-=1
V=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] and V[i][j]==0:R2=max(R2,BFS(i,j))
print(R1)
print(R2)