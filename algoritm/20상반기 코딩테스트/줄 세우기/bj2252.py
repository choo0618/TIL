import sys
sys.stdin = open('bj2252.txt','r')

from collections import deque
N,M=map(int,input().split())
Map=[[]for _ in range(N+1)]
D=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    Map[a].append(b)
    D[b]+=1
Q=deque()
for i in range(1,N+1):
    if not D[i]:Q.append(i)
while Q:
    a=Q.popleft()
    print(a,end=' ')
    for i in Map[a]:
        D[i]-=1
        if not D[i]:Q.append(i)


# 위상 정렬
def DFS(x):
    D[x]-=1
    if D[x]==-1:R.append(x)
    for a in Map[x]:
        D[a]-=1
        if D[a]==0:DFS(a)
N,M=map(int,input().split())
Map=[[]for _ in range(N+1)]
D=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    Map[a].append(b)
    D[b]+=1
R=[]
for i in range(1,N+1):
    if D[i]==0:DFS(i)
print(*R)
