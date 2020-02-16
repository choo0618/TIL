import sys
sys.stdin = open('4740.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def Up(List):
    for c in List:
        if c!='#':return False
    return True
def BFS(i,j,color):
    Q=deque([(i,j)])
    Set=[(i,j)]
    while Q:
        y,x=Q.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and not Map[Y][X] and A[Y][X]==color:
                Map[Y][X]=1
                Q.append((Y,X))
                Set.append((Y,X))
    return Set,len(Set)
def Check():
    B=[]
    Max=0
    for i in range(N):
        for j in range(M):
            if A[i][j]!='#' and not Map[i][j]:
                Map[i][j]=1
                b,l=BFS(i,j,A[i][j])
                B.append(b)
                Max=max(Max,l)
    for d in B:
        if len(d)!=Max:continue
        for e in d:A[e[0]][e[1]]='#'
def Down(Y,X,qu):
    global A
    if qu=='L' or qu=='R':Y,X=X,Y
    for j in range(X):
        for i in range(Y-1,0,-1):
            if A[i][j]!='#':continue
            y=i
            while A[y][j]=='#' and y!=-1:y-=1
            if y==-1:break
            A[i][j],A[y][j]=A[y][j],A[i][j]
    if qu=='L' or qu=='R':
        t=1 if qu=='L' else 3
        for _ in range(t):A=list(map(list,zip(*A[::-1])))
for tc in range(int(input())):
    print('#%d'%(tc+1))
    N,M,Q=map(int,input().split())
    A=[list(map(str,input()))for _ in range(N)]
    for _ in range(Q):
        q=input()
        Map=[[0]*M for _ in range(N)]
        T=0
        if q=='D':Check()
        elif q=='L':T=3
        elif q=='R':T=1
        else:
            new=list(map(str,q[2:]))
            if Up(A[0]):A.append(new);A.pop(0)
        for t in range(T):A=list(map(list,zip(*A[::-1])))
        Down(N,M,q)
    for _ in range(N):print(''.join(map(str,A[_])))
    print()