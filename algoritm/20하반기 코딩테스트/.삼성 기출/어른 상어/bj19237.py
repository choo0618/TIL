import sys
sys.stdin = open('bj19237.txt','r')

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def IS(y,x):
    return -1<y<N and -1<x<N
N,M,K=map(int,input().split())
A=[[int(x) for x in input().split()]for y in range(N)]
D=[0]+[int(x)-1 for x in input().split()]
PD=[0]+[[[int(x)-1for x in input().split()]for y in range(4)]for z in range(M)]
Shark,Area={},{}
for i in range(N):
    for j in range(N):
        tmp=A[i][j]
        if tmp:Shark[tmp],Area[(i,j)]=(i,j,PD[tmp][D[tmp]]),[tmp,K]
        else:Area[(i,j)]=0
Cnt,S=0,M
while Cnt<1001 and S!=1:
    L=[0]*(M+1)
    for i in range(1,M+1):
        if Shark[i]==0:continue
        y,x,dl=Shark[i]
        Chk,tmp=1,0
        for d in dl:
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X):
                if Area[(Y,X)]==0:L[i]=(Y,X,PD[i][d]);Chk=0;break
                if Area[(Y,X)][0]==i and tmp==0:tY,tX,td,tmp=Y,X,PD[i][d],1
        if Chk:L[i]=(tY,tX,td)
    for i in range(1,M+1):
        if L[i]==0:continue
        y,x,td=L[i]
        if Area[(y,x)] and Area[(y,x)][0]!=i:Shark[i]=0;S-=1
        else:Area[(y,x)],Shark[i]=[i,K+1],(y,x,td)
    for i in range(N):
        for j in range(N):
            if Area[(i,j)]!=0:
                Area[(i,j)][1]-=1
                if Area[(i,j)][1]==0:Area[(i,j)]=0
    Cnt+=1
print(Cnt if Cnt!=1001 else -1)