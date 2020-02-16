import sys
sys.stdin = open('1238.txt','r')

from collections import deque
for t in range(1,11):
    N,S=map(int,input().split())
    L=[int(x)for x in input().split()]
    Map=[[]for _ in range(101)]
    for i in range(0,N,2):
        Map[L[i]].append(L[i+1])
    Q=deque([(S,0)])
    D=[-1]*101
    while Q:
        a,d=Q.popleft()
        for n in Map[a]:
            if D[n]==-1:D[n]=d+1;Q.append((n,d+1))
    Max=max(D)
    for i in range(100,-1,-1):
        if D[i]==Max:print('#%d %d'%(t,i));break