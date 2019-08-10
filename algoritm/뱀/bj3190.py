import sys
sys.stdin = open('bj3190.txt','r')

import copy
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if 0<x<N+1 and 0<y<N+1:return True
    return False
N=int(input())
K=int(input())
A=[[int(x)for x in input().split()]for y in range(K)]
S=int(input())
L=[[x for x in input().split()]for y in range(S)]
T=0
d,i,l=0,0,1
s=[[1,1]]
while T>=0:
    if i<len(L) and int(L[i][0])==T:
        if L[i][1]=='L':
            d-=1
            if d==-1:d=3
        else:
            d+=1
            if d==4:d=0
        i+=1
    T+=1
    t=copy.deepcopy(s[0:l])
    h=s.pop(0)
    h[0]+=dy[d]
    h[1]+=dx[d]
    if not IS(h[0],h[1])or h in s:break
    if h in A:
        A.pop(A.index(h))
        s=[h]+t
        l+=1
    else:
        s=[h]+t[0:l-1]
print(T)