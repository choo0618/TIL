import sys
sys.stdin = open('bj13460.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def move(y,x,d):
    cnt=0
    while A[y+dy[d]][x+dx[d]]!='#' and A[y][x]!='O':
        y+=dy[d]
        x+=dx[d]
        cnt+=1
    return (y,x,cnt)
N,M=map(int,input().split())
A=[input()for _ in range(N)]
R,B,T,Check=0,0,0,0
for i in range(N):
    for j in range(M):
        if A[i][j]=='R':R=(i,j)
        elif A[i][j]=='B':B=(i,j)
Map=[[[[-1]*M for _ in range(N)]for _ in range(M)] for _ in range(N)]
Que=[(R[0],R[1],B[0],B[1])]
while T!=11 and not Check:
    T+=1
    Q=[]
    for q in Que:
        RY,RX,BY,BX=q
        for d in range(4):
            nRY,nRX,tR=move(RY,RX,d)
            nBY,nBX,tB=move(BY,BX,d)
            if A[nBY][nBX]=='O':continue
            if A[nRY][nRX]=='O':Check=1;break
            if (nRY,nRX)==(nBY,nBX):
                if tR>tB:
                    nRY-=dy[d]
                    nRX-=dx[d]
                else:
                    nBY-=dy[d]
                    nBX-=dx[d]
            if Map[nRY][nRX][nBY][nBX]!=-1:continue
            Q.append(((nRY,nRX,nBY,nBX)))
            Map[nRY][nRX][nBY][nBX]=T
        if Check:break
    Que=Q
if T==11:print(-1)
else:print(T)
