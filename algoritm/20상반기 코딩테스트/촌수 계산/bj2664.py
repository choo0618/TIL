import sys
sys.stdin = open('bj2664.txt','r')

import heapq
N=int(input())
S,E=map(int,input().split())
P=int(input())
Map=[[]for _ in range(N)]
for i in range(P):
    s,e=map(int,input().split())
    Map[s-1].append(e-1)
    Map[e-1].append(s-1)
L=[987654321]*N
L[S-1]=0
Que=[]
heapq.heappush(Que,(S-1,0))
while Que:
    now,d=heapq.heappop(Que)
    for i in Map[now]:
        if L[i]>d+1:
            L[i]=d+1
            heapq.heappush(Que,(i,d+1))
if L[E-1]!=987654321:print(L[E-1])
else:print(-1)