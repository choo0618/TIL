import sys
sys.stdin = open('bj1719.txt','r')

N,M=map(int,input().split())
Map=[[987654321]*N for _ in range(N)]
for i in range(M):
    x,y,c=map(int,input().split())
    Map[x-1][y-1]=c
    Map[y-1][x-1]=c
P=[[int(x)+1 for x in range(N)]for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if Map[i][j]>Map[i][k]+Map[k][j]:
                Map[i][j]=Map[i][k]+Map[k][j]
                P[j][i]=P[j][k]

for p in range(N):
    P[p][p]='-'
    print(' '.join(map(str,P[p])))
