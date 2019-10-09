def solution(priorities, location):
    R = 1
    n = 0
    while True:
        if priorities[n] != max(priorities[n:len(priorities)]):
            priorities.append(priorities.pop(n))
            location -= 1
            if location < n:
                location = len(priorities) - 1
        else:
            if location == n: break
            n += 1
            R += 1
    return R