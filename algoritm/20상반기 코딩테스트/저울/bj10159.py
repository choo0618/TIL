import sys
sys.stdin=open('bj10159.txt','r')

def DFS(x,idx):
    for i in Map[x]:
        if R[idx][i]:
            R[idx][i]=0
            R[i][idx]=0
            DFS(i,idx)
N=int(input())
M=int(input())
Map=[[]for _ in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    Map[a-1].append(b-1)
R=[[1]*N for _ in range(N)]
for i in range(N):R[i][i]=0;DFS(i,i)
for p in R:print(sum(p))

