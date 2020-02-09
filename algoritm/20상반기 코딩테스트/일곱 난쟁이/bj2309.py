import sys
sys.stdin=open('bj2309.txt','r')

def DFS(c,List):
    global R
    if c==7:
        if sum(List)==100:R=List
        return
    for i in range(9):
        if Map[i]:continue
        Map[i]=1
        List.append(L[i])
        DFS(c+1,List)
        if R:return
        Map[i]=0
        List.pop()
L=[int(input())for _ in range(9)]
L.sort()
Map=[0]*9
R=0
DFS(0,[])
for r in R:print(r)

import itertools
L=[int(input())for _ in range(9)]
L.sort()
for comb in itertools.combinations(L,7):
    if sum(comb)!=100:continue
    for p in comb:print(p)
    break