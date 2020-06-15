import sys
sys.stdin = open('bj19236.txt','r')

import copy
dx=[0,0,-1,-1,-1,0,1,1,1]
dy=[0,-1,-1,0,1,1,1,0,-1]
def IS(y,x):
    return -1<y<4 and -1<x<4
def Move(I,J,Map):
    Shark=[0]*17
    M=copy.deepcopy(Map)
    for i in range(4):
        for j in range(4):
            if Map[i][j]:Shark[Map[i][j][0]]=[i,j,Map[i][j][1]]
    for i in range(1,17):
        if Shark[i]==0:continue
        y,x,d=Shark[i]
        while not IS(y+dy[d],x+dx[d]) or (y+dy[d],x+dx[d])==(I,J):
            d+=1
            if d==9:d=1
        M[y][x][1]=d
        Y,X=y+dy[d],x+dx[d]
        Shark[i]=[Y,X,d]
        if M[Y][X]:
            Shark[M[Y][X][0]]=[y,x,M[Y][X][1]]
        M[Y][X],M[y][x]=M[y][x],M[Y][X]
    return M
def DFS(y,x,r,Map):
    global R
    if not IS(y,x) or Map[y][x]==0:R=max(R,r);return
    r+=Map[y][x][0]
    D=Map[y][x][1]
    tmp=Map[y][x]
    Map[y][x]=0
    M=Move(y,x,Map)
    for n in range(1,4):
        Y,X=y+n*dy[D],x+n*dx[D]
        DFS(Y,X,r,M)
    Map[y][x]=tmp
A=[[]for _ in range(4)]
for i in range(4):
    L=[int(x)for x in input().split()]
    for j in range(0,8,2):
        A[i].append([L[j],L[j+1]])
R=0
DFS(0,0,0,A)
print(R)