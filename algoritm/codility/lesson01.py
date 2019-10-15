def solution(N):
    # write your code in Python 3.6
    Binary = bin(N)[2:]
    Result = 0
    result = 0
    for binary in Binary:
        if binary == '0':
            result +=1
        if binary == '1':
            if result > Result:
                Result = result
            result = 0
    return Result
print(solution(9))