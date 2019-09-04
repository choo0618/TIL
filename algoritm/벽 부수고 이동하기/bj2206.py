import sys
sys.stdin = open('bj2206.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]:return True
    return False
L=[int(x)for x in input().split()]
A=[list(map(int,input()))for y in range(L[0])]
M=[[[0,0]for x in range(L[1])]for y in range(L[0])]
R=-1
Q=[[0,0,1,0]]
M[0][0]=[1,1]
while Q:
    hY,hX,d,w=Q.pop(0)
    if [hY,hX]==[L[0]-1,L[1]-1]:R=d;break
    for dir in range(4):
        nY=hY+dy[dir]
        nX=hX+dx[dir]
        nD=d+1
        if IS(nY,nX):
            if not A[nY][nX]and not M[nY][nX][w]:M[nY][nX][w]=nD;Q.append([nY,nX,nD,w])
            elif A[nY][nX]==1 and not w and not M[nY][nX][1]:M[nY][nX][1]=nD;Q.append([nY,nX,nD,w+1])
print(R)