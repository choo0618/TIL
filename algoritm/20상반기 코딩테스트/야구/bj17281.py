import sys
sys.stdin = open('bj17281.txt','r')

import itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for per in itertools.permutations(range(1,9),8):
    l=list(per[:3])+[0]+list(per[3:])
    n,r=0,0
    for i in range(N):
        o,b1,b2,b3=0,0,0,0
        while o!=3:
            t=A[i][l[n]]
            if not t:o+=1
            elif t==1:r+=b3;b1,b2,b3=1,b1,b2
            elif t==2:r+=(b2+b3);b1,b2,b3=0,1,b1
            elif t==3:r+=(b1+b2+b3);b1,b2,b3=0,0,1
            else:r+=(b1+b2+b3+1);b1,b2,b3=0,0,0
            n=(n+1)%9
    R=max(R,r)
print(R)