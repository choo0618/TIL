import sys
sys.stdin = open('bj9576.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if b[i]==-1 or (not V[b[i]] and DFS(b[i])):
            m[x]=i
            b[i]=x
            return 1
    return 0
for t in range(int(input())):
    N,M=map(int,input().split())
    Map=[[]]
    for i in range(M):
        a,b=map(int,input().split())
        Map.append(list(range(a,b+1)))
    m=[-1]*(M+1)
    b=[-1]*(N+1)
    R=0
    for i in range(1,M+1):
        V=[0]*(M+1)
        if DFS(i):R+=1
    print(R)
