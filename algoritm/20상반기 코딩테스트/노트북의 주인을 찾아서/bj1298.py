import sys
sys.stdin = open('bj1298.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if n[i]==-1 or (not V[n[i]] and DFS(n[i])):
            h[x]=i
            n[i]=x
            return 1
    return 0
N,M=map(int,input().split())
Map=[[]for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    Map[x].append(y)
h=[-1]*(N+1)
n=[-1]*(N+1)
R=0
for i in range(1,N+1):
    V=[0]*(N+1)
    if DFS(i):R+=1
print(R)