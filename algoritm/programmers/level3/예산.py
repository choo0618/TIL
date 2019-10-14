def solution(budgets, M):
    Left = 0
    Right = max(budgets)
    answer = 0
    while Left <= Right:
        Mid  = (Left+Right) // 2
        Budget = 0
        for b in budgets:
            if b < Mid:
                Budget += b
            else:
                Budget += Mid
        if Budget <= M:
            if Budget >= answer:
                answer = Mid
            Left = Mid + 1
        else:
            Right = Mid - 1
    return answer
print(solution([120, 110, 140, 150], 485))