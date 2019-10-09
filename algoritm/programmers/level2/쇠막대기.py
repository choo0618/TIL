def solution(arrangement):
    answer = 0
    arrangement = arrangement.replace("()","L")
    Q = []
    for c in arrangement:
        if c == '(':
            Q.append('(')
            answer += 1
        elif c == ')':
            Q.pop()
        else:
            answer += len(Q)
    return answer
solution('()(((()())(())()))(())')