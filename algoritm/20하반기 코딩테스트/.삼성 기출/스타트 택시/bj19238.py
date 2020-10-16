import sys
sys.stdin = open('bj19238.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x,tmp,G):
    V=[[0]*N for _ in range(N)]
    V[y][x]=1
    Q=deque([(y,x,0)])
    l,D=[],10**9
    while Q:
        y,x,d=Q.popleft()
        if d>D:break
        elif tmp==0 and A[y][x]>0 and d<=D:D=d;l.append((y,x,G-D,A[y][x]));continue
        elif tmp and (y,x)==tmp:
            if d<=G:return (y,x,G+d,A[y][x])
            break
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and V[Y][X]==0 and A[Y][X]!=-1:
                Q.append((Y,X,d+1))
                V[Y][X]=1
    if not l:return -1,-1,-1,-1
    l.sort()
    return l[0]
N,M,G=map(int,input().split())
A=[[int(x)if x=='0' else -1for x in input().split()]for y in range(N)]
y,x=map(int,input().split())
y-=1;x-=1
Dic={}
for t in range(M):
    i,j,I,J=map(int,input().split())
    A[i-1][j-1],Dic[t+1]=t+1,(I-1,J-1)
while M:
    y,x,G,n=BFS(y,x,0,G)
    if G<0:G=-1;break
    A[y][x]=0
    y,x,G,n=BFS(y,x,Dic[n],G)
    if G<0:G=-1;break
    M-=1
print(G)