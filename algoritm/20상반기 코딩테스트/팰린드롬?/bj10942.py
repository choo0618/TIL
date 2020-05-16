import sys
sys.stdin = open('bj10942.txt','r')

N=int(input())
S=[0]+[x for x in input().split()]
DP=[[0]*(N+1)for _ in range(N+1)]
for i in range(1,N+1):
    DP[0][i]=DP[1][i]=1
for i in range(2,N+1):
    for j in range(1,N-i+2):
        if S[j]==S[j+i-1] and DP[i-2][j+1]:DP[i][j]=1
for t in range(int(input())):
    a,b=map(int,input().split())
    print(DP[b-a+1][a])