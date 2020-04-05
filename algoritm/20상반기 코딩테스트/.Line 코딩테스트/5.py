def solution(dataSource, tags):
    answer = []
    Result = []

    for Doc,*Tag in dataSource:
        cnt=0
        for t in tags:
            if t in Tag:cnt+=1
        if cnt:answer.append((Doc,cnt))
    answer.sort(key=lambda x:x[1],reverse=True)

    rCnt=0
    for Doc,cnt in answer:
        if rCnt==10:break
        Result.append(Doc)
        rCnt+=1

    return Result

solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
],
["t1", "t2", "t3"])
print(ord('1'))
print(ord('4'))