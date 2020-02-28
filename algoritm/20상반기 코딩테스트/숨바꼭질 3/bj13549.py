import sys
sys.stdin = open('bj13549.txt','r')

import heapq
N,K=map(int,input().split())
Map=[0]*100001
Q=[(0,N)]
while Q:
    c,n=heapq.heappop(Q)
    if Map[n]:continue
    Map[n]=1
    if n==K:print(c);break
    for next in [2*n,n+1,n-1]:
        if not 0<=next<=100000:continue
        C=c+1 if next!=2*n else c
        heapq.heappush(Q,(C,next))

from collections import deque
N,K=map(int,input().split())
Map=[-1]*100001
Map[N]=0
Q=deque([N])
while Q:
    n=Q.popleft()
    if 2*n<=100000 and Map[2*n]==-1:Map[2*n]=Map[n];Q.appendleft(2*n)
    for next in [n+1,n-1]:
        if 0<=next<=100000 and Map[next]==-1:Map[next]=Map[n]+1;Q.append(next)
print(Map[K])


from collections import deque
N,K=map(int,input().split())
Map=[0]*100001
Map[N]=1
Q=deque([(N,0)])
while Q:
    n,c=Q.popleft()
    if n==K:print(c);break
    if 2*n<=100000 and not Map[2*n]:Map[2*n]=1;Q.appendleft((2*n,c))
    for next in [n+1,n-1]:
        if 0<=next<=100000 and not Map[next]:Map[next]=1;Q.append((next,c+1))