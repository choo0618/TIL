import sys
sys.stdin = open('bj17144.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
def S():
    Map=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j]<=0:continue
            t1,t2=A[i][j],A[i][j]//5
            for I,J in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                if IS(I,J) and (I,J)!=(Y,0) and (I,J)!=(Y+1,0):t1-=t2;Map[I][J]+=t2
            Map[i][j]+=t1
    return Map
def Move(y,x,D):
    i,j,d=y,x,0
    while 1:
        I,J=i+dy[D[d]],j+dx[D[d]]
        if (I,J)==(y,0):break
        if not IS(I,J) or ((i,j)==(y,C-1) and d!=3):d+=1;continue
        A[i][j]=A[I][J]
        i,j=I,J
    A[y][x+1]=A[y][x]=0
R,C,T=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(R)]
Y=0
for i in range(R):
    if A[i][0]==-1:Y=i;break
while T:
    A=S()
    # for a in A:print(*a)
    Move(Y,0,[3,0,1,2])
    Move(Y+1,0,[1,0,3,2])
    # print('------------')
    # for a in A:print(*a)
    # print()
    T-=1
cnt=0
for i in range(R):
    for j in range(C):cnt+=A[i][j]
print(cnt)