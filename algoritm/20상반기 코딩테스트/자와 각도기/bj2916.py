import sys
sys.stdin = open('bj2916.txt','r')

def DFS(idx,s):
    if idx==N or DP[idx][s]:return
    DP[idx][s]=1
    R[s]='YES'
    DFS(idx,(360+s+L[idx])%360)
    DFS(idx,(360+s-L[idx])%360)
    DFS(idx+1,s)
N,K=map(int,input().split())
L=[int(x)for x in input().split()]
DP=[[0]*361 for _ in range(N)]
R=['NO']*361
L.sort()
DFS(0,0)
for p in map(int,input().split()):print(R[p])