import sys
sys.stdin = open('bj12015.txt','r')

import bisect
N=int(input())
L=[int(x)for x in input().split()]
DP=[]
for i in L:
    n=bisect.bisect_left(DP,i)
    if len(DP)<=n:DP.append(i)
    else:DP[n]=i
print(len(DP))