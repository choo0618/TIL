def solution(triangle):
    for i in range(1,len(triangle)):
        for idx,p in enumerate(triangle[i]):
            if not idx:
                triangle[i][idx] += triangle[i - 1][0]
            elif idx == len(triangle[i])-1:
                triangle[i][idx] += triangle[i - 1][len(triangle[i-1])-1]
            else:
                tmp = triangle[i][idx]
                tmp1 = tmp + triangle[i-1][idx-1]
                tmp2 = tmp + triangle[i-1][idx]
                triangle[i][idx] = max(tmp1,tmp2)

    return max(triangle[len(triangle)-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])