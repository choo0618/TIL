import sys
sys.stdin=open('bj2931.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
Dic={'.':[0,0,0,0],'M':[1,1,1,1],'Z':[1,1,1,1],'|':(0,1,0,1),'-':(1,0,1,0),'+':(1,1,1,1),'1':(1,1,0,0),'2':(1,0,0,1),'3':(0,0,1,1),'4':(0,1,1,0)}
def IS(y,x):
    return -1<y<R and -1<x<C
R,C=map(int,input().split())
Arr=[list(map(str,input()))for y in range(R)]
T=[]
for i in range(R):
    for j in range(C):
        if not Arr[i][j] in '.MZ':T.append((i,j,Arr[i][j]))
Here=0
for t in T:
    for idx,d in enumerate(Dic[t[2]]):
        if not d:continue
        Y,X=t[0]+dy[idx],t[1]+dx[idx]
        if Arr[Y][X]=='.':Here=(Y,X)
    if Here:break
for i in ['|','-','+','1','2','3','4']:
    Check=1
    for idx,d in enumerate(Dic[i]):
        Y,X=Here[0]+dy[idx],Here[1]+dx[idx]
        if d and not IS(Y,X):Check=0;break
        if not d and not IS(Y,X):continue
        nD=(idx+2)%4
        if d!=Dic[Arr[Y][X]][nD]:
            if Arr[Y][X]=='M' or Arr[Y][X]=='Z':continue
            Check=0;break
    if Check:print(Here[0]+1,Here[1]+1,i);break

# BFS
from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
Dic={'|':[0,1,0,1],'-':[1,0,1,0],'+':[1,1,1,1],'1':[1,1,0,0],'2':[1,0,0,1],'3':[0,0,1,1],'4':[0,1,1,0]}
def IS(y,x):
    return -1<y<R and -1<x<C
R,C=map(int,input().split())
A=[list(map(str,input()))for y in range(R)]
V=[[0]*C for _ in range(R)]
Q=deque()
for i in range(R):
    for j in range(C):
        if not A[i][j] in 'MZ':continue
        D=[0,0,0,0]
        for d in range(4):
            y,x=i+dy[d],j+dx[d]
            if IS(y,x) and not A[y][x] in '.MZ':D[d]=1;break
        Q.append((i,j,D))
        V[i][j]=1
i,j,r=0,0,[0,0,0,0]
while Q:
    y,x,D=Q.popleft()
    for d in range(4):
        if not D[d]:continue
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and not V[Y][X]:
            if A[Y][X]=='.':i,j,r[(d+2)%4]=Y+1,X+1,1;continue
            V[Y][X]=1
            Q.append((Y,X,Dic[A[Y][X]]))
for k,v in Dic.items():
    if v==r:print(i,j,k);break

dx=[1,0,-1,0]
dy=[0,1,0,-1]
Dic={'|':[0,1,0,1],'-':[1,0,1,0],'+':[1,1,1,1],'1':[1,1,0,0],'2':[1,0,0,1],'3':[0,0,1,1],'4':[0,1,1,0]}
R,C=map(int,input().split())
A=[input()for y in range(R)]
y,x,r=0,0,[0]*4
for i in range(R):
    for j in range(C):
        if A[i][j] in '.MZ':continue
        D=Dic[A[i][j]]
        for d in range(4):
            if not D[d]:continue
            Y,X=i+dy[d],j+dx[d]
            if A[Y][X]=='.':y,x,r[(d+2)%4]=Y+1,X+1,1
for k,v in Dic.items():
    if v==r:print(y,x,k);break

