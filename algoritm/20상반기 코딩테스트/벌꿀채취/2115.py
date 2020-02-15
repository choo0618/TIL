import sys
sys.stdin = open('2115.txt','r')

def DFS(y,x,r,R):
    if r>C:return
    Map[y][j]=max(R,Map[y][j])
    for i in range(x,x+M):
        if V[i-x]:continue
        V[i-x]=1
        DFS(y,x,r+A[y][i],R+A[y][i]**2)
        V[i-x]=0
for t in range(int(input())):
    N,M,C=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    Map=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            V=[0]*C
            DFS(i,j,0,0)
    Max,R=[max(x) for x in Map],0
    for i in range(N):
        rMax=max(Max[r]for r in range(N) if r!=i)
        for j in range(N-M+1):
            c=Map[i][j+M:]
            cMax=max(c) if c else 0
            R=max(R,Map[i][j]+max(rMax,cMax))
    print('#%d %d'%(t+1,R))

