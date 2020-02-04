import sys
sys.stdin = open('bj2191.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if B[i]==-1 or (not V[B[i]] and DFS(B[i])):
            A[x]=i
            B[i]=x
            return 1
    return 0
N,M,S,V=map(int,input().split())
n=[[float(x)for x in input().split()]for y in range(N)]
m=[[float(x)for x in input().split()]for y in range(M)]
Map=[[]for _ in range(N)]
for i in range(N):
    for j in range(M):
        dis=(abs(n[i][0]-m[j][0])**2+abs(n[i][1]-m[j][1])**2)**0.5
        T=dis/V
        if T<=S:Map[i].append(j)
A=[-1]*N
B=[-1]*M
R=N
for i in range(N):
    V=[0]*N
    if DFS(i):R-=1
print(R)