def solution(N, stages):
    answer=[]
    Len=len(stages)
    for n in range(1,N+1):
        if Len==0:answer.append((0,n));continue
        tmp=[]
        F=0
        for i in stages:
            if i<=n:F+=1
            else:tmp.append(i)
        answer.append((F/Len,n))
        stages=tmp
        Len-=F
    answer.sort(key=lambda x:(-x[0],x[1]))
    for _ in range(N):
        answer[_]=answer[_][1]
    return answer

solution(4,[1,1,1,1])
solution(4, [4, 4, 4, 4, 4])
solution(5,[2,1,2,6,2,4,3,3])