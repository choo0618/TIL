import sys
sys.stdin = open('bj1486.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(q,Mid):
    if A[0][0]>=Mid:return True
    Map=[[[-1]*M for _ in range(N)]for __ in range(2)]
    Map[0][0][0]=0
    Que=deque([q])
    while Que:
        y,x,t,tmp=Que.popleft()
        if Map[1][0][0]!=-1:return True
        for d in range(4):
            Y,X,ntmp=y+dy[d],x+dx[d],tmp
            if IS(Y,X):
                if abs(A[Y][X]-A[y][x])>T:continue
                if A[Y][X]>=Mid:ntmp=1
                if A[y][x]>=A[Y][X]:nT=t+1
                else:nT=t+(A[Y][X]-A[y][x])**2
                if nT<=D and (Map[ntmp][Y][X]==-1 or Map[ntmp][Y][X]>nT):
                    Map[ntmp][Y][X]=nT
                    Que.append((Y,X,nT,ntmp))
    return False
N,M,T,D=map(int,input().split())
A=[list(map(str,input()))for _ in range(N)]
for i in range(N):
    for j in range(M):
        k=ord(A[i][j])
        if k>=97:k-=71
        else:k-=65
        A[i][j]=k
l,r=A[0][0],51
while l<=r:
    Mid=(l+r)//2
    if BFS((0,0,0,0),Mid):l=Mid+1
    else:r=Mid-1
print(r)