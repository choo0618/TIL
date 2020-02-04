import sys
sys.stdin = open('bj11378.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if B[i]==-1 or (not V[B[i]] and DFS(B[i])):
            A[x]=i
            B[i]=x
            return 1
    return 0
N,M,K=map(int,input().split())
Map=[[]]
for i in range(N):
    I=[int(x)for x in input().split()]
    Map.append(I[1:])
A=[-1]*(N+1)
B=[-1]*(M+1)
R=0
for i in range(1,N+1):
    V=[0]*(N+1)
    if DFS(i):R+=1
for i in range(1,N+1):
    while K:
        V=[0]*(N+1)
        if DFS(i):R+=1;K-=1
        else:break
print(A)
print(B)
print(R)