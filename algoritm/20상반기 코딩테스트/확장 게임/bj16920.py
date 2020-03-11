import sys
sys.stdin = open('bj16920.txt','r')

import sys,collections
input=sys.stdin.readline
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(t):
    while S[t] and S[t][0][2]!=p[t]:
        y,x,c=S[t].popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y, X) and not Map[Y][X]:
                Map[Y][X]=1
                S[t].append([Y,X,c+1])
                C[t]+=1
    for i in range(len(S[t])):S[t][i][2]=0
N,M,P=map(int,input().split())
p=[[0]]+[int(x)for x in input().split()]
A=[input()for _ in range(N)]
C=[0]*(P+1)
S=[collections.deque()for _ in range(P+1)]
Map=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j]=='#':Map[i][j]=1
        elif A[i][j]!='.':
            tmp=int(A[i][j])
            Map[i][j]=1
            C[tmp]+=1
            S[tmp].append((i,j,0))
while any(S):
    for l in range(1,P+1):BFS(l)
print(' '.join(map(str,C[1:])))
