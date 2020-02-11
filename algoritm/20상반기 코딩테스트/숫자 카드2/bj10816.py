import sys
sys.stdin = open('bj10816.txt','r')

import bisect
N=int(input())
A=[int(x)for x in input().split()]
A.sort()
M=int(input())
B=[int(x)for x in input().split()]
for b in B:
    print(bisect.bisect_right(A,b)-bisect.bisect_left(A,b),end=' ')

