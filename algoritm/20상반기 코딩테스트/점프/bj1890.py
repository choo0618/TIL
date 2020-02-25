import sys
sys.stdin = open('bj1890.txt','r')

def DFS(y,x,t):
    global R
    if y==x==N-1:return 1
    if V[y][x]!=-1:return V[y][x]
    V[y][x]=0
    for d in (0,1),(1,0):
        Y,X=y+t*d[0],x+t*d[1]
        if Y>=N or X>=N:continue
        V[y][x]+=DFS(Y,X,A[Y][X])
    return V[y][x]
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
V=[[-1]*N for _ in range(N)]
print(DFS(0,0,A[0][0]))

N=int(input())
DP=[[0]*N for _ in range(N)]
DP[0][0]=1
for i in range(N):
    for j,k in enumerate(map(int,input().split())):
        if k and i+k<N:DP[i+k][j]+=DP[i][j]
        if k and j+k<N:DP[i][j+k]+=DP[i][j]
print(DP[-1][-1])

