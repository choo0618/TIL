import sys
sys.stdin = open('bj10844.txt','r')

N=int(input())
DP=[[0]+[1]*9]+[[0]*10 for _ in range(N)]
for i in range(1,N+1):
    for j in range(10):
        if not j:DP[i][j]=DP[i-1][j+1]
        elif j==9:DP[i][j]=DP[i-1][j-1]
        else:DP[i][j]=DP[i-1][j-1]+DP[i-1][j+1]
print(sum(DP[N-1])%1000000000)


