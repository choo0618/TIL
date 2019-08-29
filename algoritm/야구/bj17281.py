import sys
sys.stdin = open('bj17281.txt','r')

import itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Per=list(itertools.permutations([1,2,3,4,5,6,7,8],8))
R=0
for per in Per:
    per=list(per)
    per.insert(3,0)
    n,r=0,0
    for i in range(N):
        o,g=0,[1,0,0,0]
        while o!=3:
            t=A[i][per[n]]
            if not t:o+=1
            elif t==1:r+=g.pop();g.insert(0,1)
            elif t==2:r+=sum(g[2:4]);g=[1,0]+g[0:2]
            elif t==3:r+=sum(g[1:4]);g=[1,0,0,1]
            else:r+=sum(g);g=[1,0,0,0]
            n+=1
            if n==9:n=0
    if r>R:R=r
print(R)

