import sys
sys.stdin = open('bj3372.txt','r')

def DFS(y,x):
    if y==x==N-1:return 1
    if A[y][x]==0:return 0
    if DP[y][x]:return DP[y][x]
    for Y,X in (y,x+A[y][x]),(y+A[y][x],x):
        if Y>=N or X>=N:continue
        DP[y][x]+=DFS(Y,X)
    return DP[y][x]
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
DP=[[0]*N for _ in range(N)]
print(DFS(0,0))

N=int(input())
DP=[[0]*N for _ in range(N)]
DP[0][0]=1
for i in range(N):
    for j,k in enumerate(map(int,input().split())):
        if k and i+k<N:DP[i+k][j]+=DP[i][j]
        if k and j+k<N:DP[i][j+k]+=DP[i][j]
print(DP[-1][-1])