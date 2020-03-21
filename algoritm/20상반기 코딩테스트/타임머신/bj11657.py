import sys
sys.stdin = open('bj11657.txt','r')

N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for _ in range(M)]
Dis=[0,0]+[10**9]*(N-1)
Check=0
for i in range(N):
    for now,next,w in A:
        if Dis[now]!=10**9 and Dis[next]>Dis[now]+w:
            Dis[next]=Dis[now]+w
            if i==N-1:Check=1
if Check:print(-1)
else:
    for p in range(2,N+1):
        if Dis[p]==10**9:print(-1)
        else:print(Dis[p])


N=int(input())
A=[[int(x)for x in input().split()]for _ in range(N)]
A.sort(key=lambda x:(x[1],x[0]))
for x,y in A:print(x,y)