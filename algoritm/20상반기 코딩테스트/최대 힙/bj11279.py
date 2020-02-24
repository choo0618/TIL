import sys
sys.stdin=open('bj11279.txt','r')

import heapq
Q=[]
for _ in range(int(input())):
    n=int(input())
    if n:heapq.heappush(Q,-n)
    else:print(-heapq.heappop(Q) if Q else 0)