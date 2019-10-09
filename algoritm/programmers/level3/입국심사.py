def solution(n, times):
    Left = 0
    Right = max(times) * n
    tmp = Right
    answer = Right
    while Right >= Left:
        mid = (Left + Right) // 2
        P = 0
        for i in times:
            P += mid // i
        if P == n:
            answer = mid
            Right = mid - 1
        elif P > n:
            Right = mid - 1
        else:
            Left = mid + 1
    if answer == tmp:
        answer = Right+1

    return answer

print(solution(1,[7,10]))