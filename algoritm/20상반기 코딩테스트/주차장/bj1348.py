import sys
sys.stdin= open('bj1348.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def DFS(i,mid):
    V[i]=1
    for nt,nx in Pa[i]:
        if nt>mid:break
        if P[nx]==-1 or (not V[P[nx]] and DFS(P[nx],mid)):
            C[i]=nx
            P[nx]=i
            Z[i]=nt
            return 1
    return 0
def BFS(q):
    global r
    Que=deque([q])
    V=[[-1]*M for _ in range(N)]
    V[q[0]][q[1]]=0
    while Que:
        y,x,t=Que.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and A[Y][X]!='X' and V[Y][X]==-1:
                V[Y][X]=t+1
                Que.append((Y,X,t+1))
                r=max(r,t+1)
                if A[Y][X]=='P':Pa[idx].append((t+1,Map[Y][X]))
N,M=map(int,input().split())
A=[input() for _ in range(N)]
Map=[[-1]*M for _ in range(N)]
Que,tmp=[],0
for i in range(N):
    for j in range(M):
        if A[i][j]=='C':Que.append((i,j,0))
        elif A[i][j]=='P':Map[i][j]=tmp;tmp+=1
if not len(Que):print(0);exit(0)
if len(Que)>tmp:print(-1);exit(0)
Pa=[[]for _ in range(len(Que))]
l,r=0,0
for idx,q in enumerate(Que):
    BFS(q)
    Pa[idx]=sorted(Pa[idx])
Re=-1
while l<=r:
    Mid=(l+r)//2
    C=[-1]*len(Que)
    P=[-1]*tmp
    Z=[-1]*len(Que)
    R=0
    for i in range(len(Que)):
        if C[i]==-1:
            V=[0]*len(Que)
            if DFS(i,Mid):R+=1
    if R==len(Que):
        Re=max(Z)
        r=Mid-1
    else:l=Mid+1
print(Re)
