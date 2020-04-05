def Result(Road):
    List=[0]
    for n in Road:
        if n:List[-1]+=n
        else:List.append(0)
    return max(List)

def DFS(idx,n,Road,Len):
    global answer
    if not n:
        answer=max(answer, Result(Road))
        return
    for i in range(idx, Len):
        if Road[i]:continue
        Road[i]=1
        DFS(i+1,n-1,Road,Len)
        Road[i]=0

def solution(road, n):
    zeroCnt=0
    roadCnt=0
    Road=[]
    for z in road:
        if z=='0':
            zeroCnt+=1
            if roadCnt:
                Road+=[roadCnt,0]
                roadCnt=0
            else:Road.append(0)
        else:roadCnt+=1
    if roadCnt:Road.append(roadCnt)
    Len=len(Road)

    if n>=zeroCnt:return len(road)
    DFS(0,n,Road,Len)
    print(answer)
    return answer
answer=0
solution("111011110011111011111100011111",3)