import sys
sys.stdin = open('bj7569.txt','r')

dh=[0,0,0,0,1,-1]
dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]
def IS(z,y,x):
    return -1<z<H and -1<y<N and -1<x<M
M,N,H=map(int,input().split())
A,Que,R,c=[],[],0,1
for h in range(H):
    a=[]
    for i in range(N):
        I=[int(x)for x in input().split()]
        a.append(I)
    A.append(a)
for z in range(H):
    for i in range(N):
        for j in range(M):
            if A[z][i][j]==1:Que.append((z,i,j));c=0
while Que:
    Q=[]
    for q in Que:
        for d in range(6):
            nH=q[0]+dh[d]
            nY=q[1]+dy[d]
            nX=q[2]+dx[d]
            if IS(nH,nY,nX)and(not A[nH][nY][nX] or A[q[0]][q[1]][q[2]]<A[nH][nY][nX]<R):
                A[nH][nY][nX]=R+1
                Q.append((nH,nY,nX))
    R+=1
    Que=Q
if c:print(-1)
else:
    for z in range(H):
        for i in range(N):
            if 0 in A[z][i]:R=0
    print(R-1)
