import sys
sys.stdin = open('bj2169.txt','r')

N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
DP=[[0]*M for _ in range(N)]
R=[0]*M
DP[0][0]=A[0][0]
for j in range(1,M):DP[0][j]=DP[0][j-1]+A[0][j]
for i in range(1,N):
    DP[i][0]=DP[i-1][0]+A[i][0]
    for j in range(1,M):
        DP[i][j]=max(DP[i-1][j],DP[i][j-1])+A[i][j]
    R[M-1]=DP[i-1][M-1]+A[i][M-1]
    for j in range(M-2,-1,-1):
        R[j]=max(DP[i-1][j],R[j+1])+A[i][j]
    for j in range(M):
        DP[i][j]=max(DP[i][j],R[j])
print(DP[N-1][M-1])