import sys
sys.stdin = open('bj2293.txt','r')

N,K=map(int,input().split())
DP=[1]+[0]*K
for i in range(N):
    n=int(input())
    for j in range(n,K+1):
        if j-n>=0:DP[j]+=DP[j-n]
print(DP[K])