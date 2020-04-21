import sys
sys.stdin = open('5650.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
Block=[0,[2,0,3,1],[2,3,1,0],[1,3,0,2],[3,2,0,1],[2,3,0,1]]
def Check(y,x,t):
    for i,j in W[t]:
        if (i,j)!=(y,x):return (i,j)
def BFS(y,x,d,c,tmp):
    while True:
        if (tmp and (i,j)==(y,x)) or A[y][x]==-1:return c
        if 0<A[y][x]<6:d,c=Block[A[y][x]][d],c+1
        y,x=y+dy[d],x+dx[d]
        if A[y][x]>5:y,x=Check(y,x,A[y][x]-6)
        tmp=1
for t in range(int(input())):
    N=int(input())+2
    A=[[5]*N]+[[5]+[int(x)for x in input().split()]+[5]for y in range(N-2)]+[[5]*N]
    R,S,W=0,[],[[],[],[],[],[]]
    for i in range(N):
        for j in range(N):
            if not A[i][j]:S.append((i,j))
            elif A[i][j]>5:W[A[i][j]-6].append((i,j))
    for i,j in S:
        for d in range(4):R=max(R,BFS(i,j,d,0,0))
    print('#%d %d'%(t+1,R))