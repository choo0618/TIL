import sys
sys.stdin = open('bj15686.txt','r')

import itertools
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
N=L[0]
R=987654321
C=[]
H=[]
for i in range(N):
    for j in range(N):
        if A[i][j]==2:C.append([i,j])
        elif A[i][j]:H.append([i,j])
c=[]
for _ in range(len(C)):
    c.append(_)
comb=list(itertools.combinations(c,L[1]))
for n in comb:
    M=[[[0for _ in range(L[1])]for _ in range(N)]for _ in range(N)]
    r=0
    ccc=0
    for cc in n:
        for h in H:
            y = abs(C[cc][0]-h[0])
            x = abs(C[cc][1]-h[1])
            M[h[0]][h[1]][ccc] = y + x
        ccc+=1
    for d in H:
        r+=min(M[d[0]][d[1]])
    if r<R:R=r
print(R)