def solution(S):
    S = S.replace('aa','*')
    print(S)
    List = list(S)
    print(List)

solution('aabab')

def solution(S):
    res = 0
    a_cnt = 0
    for i, s in enumerate(S):
        if s == 'a':
            a_cnt += 1
        else:
            res += 2 - a_cnt
            a_cnt = 0
        if a_cnt >= 3:
            return -1
    if a_cnt < 2:
        res += 2 - a_cnt
    return res

print(solution(''))