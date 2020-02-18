import sys
sys.stdin=open('bj16946.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    Island[y][x]=t
    Q=deque([(y,x)])
    s=1
    while Q:
        hy,hx=Q.popleft()
        for d in range(4):
            Y,X=hy+dy[d],hx+dx[d]
            if IS(Y,X) and not A[Y][X] and not Island[Y][X]:
                Island[Y][X]=t
                s+=1
                Q.append((Y,X))
    Dic[n]=s
def Check(y,x):
    global n
    r,V=1,[]
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and not A[Y][X]:
            if not Island[Y][X]:n+=1;BFS(Y,X,n)
            t=Island[Y][X]
            if t in V:continue
            r+=Dic[t]
            V.append(t)
    return r
N,M=map(int,input().split())
A=[list(map(int,input()))for _ in range(N)]
Island=[[0]*M for _ in range(N)]
Dic={0:0}
n=0
for i in range(N):
    for j in range(M):
        if A[i][j]:print(Check(i,j)%10,end='')
        else:print(0,end='')
    print()
