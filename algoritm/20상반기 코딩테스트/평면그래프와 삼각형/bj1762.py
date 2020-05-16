import sys
sys.stdin = open('bj1762.txt','r')

# def DFS(c,x):
    # global R
    # if c==3:
    #     if i==x:R+=1
    #     return
    # for n in Map[x]:
    #     if V[n]:continue
    #     V[n]=1
    #     DFS(c+1,n)
    #     V[n]=0
def Solution(x):
    r=0
    for i in range(C[x]):
        for j in range(i+1,C[x]):
            if Map[x][j] in Map[Map[x][i]]:r+=1
    return r
N,M=map(int,input().split())
Map=[[]for _ in range(N+1)]
C=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    Map[a].append(b)
    Map[b].append(a)
    C[a]+=1;C[b]+=1
R=0
V=[0]*(N+1)
for i in range(1,N+1):
    if C[i]>=2:
        R+=Solution(i)
print(R//3)