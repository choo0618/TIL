import sys
sys.stdin = open('bj1761.txt','r')

from collections import deque
def LCA(x,y):
    if Depth[x]>Depth[y]:x,y=y,x
    for i in range(20,-1,-1):
        if Depth[y]-Depth[x]>=1<<i:y=Par[y][i]
    if x==y:return x
    for i in range(20,-1,-1):
        if Par[x][i]!=Par[y][i]:
            x=Par[x][i]
            y=Par[y][i]
    return Par[x][0]
N=int(input())
Map=[[]for _ in range(N+1)]
for _ in range(N-1):
    a,b,l=map(int,input().split())
    Map[a].append((b,l))
    Map[b].append((a,l))
Dis=[0]*(N+1)
Depth=[-1]*(N+1)
Depth[1]=0
Q=deque([(1,0,0)])
Par=[[0]*21 for _ in range(N+1)]
while Q:
    a,depth,dis=Q.popleft()
    for n in Map[a]:
        b,d=n
        if Depth[b]!=-1:continue
        Depth[b]=depth+1
        Dis[b]=dis+d
        Par[b][0]=a
        Q.append((b,depth+1,dis+d))
for j in range(1,20):
    for i in range(1,N+1):
        Par[i][j]=Par[Par[i][j-1]][j-1]
for _ in range(int(input())):
    a,b=map(int,input().split())
    x=LCA(a,b)
    print(Dis[a]+Dis[b]-2*Dis[x])