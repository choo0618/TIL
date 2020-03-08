import sys
sys.stdin = open('bj17780.txt','r')

dx=[1,-1,0,0]
dy=[0,0,-1,1]
def IS(y,x):
    return -1<y<N and -1<x<N and A[y][x]!=2
def Dir(d):
    if d%2:return d-1
    return d+1
N,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
D=[]
Map=[[[]for _ in range(N)]for __ in range(N)]
for i in range(K):
    y,x,d=map(int,input().split())
    Map[y-1][x-1].append(i)
    D.append([i,y-1,x-1,d-1])
R=-1
for t in range(1000):
    C=0
    for i,y,x,d in D:
        if Map[y][x][0]!=i:continue
        Y,X=y+dy[d],x+dx[d]
        if not IS(Y,X):
            d=Dir(d)
            D[i][3]=d
            Y+=2*dy[d]
            X+=2*dx[d]
            if not IS(Y,X):continue
        if A[Y][X]==1:Map[y][x].reverse()
        Map[Y][X]+=Map[y][x]
        Map[y][x]=[]
        for i in Map[Y][X]:D[i][1]=Y;D[i][2]=X
        if len(Map[Y][X])>=4:C=1;break
    if C:R=t+1;break
print(R)



