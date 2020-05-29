import sys
sys.stdin = open('bj14889.txt','r')

import itertools
def Chk():
    a,b=0,0
    for i in range(N//2):
        for j in range(i+1,N//2):
            a+=M[A[i]][A[j]]+M[A[j]][A[i]]
            b+=M[B[i]][B[j]]+M[B[j]][B[i]]
    return abs(a-b)
N=int(input())
M=[[int(x)for x in input().split()]for y in range(N)]
R=10**9
for A in itertools.combinations(range(N),N//2):
    B=[int(x)for x in range(N)if not x in A]
    R=min(R,Chk())
print(R)
