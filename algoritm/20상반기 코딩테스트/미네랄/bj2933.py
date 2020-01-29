import sys
sys.stdin = open('bj2933.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
def BFS(y,x,t):
    Map[y][x]=t
    Dic[t].append([y,x])
    Que=deque([(y,x)])
    while Que:
        Y,X=Que.popleft()
        for d in range(4):
            nY,nX=Y+dy[d],X+dx[d]
            if IS(nY,nX) and A[nY][nX]=='x' and not Map[nY][nX]:
                Map[nY][nX]=t
                Dic[t].append([nY,nX])
                Que.append((nY,nX))
def Possible(Arr,now):
    for t in Arr:
        if not IS(t[0]+1,t[1]) or (Map[t[0]+1][t[1]] and Map[t[0]+1][t[1]]!=now):return False
    return True
R,C=map(int,input().split())
A=[list(map(str,input()))for _ in range(R)]
N=int(input())
L=0
for i in [int(x)for x in input().split()]:
    if not L:a,b,c=0,C,1
    else:a,b,c,=C-1,-1,-1
    for n in range(a,b,c):
        if A[R-i][n]=='x':A[R-i][n]='.';break
    Map=[[0]*C for m in range(R)]
    Dic,tmp={},0
    for i in range(R):
        for j in range(C):
            if A[i][j]=='x' and not Map[i][j]:tmp+=1;Dic[tmp]=[];BFS(i,j,tmp)
    Check=[0]*(tmp+1)
    for c in Map[R-1]:Check[c]=1
    for dic in Dic.items():
        if Check[dic[0]]:continue
        for e in dic[1]:A[e[0]][e[1]]='.'
        while Possible(dic[1],dic[0]):
            for now in dic[1]:
                now[0]+=1
        for e in dic[1]:A[e[0]][e[1]]='x'
    L=(L+1)%2
for i in A:print(''.join(map(str,i)))

