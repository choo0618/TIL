def solution(n, computers):
    M=[0] * n
    n = 1
    for idx,m in enumerate(M):
        if not m:
            Q = [idx]
            M[idx] = n
            while Q:
                q = []
                for tmp in Q:
                    for id, i in enumerate(computers[tmp]):
                        if tmp == id or not i: continue
                        elif not M[id]:
                            M[id] = n
                            q.append(id)
                Q = q
            n+=1
    return max(M)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
