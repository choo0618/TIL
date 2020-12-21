import sys
sys.stdin = open('bj17406.txt','r')

from itertools import permutations
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def Rotate(y,x,s):
    Y,X=y-s,x-s
    tmp=Map[Y][X]
    for dy,dx in (1,0),(0,1),(-1,0),(0,-1):
        for x in range(2*s):
            Map[Y][X]=Map[Y+dy][X+dx]
            Y+=dy;X+=dx
    Map[Y][X+1]=tmp
N,M,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
P=[[int(x)for x in input().split()]for y in range(K)]
R=10**9
for p in permutations(P,K):
    Map=[a[:]for a in A]
    for r,c,s in p:
        for i in range(1,s+1):Rotate(r-1,c-1,i)
    for m in Map:R=min(R,sum(m))
print(R)