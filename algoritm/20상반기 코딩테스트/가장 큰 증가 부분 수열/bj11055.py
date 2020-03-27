import sys
sys.stdin = open('bj11055.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
DP=[0]*N
for i in range(N):
    DP[i]=L[i]
    for j in range(i):
        if L[i]>L[j]:DP[i]=max(DP[i],DP[j]+L[i])
print(max(DP))