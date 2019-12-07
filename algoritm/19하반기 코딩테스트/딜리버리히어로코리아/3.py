def solution(A):
    Map = [0]*len(A)
    for idx,a in enumerate(A):
        for n in A:
            if a == n:continue
            elif a+n == 7:
                Map[idx] += 2
            else:
                Map[idx] += 1
    return min(Map)
    # Result = 987654321
    # for idx, n in enumerate(A):
    #     M = [0]* len(A)
    #     for check_idx,s in enumerate(A):
    #         if idx == check_idx or n ==s:continue
    #         if n + s == 7:
    #             M[check_idx]+=2
    #         else:
    #             M[check_idx]=1
    #     result = sum(M)
    #     if result < Result:
    #         Result = result
    return Result

print(solution([1,1,6]))