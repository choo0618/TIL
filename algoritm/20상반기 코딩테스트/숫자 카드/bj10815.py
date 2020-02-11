import sys
sys.stdin = open('bj10815.txt','r')

import bisect
N=int(input())
A=[int(x)for x in input().split()]
A.sort()
M=int(input())
B=[int(x)for x in input().split()]
for b in B:
    print(1 if bisect.bisect_left(A,b)!=bisect.bisect_right(A,b) else 0, end=' ')

