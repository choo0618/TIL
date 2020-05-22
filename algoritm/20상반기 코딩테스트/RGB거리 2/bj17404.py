import sys
sys.stdin = open('bj17404.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=10**6
for t in range(3):
    DP=[[0]*3 for _ in range(N+1)]
    tmp=A[0][::]
    for j in range(3):
        if t!=j:A[0][j]=10**6
    for i in range(1,N+1):
        DP[i][0]=min(DP[i-1][1],DP[i-1][2])+A[i-1][0]
        DP[i][1]=min(DP[i-1][0],DP[i-1][2])+A[i-1][1]
        DP[i][2]=min(DP[i-1][0],DP[i-1][1])+A[i-1][2]
    for j in range(3):
        if t!=j:R=min(R,DP[-1][j])
    A[0]=tmp
print(R)