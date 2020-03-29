import sys
sys.stdin = open('test.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            A[i][j]=min(A[i][j],A[i][k]+A[k][j])
print(A)