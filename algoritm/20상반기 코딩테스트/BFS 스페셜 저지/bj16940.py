import sys
sys.stdin = open('bj16940.txt','r')

from collections import deque
def BFS():
    i=0
    V=[0]*(N+1)
    V[1]=1
    Q=deque([1])
    while Q:
        q=[]
        a=Q.popleft()
        if a!=R[i]:return 0
        for b in Map[a]:
            if V[b]:continue
            V[b]=1
            q.append((I[b],b))
        for n,b in sorted(q):Q.append(b)
        i+=1
    return 1
N=int(input())
Map=[[]for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    Map[a].append(b)
    Map[b].append(a)
R=[int(x)for x in input().split()]
I=[0]*(N+1)
for i in range(N):I[R[i]]=i
print(BFS())