import sys
sys.stdin = open('5684.txt','r')

for t in range(int(input())):
    N,M=map(int,input().split())
    Map=[[10**9]*N for _ in range(N)]
    R=10**9
    for i in range(M):
        a,b,c=map(int,input().split())
        Map[a-1][b-1]=c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if Map[i][k] and Map[k][j]:Map[i][j]=min(Map[i][j],Map[i][k]+Map[k][j])
                if i==j:R=min(R,Map[i][j])
    if R==10**9:R=-1
    print('#%d %d'%(t+1,R))