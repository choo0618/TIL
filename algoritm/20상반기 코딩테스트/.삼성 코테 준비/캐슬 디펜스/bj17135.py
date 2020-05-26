import sys
sys.stdin = open('bj17135.txt','r')

import itertools
from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,D):
    Q=deque([(y,x,D)])
    while Q:
        y,x,c=Q.popleft()
        if A[y][x]:Set.add((y,x));return
        for Y,X in (y,x-1),(y-1,x),(y,x+1):
            if IS(Y,X) and c:Q.append((Y,X,c-1))
N,M,D=map(int,input().split())
D-=1
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for C in itertools.combinations(range(M),3):
    Set=set()
    for i in range(N-1,-1,-1):
        for j in C:BFS(i,j,D)
        for y,x in Set:A[y][x]=0
    for i,j in Set:A[i][j]=1
    R=max(R,len(Set))
print(R)
