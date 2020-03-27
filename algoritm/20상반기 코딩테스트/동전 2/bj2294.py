import sys
sys.stdin = open('bj2294.txt','r')

N,K=map(int,input().split())
DP=[0]+[10**9]*K
for i in range(N):
    n=int(input())
    for j in range(n,K+1):
        DP[j]=min(DP[j],DP[j-n]+1)
print(DP)
print(DP[K] if DP[K]!=10**9 else -1)