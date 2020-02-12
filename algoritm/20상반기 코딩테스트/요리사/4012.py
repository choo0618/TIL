import sys
sys.stdin = open('4012.txt','r')

import itertools
def Sum(List):
    r=0
    for l1 in List:
        for l2 in List:
            r+=A[l1][l2]
    return r
for t in range(int(input())):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R=10**9
    for a in itertools.combinations(range(N),N//2):
        Sa=Sum(a)
        Sb=Sum(tuple(int(x)for x in range(N) if not x in a))
        R=min(R,abs(Sa-Sb))
    print('#%d %d'%(t+1,R))