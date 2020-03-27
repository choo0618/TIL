import sys
sys.stdin = open('bj2193.txt','r')

N=int(input())
DP=[[0,1]]+[[0]*2 for _ in range(N)]
for i in range(1,N+1):
    DP[i][0]+=sum(DP[i-1])
    DP[i][1]+=DP[i-1][0]
print(sum(DP[N-1]))
