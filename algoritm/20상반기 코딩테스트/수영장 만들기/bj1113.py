import sys
sys.stdin = open('bj1113.txt','r')

from collections import deque
def BFS(y,x,h):
    Map[y][x]=1
    Q,water,tmp=deque([(y,x)]),[(y,x)],0
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if A[Y][X]>h or Map[Y][X]:continue
            if Y==0 or Y==N-1 or X==0 or X==M-1 or A[Y][X]<h:tmp=1;continue
            Map[Y][X]=1
            water.append((Y,X))
            Q.append((Y,X))
    if tmp:return []
    return water
N,M=map(int,input().split())
A=[list(map(int,input()))for y in range(N)]
Max,R=max(max(x)for x in A),0
for m in range(1,Max):
    Map=[[0]*M for _ in range(N)]
    Water=[]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if A[i][j]==m and not Map[i][j]:Water+=BFS(i,j,m)
    for y,x in Water:A[y][x]+=1;R+=1
print(R)

