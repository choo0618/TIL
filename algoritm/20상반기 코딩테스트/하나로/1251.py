import sys
sys.stdin = open('1251.txt','r')

def MST():
    P=list(range(N+1))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R=0
    for l,a,b in L:
        if find(a)!=find(b):R+=l;union(a,b)
    return R
for t in range(int(input())):
    N=int(input())
    X=[int(x)for x in input().split()]
    Y=[int(x)for x in input().split()]
    E=float(input())
    L=[]
    for i in range(N):
        for j in range(i+1,N):
            L.append(((abs(X[i]-X[j])**2+abs(Y[i]-Y[j])**2)*E,i,j))
    L.sort()
    print('#%d %d'%(t+1,round(MST())))