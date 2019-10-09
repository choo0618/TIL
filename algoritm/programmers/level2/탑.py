def solution(heights):
    R = [0]
    for i in range(1, len(heights)):
        if heights[i] >= max(heights[0:i]):
            R.append(0)
        else:
            Index = i-1
            while heights[Index] < heights[i]:
                Index -= 1
            R.append(Index+1)
    return R

solution([6,9,5,7,4])