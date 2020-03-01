import sys
sys.stdin = open('bj1912.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
DP=[0]*N
DP[0]=L[0]
R=-10**9
for i in range(1,N):
    DP[i]=max(DP[i-1]+L[i],L[i])
    R=max(R,DP[i])
print(max(R,DP[0]))
