import sys
sys.stdin = open('2383.txt','r')

import itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
print(A)
S,P,G=[],[],[[],[]]
for i in range(N):
    for j in range(N):
        if A[i][j]==1:P.append([i,j])
        elif A[i][j]:S.append([i,j,A[i][j]])
Pc=len(P)
print(S)
print(P)
Per=list(itertools.product([0,1],repeat=Pc))
print(Per)
for per in Per:
    D=[0]*Pc
    for d in range(Pc):
        D[d]=abs(P[d][0]-S[per[d]][0])+abs(P[d][1]-S[per[d]][1])
    print(D)
    t=1
    while t:
        for d in range(Pc):
            D[d]-=1
            if not D[d]:G[per[d]].append(S[per[d]][2]+2)
        for g in G:
            if not g:continue
            w=3
            if len(g)<3:w=len(g)
            for do in range(w):
                g[do]-=1

        t+=1