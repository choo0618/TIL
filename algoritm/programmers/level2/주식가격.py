# 효율성 실패
def solution(prices):
    R = []
    for i in range(len(prices)-1):
        if prices[i] <= min(prices[i+1:len(prices)]):
            R.append(len(prices)-i-1)
        else:
            Index = i+1
            while prices[Index] >= prices[i]:
                Index += 1
            R.append(Index-i)
    R.append(0)
    return R
solution([1,2,3,2,3])