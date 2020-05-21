import sys
sys.stdin = open('test.txt','r')

import heapq
Q=[]
for idx,i in enumerate([9,2,3,4,1,2,3,2,3,0,1]):heapq.heappush(Q,(i,idx))
for i in range(10):
    print(heapq.heappop(Q))


