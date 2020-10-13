import sys
sys.stdin = open('bj17837.txt','r')

dx=[1,-1,0,0]
dy=[0,0,-1,1]
dd=[1,0,3,2]
def IS(y,x):
    return -1<y<N and -1<x<N and A[y][x]!=2
N,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[[[]for x in range(N)]for y in range(N)]
H=[]
for k in range(K):
    y,x,d=map(int,input().split())
    Map[y-1][x-1].append(k)
    H.append([y-1,x-1,d-1])
R=-1
for t in range(1000):
    for i in range(K):
        y,x,d=H[i]
        Y,X=y+dy[d],x+dx[d]
        if not IS(Y,X):
            d=dd[d]
            Y,X=y+dy[d],x+dx[d]
        H[i][2]=d
        if not IS(Y,X):continue
        idx=Map[y][x].index(i)
        tmp=Map[y][x][idx:]
        Map[y][x]=Map[y][x][:idx]
        for j in tmp:H[j][0],H[j][1]=Y,X
        if A[Y][X]==1:tmp.reverse()
        Map[Y][X]+=tmp
        if len(Map[Y][X])>=4:R=t+1
    if R!=-1:break
print(R)



