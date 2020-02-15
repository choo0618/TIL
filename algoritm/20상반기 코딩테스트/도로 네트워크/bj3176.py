import sys
sys.stdin = open('bj3176.txt','r')

from collections import deque
def LCA(x,y):
    global Min,Max
    if Depth[x]>Depth[y]:x,y=y,x
    for i in range(20,-1,-1):
        if Depth[y]-Depth[x]>=1<<i:
            Min=min(Min,PMin[y][i])
            Max=max(Max,PMax[y][i])
            y=Par[y][i]
    if x==y:return
    for i in range(20,-1,-1):
        if Par[x][i]!=Par[y][i]:
            Min=min(Min,min(PMin[x][i],PMin[y][i]))
            Max=max(Max,max(PMax[x][i],PMax[y][i]))
            x=Par[x][i]
            y=Par[y][i]
    Min=min(Min,min(PMin[x][0],PMin[y][0]))
    Max=max(Max,max(PMax[x][0],PMax[y][0]))
    return
N=int(input())
Map=[[]for _ in range(N+1)]
for _ in range(N-1):
    a,b,l=map(int,input().split())
    Map[a].append((b,l))
    Map[b].append((a,l))
Depth=[-1]*(N+1)
Depth[1]=0
Q=deque([(1,0,0)])
Par=[[0]*21 for _ in range(N+1)]
PMax=[[0]*21 for _ in range(N+1)]
PMin=[[0]*21 for _ in range(N+1)]
while Q:
    a,depth,dis=Q.popleft()
    for n in Map[a]:
        b,d=n
        if Depth[b]!=-1:continue
        Depth[b]=depth+1
        Par[b][0]=a
        PMin[b][0]=d
        PMax[b][0]=d
        Q.append((b,depth+1,dis+d))
for j in range(1,20):
    for i in range(1,N+1):
        Par[i][j]=Par[Par[i][j-1]][j-1]
        PMax[i][j]=max(PMax[i][j-1],PMax[Par[i][j-1]][j-1])
        PMin[i][j]=min(PMin[i][j-1],PMin[Par[i][j-1]][j-1])
for _ in range(int(input())):
    a,b=map(int,input().split())
    Min,Max=10**9,0
    LCA(a,b)
    print('%d %d'%(Min,Max))