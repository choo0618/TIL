import sys
sys.stdin=open('bj1182.txt','r')

def DFS(idx,c,r):
    global R
    if r==S and c:R+=1
    for i in range(idx,N):
        DFS(i+1,c+1,r+L[i])
N,S=map(int,input().split())
L=[int(x)for x in input().split()]
R=0
DFS(0,0,0)
print(R)

import itertools
N,S=map(int,input().split())
L=[int(x)for x in input().split()]
R=0
for c in range(N):
    for comb in itertools.combinations(L,c+1):
        if sum(comb)==S:R+=1
print(R)