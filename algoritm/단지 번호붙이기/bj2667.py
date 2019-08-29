import sys
sys.stdin = open('bj2667.txt','r')

dx=[0,1,0,-1]
dy=[-1,0,1,0]
def IS(y,x):
    if -1<x<N and -1<y<N and A[y][x]=='1':return True
    return False
def BFS(y,x):
    r=0
    Q=[[y,x]]
    while Q:
        tmp=Q.pop(0)
        r+=1
        hY=tmp[0]
        hX=tmp[1]
        A[hY][hX]='0'
        for dir in range(4):
            nY=hY+dy[dir]
            nX=hX+dx[dir]
            if IS(nY,nX) and not [nY,nX]in Q:Q.append([nY,nX])
    R.append(r)
N=int(input())
A=[list(input())for y in range(N)]
R=[]
for i in range(N):
    for j in range(N):
        if A[i][j]=='1':
            BFS(i,j)
print(len(R))
R.sort()
for r in R:print(r)