import sys
sys.stdin=open('3124.txt','r')

def MST():
    P=list(range(V+1))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R=0
    for c,a,b in Q:
        if find(a)!=find(b):R+=c;union(a,b)
    return R
for t in range(int(input())):
    V,E=map(int,input().split())
    Q=[]
    for i in range(E):
        a,b,c=map(int,input().split())
        Q.append((c,a,b))
    Q.sort()
    print('#%d %d'%(t+1,MST()))