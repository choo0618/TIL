import sys
sys.stdin = open('bj17406.txt','r')

import itertools
def Rotate(y,x,s):
    Y,X=y-s,x-s
    tmp=M[Y][X]
    for dy,dx in (1,0),(0,1),(-1,0),(0,-1):
        while y-s<=Y+dy<=y+s and x-s<=X+dx<=x+s:
            M[Y][X]=M[Y+dy][X+dx]
            Y+=dy;X+=dx
    M[Y][X+1]=tmp
N,M,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
L=[[int(x)for x in input().split()]for y in range(K)]
R=10**9
for per in itertools.permutations(L,K):
    M=[a[:]for a in A]
    for r,c,s in per:
        for i in range(1,s+1):Rotate(r-1,c-1,i)
    R=min(R,min(sum(x)for x in M))
print(R)
