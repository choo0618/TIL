# 정점사이의 최단거리
# 다익스트라 플로이드워셜과 달리 음의 가중치도 구할 수 있다.
# 다익스트라보다 시간적 효율이 좋지않다
# 간선을 기준으로 최단거리를 구한


N=int(input())
A=[[int(x)for x in input().split()]for _ in range(N)]       # 정점 a 에서 정점 b 로의 가중치 c
Dis=[10**9]*(N+1)
Dis[1]=0
for i in range(N):
    for now,next,weight in A:
        if Dis[now]!=10**9 and Dis[next]>Dis[now]+weight:   # 방문하지 않은 간선은 스킵한다.
            Dis[next]=Dis[now]+weight
