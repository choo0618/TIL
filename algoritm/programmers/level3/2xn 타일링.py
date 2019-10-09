def solution(n):
    answer = 0
    temp_n1 = 1
    temp_n2 = 3

    for i in range(1, n+1):
        if i == 1:
            answer += 1
        elif i == 2:
            answer += 2
        else:
            answer = temp_n1 * 2 + temp_n2
            temp_n1 = temp_n2
            temp_n2 = answer
    return answer % 10007

print(solution(4))