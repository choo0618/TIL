import sys
sys.stdin = open('bj11052.txt','r')

N=int(input())
i,DP=0,[0]*(N+1)
for n in map(int,input().split()):
    i+=1
    for j in range(i,N+1):DP[j]=max(DP[j],DP[j-i]+n)
print(DP[N])