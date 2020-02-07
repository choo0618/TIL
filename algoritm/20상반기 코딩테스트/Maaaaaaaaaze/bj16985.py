import sys
sys.stdin = open('bj16985.txt','r')

import itertools
from collections import deque
dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]
def IS(z,y,x):
    return -1<z<5 and -1<y<5 and -1<x<5
def BFS():
    V=[[[0]*5 for _ in range(5)]for __ in range(5)]
    Que=deque([(0,0,0,0)])
    V[0][0][0]=1
    while Que:
        z,y,x,c=Que.popleft()
        for d in range(6):
            Z,Y,X=z+dz[d],y+dy[d],x+dx[d]
            if IS(Z,Y,X) and A[Z][Y][X] and not V[Z][Y][X]:
                if Z==Y==X==4:return c+1
                Que.append((Z,Y,X,c+1))
                V[Z][Y][X]=1
    return 987654321
def DFS(x):
    global A,R
    if x==5:
        C=BFS()
        R=min(R,C)
        return
    for t in range(4):
        A[x]=list(map(list,zip(*A[x][::-1])))
        if (not x and not A[x][0][0]) or (x==4 and not A[x][4][4]):continue
        DFS(x+1)
Arr=[[[int(x)for x in input().split()]for y in range(5)]for z in range(5)]
R=987654321
for p in itertools.permutations([0,1,2,3,4]):
    A=[]
    for i in p:A.append(Arr[i])
    DFS(0)
print(-1 if R==987654321 else R)