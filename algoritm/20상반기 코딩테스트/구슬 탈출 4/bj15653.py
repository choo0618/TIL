import sys
sys.stdin = open('bj15653.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def Go(y,x):
    t=0
    while Arr[y][x]!='#':
        y+=dy[d]
        x+=dx[d]
        t+=1
        if Arr[y][x]=='O':return y,x,t
    return y-dy[d],x-dx[d],t
N,M=map(int,input().split())
Arr=[input()for _ in range(N)]
Map=[[[[0]*M for _ in range(N)]for __ in range(M)]for ___ in range(N)]
for i in range(N):
    for j in range(M):
        if Arr[i][j]=='R':R=(i,j)
        elif Arr[i][j]=='B':B=(i,j)
        elif Arr[i][j]=='O':O=(i,j)
Que=deque([(R,B,1)])
Map[R[0]][R[1]][B[0]][B[1]]=1
Check=-1
while Que and Check==-1:
    (ry,rx),(by,bx),t=Que.popleft()
    for d in range(4):
        rY,rX,rt=Go(ry,rx)
        bY,bX,bt=Go(by,bx)
        if (bY,bX)==O:continue
        if (rY,rX)==(bY,bX):
            if rt>bt:
                rY-=dy[d]
                rX-=dx[d]
            else:
                bY-=dy[d]
                bX-=dx[d]
        if (rY,rX)==O:Check=t;break
        if not Map[rY][rX][bY][bX]:
            Map[rY][rX][bY][bX]=1
            Que.append(((rY,rX),(bY,bX),t+1))
print(Check)

