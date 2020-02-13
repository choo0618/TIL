import sys
sys.stdin = open('1855.txt','r')

from collections import deque
def LCA(x,y):
    r=0
    if D[x]>D[y]:x,y=y,x
    while D[x]!=D[y]:y=T[y];r+=1
    while x!=y:
        x=T[x]
        y=T[y]
        r+=2
    return r
for tc in range(int(input())):
    N=int(input())
    T=[0,0]+[int(x)for x in input().split()]
    D=[0,0]*(N-1)
    Map=[[]for _ in range(N+1)]
    for t in range(2,N+1):
        D[t]=D[T[t]]+1
        Map[T[t]].append(t)
    R=0
    Q=deque([1])
    while Q:
        a=Q.popleft()
        Q+=Map[a]
        if not Q: break
        R+=LCA(a,Q[0])
    print('#%d %d'%(tc+1,R))