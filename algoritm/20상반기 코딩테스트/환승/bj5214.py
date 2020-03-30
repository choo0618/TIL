import sys
sys.stdin = open('bj5214.txt','r')

from collections import deque
N,K,M=map(int,input().split())
A=[[]for _ in range(N+M+1)]
for i in range(M):
    a=[int(x)for x in input().split()]
    for j in range(K):
        A[a[j]].append(N+i+1)
        A[N+i+1].append(a[j])
Q=deque([(1,1)])
Dis=[-1]*(N+M+1)
Dis[1]=1
while Q:
    a,d=Q.popleft()
    for b in A[a]:
        if Dis[b]==-1 or d+1<Dis[b]:
            Dis[b]=d+1
            Q.append((b,d+1))
print(Dis[N]//2+1 if Dis[N]!=-1 else -1)