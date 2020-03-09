import sys
sys.stdin = open('bj3109.txt','r')

def IS(y,x):
    return -1<y<R and -1<x<C
def DFS(y,x):
    global r,c
    V[y][x]=1
    if x==C-1:
        r+=1
        c=1
        return
    for Y,X in (y-1,x+1),(y,x+1),(y+1,x+1):
        if IS(Y,X) and not V[Y][X] and A[Y][X]!='x':
            DFS(Y,X)
            if c:return
R,C=map(int,input().split())
A=[input()for _ in range(R)]
V=[[0]*C for _ in range(R)]
r=0
for i in range(R):
    c=0
    DFS(i,0)
print(r)