import sys
sys.stdin = open('bj3179.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
def Dot(y,x):
    for d in range(4):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X)and Arr[Y][X]=='X':return True
    return False
def Check(L):
    for l in L:Map[l[0]][l[1]]=l[2]
    Que=L
    r=[]
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                Y,X=q[0]+dy[d],q[1]+dx[d]
                if IS(Y,X) and Arr[Y][X]=='.' and not Map[Y][X]:
                    Map[Y][X]=q[2]
                    Q.append((Y,X,q[2]))
                elif IS(Y,X) and Map[Y][X]>0 and Map[Y][X]!=Map[q[0]][q[1]]:return False
                elif IS(Y,X) and Arr[Y][X]=='X' and Map[Y][X]!=-1:
                    Map[Y][X]=-1
                    r.append((Y,X,q[2]))
        Que=Q
    return r
R,C=map(int,input().split())
Arr=[list(map(str,input()))for y in range(R)]
Que,L,tmp,r=[],[],1,0
Map=[[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if Arr[i][j]=='.'and Dot(i,j):Que.append((i,j))
        elif Arr[i][j]=='L':L.append((i,j,tmp));tmp+=1;Que.append((i,j));Arr[i][j]='.'
while True:
    Q=[]
    for q in Que:
        for d in range(4):
            Y,X=q[0]+dy[d],q[1]+dx[d]
            if IS(Y,X) and Arr[Y][X]=='X':
                Arr[Y][X]='.'
                if Dot(Y,X):Q.append((Y,X))
    Que=Q
    L=Check(L)
    if not L:break
    r+=1
print(r+1)


