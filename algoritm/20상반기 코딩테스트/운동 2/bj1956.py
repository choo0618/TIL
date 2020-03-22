import sys
sys.stdin = open('bj1956.txt','r')

V,E=map(int,input().split())
Dis=[[10**9]*V for _ in range(V)]
for _ in range(E):
    a,b,c=map(int,input().split())
    Dis[a-1][b-1]=c
for k in range(V):
    for i in range(V):
        for j in range(V):
            Dis[i][j]=min(Dis[i][j],Dis[i][k]+Dis[k][j])
R=min(Dis[x][x]for x in range(V))
print(R if R!=10**9 else -1)