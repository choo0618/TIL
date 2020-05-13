import sys
sys.stdin = open('bj2463.txt','r')

def MST(t):
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[a]=b
    r,cnt=0,0
    L=[1]*N
    for w,a,b in A:
        tA,tB=find(a),find(b)
        if tA!=tB:
            r+=t*L[tB]*L[tA]
            r%=10**9
            union(tA,tB)
            L[tB]+=L[tA]
            cnt+=1
        t-=w
        if cnt==N-1:return r
    return r
N,M=map(int,input().split())
D=[[]for _ in range(N+1)]
T,A=0,[]
for i in range(M):
    x,y,w=map(int,input().split())
    if x>y:x,y=y,x
    A.append((w,x-1,y-1))
    T+=w
A.sort(reverse=1)
print(MST(T)%(10**9))
