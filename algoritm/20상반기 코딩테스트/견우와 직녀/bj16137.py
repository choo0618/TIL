import sys
sys.stdin = open('bj16137.txt','r')

import heapq
def IS(y,x):
    return -1<y<N and -1<x<N
def Check(y,x):
    cnt=0
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X) and A[Y][X]==1:cnt+=1
        if cnt==2:return 1
    return 0
def Time(t,x):
    while t%x:t+=1
    return t,1
def BFS():
    V=[[10**9]*N for _ in range(N)]
    V[0][0]=0
    Q=[(0,0,0,0)]
    while Q:
        t,y,x,b=heapq.heappop(Q)
        if y==x==N-1:return t
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if not IS(Y,X):continue
            if b:
                if A[Y][X]==1 and V[Y][X]>t+1:V[Y][X]=y+1;heapq.heappush(Q,(t+1,Y,X,0))
            else:
                if A[Y][X]==0:continue
                T,B=t+1,0
                if A[Y][X]!=1:T,B=Time(T,A[Y][X])
                if V[Y][X]>T:V[Y][X]=T;heapq.heappush(Q,(T,Y,X,B))
    return 10**9
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
B=[]
for i in range(N):
    for j in range(N):
        if not A[i][j] and Check(i,j):B.append((i,j))
R=10**9
for i,j in B:
    A[i][j]=M
    R=min(R,BFS())
    A[i][j]=0
print(R)