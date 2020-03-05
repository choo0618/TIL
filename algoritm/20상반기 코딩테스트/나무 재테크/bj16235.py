import sys
sys.stdin = open('bj16235.txt','r')

def New(i,j):
    for X,Y in (i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1):
        if -1<X<N and -1<Y<N:new[X][Y].append(1)
N,M,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
T=[[[]for _ in range(N)]for __ in range(N)]
for t in range(M):
    x,y,Y=map(int,input().split())
    T[x-1][y-1].append(Y)
M=[[5]*N for _ in range(N)]
while K:
    new=[[[]for _ in range(N)] for _ in range(N)]
    die=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not T[i][j]:continue
            T[i][j].sort()
            for y in T[i][j]:
                if y<=M[i][j]:
                    M[i][j]-=y
                    new[i][j].append(y+1)
                    if not (y+1)%5:New(i,j)
                else:die[i][j]+=y//2;continue
    for i in range(N):
        for j in range(N):
            M[i][j]+=(A[i][j]+die[i][j])
            T[i][j]=new[i][j]
    K-=1
print(sum(len(T[i][j])for i in range(N)for j in range(N)))