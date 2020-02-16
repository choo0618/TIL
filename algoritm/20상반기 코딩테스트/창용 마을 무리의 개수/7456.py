import sys
sys.stdin = open('7456.txt','r')

def solution():
    P=list(range(N+1))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    r=N
    for i in range(M):
        a,b=map(int,input().split())
        if find(a)!=find(b):r-=1;union(a,b)
    return r
for t in range(int(input())):
    N,M=map(int,input().split())
    print('#%d %d'%(t+1,solution()))