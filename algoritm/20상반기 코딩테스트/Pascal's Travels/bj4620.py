import sys
sys.stdin = open('bj4620.txt','r')

while True:
    N=int(input())
    if N==-1:break
    DP=[[0]*N for _ in range(N)]
    DP[0][0]=1
    for i in range(N):
        for j,n in enumerate(map(int,input())):
            if not n:continue
            if i+n<N:DP[i+n][j]+=DP[i][j]
            if j+n<N:DP[i][j+n]+=DP[i][j]
    print(DP[-1][-1])