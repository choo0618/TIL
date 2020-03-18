import sys
sys.stdin = open('bj14503.txt','r')

dx=[0,1,0,-1]
dy=[-1,0,1,0]
N,M=map(int,input().split())
y,x,d=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
while A[y][x]!=1:
    if not A[y][x]:A[y][x]=-1;R+=1
    c=1
    for _ in range(4):
        d=(d+3)%4
        Y,X=y+dy[d],x+dx[d]
        if not A[Y][X]:y,x,c=Y,X,0;break
    if c:
        y-=dy[d]
        x-=dx[d]
print(R)

