import sys
sys.stdin = open('bj14889.txt','r')

import itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=99999999
c=[]
for _ in range(N):
    c.append(_)
comb=list(itertools.combinations(c,N//2))
comb=comb[0:len(comb)//2]
for l in comb:
    S,L=0,0
    for i in range(N):
        for j in range(N):
            if i in l and j in l:S+=A[i][j]
            elif not i in l and not j in l:L+=A[i][j]
    if abs(S-L)<R:R=abs(S-L)
print(R)