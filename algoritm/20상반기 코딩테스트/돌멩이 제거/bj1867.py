import sys
sys.stdin = open('bj1867.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if b[i]==-1 or (not V[b[i]] and DFS(b[i])):
            a[x]=i
            b[i]=x
            return 1
    return 0
N,K=map(int,input().split())
Map=[[]for _ in range(N)]
for i in range(K):
    a,b=map(int,input().split())
    Map[a-1].append(b-1)
a=[-1]*N
b=[-1]*N
R=0
for i in range(N):
    V=[0]*N
    if DFS(i):R+=1
print(R)