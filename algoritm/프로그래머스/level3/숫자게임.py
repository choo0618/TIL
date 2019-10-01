def solution(A, B):
    R=0
    A.sort()
    B.sort()
    for i in range(len(A)):
        check=0
        if B[i]>A[i]:
            R+=1
            continue
        else:
            n=0
            while B[i]<=A[i]:
                B.append(B.pop(i))
                if n == len(A)-i:
                    check=1
                    break
                n+=1
            if check:
                break
            else:
                R+=1
    return R
print(solution([5,5,5,3,3],[1,2,3,4,4]))