import sys
sys.stdin = open('bj11286.txt','r')

import heapq
N=int(input())
Q=[]
for _ in range(N):
    n=int(input())
    if n:heapq.heappush(Q,(abs(n),n))
    else:
        if not Q:print(0)
        else:print(heapq.heappop(Q)[1])
