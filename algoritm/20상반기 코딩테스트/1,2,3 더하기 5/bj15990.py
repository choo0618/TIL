import sys
sys.stdin = open('bj15990.txt','r')

DP=[[0]*4 for _ in range(100001)]
for i in range(1,4):DP[i][i]=1
DP[3][1]=DP[3][2]=1
for i in range(4,100001):
    DP[i][1]=(DP[i-1][2]+DP[i-1][3])%1000000009
    DP[i][2]=(DP[i-2][1]+DP[i-2][3])%1000000009
    DP[i][3]=(DP[i-3][1]+DP[i-3][2])%1000000009
for t in range(int(input())):print(sum(DP[int(input())])%1000000009)