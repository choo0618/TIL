import sys
sys.stdin = open('bj1699.txt','r')

N=int(input())
DP=[int(x)for x in range(N+1)]
for i in range(1,N+1):
    j=1
    while j*j<=i:
        DP[i]=min(DP[i],DP[i-j*j]+1)
        j+=1
print(DP[N])