import sys
sys.stdin = open('bj13460.txt','r')

#상 우 하 좌
dx=[0,1,0,-1]
dy=[-1,0,1,0]
def DFS(r,b,d,rr):
    global R,H
    if r==H:
        R=rr
        return
    
    for dir in range(4):
        rY,bY=r[0]+dy[dir],b[0]+dy[dir]
        rX,bX=r[1]+dx[dir],b[1]+dx[dir]
        if A[rY][rX]=='.':

            DFS()

L=[int(x)for x in input().split()]
A=[input()for y in range(L[0])]
R=-1
print(A)
r,b,H=0,0,0
for y in range(L[0]):
    for x in range(L[1]):
        if A[y][x]=='R':r=[y,x]
        elif A[y][x]=='B':b=[y,x]
        elif A[y][x]=='O':H=[y,x]
DFS(r,b,4,0)