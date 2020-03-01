import sys
sys.stdin = open('bj2075.txt','r')

import heapq
N=int(input())
Q=[]
for _ in range(N):
    for n in [int(x)for x in input().split()]:
        if len(Q)<N:heapq.heappush(Q,n)
        else:
            Min=heapq.heappop(Q)
            if n>=Min:heapq.heappush(Q,n)
            else:heapq.heappush(Q,Min)
print(heapq.heappop(Q))