import sys
sys.stdin = open('bj19237.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<N
dy=[-1,1,0,0]
dx=[0,0,-1,1]
N,M,K=map(int,input().split())
Map=[[int(x)for x in input().split()]for y in range(N)]
Shark=[int(x)-1for x in input().split()]
R,cnt=0,M
for i in range(N):
    for j in range(N):
        m=Map[i][j]
        if Map[i][j]:Shark[m-1]=[i,j,Shark[m-1],m];Map[i][j]=[m,K]
        else:Map[i][j]=[0,0]
Pri=[0]
for P in range(M):
    p=[]
    for _ in range(4):p.append([int(x)-1for x in input().split()])
    Pri.append(p)
while R<=1000 and M>1:
    for i in range(N):
        for j in range(N):
            if Map[i][j][0]:
                Map[i][j][1]-=1
                if Map[i][j][1]==-1:Map[i][j]=[0,0]
    tmp,cnt=[],0
    for _ in range(M):
        y,x,d,m=Shark[_]
        cnt+=1
        chk=0
        for D in Pri[m][d]:
            Y,X=y+dy[D],x+dx[D]
            if IS(Y,X) and Map[Y][X][0]==0:
                tmp.append([Y,X,D,m])
                chk=1
                break
        if chk:continue
        for D in Pri[m][d]:
            Y,X=y+dy[D],x+dx[D]
            if IS(Y,X) and Map[Y][X][0]==m:tmp.append([Y,X,D,m]);break
    Shark=[]
    for _ in range(cnt):
        y,x,d,m=tmp[_]
        if Map[y][x][0] and Map[y][x][0]!=m:M-=1;continue
        Map[y][x]=[m,K]
        Shark.append([y,x,d,m])
    R+=1
print(R if R!=1001 else -1)