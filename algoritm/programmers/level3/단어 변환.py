def check(tmp, w):
    n=0
    for t in range(len(tmp)):
        if tmp[t] != w[t]:
            n += 1
            if n == 2:return False
    return True
def solution(begin, target, words):
    if not target in words:
        return 0
    else:
        M = [0] * len(words)
        Q = [begin]
        n = 1
        while Q:
            q = []
            for tmp in Q:
                for idx, w in enumerate(words):
                    if not M[idx] and check(tmp, w):
                        M[idx] = n
                        q.append(w)
            n += 1
            Q = q
    return M[words.index(target)]

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
