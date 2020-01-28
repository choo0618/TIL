import sys
sys.stdin = open('bj11404.txt','r')

N=int(input())
M=int(input())
Map=[[987654321]*N for _ in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    Map[a-1][b-1]=min(c,Map[a-1][b-1])
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j!=k:Map[j][k]=min(Map[j][k],Map[j][i]+Map[i][k])
for i in range(N):
    for j in range(N):
        if Map[i][j]==987654321:Map[i][j]=0
for p in Map:print(' '.join(map(str,p)))