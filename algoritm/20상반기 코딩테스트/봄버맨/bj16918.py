import sys
sys.stdin = open('bj16918.txt','r')

def Drop():
    l=[]
    for i in range(R):
        for j in range(C):
            if not A[i][j]:A[i][j]=3;continue
            A[i][j]-=1
            if not A[i][j]:l.append((i,j))
    return l
R,C,N=map(int,input().split())
A=[list(input())for _ in range(R)]
for i in range(R):
    for j in range(C):
        if A[i][j]=='.':A[i][j]=0
        else:A[i][j]=2
for _ in range(N-1):
    B=Drop()
    for i,j in B:
        for y,x in (i+1,j),(i,j+1),(i-1,j),(i,j-1):
            if -1<y<R and -1<x<C:A[y][x]=0
for i in A:
    for p in i:print('O'if p else '.',end='')
    print()


