import sys
sys.stdin = open('bj2458.txt','r')

N,M=map(int,input().split())
Map=[[0]*N for _ in range(N)]
R=0
for i in range(M):
    a,b=map(int,input().split())
    Map[a-1][b-1]=1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if Map[i][k] and Map[k][j]:Map[i][j]=Map[i][k]+Map[k][j]
for i in range(N):
    cnt=0
    for j in range(N):
        if i==j:continue
        if Map[i][j]==Map[j][i]==0:cnt+=1
    if not cnt:R+=1
print(R)