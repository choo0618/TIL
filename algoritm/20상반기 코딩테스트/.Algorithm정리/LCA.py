from collections import deque
def LCA(x,y):
    if D[x]>D[y]:x,y=y,x
    for i in range(20,-1,-1):
        if D[y]-D[x]>=(1<<i):y=Par[y][i]
    if x==y:return x
    for i in range(20,-1,-1):
        if Par[x][i]!=Par[y][i]:
            x=Par[x][i]
            y=Par[y][i]
    return Par[x][0]
N=int(input())
D,M,Par=[-1]*(N+1),[[]for _ in range(N+1)],[[0]*21 for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    M[a].append(b)
    M[b].append(a)
Q=deque([(1,0)])
while Q:
    a,c=Q.popleft()
    D[a]=c
    for m in M[a]:
        if D[m]!=-1:continue
        Par[m][0]=a
        Q.append((m,c+1))
for j in range(1,21):
    for i in range(1,N+1):
        Par[i][j]=Par[Par[i][j-1]][j-1]
for p in range(int(input())):
    a,b=map(int,input().split())
    print(LCA(a,b))