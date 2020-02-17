import sys
sys.stdin = open('5643.txt','r')

for t in range(int(input())):
    N=int(input())
    M=int(input())
    Map=[[0]*N for _ in range(N)]
    for i in range(M):
        a,b=map(int,input().split())
        Map[a-1][b-1]=1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if Map[i][k] and Map[k][j]:
                    Map[i][j]=1
    R=0
    for i in range(N):
        r=0
        for j in range(N):
            if i!=j:r+=Map[i][j]+Map[j][i]
        if r==N-1:R+=1
    print('#%d %d'%(t+1,R))
