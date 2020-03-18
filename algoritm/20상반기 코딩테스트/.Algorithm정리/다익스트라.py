# 0>>N 까지 최소거리
def dijkstra():
    Dis=[10**9]*(N+1)
    Dis[0]=0
    Q=[(0,0)]   # 현재위치,거리
    while Q:
        now,cnt = Q.pop()
        for next,c in Map[now]:
            if cnt+c>=Dis[next]:continue
            Dis[next]=cnt+c
            Q.append((cnt+c,next))

N=int(input())
Map=[[(b,cnt)]....]       # 2차원 배열: Map[현재위치]에 (다음위치,거리)