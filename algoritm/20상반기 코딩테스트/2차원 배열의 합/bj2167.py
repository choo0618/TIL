import sys
sys.stdin = open('bj2167.txt','r')

N,M=map(int,input().split())
A=[[0]*(M+1)]+[[0]+[int(x)for x in input().split()]for y in range(N)]
for i in range(1,N+1):
    for j in range(1,M+1):
        A[i][j]=A[i-1][j]+A[i][j-1]+A[i][j]-A[i-1][j-1]
for t in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    print(A[x2][y2]-A[x1-1][y2]-A[x2][y1-1]+A[x1-1][y1-1])