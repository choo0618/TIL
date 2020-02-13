import sys
sys.stdin = open('bj11437.txt','r')

from collections import deque
def LCA(x,y):
    if D[x]>D[y]:x,y=y,x
    while D[x]!=D[y]:y=P[y]
    while x!=y:
        x=P[x]
        y=P[y]
    return x
N=int(input())
Map,P,D=[[]for _ in range(N+1)],[0]*(N+1),[0]*(N+1)
for i in range(N-1):
    a,b=map(int,input().split())
    Map[a].append(b)
    Map[b].append(a)
check=[0]*(N+1)
Q=deque([1])
check[1]=1
while Q:
    x=Q.popleft()
    for i in Map[x]:
        if check[i]:continue
        D[i]=D[x]+1
        check[i]=1
        P[i]=x
        Q.append(i)
for r in range(int(input())):
    a,b=map(int,input().split())
    print(LCA(a,b))

