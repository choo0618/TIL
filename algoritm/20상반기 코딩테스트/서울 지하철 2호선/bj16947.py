import sys
sys.stdin = open('bj16947.txt','r')

from collections import deque
def DFS(a,b):
    if C[a]==1:
        return a
    C[a]=1
    for n in Map[a]:
        if n==b:continue
        tmp=DFS(n,a)
        if tmp==-2:return -2
        if tmp>=0:
            C[a]=2
            if a==tmp:return -2
            else:return tmp
    return -1
def BFS(x):
    V=[0]*N
    V[x]=1
    Q=deque([(x,0)])
    while Q:
        x,t=Q.popleft()
        if C[x]==2:return t
        for n in Map[x]:
            if not V[n]:V[n]=t+1;Q.append((n,t+1))
N=int(input())
Map=[[]for _ in range(N)]
C=[0]*N
for t in range(N):
    a,b=map(int,input().split())
    a-=1;b-=1
    Map[a].append(b)
    Map[b].append(a)
DFS(0,-1)
R=[]
for i in range(N):
    if C[i]==2:R.append(0)
    else:R.append(BFS(i))
print(*R)