import sys
sys.stdin = open('bj14620.txt','r')

def Check(y,x):
    for Y,X in (y,x),(y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if V[Y][X]:return 1
    return 0
def DFS(idx,c,r):
    global R
    if r>=R:return
    if c==3:
        R=min(R,r)
        return
    for i in range(idx,(N-2)**2):
        y,x=S[i]
        rr=0
        if Check(y,x):continue
        for Y,X in (y,x),(y,x+1),(y+1,x),(y,x-1),(y-1,x):V[Y][X]=1;rr+=A[Y][X]
        DFS(idx+1,c+1,r+rr)
        for Y,X in (y,x),(y,x+1),(y+1,x),(y,x-1),(y-1,x):V[Y][X]=0
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[[0]*N for _ in range(N)]
S=[]
R=10**9
for i in range(1,N-1):
    for j in range(1,N-1):
        S.append((i,j))
DFS(0,0,0)
print(R)