def solution(S):
    N, M = len(S), len(S[0])
    for i in range(N):
        for j in range(i+1, N):
            for idx in range(M):
                if S[i][idx] == S[j][idx]:
                    return [i, j, idx]
    return []