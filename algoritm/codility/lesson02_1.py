def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result
print(solution([7, 3, 9, 3, 9, 9, 9]))

print(bin(5))