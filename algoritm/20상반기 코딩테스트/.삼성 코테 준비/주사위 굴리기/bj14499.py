import sys
sys.stdin = open('bj14499.txt','r')

from collections import deque
dx=[0,1,-1,0,0]
dy=[0,0,0,-1,1]
def IS(y,x):
    return -1<y<N and -1<x<M
def UD(t,a):
    D.rotate(t)
    D[a][0],D[a][2],D[1][0],D[1][2]=0,0,D[a][0],D[a][2]
def LR(t,a):
    D[1][a],D[3][1]=D[3][1],D[1][a]
    D[1].rotate(t)
N,M,y,x,k=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
D=deque(deque([0]*3)for _ in range(4))
for t in map(int,input().split()):
    if not IS(y+dy[t],x+dx[t]):continue
    x+=dx[t];y+=dy[t]
    if t==1:LR(-1,0)
    elif t==2:LR(1,2)
    elif t==3:UD(1,2)
    else:UD(-1,0)
    if A[y][x]:D[1][1],A[y][x]=A[y][x],0
    else:A[y][x]=D[1][1]
    print(D[3][1])
