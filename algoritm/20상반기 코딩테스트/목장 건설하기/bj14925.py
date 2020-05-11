import sys
sys.stdin = open('bj14925.txt','r')

N,M=map(int,input().split())
A=[[0]*(M+1)]+[[0]+[int(x)for x in input().split()]for y in range(N)]
DP=[[0]*(M+1)for _ in range(N+1)]
R=0
for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i][j]:continue
        DP[i][j]=min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])+1
        R=max(R,DP[i][j])
print(R)