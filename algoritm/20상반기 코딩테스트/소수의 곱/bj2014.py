import sys
sys.stdin = open('bj2014.txt','r')

import heapq
K,N=map(int,input().split())
L=[int(x)for x in input().split()]
Q=[]
for l in L:heapq.heappush(Q,l)
while True:
    a=heapq.heappop(Q)
    N-=1
    if not N:print(a);break
    for l in L:
        b=a*l
        heapq.heappush(Q,b)
        if not a%l:break