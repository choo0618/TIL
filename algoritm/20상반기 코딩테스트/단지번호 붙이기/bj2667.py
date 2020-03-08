import sys
sys.stdin = open('bj2667.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N and A[y][x]=='1' and not Map[y][x]
def BFS(y,x,t):
    r=1
    Map[y][x]=t
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X):Map[Y][X]=t;r+=1;Q.append((Y,X))
    R.append(r)
N=int(input())
A=[input()for _ in range(N)]
t,R,Map=0,[],[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j]=='1' and not Map[i][j]:t+=1;BFS(i,j,t)
R.sort()
print(t)
for _ in R:print(_)