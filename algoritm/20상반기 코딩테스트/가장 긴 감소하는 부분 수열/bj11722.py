import sys
sys.stdin = open('bj11722.txt','r')

def DFS(li,idx,r):
    global R
    R=max(R,r)
    for i in range(idx,N):
        if L[i]>=li:continue
        DFS(L[i],i+1,r+1)
N=int(input())
L=[int(x)for x in input().split()]
R=0
DFS(1001,0,0)
print(R)

N=int(input())
L=[int(x)for x in input().split()]
DP=[1]*N
for i in range(N):
    for j in range(i):
        if L[i]<L[j] and DP[i]<DP[j]+1:DP[i]=DP[j]+1
print(max(DP))
