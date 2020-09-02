def solution(s):
    answer=[]
    s=s[2:-2].split('},{')
    Len=len(s)
    for i in range(Len):
        s[i]=s[i].split(',')
    s.sort(key=lambda x:len(x))
    print(s)
    for i in range(Len):
        for j in s[i]:
            if int(j) not in answer:
                answer.append(int(j))
                break
    print(answer)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")