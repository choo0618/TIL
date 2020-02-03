import sys
sys.stdin = open('bj11375.txt','r')

def DFS(x):
    v[x]=1
    for a in Map[x]:
        if m[a]==-1 or (not v[m[a]] and DFS(m[a])):
            n[x]=a
            m[a]=x
            return 1
    return 0
N,M=map(int,input().split())
Map=[[]]
for i in range(N):
    I=[int(x)for x in input().split()]
    Map.append(I[1:])
n=[-1]*(N+1)
m=[-1]*(M+1)
R=0
for w in range(N):
    v=[0]*(N+1)
    if DFS(w+1):R+=1
print(R)