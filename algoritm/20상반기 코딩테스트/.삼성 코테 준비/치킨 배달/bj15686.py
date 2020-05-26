import sys
sys.stdin = open('bj15686.txt','r')

from itertools import combinations
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
C,H,c,h=[],[],0,0
for i in range(N):
    for j in range(N):
        if A[i][j]==1:H.append((i,j));h+=1
        elif A[i][j]==2:C.append((i,j));c+=1
D=[[0]*h for _ in range(c)]
for i,(cy,cx) in enumerate(C):
    for j,(hy,hx) in enumerate(H):
        D[i][j]=abs(cy-hy)+abs(cx-hx)
R=10**9
for comb in combinations(range(c),M):
    r=0
    for x in range(h):r+=min(D[y][x]for y in comb)
    R=min(R,r)
print(R)
