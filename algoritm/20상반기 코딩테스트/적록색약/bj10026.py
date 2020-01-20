import sys
sys.stdin = open('bj10026.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x,c):
    global R1,R2
    Que=[[],[]]
    if not Map1[y][x]:
        R1+=1
        Map1[y][x]=R1
        Que[0].append([y,x])
    if not Map2[y][x]:
        R2+=1
        Map2[y][x]=R2
        Que[1].append([y,x])
    while Que[0] or Que[1]:
        Q=[[],[]]
        for idx,q in enumerate(Que):
            for qq in q:
                for d in range(4):
                    nY=qq[0]+dy[d]
                    nX=qq[1]+dx[d]
                    if not idx and IS(nY,nX)and not Map1[nY][nX] and A[nY][nX]==c:
                        Map1[nY][nX]=R1
                        Q[0].append([nY,nX])
                    if idx==1 and IS(nY,nX)and not Map2[nY][nX]:
                        if ((c=='R' or c=='G') and (A[nY][nX]=='R' or A[nY][nX]=='G')) or A[nY][nX]==c:
                            Map2[nY][nX]=R2
                            Q[1].append([nY,nX])
        Que=Q
N=int(input())
A=[input()for _ in range(N)]
Map1=[[0]*N for m in range(N)]
Map2=[[0]*N for m in range(N)]
R1,R2=0,0
for i in range(N):
    for j in range(N):
        if not Map1[i][j] or not Map2[i][j]:BFS(i,j,A[i][j])
print(R1,R2)