import sys
sys.stdin = open('bj17822.txt','r')

from collections import deque
def BFS(i,j,t):
    global Sum,C
    c,l=1,[(i,j)]
    V[i][j]=1
    Q=[(i,j)]
    while Q:
        y,x=Q.pop()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if Y==-1 or Y==N:continue
            if X==-1:X=M-1
            elif X==M:X=0
            if V[Y][X]==0 and A[Y][X]==t:
                V[Y][X]=1
                Q.append((Y,X))
                l.append((Y,X))
                c+=1
    if c==1:return
    for y,x in l:A[y][x]=0
    Sum-=c*t;C-=c
def Avg(a):
    s=0
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                if A[i][j]>a:A[i][j]-=1;s-=1
                elif A[i][j]<a:A[i][j]+=1;s+=1
    return s
N,M,T=map(int,input().split())
A=[deque([int(x)for x in input().split()])for y in range(N)]
C,Sum=N*M,sum(sum(x)for x in A)
for t in range(T):
    x,d,k=map(int,input().split())
    if d:k=M-k
    for i in range(x-1,N,x):
        for j in range(k):A[i].rotate()
    V=[[0]*M for _ in range(N)]
    c=0
    for i in range(N):
        for j in range(M):
            if V[i][j]==0 and A[i][j]:c+=1;BFS(i,j,A[i][j])
    if not C:break
    if c==C:Sum+=Avg(Sum/C)
print(Sum)