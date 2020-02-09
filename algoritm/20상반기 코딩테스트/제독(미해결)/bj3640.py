import sys
sys.stdin = open('bj3640.txt','r')

import heapq
def Dijkstra(x):
    V=[-1]*(E+1)
    V[x]=0
    Q=[(0,1)]
    while Q:
        c,a=heapq.heappop(Q)
        for d in Go[a]:
            nC,b=c+d[1],d[0]
            if V[b]==-1 or nC<V[b]:
                V[b]=nC
                heapq.heappush(Q,(nC,b))
    return V

E,V=map(int,input().split())
Go=[[]for _ in range(E+1)]
Rev=[[]for _ in range(E+1)]
for i in range(V):
    a,b,c=map(int,input().split())
    Go[a].append((b,c))
    Rev[b].append((a,c))
A=Dijkstra(1)
print(A)