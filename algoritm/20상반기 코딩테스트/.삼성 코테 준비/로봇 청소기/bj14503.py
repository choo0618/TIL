import sys
sys.stdin = open('bj17503.txt','r')

dx=[0,1,0,-1]
dy=[-1,0,1,0]
dd=[3,0,1,2]
N,M=map(int,input().split())
y,x,d=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
while A[y][x]!=1:
    if A[y][x]==0:A[y][x]=2;R+=1
    D=dd[d]
    while A[y+dy[D]][x+dx[D]]!=0 and D!=d:D=dd[D]
    if A[y+dy[D]][x+dx[D]]==0:y,x,d=y+dy[D],x+dx[D],D
    else:y-=dy[d];x-=dx[d]
print(R)