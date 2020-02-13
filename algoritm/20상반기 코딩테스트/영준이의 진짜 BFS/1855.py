import sys
sys.stdin = open('1855.txt','r')

from collections import deque
def LCA(x,y):
    if D[x]>D[y]:x,y=y,x
    for i in range(20,-1,-1):
        if D[y]-D[x]>=1<<i:y=Par[y][i]
    if x==y:return x
    for i in range(20,-1,-1):
        if Par[x][i]!=Par[y][i]:
            x=Par[x][i]
            y=Par[y][i]
    return Par[x][0]
for tc in range(int(input())):
    N=int(input())
    T=[0,0]+[int(x)for x in input().split()]
    D,Par=[-1]*(N+1),[[0]*21 for y in range(N+1)]
    Map=[[]for _ in range(N+1)]
    for t in range(2,N+1):
        Map[T[t]].append(t)
        Map[t].append(T[t])
    Q=deque([(1,0)])
    while Q:
        a,c=Q.popleft()
        D[a]=c
        Map[a].sort()
        for m in Map[a]:
            if D[m]!=-1:continue
            Par[m][0]=a
            Q.append((m,c+1))
    for j in range(1,21):
        for i in range(1,N+1):
            Par[i][j]=Par[Par[i][j-1]][j-1]
    R=0
    Q=deque([1])
    Check=[0]*(N+1)
    for t in range(N-1):
        Check[Q[t]]=1
        for q in Map[Q[t]]:
            if not Check[q]:Q.append(q)
        x=LCA(Q[t],Q[t+1])
        R+=D[Q[t]]+D[Q[t+1]]-2*D[x]
    print('#%d %d'%(tc+1,R))