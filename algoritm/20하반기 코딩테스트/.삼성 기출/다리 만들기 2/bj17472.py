import sys
sys.stdin = open('bj17472.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    V[y][x]=t
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X] and V[Y][X]==0:
                V[Y][X]=t
                Q.append((Y,X))
def Dis(a,b):
    L=[]
    for i in range(a):
        s,d=0,0
        for j in range(b-1):
            if V[i][j] and V[i][j+1]==0:s,d=V[i][j],0
            elif V[i][j]==0:
                if V[i][j+1]:
                    if s and s!=V[i][j+1] and d:L.append((d+1,s,V[i][j+1]))
                    s=0
                else:d+=1
    return L
def MST():
    P=list(range(tmp))
    def Find(x):
        if P[x]!=x:P[x]=Find(P[x])
        return P[x]
    def union(a,b):
        P[a]=b
    R,cnt=0,0
    for d,a,b in L:
        A,B=Find(a),Find(b)
        if A!=B:R+=d;cnt+=1;union(A,B)
        if cnt==tmp-2:return R
    return -1
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
tmp,V=1,[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] and V[i][j]==0:BFS(i,j,tmp);tmp+=1
L=[]
L+=Dis(N,M)
V=list(map(list,zip(*V[::])))
L+=Dis(M,N)
L.sort()
print(MST())