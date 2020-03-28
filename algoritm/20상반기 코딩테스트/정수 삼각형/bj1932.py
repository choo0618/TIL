import sys
sys.stdin = open('bj1932.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
for i in range(N-2,-1,-1):
    for j in range(i+1):
        A[i][j]=max(A[i+1][j],A[i+1][j+1])+A[i][j]
print(A[0][0])