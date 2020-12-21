import sys
sys.stdin = open('bj20057.txt','r')

#        8
#     7  0  1
# 11  6     2  9
#     5  4  3
#        10
# 10,7,1,2,5
dx=[-1,0,1,0]
dy=[0,1,0,-1]
dj=[0,1,1,1,0,-1,-1,-1,0,2,0,-2]
di=[-1,-1,0,1,1,1,0,-1,-2,0,2,0]
D=[[7,5,0,4,1,3,8,10,11,6],[5,3,6,2,7,1,11,9,10,4],[1,3,0,4,7,5,8,10,9,2],[1,7,6,2,5,3,11,9,8,0]]
per=[0.1,0.1,0.07,0.07,0.01,0.01,0.02,0.02,0.05,0]
def IS(y,x):
    return -1<y<N and -1<x<N
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[[0]*N for _ in range(N)]
R=0
y,x,d=N//2,N//2,-1
V[y][x]=1
while y or x:
    if V[y+dy[(d+1)%4]][x+dx[(d+1)%4]]==0:d=(d+1)%4
    y+=dy[d];x+=dx[d]
    V[y][x]=1
    tmp=A[y][x]
    i=0
    while i!=9:
        ty,tx=y+di[D[d][i]],x+dj[D[d][i]]
        tmp1=int(A[y][x]*per[i])
        tmp-=tmp1
        if IS(ty,tx):A[ty][tx]+=tmp1
        else:R+=tmp1
        i+=1
    ty,tx=y+di[D[d][i]],x+dj[D[d][i]]
    if IS(ty,tx):A[ty][tx]+=tmp
    else:R+=tmp
    A[y][x]=0
print(R)



