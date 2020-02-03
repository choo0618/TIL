import sys
sys.stdin = open('bj11376.txt','r')

def DFS(x):
    V[x]=1
    for i in W[x]:
        if w[i]==-1 or (not V[w[i]] and DFS(w[i])):
            h[x]=i
            w[i]=x
            return 1
    return 0
N,M=map(int,input().split())
W=[[]]
for i in range(N):
    w=[int(x)for x in input().split()]
    W.append(w[1:])
h=[-1]*(N+1)
w=[-1]*(M+1)
R=0
for i in range(1,N+1):
    for t in range(2):
        V=[0]*(N+1)
        if DFS(i):R+=1
print(R)