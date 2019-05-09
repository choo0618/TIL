import sys
sys.stdin = open('bj15683.txt','r')

import copy
d=[0,4,2,4,4,1]
dy=[[0,0,0,0],[[-1],[0],[1],[0]],[[0,0],[-1,1]],[[-1,0],[0,1],[1,0],[0,-1]],[[-1,0,0],[1,0,-1],[0,1,0],[1,0,-1]],[[1,1,1,1]]]
dx=[[0,0,0,0],[[0],[1],[0],[-1]],[[-1,1],[0,0]],[[0,1],[1,0],[0,-1],[-1,0]],[[0,1,-1],[0,1,0],[1,0,-1],[0,-1,0]],[[1,1,1,1]]]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]:return True
    return False
def BFS(y,x,i):
    r=0
    for _ in range(d[i]):
        cnt=0
        M=copy.deepcopy(A)
        Q=[]
        Q.append([y,x])
        while Q:
            tmp=Q.pop(0)
            hY=tmp[0]
            hX=tmp[1]
            for dir in range(len(dy[i][_])):
                nY=hY+dy[i][_][dir]
                nX=hX+dx[i][_][dir]
                if IS(nY,nX) and not M[nY][nX]:

L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
print(L)
print(A)
R=0
for i in range(L[0]):
    for j in range(L[1]):
        if M[i][j] and M[i][j]!=6:
            BFS(i,j,M[i][j])