import sys
sys.stdin = open('bj17406.txt','r')

import itertools
def Turn(y,x,T):
    Y,X=y,x
    tmp=arr[y][x]
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        t=0
        while t!=T:
            nY=Y+d[0]
            nX=X+d[1]
            tmp1=arr[nY][nX]
            arr[nY][nX]=tmp
            tmp=tmp1
            Y,X=nY,nX
            t+=1
N,M,K=map(int,input().split())
Arr=[[int(x)for x in input().split()]for y in range(N)]
A=[tuple(int(x)for x in input().split())for y in range(K)]
R=987654321
for comb in list(itertools.permutations(A,K)):
    arr=[i[:] for i in Arr]
    for t in comb:
        r,c,s=t
        r-=1;c-=1
        tmp=0
        while tmp!=s:
            tmp+=1
            Turn(r-tmp,c-tmp,tmp*2)
    Min=min(sum(x)for x in arr)
    R=min(R,Min)
print(R)


