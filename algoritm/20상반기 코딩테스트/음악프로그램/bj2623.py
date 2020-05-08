import sys
sys.stdin = open('bj2623.txt','r')

def DFS(x):
    D[x]-=1
    if D[x]==-1:R.append(x)
    for i in A[x]:
        D[i]-=1
        if not D[i]:DFS(i)
N,M=map(int,input().split())
A=[[]for _ in range(N+1)]
D=[0]*(N+1)
R=[]
for i in range(M):
    n,*l=map(int,input().split())
    for j in range(1,n):
        A[l[j-1]].append(l[j])
        D[l[j]]+=1
for i in range(1,N+1):
    if not D[i]:DFS(i)
print('\n'.join(map(str,R))if len(R)==N else 0)