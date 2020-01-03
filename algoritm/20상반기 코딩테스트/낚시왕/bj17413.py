import sys
sys.stdin = open('bj17413.txt','r')

dy=[0,-1,1,0,0]
dx=[0,0,0,1,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
def move(y,x,s,d,z):
    nY,nX=y,x
    tmp=s
    while tmp:
        nY+=dy[d]
        nX+=dx[d]
        if not IS(nY,nX):
            if d%2:d+=1
            else:d-=1
            nY+=2*dy[d]
            nX+=2*dx[d]
        tmp-=1
    if (V[nY][nX] and z>V[nY][nX][2]) or not V[nY][nX]:V[nY][nX]=[s,d,z]

R,C,M = map(int,input().split())
Shark = [[int(x)for x in input().split()]for y in range(M)]
Map=[[0]*C for _ in range(R)]
r=0
for s in Shark:Map[s[0]-1][s[1]-1] = s[2:]
m=0
while m!=C:
    for catch in range(R):
        if Map[catch][m]:
            r+=Map[catch][m][2]
            Map[catch][m]=0
            break
    V=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if Map[i][j]:move(i,j,Map[i][j][0],Map[i][j][1],Map[i][j][2])
    Map=V
    m+=1
print(r)