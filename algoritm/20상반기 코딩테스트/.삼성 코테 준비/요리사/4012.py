import sys
sys.stdin = open('4012.txt','r')

import itertools
def Score(L):
    r=0
    for i in range(N//2):
        for j in range(i+1,N//2):
            r+=S[L[i]][L[j]]+S[L[j]][L[i]]
    return r
for t in range(int(input())):
    N=int(input())
    S=[[int(x)for x in input().split()]for y in range(N)]
    R=10**9
    for A in itertools.combinations(range(N),N//2):
        B=[int(x)for x in range(N)if not x in A]
        a,b=Score(A),Score(B)
        R=min(R,abs(a-b))
    print('#%d %d'%(t+1,R))

