import sys
sys.stdin = open('bj14889.txt','r')

import itertools
def Chk(l,Len):
    r=0
    for i in range(Len):
        for j in range(i+1,Len):
            r+=M[l[i]][l[j]]+M[l[j]][l[i]]
    return r
N=int(input())
M=[[int(x)for x in input().split()]for y in range(N)]
R=10**9
for i in range(1,N//2+1):
    for A in itertools.combinations(range(N),i):
        B=[int(x)for x in range(N)if not x in A]
        R=min(R,abs(Chk(A,i)-Chk(B,N-i)))
print(R)
