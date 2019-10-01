def solution(n, times):
    List=[0,0]
    while n!=1:
        i = List.index(min(List))
        List[i]+=times[i]
        n-=1
    for i in range(len(times)):
        List[i]+=times[i]
    return min(List)
print(solution(6,[7,10]))