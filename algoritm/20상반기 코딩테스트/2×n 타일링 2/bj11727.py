import sys
sys.stdin = open('bj11727.txt','r')

N=int(input())
DP=[1,3]+[0]*(N-2)
for i in range(2,N):DP[i]=(DP[i-1]+2*DP[i-2])%10007
print(DP[N-1])

print(input())