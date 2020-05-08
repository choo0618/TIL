import sys
sys.stdin = open('bj1005.txt','r')

def DFS(x):
    D[x]-=1
    T[x]+=R[x]
    for i in A[x]:
        D[i]-=1
        R[i]=max(R[i],T[x])
        if not D[i]:DFS(i)
for t in range(int(input())):
    N,K=map(int,input().split())
    T=[0]+[int(x)for x in input().split()]
    A=[[]for _ in range(N+1)]
    D=[0]*(N+1)
    R=[0]*(N+1)
    for i in range(K):
        a,b=map(int,input().split())
        A[a].append(b)
        D[b]+=1
    for i in range(1,N+1):
        if not D[i]:DFS(i)
    print(T[int(input())])
