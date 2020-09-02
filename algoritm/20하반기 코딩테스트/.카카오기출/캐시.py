def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:return 5*len(cities)
    Q,Len=[],0
    for c in cities:
        c=c.upper()
        if c in Q:
            answer+=1
            Q.pop(Q.index(c))
        else:
            if Len>=cacheSize:Q=Q[1:]
            answer+=5
            Len+=1
        Q.append(c)
    print(answer)

    return answer

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])