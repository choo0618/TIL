def solution(A):
    answer = 0
    N = len(A)
    Chk = [0]*(N+1)
    for n in A:
        Chk[n] += 1

    for i in range(1, N):
        if Chk[i] > 1:
            answer += Chk[i]-1
            Chk[i+1] += Chk[i]-1
        elif Chk[i] < 1:
            answer += 1-Chk[i]
            Chk[i+1] -= 1-Chk[i]
        if answer > 10**12:
            return -1
        Chk[i] = 1
    print(answer)
    return answer


solution([4, 4, 4, 4] )