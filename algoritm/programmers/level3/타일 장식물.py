def solution(N):
    Q = [1, 1]
    n = 0
    while len(Q) != N:
        Q.append(Q[n] + Q[n+1])
        n += 1

    return 2*(2*Q[N-1] + Q[N-2])
solution(5)