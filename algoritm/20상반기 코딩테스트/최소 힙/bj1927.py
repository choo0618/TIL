import sys
sys.stdin=open('bj1927.txt','r')

import heapq
import sys
input=sys.stdin.readline
N=int(input())
Q=[]
for i in range(N):
    n=int(input())
    if not n:print(heapq.heappop(Q) if Q else 0)
    else:heapq.heappush(Q,n)