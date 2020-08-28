def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        B=bin(arr1[i]|arr2[i])[2:]
        B='0'*(n-len(B))+B
        B=B.replace('1','#')
        B=B.replace('0',' ')
        answer.append(B)

    return answer

solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])