def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:return 5*len(cities)
    Q,Len=[],0
    for c in cities:
        if c in Q:
            idx=Q.index(c)
            answer+=idx + 1
            Q.pop(idx)
        else:
            if Len>=cacheSize:Q=Q[1:]
            answer+=5
            Len+=1
        Q.append(c)
    print(answer)

    return answer

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])