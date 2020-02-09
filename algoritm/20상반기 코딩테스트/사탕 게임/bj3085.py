import sys
sys.stdin=open('bj3085.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def check(y,x,s):
    R=[0]*4
    for d in range(4):
        r=0
        Y,X=y+dy[d],x+dx[d]
        while IS(Y,X) and A[Y][X]==s:
            r+=1
            Y,X=Y+dy[d],X+dx[d]
        R[d]=r
    if R==4:print(y,x)
    return max(R[0]+R[2],R[1]+R[3])
N=int(input())
A=[list(map(str,input()))for _ in range(N)]
R=1
for i in range(N):
    for j in range(N):
        for d in range(4):
            y,x=i+dy[d],j+dx[d]
            if IS(y,x):
                A[i][j],A[y][x]=A[y][x],A[i][j]
                R=max(R,check(i,j,A[i][j]))
                A[i][j],A[y][x]=A[y][x],A[i][j]
print(R+1)