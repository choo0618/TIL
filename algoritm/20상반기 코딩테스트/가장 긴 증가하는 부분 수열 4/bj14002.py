import sys
sys.stdin = open('bj14002.txt','r')

def DFS(x,List):
    if x==-1:
        print(*List[::-1])
        return
    List.append(L[x])
    DFS(Map[x],List)
N=int(input())
L=[int(x)for x in input().split()]
DP=[0]*N
Map=[0]*N
for i in range(N):
    DP[i]=1
    Map[i]=-1
    for j in range(i):
        if L[i]>L[j] and DP[j]+1>DP[i]:
            DP[i]=DP[j]+1
            Map[i]=j
R=max(DP)
print(R)
for i in range(N-1,-1,-1):
    if DP[i]==R:DFS(Map[i],[L[i]]);break
