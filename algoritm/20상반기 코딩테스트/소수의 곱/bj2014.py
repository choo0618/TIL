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

# from queue import PriorityQueue
# K,N=map(int,input().split())
# L=[int(x)for x in input().split()]
# Q=PriorityQueue()
# for n in L:Q.put(n)
# while 1:
#     a=Q.get()
#     N-=1
#     if N==0:print(a);break
#     for l in L:
#         Q.put(a*l)
#         if not a%l:break
