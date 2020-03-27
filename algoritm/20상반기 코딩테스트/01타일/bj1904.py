import sys
sys.stdin = open('bj1904.txt','r')

# 1 1
# 2 2
# 3 3
# 4 5
# 5 8 11111 11100 11001 10011 10000 00001 00111 00100
N=int(input())
DP=[0,1,2]+[0]*(N-2)
for i in range(3,N+1):DP[i]=(DP[i-1]+DP[i-2])%15746
print(DP[N])
