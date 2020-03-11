import sys
sys.stdin = open('bj2636.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[[0]*M for _ in range(N)]
T,R=0,sum(sum(a)for a in A)
Q=deque([(0,0)])
while R:
    r=R
    q=deque()
    while Q:
        y,x=Q.popleft()
        if A[y][x]:A[y][x]=0;R-=1;q.append((y,x));continue
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and not V[Y][X]:
                V[Y][X]=1
                Q.append((Y,X))
    Q=q
    T+=1
print(T)
print(r)
