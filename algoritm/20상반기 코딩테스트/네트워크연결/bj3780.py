import sys
sys.stdin = open('bj3780.txt','r')

def find(x):
    if P[x]==x:return Dis[x]
    Dis[x]+=find(P[x])
    P[x]=P[P[x]]
    return Dis[x]
T=int(input())
for t in range(T):
    N=int(input())
    P=list(range(N+1))
    Dis=[0]*(N+1)
    while True:
        L=list(map(str,input().split()))
        if len(L)==1:break
        if L[0]=='E':print(find(int(L[1])))
        else:
            a,b=int(L[1]),int(L[2])
            Dis[a]=abs(a-b)%1000
            P[a]=b

