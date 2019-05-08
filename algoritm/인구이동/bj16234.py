import sys
sys.stdin = open('bj16234.txt', 'r')

dy=[-1,0,1,0]
dx=[0,1,0,-1]
def IS(y,x):
    if -1<y<N and -1<x<N and not M[y][x]:return True
    return False
def C():
    for y in range(N):
        for x in range(N):
            if M[y][x]:return False
    return True
def BFS(y,x,I):
    Q=[]
    Q.append([y,x])
    while Q:
        tmp=Q.pop(0)
        hY=tmp[0]
        hX=tmp[1]
        for dir in range(4):
            nY=hY+dy[dir]
            nX=hX+dx[dir]
            if IS(nY,nX) and L[1]<=abs(A[hY][hX]-A[nY][nX])<=L[2]:
                Q.append([nY,nX])
                M[nY][nX]=I
                sc[I][0]+=A[nY][nX]
                sc[I][1]+=1
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
N=L[0]
R=0
while True:
    M=[[0]*N for _ in range(N)]
    I=1
    sc=[[0,0],[0,0]]
    for i in range(N):
        for j in range(N):
            if not M[i][j]:
                BFS(i,j,I)
                if M[i][j]:
                    I+=1
                    sc.append([0,0])
    if C():break
    for m in range(1,len(sc)-1):
        tmp=sc[m][0]//sc[m][1]
        for cy in range(N):
            for cx in range(N):
                if M[cy][cx]==m:A[cy][cx]=tmp
    R+=1
print(R)