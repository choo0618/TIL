import sys
sys.stdin=open('bj1920.txt','r')

import bisect
N=int(input())
A=[int(x)for x in input().split()]
A.sort()
M=int(input())
for f in map(int,input().split()):print(1 if bisect.bisect_left(A,f)!=bisect.bisect_right(A,f) else 0)