import sys
sys.stdin = open('bj9465.txt','r')

for t in range(int(input())):
    N=int(input())
    A=[[0]+[int(x)for x in input().split()]for y in range(2)]
    DP=[[0]*(N+1) for _ in range(2)]
    DP[0][1],DP[1][1]=A[0][1],A[1][1]
    for i in range(2,N+1):
        DP[0][i]=max(DP[1][i-1],DP[1][i-2])+A[0][i]
        DP[1][i]=max(DP[0][i-1],DP[0][i-2])+A[1][i]
    print(max(DP[0][N],DP[1][N]))