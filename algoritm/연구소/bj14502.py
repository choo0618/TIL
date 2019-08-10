import sys
sys.stdin = open('bj14502.txt','r')

import itertools,copy
dy=[-1,0,1,0]
dx=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1] and (not M[y][x]):return True
    return False
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
R=0
c=[]
Q=[]
for i in range(L[0]):
    for j in range(L[1]):
        if not A[i][j]:c.append([i,j])
        elif A[i][j]==2:Q.append([i,j])
C=[]
for _ in range(len(C)):
    c.append(_)
C=list(itertools.combinations(c,3))
for _ in C:
    q=[]+Q
    r=0
    M=copy.deepcopy(A)
    for w in _:
        M[w[0]][w[1]]=1
    while q:
        tmp=q.pop(0)
        hY=tmp[0]
        hX=tmp[1]
        for dir in range(4):
            nY=hY+dy[dir]
            nX=hX+dx[dir]
            if IS(nY,nX):
                M[nY][nX]=2
                q.append([nY,nX])
    for y in range(L[0]):
        for x in range(L[1]):
            if not M[y][x]:r+=1
    if r>R:R=r
print(R)