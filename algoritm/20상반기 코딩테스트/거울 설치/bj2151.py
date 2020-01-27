import sys
sys.stdin=open('bj2151.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
N=int(input())
Arr=[list(map(str,input()))for y in range(N)]
Que,Map,R=[],[[[999]*4for __ in range(N)] for _ in range(N)],987654321
for i in range(N):
    for j in range(N):
        if Arr[i][j]=='#':
            for d in range(4):
                y,x=i+dy[d],j+dx[d]
                if IS(y,x) and Arr[y][x]!='*':
                    Que.append((i,j,d,0))
            Arr[i][j]='*'
            break
    if Que:break
while Que:
    Q=[]
    for q in Que:
        if Arr[q[0]][q[1]]=='#' and q[3]<R:R=q[3];continue
        Y,X,M=q[0]+dy[q[2]],q[1]+dx[q[2]],q[3]
        if IS(Y,X) and Arr[Y][X]!='*':
            if Arr[Y][X]=='!':
                nM=M+1
                for d in [-1,1]:
                    nD=(q[2]+d)%4
                    if Map[Y][X][nD]<=nM:continue
                    Map[Y][X][nD]=nM
                    Q.append((Y,X,nD,nM))
            if Map[Y][X][q[2]]<=M:continue
            Map[Y][X][q[2]]=M
            Q.append((Y,X,q[2],M))
    Que=Q
if R==987654321:print(-1)
else:print(R)