import sys
sys.stdin=open('bj1613.txt','r')

# 플로이드 와샬
N,K=map(int,input().split())
Map=[[0]*(N+1)for _ in range(N+1)]
for i in range(K):
    x,y=map(int,input().split())
    Map[x][y]=-1
    Map[y][x]=1
for n in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j==n:continue
            if not Map[i][j] and Map[i][n]==Map[n][j]:Map[i][j]=Map[i][n]
S=int(input())
for s in range(S):
    i,j=map(int,input().split())
    print(Map[i][j])

# deque
from collections import deque
N,K=map(int,input().split())
Map=[[-1]*N for _ in range(N)]
Dic={int(x):[]for x in range(N)}
for i in range(K):
    x,y=map(int,input().split())
    Dic[x-1].append(y-1)
Que=deque()
for n in range(N):
    Que.append(n)
    while Que:
        q=Que.popleft()
        for d in Dic[q]:
            if Map[n][d]==-1:
                Map[n][d]=1
                Que.append(d)
for s in range(int(input())):
    i,j=map(int,input().split())
    i-=1;j-=1
    if Map[i][j]==1:print(-1)
    elif Map[j][i]==1:print(1)
    else:print(0)

