import sys
sys.stdin = open('bj1003.txt','r')

for t in range(int(input())):
    N=int(input())
    DP=[[1,0],[0,1]]+[[0,0]for _ in range(N-1)]
    for i in range(2,N+1):
        DP[i][0]=DP[i-1][0]+DP[i-2][0]
        DP[i][1]=DP[i-1][1]+DP[i-2][1]
    print(' '.join(map(str, DP[N])))