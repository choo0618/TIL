import sys
sys.stdin = open('bj2933.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<R and -1<x<C
def BFS(y,x,t):
    l=[(y,x)]
    V[y][x]=t
    Q=deque([(y,x)])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X]=='x' and V[Y][X]==0:
                V[Y][X]=t
                Q.append((Y,X))
                l.append((Y,X))
    return l
def Check(l,t,d):
    for y,x in l:
        if y+d==R or (V[y+d][x] and V[y+d][x]!=t):return 0
    return 1
R,C=map(int,input().split())
A=[list(input())for _ in range(R)]
t=0
input()
for r in map(int,input().split()):
    a,b,c=0,C,1
    if t:a,b,c=C-1,-1,-1
    for j in range(a,b,c):
        if A[R-r][j]=='x':A[R-r][j]='.';break
    V=[[0]*C for _ in range(R)]
    tmp,L=1,[[]]
    for i in range(R):
        for j in range(C):
            if A[i][j]=='x' and V[i][j]==0:L.append(BFS(i,j,tmp));tmp+=1
    for i in range(1,tmp):
        d=0
        while Check(L[i],i,d+1):d+=1
        if d==0:continue
        for y,x in L[i]:A[y][x]='.'
        for y,x in L[i]:A[y+d][x]='x'
    t=(t+1)%2
for a in A:print(''.join(a))
