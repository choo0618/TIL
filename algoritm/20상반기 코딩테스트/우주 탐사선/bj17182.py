import sys
sys.stdin = open('bj17182.txt')

def DFS(now,r):
    global R
    if r>=R:return
    if all(V):
        R=min(R,r)
        return
    for i in range(N):
        if i==now or V[i]:continue
        V[i]=1
        DFS(i,r+A[now][i])
        V[i]=0
N,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[[0]*N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j or k==j:continue
            A[i][j]=min(A[i][j],A[i][k]+A[k][j])
R=10**9
V=[0]*N
V[K]=1
DFS(K,0)
print(R)


