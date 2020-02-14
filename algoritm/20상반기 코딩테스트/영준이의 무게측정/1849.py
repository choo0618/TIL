import sys
sys.stdin = open('1849.txt','r')

def find(x):
    if P[x]!=x:
        Px=P[x]
        P[x]=find(Px)
        W[x]+=W[Px]
    return P[x]
def union(a,b,w):
    pa=find(a)
    pb=find(b)
    if pa==pb:return
    wt=W[b]-W[a]
    if D[pa]>D[pb]:
        pa,pb=pb,pa
        w=-w
        wt=-wt
    W[pa]=w+wt
    P[pa]=pb
    if D[pa]==D[pb]:D[pb]+=1
for t in range(int(input())):
    print('#%d'%(t+1),end=' ')
    N,M=map(int,input().split())
    P=list(range(N+1))
    D=[0]*(N+1)
    W=[0]*(N+1)
    R=[]
    for p in range(M):
        L=input()
        if L[0]=='!':
            a,b,w=map(int,L[1:].split())
            union(a,b,w)
        else:
            a,b=map(int,L[1:].split())
            if find(a)==find(b):R.append(W[a]-W[b])
            else:R.append('UNKNOWN')
    print(' '.join(map(str,R)))
    print(D)