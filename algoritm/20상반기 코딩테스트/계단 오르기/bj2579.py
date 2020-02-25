import sys
sys.stdin = open('bj2579.txt','r')

N=int(input())
L=[0,0,0]+[int(input())for _ in range(N)]
DP=[0]*(N+3)
for i in range(3,N+3):
    DP[i]=max(DP[i-3]+L[i]+L[i-1],DP[i-2]+L[i])
print(DP)