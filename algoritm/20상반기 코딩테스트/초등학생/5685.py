import sys
sys.stdin = open('5685.txt','r')

for t in range(int(input())):
    N=int(input())
    A=[int(x)for x in input().split()]
    DP=[[0]*21 for _ in range(N-1)]
    DP[0][A[0]]=1
    for i in range(1,N-1):
        for j in range(21):
            if DP[i-1][j]:
                if j+A[i]<=20:DP[i][j+A[i]]+=DP[i-1][j]
                if j-A[i]>=0:DP[i][j-A[i]]+=DP[i-1][j]
    print('#%d %d'%(t+1,DP[-1][A[N-1]]%1234567891))

