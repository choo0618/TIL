import sys
sys.stdin = open('bj2178.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0]and-1<x<L[1]:return True
    return False
L=[int(x)for x in input().split()]
A=[list(map(int,input()))for y in range(L[0])]
R=0
Q=[[0,0,1]]
while Q:
    hY,hX,hD=Q.pop(0)
    if [hY,hX]==[L[0]-1,L[1]-1]:R=hD;break
    for dir in range(4):
        nY=hY+dy[dir]
        nX=hX+dx[dir]
        if IS(nY,nX) and A[nY][nX]:A[nY][nX]=0;Q.append([nY,nX,hD+1])
print(R)