import sys
sys.stdin = open('bj17143.txt','r')

dy=[0,-1,1,0,0]
dx=[0,0,0,1,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]:return True
    return False
def Shark(y,x,s,d,w):
    M[y][x]=0
    tmp=s
    while tmp:
        y+=dy[d]
        x+=dx[d]
        if not IS(y,x):
            if d==1:d=2;y+=2
            elif d==2:d=1;y-=2
            elif d==3:d=4;x-=2
            else:d=3;x+=2
        tmp-=1
    if V[y][x]:
        if w>V[y][x][2]:V[y][x]=[s,d,w]
    else:
        V[y][x]=[s,d,w]
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[2])]
M=[[0]*L[1]for _ in range(L[0])]
for S in A:
    M[S[0]-1][S[1]-1]=[S[2],S[3],S[4]]
m=0
R=0
while m!=L[1]:
    for c in range(L[0]):
        if M[c][m]:
            R+=M[c][m][2]
            M[c][m]=0
            break
    V=[[0]*L[1]for _ in range(L[0])]
    for i in range(L[0]):
        for j in range(L[1]):
            if M[i][j]:Shark(i,j,M[i][j][0],M[i][j][1],M[i][j][2])
    M=V
    m+=1
print(R)