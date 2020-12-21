def solution(S):
    answer = 0
    tmp = 0
    for c in S:
        if c == 'a':
            tmp += 1
            if tmp == 3: return -1
        else:
            answer += 2-tmp
            tmp = 0
    answer += 2-tmp
    print(answer)
    return answer

solution('abcdefg')