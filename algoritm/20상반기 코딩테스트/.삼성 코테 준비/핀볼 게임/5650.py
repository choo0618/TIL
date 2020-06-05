import sys
sys.stdin = open('5650.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
B=[0,[2,0,3,1],[2,3,1,0],[1,3,0,2],[3,2,0,1],[2,3,0,1]]
def WH(y,x,w):
    for i,j in W[w]:
        if (i,j)!=(y,x):return i,j
def Go(y,x,d,r):
    Y,X=y,x
    while A[Y+dy[d]][X+dx[d]]!=-1 and (Y+dy[d],X+dx[d])!=(y,x):
        Y+=dy[d];X+=dx[d]
        if 1<=A[Y][X]<=5:
            r+=1
            d=B[A[Y][X]][d]
        elif A[Y][X]>=6:Y,X=WH(Y,X,A[Y][X]-6)
    return r
for t in range(int(input())):
    N=int(input())
    A=[[5]*(N+2)]+[[5]+[int(x)for x in input().split()]+[5]for y in range(N)]+[[5]*(N+2)]
    S,W=[],[[]for _ in range(5)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if A[i][j]==0:S.append((i,j))
            elif A[i][j]>=6:W[A[i][j]-6].append((i,j))
    R=0
    for y,x in S:
        for d in range(4):R=max(R,Go(y,x,d,0))
    print('#%d %d'%(t+1,R))

