import sys
sys.stdin = open('bj1600.txt','r')

dx=[1,0,-1,0,1,2,2,1,-1,-2,-2,-1]
dy=[0,1,0,-1,-2,-1,1,2,2,1,-1,-2]
def IS(y,x):
    return -1<y<H and -1<x<W and not A[y][x]
K=int(input())
W,H=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(H)]
Map=[[[0 for n in range(K+1)]for m in range(W)] for _ in range(H)]
Map[0][0]=[1]*(K+1)
Check,tmp=1,0
Que=[(0,0,K)]
while Que and Check:
    tmp+=1
    Q=[]
    for q in Que:
        for d in range(12):
            if d>3 and not q[2]:continue
            nY=q[0]+dy[d]
            nX=q[1]+dx[d]
            nK=q[2]
            if (nY,nX)==(H-1,W-1):Check=0;break
            if d>3:nK=q[2]-1
            if IS(nY,nX) and not Map[nY][nX][nK]:
                Map[nY][nX][nK]=1
                Q.append((nY,nX,nK))
    Que=Q
if Check:print(-1)
else:print(tmp)