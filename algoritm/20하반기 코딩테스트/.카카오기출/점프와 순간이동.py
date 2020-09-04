def solution(n):
    R=0
    while n:
        if n%2:
            n-=1
            R+=1
        else:n//=2
    return R

solution(5000)
# 5000 2500 1250 (625 624) 312 156 78 (39 38) (19 18) (9 8) 4 2 (1 0)

