import sys
sys.stdin = open('bj12865.txt','r')

# DFS 시간초과
def DFS(idx,k,r):
    global R
    if k>K:return
    if r>R:R=r
    for i in range(idx,N):DFS(idx+1,k+A[i][0],r+A[i][1])
N,K=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
DFS(0,0,0)
print(R)

# DP
N,K=map(int,input().split())
A=[[0]]+[[int(x)for x in input().split()]for y in range(N)]
DP=[0]*(K+1)
for i in range(1,N+1):
    for j in range(K,0,-1):
        if A[i][0]<=j:DP[j]=max(DP[j],DP[j-A[i][0]]+A[i][1])
        else:break
print(DP[K])