def solution(cookie):
    Len=len(cookie)
    answer=0
    Sum=sum(cookie)

    def Chk(A,B):
        if B%2:return 0
        for m in range(a,b+1):
            A+=cookie[m]
            B-=cookie[m]
            if A==B:return A
            elif A>B:return 0

    for a in range(Len-1):
        tmp=Sum
        for b in range(Len-1,a,-1):
            answer=max(answer,Chk(0,tmp))
            tmp-=cookie[b]
            if tmp<2*answer:break
        Sum-=cookie[a]
        if Sum<answer*2:return answer
    return answer


solution([1, 1, 2, 3])