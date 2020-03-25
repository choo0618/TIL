import sys
sys.stdin = open('bj1715.txt','r')

import heapq
N=int(input())
R,Q=0,[]
for _ in range(N):heapq.heappush(Q,int(input()))
while N!=1:
    a=heapq.heappop(Q)
    b=heapq.heappop(Q)
    heapq.heappush(Q,a+b)
    R+=a+b
    N-=1
print(R)