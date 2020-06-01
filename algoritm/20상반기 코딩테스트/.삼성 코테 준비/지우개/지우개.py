# 1*2*2 지우개 4번 넘겼을떄 최대한 가릴수 있는 곳

Dir=[[2,1,2,1],[1,0,1,0],[0,2,0,2]]
Dyx=[[(0,1,0,2),(1,0,2,0),(0,-2,0,-1),(-2,0,-1,0)],[(0,1,0,1),(2,0,1,0),(0,-1,0,-1),(-1,0,-2,0)],[(0,2,0,1),(1,0,1,0),(0,-1,0,-2),(-1,0,-1,0)]]
def IS(y,x):
    return -1<y<N and -1<x<N
def DFS(y1,x1,y2,x2,d,r,c):
    global R
    if c==5:
        R=max(R,r)
        return
    l,cnt=[],0
    for i in range(y1,y2):
        for j in range(x1,x2):
            if A[i][j]:l.append((i,j));cnt+=1
    for i,j in l:A[i][j]=0
    for i,D in enumerate(Dir[d]):
        i1,j1,i2,j2=Dyx[d][i]
        Y1,X1,Y2,X2=y1+i1,x1+j1,y2+i2,x2+j2
        if not IS(Y1,X1) or not IS(Y2-1,X2-1):continue
        DFS(Y1,X1,Y2,X2,D,r+cnt,c+1)
    for i,j in l:A[i][j]=1
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for i in range(N):
    for j in range(N):
        if A[i][j]:DFS(i,j,i+1,j+1,0,0,0)
print(R)