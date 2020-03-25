import sys
sys.stdin = open('bj2696.txt','r')

import heapq
for t in range(int(input())):
    N=int(input())
    L=[]
    for _ in range(N//10+1):L+=[int(x)for x in input().split()]
    Max=[]
    Min=[]
    r,R=0,[[]for _ in range(N//2//10+1)]
    for idx,n in enumerate(L):
        if len(Max)==len(Min):heapq.heappush(Max,(-n,n))
        else:heapq.heappush(Min,(n,n))
        if Min and Max[0][1]>Min[0][1]:
            tMax=heapq.heappop(Max)[1]
            tMin=heapq.heappop(Min)[1]
            heapq.heappush(Max,(-tMin,tMin))
            heapq.heappush(Min,(tMax,tMax))
        if not idx%2:R[r//10].append(Max[0][1]);r+=1
    print(r)
    for p in R:print(*p)