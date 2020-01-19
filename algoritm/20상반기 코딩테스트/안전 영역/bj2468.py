import sys
sys.stdin = open('bj2468.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N and not Map[y][x]

def BFS(y,x,tmp,h):
    Que=[[y,x]]
    Map[y][x]=tmp
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX) and A[nY][nX]>h:
                    Map[nY][nX]=tmp
                    Q.append([nY,nX])
        Que=Q
N=int(input())
Max,R=0,1
A=[]
for i in range(N):
    I=[int(x)for x in input().split()]
    A.append(I)
    if max(I)>Max:Max=max(I)
for t in range(1,Max+1):
    tmp=0
    Map=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j]>t and not Map[i][j]:tmp+=1;BFS(i,j,tmp,t)
    if tmp>R:R=tmp
print(R)



