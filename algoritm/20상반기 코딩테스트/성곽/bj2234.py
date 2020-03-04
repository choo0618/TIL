import sys
sys.stdin = open('bj2234.txt','r')

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(y,x,t):
    Map[y][x]=t
    r,Q=1,[(y,x)]
    while Q:
        y,x=Q.pop()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and not Map[Y][X] and A[y][x][d]==A[Y][X][(d+2)%4]=='0':
                Map[Y][X]=t
                Q.append((Y,X))
                r+=1
    S.append(r)
M,N=map(int,input().split())
A=[[bin(int(x))[2:].zfill(4)for x in input().split()]for y in range(N)]
Map=[[0]*M for _ in range(N)]
tmp,R,S=0,0,[0]
for i in range(N):
    for j in range(M):
        if not Map[i][j]:tmp+=1;BFS(i,j,tmp)
for i in range(N):
    for j in range(M):
        for I,J in (i,j),(i+1,j),(i,j-1),(i-1,j):
            if not IS(I,J) or Map[i][j]==Map[I][J]:continue
            R=max(R,S[Map[i][j]]+S[Map[I][J]])
print(len(S)-1)
print(max(S))
print(R)
