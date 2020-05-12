import sys
sys.stdin = open('bj11060.txt','r')

N=int(input())
L=[0]+[int(x)for x in input().split()]
DP=[0]*(N+1)
DP[1]=1
for i in range(1,N+1):
    if not DP[i]:continue
    for j in range(1,L[i]+1):
        if i+j>N:continue
        if not DP[i+j] or DP[i+j]>DP[i]+1:DP[i+j]=DP[i]+1
print(DP[-1]-1 if DP[-1] else -1)