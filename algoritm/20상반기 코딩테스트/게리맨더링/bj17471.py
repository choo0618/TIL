import sys
sys.stdin=open('bj17471.txt','r')

import itertools
def DFS(List,x,ab):
    V[x]=ab
    for i in Map[x]:
        if i in List and not V[i]:DFS(List,i,ab)
N=int(input())
L=[0]+[int(x)for x in input().split()]
Map=[[]]
for i in range(N):
    I=[int(x)for x in input().split()]
    Map.append(I[1:])
R=987654321
for c in range(1,N//2+1):
    for comb in list(itertools.combinations(range(1,N+1),c)):
        V=[0]*(N+1)
        A,B=0,0
        DFS(comb,comb[0],'a')
        combB=[j for j in range(1,N+1)if j not in comb]
        DFS(combB,combB[0],'b')
        if not all(V[1:]):continue
        for r in range(1,N+1):
            if V[r]=='a':A+=L[r]
            else:B+=L[r]
        R=min(R,abs(A-B))
print(R if R!=987654321 else -1)