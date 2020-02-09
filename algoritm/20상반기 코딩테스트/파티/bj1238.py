import sys
sys.stdin=open('bj1238.txt','r')

import sys
input=sys.stdin.readline
N,M,X=map(int,input().split())
Map=[[10**9]*N for _ in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    Map[a-1][b-1]=c
for k in range(N):
    Map[k][k]=0
    for i in range(N):
        if Map[i][k]==10**9:continue
        for j in range(N):
            Map[i][j]=min(Map[i][j],Map[i][k]+Map[k][j])
print(Map)
print(max(Map[i][X-1]+Map[X-1][i]for i in range(N)))