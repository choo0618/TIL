import sys
sys.stdin = open('bj1857.txt','r')

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
def IS(y,x):
    return -1<y<M and -1<x<N
M,N=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(M)]
for i in range(M):
    for j in range(N):
        if A[i][j]==3:S=(i,j,0)
        elif A[i][j]==4:E=(i,j)
Que=[S]
Map=[[[999]*8 for _ in range(N)]for __ in range(M)]
Map[Que[0][0]][Que[0][1]]=[0]*8
Min=987654321
while Que:
    Q=[]
    for q in Que:
        if (q[0],q[1])==E:
            Min=min(q[2],Min)
            continue
        for d in range(8):
            nY,nX,nC=q[0]+dy[d],q[1]+dx[d],q[2]
            if IS(nY,nX) and A[nY][nX]!=2:
                if not A[nY][nX]:nC+=1
                if Map[nY][nX][d]>nC:
                    Map[nY][nX][d]=nC
                    Q.append((nY,nX,nC))
    Que=Q
print(Min)
Que=[S]
Map=[[[999]*8 for _ in range(N)]for __ in range(M)]
Map[Que[0][0]][Que[0][1]]=[0]*8
R=0
while Que:
    Q=[]
    for q in Que:
        if q[2]==Min:
            if (q[0],q[1])==E:R+=1
            continue
        for d in range(8):
            nY,nX,nC=q[0]+dy[d],q[1]+dx[d],q[2]
            if IS(nY,nX) and A[nY][nX]!=2:
                if (nC==Min and (nY,nX)!=E) or Map[nY][nX][d]<nC:continue
                if not A[nY][nX]: nC += 1
                Map[nY][nX][d]=nC
                Q.append((nY,nX,nC))
    Que=Q
print(Min)
print(R)

