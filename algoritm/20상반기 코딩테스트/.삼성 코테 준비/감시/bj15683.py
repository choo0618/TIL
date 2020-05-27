import sys
sys.stdin = open('bj15683.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
D=[0,[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!=6
def Check(y,x,D):
    l,c=[],0
    for d in D:
        Y,X=y+dy[d],x+dx[d]
        while IS(Y,X):
            if A[Y][X]==0:l.append((Y,X));c+=1
            Y+=dy[d];X+=dx[d]
    return l,c
def DFS(idx,r):
    global S
    if idx==c:S=min(S,r);return
    y,x,D=C[idx]
    for d in D:
        l,cnt=Check(y,x,d)
        for i,j in l:A[i][j]='#'
        DFS(idx+1,r-cnt)
        for i,j in l:A[i][j]=0
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
S,C,c=0,[],0
for i in range(N):
    for j in range(M):
        if A[i][j]==0:S+=1
        elif A[i][j]!=6:C.append((i,j,D[A[i][j]]));c+=1
DFS(0,S)
print(S)
