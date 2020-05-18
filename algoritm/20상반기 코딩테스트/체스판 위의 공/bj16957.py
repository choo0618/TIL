import sys
sys.stdin=open('bj16957.txt','r')

dx=[0,0,1,1,1,0,-1,-1,-1]
dy=[0,-1,-1,0,1,1,1,0,-1]
def DFS(y,x):
    if V[y][x]:return V[y][x]
    V[y][x]=(y,x)
    Y,X,c=y,x,300000
    for d in range(9):
        i,j=y+dy[d],x+dx[d]
        if -1<i<R and -1<j<C and A[i][j]<c:Y,X,c=i,j,A[i][j]
    V[y][x]=DFS(Y,X)
    i,j=V[y][x]
    Map[i][j]+=1
    return V[y][x]
R,C=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(R)]
Map=[[0]*C for _ in range(R)]
V=[[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not V[i][j]:DFS(i,j)
for i in range(R):print(*Map[i])