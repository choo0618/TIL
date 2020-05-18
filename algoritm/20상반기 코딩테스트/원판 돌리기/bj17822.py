import sys
sys.stdin = open('bj17822.txt','r')

from collections import deque
def BFS(i,j,t):
    global S
    V[i][j]=1
    Q=[(i,j)]
    c=1
    while Q:
        y,x=Q.pop()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if Y==-1 or Y==N:continue
            if X==-1:X=M-1
            elif X==M:X=0
            if V[Y][X] or A[Y][X]!=t:continue
            V[Y][X]=1
            Q.append((Y,X))
            A[Y][X]=-1
            c+=1
    return A[i][j]*c,c
def Avg(t):
    tmp=0
    for i in range(N):
        for j in range(M):
            if A[i][j]==-1:continue
            if A[i][j]>t:A[i][j]-=1;tmp-=1
            elif A[i][j]<t:A[i][j]+=1;tmp+=1
    return tmp
N,M,T=map(int,input().split())
A=[deque(int(x)for x in input().split())for y in range(N)]
S,C=sum(sum(x)for x in A),N*M
for t in range(T):
    if not C:break
    x,d,k=map(int,input().split())
    if d:k=M-k
    for n in range(x-1,N,x):
        for _ in range(k):A[n].rotate()
    V=[[0]*M for _ in range(N)]
    tmp=1
    for i in range(N):
        for j in range(M):
            if V[i][j] or A[i][j]==-1:continue
            s,c=BFS(i,j,A[i][j])
            if c>1:A[i][j]=-1;S-=s;C-=c;tmp=0
    if tmp:S+=Avg(S/C)
print(S)