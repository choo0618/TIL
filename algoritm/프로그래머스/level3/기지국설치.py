def solution(n, stations, w):
    N=1
    P=0
    R=0
    while N <= n:
        if stations[P]-w <= N <= stations[P]+w:
            N = stations[P]+w+1
            P += 1
            if P==len(stations):P=0
        else:
            N+=2*w+1
            R+=1
    return R
print(solution(16,[9],2))