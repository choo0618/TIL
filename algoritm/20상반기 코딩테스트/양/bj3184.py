import sys
sys.stdin=open('bj3184.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
def BFS(y,x,t):
    Map[y][x]=t
    SW=[0,0]
    if Arr[y][x]=='o':SW[0]+=1
    elif Arr[y][x]=='v':SW[1]+=1
    Que=[(y,x)]
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX) and Arr[nY][nX]!='#' and not Map[nY][nX]:
                    if Arr[nY][nX]=='o':SW[0]+=1
                    elif Arr[nY][nX]=='v':SW[1]+=1
                    Map[nY][nX]=t
                    Q.append((nY,nX))
        Que=Q
    return SW

R,C=map(int,input().split())
Arr=[input()for _ in range(R)]
Map=[[0]*C for _ in range(R)]
SW=[0,0]
tmp=1
for i in range(R):
    for j in range(C):
        if Arr[i][j]!='#' and not Map[i][j]:
            List=BFS(i,j,tmp)
            tmp+=1
            if List[0]>List[1]:SW[0]+=List[0]
            else:SW[1]+=List[1]
for p in SW:print(p,end=' ')
