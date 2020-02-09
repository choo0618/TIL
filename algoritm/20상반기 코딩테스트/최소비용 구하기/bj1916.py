import sys
sys.stdin=open('bj1916.txt','r')

import heapq
N=int(input())
M=int(input())
Map=[[]for _ in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    Map[a-1].append((b-1,c))
A,B=map(int,input().split())
V=[-1]*N
V[A-1]=0
Q=[(0,A-1)]
while Q:
    c,a=heapq.heappop(Q)
    for i in Map[a]:
        b,nC=i[0],c+i[1]
        if V[b]==-1 or nC<V[b]:
            heapq.heappush(Q,(nC,b))
            V[b]=nC
print(V)
print(V[B-1])