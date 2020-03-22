import sys
sys.stdin = open('bj1915.txt','r')

N,M=map(int,input().split())
A=[[0]*(M+1)]+[list(map(int,'0'+input()))for _ in range(N)]
R=0
for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i][j]:
            A[i][j]=min(A[i-1][j],A[i-1][j-1],A[i][j-1])+1
            R=max(R,A[i][j])
print(R*R)