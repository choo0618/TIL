import sys
sys.stdin = open('1767.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def Check(y,x,d):
    l=[]
    while True:
        y+=dy[d]
        x+=dx[d]
        if not IS(y,x):return l
        if A[y][x]:return []
        l.append((y,x))
def DFS(idx,r,c):
    global R,C
    if c+(p-idx)<C:return
    if idx==p:
        if c>C:R=r
        else:R=min(R,r)
        C=max(C,c)
        return
    y,x=P[idx]
    for d in range(4):
        l=Check(y,x,d)
        if not l:continue
        for i,j in l:A[i][j]=1
        DFS(idx+1,r+len(l),c+1)
        for i,j in l:A[i][j]=0
    DFS(idx+1,r,c)
for t in range(int(input())):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R,C,P,p=10**9,0,[],0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if A[i][j]:P.append((i,j));p+=1
    DFS(0,0,0)
    print('#%d %d'%(t+1,R))

