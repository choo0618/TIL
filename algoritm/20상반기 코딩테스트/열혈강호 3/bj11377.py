import sys
sys.stdin = open('bj11377.txt','r')

def DFS(x):
    V[x]=1
    for i in W[x]:
        if w[i]==-1 or (not V[w[i]] and DFS(w[i])):
            h[x]=i
            w[i]=x
            return 1
    return 0
N,M,K=map(int,input().split())
W=[[]]
C=[]
for i in range(N):
    I=[int(x)for x in input().split()]
    W.append(I[1:])
h=[-1]*(N+1)
w=[-1]*(M+1)
R,k=0,0
for i in range(1,N+1):
    V=[0]*(N+1)
    if DFS(i):R+=1
for i in range(1,N+1):
    V=[0]*(N+1)
    if k<K and DFS(i):R+=1;k+=1
print(R)
