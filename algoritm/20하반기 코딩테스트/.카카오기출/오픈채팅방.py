def solution(record):
    answer = []
    Dic={}
    for i in record:
        List=i.split(' ')
        if List[0]=='Enter':
            Dic[List[1]]=List[2]
            answer.append([List[1],'님이 들어왔습니다.'])
        elif List[0]=='Leave':
            answer.append([List[1],'님이 나갔습니다.'])
        else:Dic[List[1]]=List[2]
    for i in range(len(answer)):
        answer[i][0]=Dic[answer[i][0]]
        answer[i]=''.join(answer[i])
    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])