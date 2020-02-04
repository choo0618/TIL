import sys
sys.stdin = open('bj6497.txt','r')

import sys
sys.setrecursionlimit(1000000)
def MST():
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    r,k=0,0
    for d in A:
        if k==N-1:break
        a,b,c=d
        if find(a)!=find(b):r+=c;union(a,b);k+=1
    return r
while True:
    N,M=map(int,input().split())
    if not N+M:break
    A=[tuple(int(x)for x in input().split())for y in range(M)]
    Sum=sum(x[2]for x in A)
    A.sort(key=lambda x:x[2])
    print(Sum-MST())
