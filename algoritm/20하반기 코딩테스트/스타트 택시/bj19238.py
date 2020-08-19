import sys
sys.stdin = open('bj19238.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def Sol(y,x,g,c):
    if c==0:n,Guest[y][x]=Guest[y][x],0
    V=[[0]*N for _ in range(N)]
    V[y][x]=1
    Q=deque([(y,x,0)])
    tmp,L=10**9,[]
    while Q:
        y,x,d=Q.popleft()
        if c and d>tmp:break
        if c and Guest[y][x]:tmp=d;L.append((y,x,Guest[y][x]));continue
        if c==0 and n in State[y][x]:tmp=d;break
        for Y,X in (y-1,x),(y,x-1),(y,x+1),(y+1,x):
            if not IS(Y,X) or Map[Y][X] or V[Y][X]:continue
            V[Y][X]=1
            Q.append((Y,X,d+1))
    g-=tmp
    if g<0:return -1,-1,-1
    if not c:return y,x,g+2*tmp
    L.sort()
    return L[0][0],L[0][1],g
N,M,G=map(int,input().split())
Map=[[int(x)for x in input().split()]for y in range(N)]
Guest=[[0]*N for _ in range(N)]
State=[[[] for _ in range(N)] for _ in range(N)]
Y,X=map(int,input().split())
Y-=1;X-=1
for m in range(M):
    i,j,I,J=map(int,input().split())
    Guest[i-1][j-1]=m+1
    State[I-1][J-1].append(m+1)
while M:
    Y,X,G=Sol(Y,X,G,1)
    if G<0:break
    Y,X,G=Sol(Y,X,G,0)
    if G<0:break
    M-=1
print(G)

