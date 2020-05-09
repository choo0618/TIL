import sys
sys.stdin = open('bj1766.txt','r')

import heapq
N,M=map(int,input().split())
A=[[]for _ in range(N+1)]
D=[0]*(N+1)
Q=[]
for i in range(M):
    a,b=map(int,input().split())
    A[a].append(b)
    D[b]+=1
for i in range(1,N+1):
    if not D[i]:heapq.heappush(Q,i)
while Q:
    now=heapq.heappop(Q)
    if not D[now]:print(now,end=' ')
    for next in A[now]:
        D[next]-=1
        if not D[next]:heapq.heappush(Q,next)

