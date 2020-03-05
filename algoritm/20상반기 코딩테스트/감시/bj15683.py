import sys
sys.stdin = open('bj15683.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
D=[[0],[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[0,3]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!=6
def Sight(y,x,d):
    l=[]
    while True:
        y+=dy[d];x+=dx[d]
        if not IS(y,x):break
        if not A[y][x]:A[y][x]='#';l.append((y,x))
    return l
def DFS(idx,r,c):
    global R
    if idx==c:
        R=min(R,r)
        return
    for i in C[idx][2]:
        s=[]
        for d in i:s+=Sight(C[idx][0],C[idx][1],d)
        DFS(idx+1,r-len(s),c)
        for i,j in s:A[i][j]=0
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
S,C,c=0,[],0
for i in range(N):
    for j in range(M):
        if not A[i][j]:S+=1
        elif A[i][j]!=6:C.append((i,j,D[A[i][j]]));c+=1
R=10**9
DFS(0,S,c)
print(R)