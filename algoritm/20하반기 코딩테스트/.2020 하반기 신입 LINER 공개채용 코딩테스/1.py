def solution(boxes):
    answer = 0
    Chk=[0]*1000001
    for a,b in boxes:
        Chk[a]+=1
        Chk[b]+=1
    for n in Chk:
        if n%2:answer+=1
    return answer

solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]])