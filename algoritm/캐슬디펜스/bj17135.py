import sys
sys.stdin = open('bj17135.txt','r')

import itertools, copy
dy=[0,-1,0]
dx=[-1,0,1]
def IS(y,x):
    if -1<x<L[1] and -1<y<L[0]:return True
    return False
def BFS(y,x,c):
    global Q
    Q.append([y,x,c])
    while Q:
        tmp=Q.pop(0)
        hY=tmp[0]
        hX=tmp[1]
        hC=tmp[2]
        if M[hY][hX]:
            M[hY][hX]=9
            break
        for dir in range(3):
            nY=hY+dy[dir]
            nX=hX+dx[dir]
            if hC and IS(nY,nX):
                Q.append([nY,nX,hC-1])
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
c=[]
for _ in range(L[1]):
    c.append(_)
comb=list(itertools.combinations(c,3))
R=0
for C in range(len(comb)):
    M=copy.deepcopy(A)
    cnt=0
    while len(M):
        for b in comb[C]:
            Q=[]
            BFS(len(M)-1,b,L[2]-1)
        for j in range(len(M)):
            for i in range(len(M[0])):
                if M[j][i]==9:cnt+=1;M[j][i]=0
        M.pop(-1)
    if cnt>R:R=cnt
print(R)