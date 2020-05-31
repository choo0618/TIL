import sys
sys.stdin = open('bj18809.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]==1
def BFS(l):
    f=set()
    V=[[[-1,-1]for _ in range(M)] for _ in range(N)]
    Q=deque()
    for y,x,c in l:
        V[y][x][c]=0
        Q.append((y,x,c))
    while Q:
        y,x,c=Q.popleft()
        if (y,x) in f:continue
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and V[Y][X][c]==-1:
                if V[Y][X][(c+1)%2]!=-1:
                    if V[Y][X][(c+1)%2]==V[y][x][c]+1:f.add((Y,X))
                    continue
                V[Y][X][c]=V[y][x][c]+1
                Q.append((Y,X,c))
    return len(f)
def DFS(g,r,idx,l):
    global F
    if g==r==0:
        F=max(F,BFS(l))
        return
    for i in range(idx,b):
        y,x=B[i]
        if g:
            A[y][x]='G'
            l.append((y,x,0))
            DFS(g-1,r,i+1,l)
            l.pop()
        if r:
            A[y][x]='R'
            l.append((y,x,1))
            DFS(g,r-1,i+1,l)
            l.pop()
        A[y][x]=1
N,M,G,R=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
B,b=[],0
for i in range(N):
    for j in range(M):
        if A[i][j]==2:B.append((i,j));A[i][j]=1;b+=1
F=0
DFS(G,R,0,[])
print(F)