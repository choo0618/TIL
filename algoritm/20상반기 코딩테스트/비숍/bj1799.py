import sys
sys.stdin = open('bj1799.txt','r')

dx=[1,1,-1,-1]
dy=[-1,1,1,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def Check(y,x):
    L=[(y,x)]
    for d in range(4):
        Y,X=y,x
        while True:
            Y+=dy[d]
            X+=dx[d]
            if not IS(Y,X):break
            if A[Y][X]:L.append((Y,X))
    return L
def DFS(idx,r,List,Len,bw):
    global b,w
    if idx==Len:
        if bw:b=max(b,r)
        else:w=max(w,r)
        return
    for i in range(idx,Len):
        y,x=List[i]
        if A[y][x]:
            L=Check(y,x)
            for Y,X in L:A[Y][X]=0
            DFS(i+1,r+1,List,Len,bw)
            for Y,X in L:A[Y][X]=1
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
B,W=[],[]
for i in range(N):
    for j in range(N):
        if not A[i][j]:continue
        if i%2:
            if j%2:B.append((i,j))
            else:W.append((i,j))
        else:
            if j%2:W.append((i,j))
            else:B.append((i,j))
b,w=0,0
DFS(0,0,B,len(B),1)
DFS(0,0,W,len(W),0)
print(b+w)