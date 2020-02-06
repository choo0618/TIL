import sys
sys.stdin=open('bj2638.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M
def Check(i,j):
    cnt=0
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        I,J=i+d[0],j+d[1]
        if IS(I,J) and not A[I][J]:cnt+=1
    return cnt
def BFS(i,j):
    Map[i][j]=1
    Que=deque([(i,j)])
    while Que:
        y,x=Que.popleft()
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            Y,X=y+d[0],x+d[1]
            if IS(Y,X) and not Map[Y][X]:
                if A[Y][X]:
                    if not (Y,X) in C:C[(Y,X)]=1
                    else:C[(Y,X)]+=1
                    continue
                Map[Y][X]=1
                Que.append((Y,X))
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Sum=sum(sum(a)for a in A)
R=0
while Sum:
    R+=1
    C={}
    Map=[[0]*M for _ in range(N)]
    BFS(0,0)
    for c in C.items():
        if c[1]>=2:A[c[0][0]][c[0][1]]=0;Sum-=1
print(R)