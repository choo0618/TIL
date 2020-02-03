import sys
sys.stdin = open('bj2188.txt','r')

def DFS(x):
    V[x]=1
    for i in A[x]:
        if H[i]==-1 or (not V[H[i]] and DFS(H[i])):
            C[x]=i
            H[i]=x
            return 1
    return 0
N,M=map(int,input().split())
A=[[]]
for i in range(N):
    H=[int(x)for x in input().split()]
    A.append(H[1:])
C=[-1]*(N+1)
H=[-1]*(M+1)
R=0
for c in range(1,N+1):
    V=[0]*(N+1)
    if DFS(c):R+=1
print(R)
