import sys
sys.stdin = open('bj13460.txt','r')

import copy
dx=[0,1,0,-1]
dy=[-1,0,1,0]
def P(D,i):
    if i==9:
        Per.append(copy.deepcopy(p))
        return
    for d in range(4):
        if d==D or abs(D-d)==2:continue
        p.append(d)
        P(d,i+1)
        p.pop()
L=[int(x)for x in input().split()]
A=[input()for y in range(L[0])]
R=-1
for y in range(L[0]):
    for x in range(L[1]):
        if A[y][x]=='R':r=[y,x,'R']
        elif A[y][x]=='B':b=[y,x,'B']
        elif A[y][x]=='O':H=[y,x,'H']
Per=[]
for dir in range(4):
    g=A[r[0]+dy[dir]][r[1]+dx[dir]]
    if g!='#':
        p=[dir]
        P(dir,0)
print(Per)
for C in Per:
    M=copy.deepcopy(A)
    for c in C:
        if c==0:
            if r[0]<b[0]:Q=[r,b]
            else:Q=[b,r]
        elif c==1:
            if r[1]<b[1]:Q=[b,r]
            else:Q=[r,b]
        elif c==2:
            if r[0]>b[0]:Q=[r,b]
            else:Q=[b,r]
        else:
            if r[1]<b[1]:Q=[r,b]
            else:Q=[b,r]
        while Q:
            tmp=Q.pop(0)
            hY=tmp[0]
            hX=tmp[1]
            nY=hY+dy[c]
            nX=hX+dx[c]
            color=tmp[2]
            if M[nY][nX]=='.':
                M[nY].replace('.',tmp[2],nX)
                M[hY][hX]='.'
                Q.append([nY,nX,color])

