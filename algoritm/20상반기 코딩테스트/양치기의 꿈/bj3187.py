import sys
sys.stdin = open('bj3178.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
def BFS(y,x,t):
    L=[0,0]
    Que=[(y,x)]
    Map[y][x]=t
    if A[y][x]=='v':L[1]+=1
    elif A[y][x]=='k':L[0]+=1
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                Y,X=q[0]+dy[d],q[1]+dx[d]
                if IS(Y,X) and A[Y][X]!='#' and not Map[Y][X]:
                    if A[Y][X]=='k':L[0]+=1
                    elif A[Y][X]=='v':L[1]+=1
                    Map[Y][X]=t
                    Q.append((Y,X))
        Que=Q
    return L
R,C=map(int,input().split())
A=[input()for y in range(R)]
Map=[[0]*C for _ in range(R)]
tmp=1
Re=[0,0]
for i in range(R):
    for j in range(C):
        if A[i][j]!='#' and not Map[i][j]:
            L=BFS(i,j,tmp)
            if L[0]>L[1]:Re[0]+=L[0]
            else:Re[1]+=L[1]
            tmp+=1
print('%d %d'%(Re[0],Re[1]))