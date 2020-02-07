import sys
sys.stdin = open('bj1010.txt','r')

for t in range(int(input())):
    N,M=map(int,input().split())
    Map=[[0]*(M+1) for _ in range(M+1)]
    for i in range(M+1):
        Map[i][i]=Map[i][0]=1
        for j in range(1,i):
            Map[i][j]=Map[i-1][j-1]+Map[i-1][j]
    print(Map[M][N])