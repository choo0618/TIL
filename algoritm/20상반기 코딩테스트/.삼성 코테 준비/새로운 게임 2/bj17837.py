import sys
sys.stdin = open('bj17837.txt','r')

dx=[1,-1,0,0]
dy=[0,0,-1,1]
def IS(y,x):
    return -1<y<N and -1<x<N and A[y][x]!=2
N,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[[[]for x in range(N)]for y in range(N)]
L=[]
for i in range(K):
    y,x,d=map(int,input().split())
    L.append([y-1,x-1,d-1])
    Map[y-1][x-1].append(i)
R=-1
for t in range(1000):
    for i in range(K):
        y,x,d=L[i]
        Y,X=y+dy[d],x+dx[d]
        if not IS(Y,X):
            if d%2:d-=1
            else:d+=1
            Y,X=y+dy[d],x+dx[d]
        L[i][2]=d
        if not IS(Y,X):continue
        I=Map[y][x].index(i)
        l=Map[y][x][I:]
        if A[Y][X]==1:l.reverse()
        Map[Y][X]+=l
        for j in l:L[j][0],L[j][1]=Y,X
        Map[y][x]=Map[y][x][:I]
        if len(Map[Y][X])>=4:R=t+1
    if R!=-1:break
print(R)


