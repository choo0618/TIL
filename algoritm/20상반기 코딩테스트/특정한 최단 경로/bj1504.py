import sys
sys.stdin = open('bj1504.txt','r')

import heapq
def dijkstra(x):
    V=[-1]*(N+1)
    V[x]=0
    Q=[(0,x)]
    while Q:
        c,a=heapq.heappop(Q)
        for n in Map[a]:
            b,nC=n[0],c+n[1]
            if V[b]==-1 or nC<V[b]:
                V[b]=nC
                heapq.heappush(Q,(nC,b))
    return V
import sys
input=sys.stdin.readline
N,E=map(int,input().split())
Map=[[]for _ in range(N+1)]
for i in range(E):
    a,b,c=map(int,input().split())
    Map[a].append((b,c))
    Map[b].append((a,c))
a,b=map(int,input().split())
S1=dijkstra(1)
Sa=dijkstra(a)
Sb=dijkstra(b)
AB=S1[a]+Sa[b]+Sb[N]if S1[a]!=-1 and Sa[b]!=-1 and Sb[N]!=-1 else 10**9
BA=S1[b]+Sb[a]+Sa[N]if S1[b]!=-1 and Sb[a]!=-1 and Sa[N]!=-1 else 10**9
print(-1 if min(AB,BA)==10**9 else min(AB,BA))