import sys
sys.stdin = open('bj17472.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    IL[y][x]=t
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        e=0
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and IL[Y][X]==-1:
                if A[Y][X]==0:e=1;continue
                IL[Y][X]=t
                Q.append((Y,X))
        if e:Edge.append((y,x,t))
def Dis(y,x,t):
    for d in range(4):
        Y,X,cnt=y,x,0
        while IS(Y+dy[d],X+dx[d]):
            Y+=dy[d];X+=dx[d]
            cnt+=1
            if IL[Y][X]!=-1:
                if IL[Y][X]!=t and cnt>2:D[t][IL[Y][X]]=min(cnt-1,D[t][IL[Y][X]])
                break
def MST():
    P=list(range(il))
    def Find(x):
        if P[x]!=x:P[x]=Find(P[x])
        return P[x]
    def union(a,b):P[a]=b
    R,c=0,0
    for d,a,b in DIS:
        a,b=Find(a),Find(b)
        if a!=b:union(a,b);R+=d;c+=1
        if c==il-1:return R
    return -1
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
il,IL=0,[[-1]*M for _ in range(N)]
Edge=[]
for i in range(N):
    for j in range(M):
        if A[i][j] and IL[i][j]==-1:BFS(i,j,il);il+=1
D=[[10**9]*il for _ in range(il)]
for y,x,i in Edge:Dis(y,x,i)
DIS=[]
for i in range(il):
    for j in range(i+1,il):
        if D[i][j]!=10**9:DIS.append((D[i][j],i,j))
DIS.sort()
print(MST())