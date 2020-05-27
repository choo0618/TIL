import sys
sys.stdin = open('bj17471.txt','r')

import itertools
def DFS(l,x,ab):
    V[x]=ab
    for n in Map[x]:
        if n in l and V[n]==0:DFS(l,n,ab)
N=int(input())
L=[0]+[int(x)for x in input().split()]
R,Map=10**9,[[]]
for i in range(N):
    n,*l=map(int,input().split())
    Map.append(l)
for c in range(1,N//2+1):
    for Comb in itertools.combinations(range(1,N+1),c):
        V=[0]*(N+1)
        DFS(Comb,Comb[0],'a')
        b=[int(x)for x in range(1,N+1)if not x in Comb]
        DFS(b,b[0],'b')
        if not all(V[1:]):continue
        A,B=0,0
        for i in range(1,N+1):
            if V[i]=='a':A+=L[i]
            else:B+=L[i]
        R=min(R,abs(A-B))
print(R if R!=10**9 else -1)
