import sys
sys.stdin = open('bj1733.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if B[i]==-1 or (not V[B[i]] and DFS(B[i])):
            A[x]=i
            B[i]=x
            return 1
    return 0
N=int(input())
Map=[[]for _ in range(N)]
Max=0
for i in range(N):
    f,b=map(int,input().split())
    Max=max(Max,max(f,b))
    Map[i].append(f)
    Map[i].append(b)
A=[-1]*N
B=[-1]*(Max+1)
R=0
for i in range(N):
    V=[0]*N
    if DFS(i):R+=1
    else:break
if R==N:print('\n'.join(map(str,A)))
else:print(-1)