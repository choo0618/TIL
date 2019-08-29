import sys
sys.stdin = open('bj2303.txt','r')

import itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
S,R=1,0
for t in range(len(A)):
    comb=list(itertools.combinations(A[t],3))
    for c in comb:
        s=sum(c)%10
        if s>=R:R=s;S=t+1
print(S)