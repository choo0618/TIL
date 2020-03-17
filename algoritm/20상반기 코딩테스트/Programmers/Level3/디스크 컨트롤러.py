import heapq
def solution(jobs):
    R=j=T=0
    n=len(jobs)
    jobs.sort()
    Q=[]
    while n>j or Q:
        if n>j and T>=jobs[j][0]:
            heapq.heappush(Q,(jobs[j][1],jobs[j][0]))
            j+=1
            continue
        if Q:
            b,a=heapq.heappop(Q)
            T+=b
            R+=T-a
        else:T=jobs[j][0]
    return R//n

solution([[0, 3], [1, 9], [2, 6]])