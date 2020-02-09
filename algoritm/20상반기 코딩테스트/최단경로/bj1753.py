import sys
sys.stdin=open('bj1753.txt','r')

import heapq
V,E=map(int,input().split())
K=int(input())
Map=[[]for _ in range(V)]
for i in range(E):
    a,b,c=map(int,input().split())
    Map[a-1].append((b-1,c))
V=[-1]*V
V[K-1]=0
Q=[(0,K-1)]
while Q:
    c,a=heapq.heappop(Q)
    for B in Map[a]:
        b,nC=B[0],c+B[1]
        if V[b]==-1 or nC<V[b]:
            heapq.heappush(Q,(nC,b))
            V[b]=nC
for p in V:print('INF' if p==-1 else p)