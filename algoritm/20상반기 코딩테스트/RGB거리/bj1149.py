import sys
sys.stdin = open('bj1149.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
DP=[[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    DP[i][0]=min(DP[i-1][1],DP[i-1][2])+A[i-1][0]
    DP[i][1]=min(DP[i-1][0],DP[i-1][2])+A[i-1][1]
    DP[i][2]=min(DP[i-1][0],DP[i-1][1])+A[i-1][2]
print(min(DP[N]))