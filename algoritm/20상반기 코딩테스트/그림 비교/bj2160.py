import sys
sys.stdin = open('bj2160.txt','r')

def check(y,x):
    r=0
    for i in range(5):
        for j in range(7):
            if A[y][i][j]==A[x][i][j]:r+=1
    return r
N = int(input())
A = [[list(map(str,input()))for m in range(5)]for _ in range(N)]
Map = [[0]*N for _ in range(N)]
R,P = 0,0
for y in range(N):
    for x in range(N):
        if x>y:
            r=check(y,x)
            if r>R:
                R=r
                P=[y+1,x+1]
for p in P:print(p,end=' ')
