import sys
sys.stdin = open('bj15644.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def Move(y,x,d):
    t=0
    while A[y+dy[d]][x+dx[d]]!='#' and A[y][x]!='O':
        y+=dy[d];x+=dx[d]
        t+=1
    return y,x,t
N,M=map(int,input().split())
A=[input()for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j]=='R':ry,rx=i,j
        elif A[i][j]=='B':by,bx=i,j
V=[[[[0]*M for _ in range(N)]for __ in range(M)]for ___ in range(N)]
V[ry][rx][by][bx]=1
Q=deque([(ry,rx,by,bx,'',0)])
R=0
while Q:
    ry,rx,by,bx,s,cnt=Q.popleft()
    if A[ry][rx]=='O':R=s;break
    for d,c in enumerate('RDLU'):
        rY,rX,rt=Move(ry,rx,d)
        bY,bX,bt=Move(by,bx,d)
        if A[rY][rX]==A[bY][bX]=='O':continue
        if (rY,rX)==(bY,bX):
            if rt>bt:rY-=dy[d];rX-=dx[d]
            else:bY-=dy[d];bX-=dx[d]
        if V[rY][rX][bY][bX] or cnt>=10:continue
        V[rY][rX][bY][bX]=1
        Q.append((rY,rX,bY,bX,s+c,cnt+1))
if R:print(len(R));print(R)
else:print(-1)