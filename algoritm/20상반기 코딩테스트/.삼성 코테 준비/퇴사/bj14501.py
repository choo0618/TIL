import sys
sys.stdin = open('bj14501.txt','r')

N=int(input())
DP=[0]*(N+6)
for i in range(N):
    t,p=map(int,input().split())
    DP[i+1]=max(DP[i],DP[i+1])
    DP[i+t]=max(DP[i]+p,DP[i+t])
print(DP[N])
