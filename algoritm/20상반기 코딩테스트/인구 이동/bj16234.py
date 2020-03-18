import sys
sys.stdin = open('bj16234.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x):
    Map[y][x]=1
    Q,l=[(y,x)],[(y,x)]
    cnt,p=1,A[y][x]
    while Q:
        y,x=Q.pop()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and L<=abs(A[y][x]-A[Y][X])<=R and not Map[Y][X]:
                Map[Y][X]=1
                cnt+=1
                p+=A[Y][X]
                Q.append((Y,X))
                l.append((Y,X))
    for y,x in l:A[y][x]=p//cnt
N,L,R=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
T,Check=0,1
while True:
    tmp,Map=0,[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not Map[i][j]:BFS(i,j);tmp+=1
    if tmp==N**2:break
    T+=1
print(T)