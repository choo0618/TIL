import sys
sys.stdin = open('bj7576.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[1]and -1<x<L[0]and not A[y][x]:return True
    return False
def C():
    for i in range(L[1]):
        for j in range(L[0]):
            if not A[i][j]:return False
    return True
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[1])]
Q=[]
for i in range(L[1]):
    for j in range(L[0]):
        if A[i][j]==1:Q.append([i,j,1])
R=1
while Q:
    q=[]
    for t in Q:
        for dir in range(4):
            nY=t[0]+dy[dir]
            nX=t[1]+dx[dir]
            if IS(nY,nX):A[nY][nX]=t[2]+1;R=t[2]+1;q.append([nY,nX,t[2]+1])
    Q=q
if C():print(R-1)
else:print(-1)
