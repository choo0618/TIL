import sys
sys.stdin = open('bj16986.txt','r')

import itertools
def Play():
    A,B=0,1
    idx,Win=[0]*3,[0]*3
    while max(Win)!=K:
        if idx[0]==N:return 0
        a,b=P[A][idx[A]]-1,P[B][idx[B]]-1
        idx[A]+=1
        idx[B]+=1
        next=3-(A+B)
        if not Arr[a][b]:Win[B]+=1;A,B=B,next
        elif Arr[a][b]==1:
            w=max(A,B)
            Win[w]+=1
            A,B=w,next
        else:Win[A]+=1;A,B=A,next
    if Win[0]==K:return 1
    return 0
N,K=map(int,input().split())
Arr=[[int(x)for x in input().split()]for y in range(N)]
P=[0]+[[int(x)for x in input().split()]for y in range(2)]
R=0
for Per in itertools.permutations(range(1,N+1),N):
    P[0]=Per
    if Play():R=1;break
print(R)