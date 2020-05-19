import sys
sys.stdin = open('bj14499.txt','r')

from collections import deque
dx=[0,1,-1,0,0]
dy=[0,0,0,-1,1]
def IS(y,x):
    return -1<y<N and -1<x<M
def Swap1(a):
    D[1][a],D[3][1]=D[3][1],D[1][a]
def Swap2(a,b):
    for n in [0,2]:D[a][n],D[b][n]=D[b][n],D[a][n]
N,M,y,x,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
D=deque([deque([0]*3) for _ in range(4)])
# D[0][1]=1
# D[1][0],D[1][1],D[1][2]=2,3,4
# D[2][1]=5
# D[3][1]=6
for t in map(int,input().split()):
    if not IS(y+dy[t],x+dx[t]):continue
    y,x=y+dy[t],x+dx[t]
    if t==1:Swap1(0);D[1].rotate(-1)
    elif t==2:Swap1(2);D[1].rotate()
    elif t==3:D.rotate();Swap2(2,1)
    else:D.rotate(-1);Swap2(0,1)
    if A[y][x]:D[1][1],A[y][x]=A[y][x],0
    else:A[y][x]=D[1][1]
    print(D[3][1])

# from collections import deque
# dx=[0,1,-1,0,0]
# dy=[0,0,0,-1,1]
# C=[0,-1,1,1,-1]
# def IS(y,x):
#     return -1<y<N and -1<x<M
# def Swap1(a,b):
#     if a==1:a=0
#     D[1][a],D[3][1]=D[3][1],D[1][a]
#     D[1].rotate(b)
# def Swap2(a,b):
#     if a==3:a=2
#     else:a=0
#     D.rotate(b)
#     for n in [0,2]:D[a][n],D[1][n]=D[1][n],D[a][n]
# N,M,y,x,K=map(int,input().split())
# A=[[int(x)for x in input().split()]for y in range(N)]
# D=deque([deque([0]*3) for _ in range(4)])
# for t in map(int,input().split()):
#     if not IS(y+dy[t],x+dx[t]):continue
#     y,x=y+dy[t],x+dx[t]
#     if t==1 or t==2:Swap1(t,C[t])
#     else:Swap2(t,C[t])
#     if A[y][x]:D[1][1],A[y][x]=A[y][x],0
#     else:A[y][x]=D[1][1]
#     print(D[3][1])