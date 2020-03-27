import sys
sys.stdin = open('bj11057.txt','r')

N=int(input())
DP=[[1]*10]+[[0]*10 for _ in range(N)]
for i in range(1,N+1):
    for j in range(10):
        DP[i][j]=DP[i-1][j]+DP[i][j-1]
print(DP)
