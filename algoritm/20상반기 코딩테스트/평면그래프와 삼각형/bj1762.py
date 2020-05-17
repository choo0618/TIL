import sys
sys.stdin = open('bj1762.txt','r')

import bisect
N,M=map(int,input().split())
Map=[[]for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    if a>b:a,b=b,a
    Map[a].append(b)
for i in range(N+1):Map[i].sort()
R=0
for i in range(1,N+1):
    for j in Map[i]:
        v1,v2=i,j
        if len(Map[i])>len(Map[j]):v1,v2=v2,v1
        for k in Map[v1]:
            R+=bisect.bisect_right(Map[v2],k)-bisect.bisect_left(Map[v2],k)
print(R)
