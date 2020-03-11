import sys
sys.stdin = open('bj1197.txt','r')

def MST():
    P=list(range(V))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R=0
    for d in L:
        c,a,b=d
        if find(a)!=find(b):R+=c;union(a,b)
    return R
V,E=map(int,input().split())
L=[]
for i in range(E):
    a,b,c=map(int,input().split())
    L.append((c,a-1,b-1))
L.sort()
print(MST())