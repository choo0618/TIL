import sys
sys.stdin = open('bj15686.txt','r')

import itertools
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
C,H=[],[]
for i in range(N):
    for j in range(N):
        if A[i][j]==1:H.append((i,j))
        elif A[i][j]==2:C.append((i,j))
R=10**9
for n in range(1,M+1):
    for i in itertools.combinations(C,n):
        d=[0]*len(H)
        for idx,h in enumerate(H):d[idx]=min(abs(h[0]-y)+abs(h[1]-x)for y,x in i)
        R=min(R,sum(d))
print(R)

D=[[0]*len(C)for _ in range(len(H))]
for i,h in enumerate(H):
    for j,c in enumerate(C):
        D[i][j]=abs(h[0]-c[0])+abs(h[1]-c[1])
R=10**9
for i in itertools.combinations(range(len(C)),M):
    r=0
    for j in range(len(H)):r+=min(D[j][c]for c in i)
    R=min(R,r)
print(R)