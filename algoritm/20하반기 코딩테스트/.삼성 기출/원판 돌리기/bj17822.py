import sys
sys.stdin = open('bj17822.txt','r')

from collections import deque
def BFS(n):
    global Sum,Chk
    tmp=1
    V[i][j]=1
    Q=[(i,j)]
    while Q:
        y,x=Q.pop()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if Y==-1 or Y==N:continue
            if X==-1:X=M-1
            elif X==M:X=0
            if V[Y][X]==0 and A[Y][X]==n:
                Q.append((Y,X))
                V[Y][X]=1
                A[Y][X]=0
                tmp+=1
    if tmp==1:return 0
    Sum-=tmp*A[i][j]
    A[i][j]=0
    Chk=1
    return tmp
N,M,T=map(int,input().split())
A=[deque(int(_)for _ in input().split())for __ in range(N)]
Cnt,Sum=N*M,sum(sum(a)for a in A)
for t in range(T):
    x,d,k=map(int,input().split())
    if d:k=M-k
    for i in range(x-1,N,x):
        for n in range(k):A[i].rotate()
    V=[[0]*M for _ in range(N)]
    Chk=0
    for i in range(N):
        for j in range(M):
            if A[i][j] and V[i][j]==0:Cnt-=BFS(A[i][j])
    if Chk:continue
    if Cnt==0:break
    Avg=Sum/Cnt
    for i in range(N):
        for j in range(M):
            if A[i][j]==0:continue
            if A[i][j]>Avg:A[i][j]-=1;Sum-=1
            elif A[i][j]<Avg:A[i][j]+=1;Sum+=1
print(Sum)