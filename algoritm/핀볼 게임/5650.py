import sys
sys.stdin = open('5650.txt','r')

dx=[0,1,0,-1]
dy=[-1,0,1,0]
D=[0,[2,3,1,0],[1,3,0,2],[3,2,0,1],[2,0,3,1],[2,3,0,1]]
def IS(y,x):
    if -1<y<N and -1<x<N:return True
    return False
def Go(y,x,d):
    global R
    r=0
    s=[y,x]
    nY=y+dy[d]
    nX=x+dx[d]
    while True:
        if not IS(nY,nX):
            d+=2
            if d>3:d-=4
            nY+=dy[d]
            nX+=dx[d]
            r+=1
        n=A[nY][nX]
        if [nY,nX]==s:
            if r>R:R=r
            break
        elif n==-1:
            if r>R:R=r
            break
        elif 0<n<6:
            d=D[n][d]
            r+=1
        elif 5<n<11:
            for w in M[n]:
                if w!=[nY,nX]:
                    nY,nX=w[0],w[1]
                    break
        nY+=dy[d]
        nX+=dx[d]
T=int(input())
for t in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    M=[[]for _ in range(12)]
    R=0
    for i in range(N):
        for j in range(N):
            if not A[i][j]:M[0].append([i,j])
            else:M[A[i][j]].append([i,j])
    for c in M[0]:
        for dir in range(4):
            Go(c[0],c[1],dir)
    print('#%d %d'%(t+1,R))