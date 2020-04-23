import sys
sys.stdin = open('2383.txt','r')

import itertools
def RS(P,AB):
    r=0
    while r<=R and P:
        for i in range(2):
            Len,p=min(3,len(ab[i])),0
            for l in range(len(ab[i])):
                if ab[i][l]>AB[i]:ab[i][l]-=1
                elif ab[i][l]<=AB[i] and l<Len:
                    ab[i][l]-=1
                    if not ab[i][l]:p+=1;P-=1
            ab[i]=ab[i][p:]
        r+=1
    return r
for t in range(int(input())):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    P,p,S,Sl,R=[],0,[],[],10**9
    for i in range(N):
        for j in range(N):
            if A[i][j]==1:P.append((i,j));p+=1
            elif A[i][j]:S.append((i,j)),Sl.append(A[i][j])
    for Per in itertools.product([0,1],repeat=len(P)):
        ab=[[],[]]
        for i,n in enumerate(Per):ab[n].append(abs(P[i][0]-S[n][0])+abs(P[i][1]-S[n][1])+Sl[n]+1)
        for _ in range(2):ab[_].sort()
        R=min(RS(p,Sl),R)
    print('#%d %d'%(t+1,R))



