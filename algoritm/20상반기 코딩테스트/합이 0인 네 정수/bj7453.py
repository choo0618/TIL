import sys
sys.stdin=open('bj7453.txt','r')

import bisect
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
ab=[]
cd=[]
for i in range(N):
    for j in range(N):
        ab.append(A[i][0]+A[j][1])
        cd.append(A[i][2]+A[j][3])
ab.sort()
cd.sort()
R=0
for n in ab:R+=bisect.bisect_right(cd,-n)-bisect.bisect_left(cd,-n)
print(R)


from collections import Counter
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
ab=[]
cd=[]
for i in range(N):
    for j in range(N):
        ab.append(A[i][0]+A[j][1])
        cd.append(A[i][2]+A[j][3])
cd=Counter(cd)
R=0
for n in ab:R+=cd[-n]
print(R)