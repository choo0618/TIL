import sys
sys.stdin = open('레이싱게임.txt','r')

N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(M)]
Result=[10**9 for _ in range(N+1)]
Result[1]=0
for i in range(N):
    for s,e,d in A:
        if Result[s]!=10**9 and Result[e]>Result[s]+d:
            Result[e]=Result[s]+d
R=Result[N] if Result[N]!=10**9 else 'bug'
for i in range(1,N+1):
    if Result[i]<0:R='bug'
print(R)