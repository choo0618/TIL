import sys
sys.stdin = open('bj14499.txt','r')

dx=[0,1,-1,0,0]
dy=[0,0,0,-1,1]
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
C=[int(x)for x in input().split()]
d=[[0]*3for _ in range(4)]
R=[]
for c in C:
    if not (-1<L[2]+dy[c]<L[0] and -1<L[3]+dx[c]<L[1]): continue
    if c==1:
        d[1].insert(0, d[1].pop(-1))
        d[3][1],d[1][0]=d[1][0],d[3][1]
    elif c==2:
        d[1].append(d[1].pop(0))
        d[3][1],d[1][2]=d[1][2],d[3][1]
    elif c==3:
        n=d[0][1]
        for _ in range(3):d[_][1]=d[_+1][1]
        d[3][1]=n
    else:
        n=d[3][1]
        for _ in range(-1,-4,-1):d[_][1]=d[_-1][1]
        d[0][1]=n
    L[2]+=dy[c]
    L[3]+=dx[c]
    g=A[L[2]][L[3]]
    if not g:A[L[2]][L[3]]=d[3][1]
    else:d[3][1]=g;A[L[2]][L[3]]=0
    R.append(d[1][1])
for r in R:print(r)