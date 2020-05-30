import sys
sys.stdin = open('bj1194.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!='#'
N,M=map(int,input().split())
A=[input()for y in range(N)]
V=[[[0]*M for _ in range(N)]for __ in range(1<<6)]
Q=deque()
for i in range(N):
    for j in range(M):
        if A[i][j]=='0':Q.append((i,j,0,0));V[0][i][j]=1
R=10**9
while Q:
    y,x,k,c=Q.popleft()
    if A[y][x]=='1':R=c;break
    for Y,X,K in (y,x+1,k),(y+1,x,k),(y,x-1,k),(y-1,x,k):
        if IS(Y,X):
            tmp=ord(A[Y][X])
            if tmp>=97:K=k|(1<<tmp-97)
            elif tmp>=65 and K&(1<<tmp-65)==0:continue
            if V[K][Y][X]:continue
            V[K][Y][X]=1
            Q.append((Y,X,K,c+1))
print(R if R!=10**9 else -1)



