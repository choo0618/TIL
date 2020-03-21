import sys
sys.stdin = open('2.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS():
    fl=set()
    Map=[[0]*M for _ in range(N)]
    Q=deque()
    for i in range(N):
        for j in range(M):
            if A[i][j]=='G':Map[i][j]=(1,0);Q.append((i,j,0,1))
            elif A[i][j]=='R':Map[i][j]=(2,0);Q.append((i,j,0,2))
    while Q:
        y,x,t,tmp=Q.popleft()
        if (y,x) in fl:continue
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X]:
                if Map[Y][X]:
                    if Map[Y][X][0]!=tmp and Map[Y][X][1]==t+1:fl.add((Y,X))
                    continue
                Map[Y][X]=(tmp,t+1)
                Q.append((Y,X,t+1,tmp))
    return len(fl)
def DFS(G,R,I):
    global F
    if G==R==0:
        F=max(F,BFS())
        return
    for idx in range(I,b):
        i,j=B[idx]
        if G:
            A[i][j]='G'
            DFS(G-1,R,idx+1)
            A[i][j]=2
        if R:
            A[i][j]='R'
            DFS(G,R-1,idx+1)
            A[i][j]=2
N,M,G,R=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
F=0
B,b=[],0
for i in range(N):
    for j in range(M):
        if A[i][j]==2:B.append((i,j));b+=1
DFS(G,R,0)
print(F)


from collections import deque
import itertools
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(L,G):
    fl=set()
    Map=[[0]*M for _ in range(N)]
    Q,t=deque(),1
    for i,(y,x) in enumerate(L):
        if i==G:t=2
        Map[y][x]=(t,0)
        Q.append((y,x,0,t))
    while Q:
        y,x,t,tmp=Q.popleft()
        if (y,x) in fl:continue
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X]:
                if Map[Y][X]:
                    if Map[Y][X][0]!=tmp and Map[Y][X][1]==t+1:fl.add((Y,X))
                    continue
                Map[Y][X]=(tmp,t+1)
                Q.append((Y,X,t+1,tmp))
    return len(fl)
def seed(l,t):
    for i,j in l:A[i][j]=t
N,M,G,R=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
F=0
B,b=[],0
for i in range(N):
    for j in range(M):
        if A[i][j]==2:B.append((i,j));b+=1
for Per in itertools.permutations(B,G+R):
    seed(Per[:G],'G')
    seed(Per[G:],'R')
    F=max(F,BFS(Per,G))
    seed(Per,2)
print(F)


