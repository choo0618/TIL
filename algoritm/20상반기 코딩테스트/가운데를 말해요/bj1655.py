import sys
sys.stdin = open('bj1655.txt','r')

import heapq
N=int(input())
MaxQ=[]
MinQ=[]
for _ in range(N):
    n=int(input())
    if len(MaxQ)==len(MinQ):heapq.heappush(MaxQ,(-n,n))
    else:heapq.heappush(MinQ,(n,n))
    if MinQ and MaxQ[0][1]>MinQ[0][1]:
        tmpmax=heapq.heappop(MaxQ)[1]
        tmpmin=heapq.heappop(MinQ)[1]
        heapq.heappush(MaxQ,(-tmpmin,tmpmin))
        heapq.heappush(MinQ,(tmpmax,tmpmax))
    print(MaxQ[0][1])