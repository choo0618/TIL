import sys
sys.stdin = open('bj2133.txt','r')

N=int(input())
DP=[1,0,3]+[0]*(N-2)
if not N%2:
    for i in range(4,N+1,2):
        DP[i]=3*DP[i-2]
        for j in range(4,i+1,2):
            DP[i]+=2*DP[i-j]
print(DP[N])