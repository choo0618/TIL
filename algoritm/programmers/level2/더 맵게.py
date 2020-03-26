import heapq
def solution(scoville, K):
    Len=len(scoville)
    Q=[]
    for s in scoville:heapq.heappush(Q,s)
    R,S=0,0
    while Len!=1:
        a=heapq.heappop(Q)
        if a>=K:break
        b=heapq.heappop(Q)
        tmp=a+2*b
        heapq.heappush(Q,tmp)
        S+=tmp
        R+=1
        Len-=1
    if Len==1 and Q[0]<K:R=-1
    return R
print(solution([1,1],7))