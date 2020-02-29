import sys
sys.stdin = open('bj11048.txt','r')

N,M=map(int,input().split())
A=[[0]*(M+1)]+[[0]+[int(x)for x in input().split()]for y in range(N)]
for i in range(1,N+1):
    for j in range(1,M+1):
        A[i][j]=max(A[i-1][j]+A[i][j],A[i][j-1]+A[i][j])
print(A[N][M])