import sys
sys.stdin = open('bj1113.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x):
    r,l=1,[(y,x)]
    Q=[(y,x)]
    V[y][x]=1
    tmp=0
    while Q:
        y,x=Q.pop()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and A[Y][X]<=h and V[Y][X]==0:
                if A[Y][X]<h or Y==0 or Y==N-1 or X==0 or X==M-1:tmp=1
                V[Y][X]=1
                Q.append((Y,X))
                l.append((Y,X))
                r+=1
    if tmp:return 0
    for i,j in l:A[i][j]+=1
    return r
N,M=map(int,input().split())
A=[list(map(int,input()))for y in range(N)]
R=0
for h in range(1,9):
    V=[[0]*M for _ in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if A[i][j]==h and V[i][j]==0:R+=BFS(i,j)
print(R)