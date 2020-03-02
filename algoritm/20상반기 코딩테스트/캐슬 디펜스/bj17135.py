import sys
sys.stdin = open('bj17135.txt','r')

import itertools
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,c):
    Q=[(y,x,c)]
    while Q:
        y,x,c=Q.pop(0)
        if A[y][x]:Set.add((y,x));return
        for Y,X in (y,x-1),(y-1,x),(y,x+1):
            if IS(Y,X) and c:Q.append((Y,X,c-1))
N,M,D=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for C in itertools.combinations(range(M),3):
    L,t=[],N-1
    while t!=-1:
        Set=set()
        for c in C:BFS(t,c,D-1)
        for i,j in Set:A[i][j]=0;L+=[(i,j)]
        t-=1
    R=max(R,len(L))
    for i,j in L:A[i][j]=1
print(R)
