import sys
sys.stdin = open('bj10282.txt','r')

import heapq
for t in range(int(input())):
    N,D,C=map(int,input().split())
    Map=[[]for _ in range(N+1)]
    for i in range(D):
        a,b,c=map(int,input().split())
        Map[b].append((a,c))
    V=[-1]*(N+1)
    V[C]=0
    Q=[(0,C)]
    while Q:
        t,a=heapq.heappop(Q)
        for i in Map[a]:
            nt,b=t+i[1],i[0]
            if V[b]==-1 or V[b]>nt:
                V[b]=nt
                heapq.heappush(Q,(nt,b))
    print('%d %d'%(sum(1for i in V if i!=-1),max(V)))
