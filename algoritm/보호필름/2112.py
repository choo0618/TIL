import sys
sys.stdin = open('2112.txt','r')

import itertools,copy
def Check():
    c=1
    for x in range(L[1]):
        for y in range(0,L[0]-L[2]+1,1):
            s=sum(list(zip(*(M[y:y+L[2]+1])))[x])
            # for z in range(L[2]):
            #     ss+=M[y+z][x]
            if s==L[2] or not s:c=1;break
            else:c=0
        if not c:return False
    return True
def DFS(x,y):
    global R,r
    if r==1:return
    if x==y:
        if Check():r=1
        return
    for ab in range(1,3,1):
        M[i[x][0]]=i[x][ab]
        DFS(x+1,y)
        M[i[x][0]]=A[i[x][0]]
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[0])]
    c=[[int(x),[0]*L[1],[1]*L[1]]for x in range(L[0])]
    R,r=0,0
    M=copy.deepcopy(A)
    if not Check():
        while R<L[2]:
            C=list(itertools.combinations(c,R+1))
            R+=1
            for i in C:
                DFS(0,R)
            if r:break
    print('#%d %d'%(n+1,R))
