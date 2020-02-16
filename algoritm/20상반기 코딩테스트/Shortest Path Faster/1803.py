import sys
sys.stdin = open('1803.txt','r')

from collections import deque
for t in range(int(input())):
    N,M,A,B=map(int,input().split())
    Map=[[]for _ in range(N+1)]
    for i in range(M):
        a,b,c=map(int,input().split())
        Map[a].append((b,c))
        Map[b].append((a,c))
    R=[-1]*(N+1)
    R[A]=0
    Q=deque([(A,0)])
    while Q:
        a,c=Q.popleft()
        for b,d in Map[a]:
            if R[b]==-1 or c+d<R[b]:
                R[b]=c+d
                Q.append((b,c+d))
    print('#%d %d'%(t+1,R[B]))