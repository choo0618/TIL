import sys
sys.stdin = open('bj10217.txt','r')

import heapq
for t in range(int(input())):
    N,M,K=map(int,input().split())
    Map=[[]for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,input().split())
        Map[u].append((v,c,d))
    D=[[10**9]*(M+1) for _ in range(N+1)]
    D[1][0]=0

    # DP
    for m in range(M+1):
        for n in range(1,N+1):
            if D[n][m]==10**9:continue
            t=D[n][m]
            for next,c,d in Map[n]:
                if m+c>M:continue
                D[next][m+c]=min(D[next][m+c],t+d)
    R=min(D[N])
    print(R if R!=10**9 else 'Poor KCM')

    # 다익스트라
    Q=[(0,0,1)]
    R='Poor KCM'
    while Q:
        d,c,now=heapq.heappop(Q)
        if now==N:R=d;break
        if D[now][c]<d:continue
        D[now][c]=d
        for next,nc,nd in Map[now]:
            if nc+c<=M and D[next][nc+c]>nd+d:
                D[next][nc+c]=nd+d
                heapq.heappush(Q,(nd+d,nc+c,next))
    print(R)
