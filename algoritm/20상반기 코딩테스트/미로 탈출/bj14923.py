import sys
sys.stdin = open('bj14923.txt','r')

from collections import deque
def IS(x,y):
    return -1<x<N and -1<y<M
N,M=map(int,input().split())
Hx,Hy=map(int,input().split())
Ex,Ey=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Q=deque([(Hx-1,Hy-1,0,0)])
Map=[[[0]*M for _ in range(N)]for __ in range(2)]
R=-1
while Q:
    x,y,w,d=Q.popleft()
    if (x,y)==(Ex-1,Ey-1):R=d;break
    for X,Y in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
        if IS(X,Y):
            W=w+A[X][Y]
            if W<2 and not Map[W][X][Y]:
                Map[W][X][Y]=1
                Q.append((X,Y,W,d+1))
print(R)

