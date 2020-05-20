import sys
sys.stdin = open('bj2422.txt','r')

def DFS(s,x,cnt):
    global R
    if cnt==2:
        R+=Map[s][x]
        return
    for i in range(x+1,N+1):
        if Map[x][i]:DFS(s,i,cnt+1)
N,M=map(int,input().split())
Map=[[1]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    Map[a][b]=0
    Map[b][a]=0
R=0
for i in range(1,N-1):DFS(i,i,0)
print(R)