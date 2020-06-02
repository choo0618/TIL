import sys
sys.stdin = open('bj16236.txt','r')

from collections import deque
def IS(y,x,s):
    return -1<y<N and -1<x<N and A[y][x]<=s
def BFS(i,j,s):
    V=[[0]*N for _ in range(N)]
    Q=deque([(i,j,0)])
    V[i][j],l,T=1,[],10**9
    while Q:
        y,x,t=Q.popleft()
        if t>T:break
        if 0<A[y][x]<s:
            T=t
            l.append((y,x))
            continue
        for Y,X in (y-1,x),(y,x-1),(y,x+1),(y+1,x):
            if IS(Y,X,s) and V[Y][X]==0:
                V[Y][X]=1
                Q.append((Y,X,t+1))
    if not l:return 0,0,0
    l.sort()
    y,x=l[0]
    A[y][x]=0
    return y,x,T
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Q=deque()
for i in range(N):
    for j in range(N):
        if A[i][j]==9:A[i][j],y,x=0,i,j
R,s,e=0,2,0
while 1:
    y,x,r=BFS(y,x,s)
    if r==0:break
    R+=r;e+=1
    if s==e:s,e=s+1,0
print(R)