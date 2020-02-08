import sys
sys.stdin = open('bj17836.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
N,M,T=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
k=0
if A[0][0]==2:k=1
Q=deque([(0,0,k,0)])
Map=[[[0,0]for _ in range(M)]for __ in range(N)]
TI=[[[10**9,10**9]for __ in range(M)] for _ in range(N)]
while Q:
    y,x,s,t=Q.popleft()
    for d in range(4):
        Y,X,S,Ti=y+dy[d],x+dx[d],s,t+1
        if IS(Y,X) and (A[Y][X]!=1 or s) and not Map[Y][X][S] and TI[Y][X][s]>Ti and Ti<=T:
            if A[Y][X]==2:S=1
            TI[Y][X][s]=Ti
            Map[Y][X][S]=1
            Q.append((Y,X,S,Ti))
print(min(TI[N-1][M-1]) if min(TI[N-1][M-1])!=10**9 else 'Fail')


