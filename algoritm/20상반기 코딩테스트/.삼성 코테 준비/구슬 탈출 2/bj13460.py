import sys
sys.stdin = open('bj13460.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
from collections import deque
def Move(y,x,d):
    t=0
    while A[y+dy[d]][x+dx[d]]!='#':
        t+=1
        y+=dy[d];x+=dx[d]
        if A[y][x]=='O':return y,x,t
    return y,x,t
N,M=map(int,input().split())
A=[input()for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j]=='B':by,bx=i,j
        elif A[i][j]=='R':ry,rx=i,j
V=[[[[0]*M for _ in range(N)]for __ in range(M)]for ___ in range(N)]
V[ry][rx][by][bx]=1
R,Q=-1,deque([(ry,rx,by,bx,0)])
while Q:
    ry,rx,by,bx,c=Q.popleft()
    if A[ry][rx]=='O':R=c;break
    if c==10:continue
    for d in range(4):
        rY,rX,rt=Move(ry,rx,d)
        bY,bX,bt=Move(by,bx,d)
        if A[rY][rX]==A[bY][bX]=='O' or A[bY][bX]=='O':continue
        if (rY,rX)==(bY,bX):
            if rt<bt:bY-=dy[d];bX-=dx[d]
            else:rY-=dy[d];rX-=dx[d]
        if V[rY][rX][bY][bX]:continue
        V[rY][rX][bY][bX]=1
        Q.append((rY,rX,bY,bX,c+1))
print(R)

