import sys
sys.stdin = open('bj1309.txt','r')

N=int(input())
DP=[0,3,7]+[0]*(N-2)
for i in range(3,N+1):DP[i]=(2*DP[i-1]+DP[i-2])%9901
print(DP[N])


# N=10 일때
# [0, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119]