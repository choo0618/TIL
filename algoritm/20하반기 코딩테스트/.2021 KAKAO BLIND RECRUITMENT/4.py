from collections import deque
def solution(n, s, a, b, fares):
    answer=10**9

    Map=[[]for _ in range(n+1)]
    for i,j,f in fares:
        Map[i].append((j,f))
        Map[j].append((i,f))

    def dijkstra(q):
        Dis=[10**9]*(n+1)
        Dis[q]=0
        Q=deque([(q,0)])
        while Q:
            now,f=Q.popleft()
            for next,c in Map[now]:
                if f+c>=Dis[next]:continue
                Dis[next]=f+c
                Q.append((next,f+c))
        return Dis
    Result=[]
    for q in (s,a,b):
        Result.append(dijkstra(q))

    for idx in range(1,n+1):
        answer=min(answer,Result[0][idx]+Result[1][idx]+Result[2][idx])
    print(answer)

    return answer

solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])