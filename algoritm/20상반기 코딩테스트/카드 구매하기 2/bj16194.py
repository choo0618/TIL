import sys
sys.stdin=open('bj16194.txt','r')

N=int(input())
L=[0]+[int(x)for x in input().split()]
DP=[0]+[10**9]*N
for i in range(1,N+1):
    for j in range(1,i+1):DP[i]=min(DP[i],DP[i-j]+L[j])
print(DP[-1])