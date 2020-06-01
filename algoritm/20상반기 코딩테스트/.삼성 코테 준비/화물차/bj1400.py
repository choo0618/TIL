import sys
sys.stdin = open('bj1400.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!='.'
def DFS(y,x,r,D):
    global R
    if A[y][x]=='B':
        R=min(R,r)
        return
    for d,Y,X,t in (0,y,x+1,1),(1,y+1,x,1),(2,y,x-1,1),(3,y-1,x,1):
        if not IS(Y,X) or V[Y][X] or (D!=-1 and d==(D+2)%4):continue
        V[Y][X]=1
        if A[Y][X] in Dic:
            a,b,c,s=Dic[A[Y][X]]
            if d in a and ((r+t)%s==0 or (r+t)%s>b):t+=s-r%s
            if not d in a and 0<(r+t)%s<=b:t+=b-r%s
        DFS(Y,X,r+t,d)
        V[Y][X]=0
while 1:
    N,M=map(int,input().split())
    if N+M==0:break
    A=[input()for _ in range(N)]
    V=[[0]*M for _ in range(N)]
    d,Dic=0,{}
    for i in range(N):
        for j in range(M):
            if A[i][j]=='A':V[i][j],sY,sX=1,i,j
            elif A[i][j] in '0123456789':d+=1
    for i in range(d):
        a,b,c,d=map(str,input().split())
        c,d=int(c),int(d)
        if b=='|':c,d=d,c
        b=[0,2] if b=='-' else [1,3]
        Dic[a]=[b,c,d,c+d]
    R=10**9
    DFS(sY,sX,0,-1)
    print(R if R!=10**9 else 'impossible')
    input()