import sys
sys.stdin = open('bj16234.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x,t):
    l=[(y,x)]
    s,c=A[y][x],1
    V[y][x]=t
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and V[Y][X]==0 and L<=abs(A[y][x]-A[Y][X])<=R:
                V[Y][X]=t
                Q.append((Y,X))
                s+=A[Y][X];c+=1
                l.append((Y,X))
    for i,j in l:A[i][j]=s//c
N,L,R=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
r=0
while True:
    V=[[0]*N for _ in range(N)]
    tmp=0
    Sum=[0]
    for i in range(N):
        for j in range(N):
            if V[i][j]==0:tmp+=1;BFS(i,j,tmp)
    if tmp==N*N:break
    r+=1
print(r)