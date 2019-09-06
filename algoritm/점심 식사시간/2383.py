import sys
sys.stdin = open('2383.txt','r')

import itertools
T=int(input())
for n in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    S,P=[],[]
    for i in range(N):
        for j in range(N):
            if A[i][j]==1:P.append([i,j])
            elif A[i][j]:S.append([i,j,A[i][j]])
    Pc=len(P)
    Per=list(itertools.product([0,1],repeat=Pc))
    R=987654321
    for per in Per:
        G,D=[[],[]],[0]*Pc
        for d in range(Pc):
            D[d]=abs(P[d][0]-S[per[d]][0])+abs(P[d][1]-S[per[d]][1])
        t,m=1,0
        while m!=Pc:
            if t>R:t=999;break
            for d in range(Pc):
                D[d]-=1
                if not D[d]:G[per[d]].append(S[per[d]][2]+1)
            i=-1
            for g in G:
                i+=1
                if not g:continue
                w,z,l=3,0,len(g)
                if l<=3:w=l
                else:
                    for ww in range(3):
                        if g[ww]==1:
                            w+=1
                            if w==l:break
                        else:break
                for do in range(w):
                    g[do]-=1
                    if not g[do]:z+=1;m+=1
                G[i]=g[z:l+1]
            t+=1
        if t<R:R=t
    print('#%d %d'%(n+1,R))
