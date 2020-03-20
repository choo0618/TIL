import sys
sys.stdin = open('bj11054.txt','r')

def DP():
    dp=[0]*N
    for i in range(N):
        dp[i]=1
        for j in range(i):
            if L[i]>L[j]:dp[i]=max(dp[i],dp[j]+1)
    return dp
N=int(input())
L=[int(x)for x in input().split()]
# DP=[0]*N
# RDP=[0]*N
# for i in range(N):
#     DP[i]=1
#     for j in range(i):
#         if L[i]>L[j]:DP[i]=max(DP[i],DP[j]+1)
# for i in range(N-1,-1,-1):
#     RDP[i]=1
#     for j in range(N-1,i-1,-1):
#         if L[i]>L[j]:RDP[i]=max(RDP[i],RDP[j]+1)
# print(max(DP[x]+RDP[x]-1 for x in range(N)))
a=DP()
L.reverse()
b=DP()
b.reverse()
print(max(a[x]+b[x]-1 for x in range(N)))