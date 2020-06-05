import sys
sys.stdin = open('2383.txt','r')

import itertools
def Sol(P):
    r=0
    while r<R and P:
        for i in range(2):
            p=0
            for j in range(len(s[i])):
                if s[i][j]>S[i][2]:s[i][j]-=1
                elif s[i][j]<=S[i][2] and j<3:
                    s[i][j]-=1
                    if s[i][j]==0:p+=1;P-=1
            s[i]=s[i][p:]
        r+=1
    return r
for t in range(int(input())):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    P,p,S=[],0,[]
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                if A[i][j]==1:P.append((i,j));p+=1
                else:S.append((i,j,A[i][j]))
    R=10**9
    for Per in itertools.product(range(2),repeat=p):
        s=[[],[]]
        for i,(y,x) in enumerate(P):s[Per[i]].append(abs(y-S[Per[i]][0])+abs(x-S[Per[i]][1])+S[Per[i]][2]+1)
        for i in range(2):s[i].sort()
        R=min(R,Sol(p))
    print('#%d %d'%(t+1,R))