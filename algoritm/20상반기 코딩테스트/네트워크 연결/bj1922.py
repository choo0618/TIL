import sys
sys.stdin = open('bj1922.txt','r')

def MST(A):
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(b)]=find(a)
    R=0
    for d in A:
        c,a,b=d
        if find(a)!=find(b):R+=c;union(a,b)
    return R
N=int(input())
M=int(input())
A=[]
for i in range(M):
    a,b,c=map(int,input().split())
    A.append((c,a-1,b-1))
A.sort()
print(MST(A))
