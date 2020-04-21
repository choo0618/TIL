import sys
sys.stdin = open('5656.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<H and -1<x<W
def Ball(Map,j):
    S=[l[:]for l in Map]
    Q=[]
    for i in range(H):
        if S[i][j]:
            if S[i][j]==1:S[i][j]=0;return S
            Q.append((i,j,S[i][j]))
            break
    if not Q:return S
    while Q:
        y,x,C=Q.pop()
        S[y][x]=0
        if C==1:continue
        for d in range(4):
            for c in range(1,C):
                Y,X=y+c*dy[d],x+c*dx[d]
                if not IS(Y,X):break
                if not S[Y][X]:continue
                Q.append((Y,X,S[Y][X]))
    for x in range(W):
        for y in range(H-1,0,-1):
            if S[y][x]:continue
            tmp=y-1
            while tmp>=0:
                if S[tmp][x]:S[y][x],S[tmp][x]=S[tmp][x],0;break
                tmp-=1
    return S
def DFS(Map,c):
    global R
    if c==N:
        R=min(R,W*H-sum(l.count(0)for l in Map))
        return
    for j in range(W):
        DFS(Ball(Map,j),c+1)
for t in range(int(input())):
    N,W,H=map(int,input().split())
    R,A=10**9,[[int(x)for x in input().split()]for y in range(H)]
    DFS(A,0)
    print('#%d %d'%(t+1,R))
