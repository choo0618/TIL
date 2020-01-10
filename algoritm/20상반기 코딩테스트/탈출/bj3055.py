import sys
sys.stdin = open('bj3055.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C

R,C = map(int,input().split())
A=[list(map(str,input()))for y in range(R)]
Water,Go,T,Result = [],[],1,'KAKTUS'
for i in range(R):
    for j in range(C):
        if A[i][j]==('*' or 'X'):
            if A[i][j] == '*': Water.append([i,j])
            A[i][j] = -1
        elif A[i][j]=='S':
            A[i][j]=1
            Go.append([i,j])
        elif A[i][j] == '.':A[i][j]=0
while Go:
    W,G,check=[],[],0
    for w in Water:
        hY,hX=w
        for dir in range(4):
            nY = hY+dy[dir]
            nX = hX+dx[dir]
            if IS(nY,nX) and (not A[nY][nX] or A[nY][nX]==1):
                A[nY][nX]=-1
                W.append([nY,nX])
    for g in Go:
        hY,hX=g
        for dir in range(4):
            nY = hY+dy[dir]
            nX = hX+dx[dir]
            if IS(nY,nX):
                if A[nY][nX]=='D':
                    Result=T
                    check=1
                if not A[nY][nX]:
                    A[nY][nX] = 1
                    G.append([nY,nX])
    Water,Go=W,G
    if check:break
    T+=1
print(Result)



