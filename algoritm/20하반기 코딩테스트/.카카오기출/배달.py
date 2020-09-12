from collections import deque
def solution(N, road, K):
    answer = 0
    Map=[[]for _ in range(N+1)]
    for a,b,c in road:
        Map[a].append((b,c))
        Map[b].append((a,c))
    Dis=[10**9]*(N+1)
    Dis[1]=0
    Q=deque([(1,0)])
    while Q:
        now,dis=Q.popleft()
        for next,d in Map[now]:
            if Dis[next]>dis+d:
                Dis[next]=dis+d
                Q.append((next,dis+d))
    for n in Dis:
        if K>=n:answer+=1
    return answer

solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)