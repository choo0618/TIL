import sys
sys.stdin = open('bj18809.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]==1
def BFS():
    r=0
    V=[[0]*M for _ in range(N)]
    Q=deque()
    while Q:
        y,x,n=Q.popleft()
        if V[y][x]==9:r+=1;continue
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X):
                if V[Y][X]==0:
                    V[Y][X]=n
                    Q.append((Y,X,n))
                elif V[Y][X]!=n:V[Y][X]=9
    print(r)
    return r
def DFS(g,r,idx,l):
    global F
    if g==r==0:
        F=max(F,BFS())
        return
    for i in range(idx,b):
        y,x=B[i]
        if g:
            A[y][x]='G'
            DFS(g-1,r,i+1,l)
        if r:
            A[y][x]='R'
            DFS(g,r-1,i+1,l)
        A[y][x]=2
N,M,G,R=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
B,b=[],0
for i in range(N):
    for j in range(M):
        if A[i][j]==2:B.append((i,j));A[i][j]=1;b+=1
F=0
DFS(G,R,0,[])
print(F)