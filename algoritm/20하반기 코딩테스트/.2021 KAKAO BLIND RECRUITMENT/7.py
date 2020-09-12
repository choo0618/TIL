def solution(sales, links):
    answer = 0
    Map=[[]for _ in range(len(sales)+1)]
    for a,b in links:
        Map[a].append(b)


    return answer