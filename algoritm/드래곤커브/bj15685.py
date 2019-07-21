import sys
sys.stdin = open('bj15685.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for _ in range(N)]
print(A)
M=[[0]*100for _ in range(100)]
print(M)