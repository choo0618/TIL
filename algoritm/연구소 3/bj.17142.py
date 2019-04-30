import sys
sys.stdin = open('bj.17142.txt','r')
import itertools,copy
dy=[-1,0,1,0]
dx=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[0] and (not M[y][x] or M[y][x]=='*'):return True
    return False
def C():
    for y in range(L[0]):
        for x in range(L[0]):
            if not M[y][x]:return False
    return True
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
V=[]
for i in range(L[0]):
    for j in range(L[0]):
        if A[i][j]==2:
            V.append([i,j,0])
c=[]
for _ in range(len(V)):
    c.append(_)
comb=list(itertools.combinations(c,L[1]))
R=9999999
for a in comb:
    Q=[]
    M=copy.deepcopy(A)
    r=0
    for n in range(len(V)):
        if n in a:Q.append(V[n])
        else:M[V[n][0]][V[n][1]]='*'
    while Q:
        tmp=Q.pop(0)
        hY=tmp[0]
        hX=tmp[1]
        t=tmp[2]
        for dir in range(4):
            nY=hY+dy[dir]
            nX=hX+dx[dir]
            nt=t+1
            if IS(nY,nX):
                M[nY][nX]=nt
                Q.append([nY,nX,nt])
                if A[nY][nX]!=2:r=nt
    if C() and r<R:R=r
if R==9999999:print(-1)
else:print(R)