import sys
sys.stdin = open('bj2211.txt','r')

import heapq
N,M=map(int,input().split())
D=[[]for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))
Que=[(1,1)]
Map=[987654321]*(N+1)
Map[1]=0
P=list(range(N+1))
while Que:
    c,a=heapq.heappop(Que)
    for n in D[a]:
        nC,to=n
        if Map[to]>Map[a]+nC:
            Map[to]=Map[a]+nC
            heapq.heappush(Que,(Map[to],to))
            P[to]=a
print(N-1)
for i in range(2,N+1):print('%d %d'%(P[i],i))


