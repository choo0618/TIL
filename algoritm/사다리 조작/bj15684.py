import sys
sys.stdin = open('bj15684.txt','r')

import itertools
def LD():
    c=[[0,0]for _ in range(2*L[0])]
    for x in range(1,2*L[0],2):
        y,d=1,x
        while y!=L[2]+1:
            if M[y][d-1]:
                while M[y][d-1]:d-=1
                c[x][0]+=1
            elif M[y][d+1]:
                while M[y][d+1]:d+=1
                c[x][1]+=1
            y+=1
        if c[x][0]!=c[x][1]:return False
    return True
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[1])]
M=[[0,1]*L[0]+[0]for _ in range(L[2]+2)]
for g in A:
    M[g[0]][2*g[1]]=1
p=[]
for y in range(1,L[2]+1,1):
    for x in range(2,2*L[0]-1,2):
        if not M[y][x] and not M[y][x-2] and not M[y][x+2]:
            p.append([y,x])
R,CC=0,0
while R!=4:
    C=list(itertools.combinations(p,R))
    if not R and LD():break
    elif R==1:
        for c in C:
            M[c[0][0]][c[0][1]]=1
            if LD():CC=1;break
            M[c[0][0]][c[0][1]]=0
    else:
        for c in C:
            t=0
            for cc in range(R-1):
                if c[cc][0]==c[cc+1][0] and c[cc+1][1]-c[cc][1]==2:t=1;break
            if t:continue
            for l in c:M[l[0]][l[1]]=1
            if LD():CC=1;break
            for l in c:M[l[0]][l[1]]=0
    if CC:break
    R+=1
if R==4:print(-1)
else:print(R)