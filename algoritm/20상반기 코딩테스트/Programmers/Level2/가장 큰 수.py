def solution(numbers):
    numbers.sort(key=lambda x:((str(x)*4)[:4]),reverse=1)
    print(''.join(map(str,numbers)))
    return ''.join(map(str,numbers)) if numbers[0]!='0' else '0'

solution([3, 30, 34, 5, 9])