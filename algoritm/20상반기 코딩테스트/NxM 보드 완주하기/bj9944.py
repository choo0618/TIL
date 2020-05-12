import sys
sys.stdin = open('bj9944.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!='*'
def find(y,x,d):
    l,c=[],0
    while True:
        y,x=y+dy[d],x+dx[d]
        if IS(y,x):l.append((y,x));c+=1
        else:return l,c,y-dy[d],x-dx[d]
def DFS(y,x,r,s):
    global R
    if r>=R:return
    if not s:
        R=min(R,r)
        return
    for d in range(4):
        l,cnt,Y,X=find(y,x,d)
        if cnt==0:continue
        for i,j in l:A[i][j]='*'
        DFS(Y,X,r+1,s-cnt)
        for i,j in l:A[i][j]='.'
t=1
while True:
    try:N,M=map(int,input().split())
    except:break
    A=[]
    S,s=[],0
    R=10**6
    for i in range(N):
        l=list(input())
        for j in range(M):
            if l[j]=='.':S.append((i,j));s+=1
        A.append(l)
    for y,x in S:A[y][x]='*';DFS(y,x,0,s-1);A[y][x]='.'
    if R==10**6:R=-1
    print('Case %d: %d'%(t,R))
    t+=1