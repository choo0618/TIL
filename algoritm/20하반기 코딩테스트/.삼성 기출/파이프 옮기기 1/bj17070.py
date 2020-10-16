import sys
sys.stdin = open('bj17070.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
DP=[[[0,0,0]for _ in range(N)]for _ in range(N)]
for j in range(1,N):
    if A[0][j]:break
    DP[0][j][0]=1
for i in range(1,N):
    for j in range(2,N):
        if A[i][j]:continue
        DP[i][j][0]+=DP[i][j-1][0]+DP[i][j-1][2]
        DP[i][j][1]+=DP[i-1][j][1]+DP[i-1][j][2]
        if A[i-1][j-1]==A[i-1][j]==A[i][j-1]==0:DP[i][j][2]+=sum(DP[i-1][j-1])
print(sum(DP[-1][-1]))