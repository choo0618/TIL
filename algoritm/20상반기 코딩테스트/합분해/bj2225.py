import sys
sys.stdin = open('bj2225.txt','r')

N,K=map(int,input().split())
DP=[[0]*(N+1)for _ in range(K)]
for i in range(N+1):DP[0][i]=1
for k in range(1,K):
    for i in range(N+1):
        for j in range(N+1):
            if DP[k-1][i]==0 or i+j>N:continue
            DP[k][i+j]+=DP[k-1][i]
print(DP[-1][-1]%1000000000)