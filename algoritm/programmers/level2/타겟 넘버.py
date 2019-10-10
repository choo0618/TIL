def solution(numbers, target):
    Q = [-numbers[0], numbers[0]]
    n=1
    while n != len(numbers):
        q = []
        for stack in Q:
            q.append(stack + numbers[n])
            q.append(stack - numbers[n])
        n+=1
        Q = q
    return Q.count(target)

print(solution([1,1,1,1,1],3))