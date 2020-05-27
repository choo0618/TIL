import sys
sys.stdin = open('bj17144.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
D=[[3,0,1,2],[1,0,3,2]]
def IS(y,x):
    return -1<y<R and -1<x<C
def Dust():
    Map=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j]==0:continue
            n,tmp=A[i][j],A[i][j]//5
            for y,x in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                if IS(y,x) and (y,x)!=(m,0) and (y,x)!=(m+1,0):
                    Map[y][x]+=tmp
                    n-=tmp
            Map[i][j]+=n
    return Map
def Air(y,t):
    Y,X=y,0
    for d in D[t]:
        while IS(Y+dy[d],X+dx[d]):
            if t and Y+dy[d]<y:break
            elif t==0 and Y+dy[d]>y:break
            A[Y][X]=A[Y+dy[d]][X+dx[d]]
            Y+=dy[d];X+=dx[d]
    A[y][0]=A[y][1]=0
R,C,T=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(R)]
for i in range(R):
    if A[i][0]==-1:m=i;break
A[m][0]=A[m+1][0]=0
for t in range(T):
    A=Dust()
    Air(m,0)
    Air(m+1,1)
print(sum(sum(x)for x in A))

