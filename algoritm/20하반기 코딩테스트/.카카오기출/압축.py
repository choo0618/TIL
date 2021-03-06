def solution(msg):
    answer = []
    Dic={c:n+1 for n,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    idx,Len,n=1,len(msg),27
    word=msg[0]
    while idx!=Len:
        while word in Dic and idx!=Len:
            word+=msg[idx]
            idx+=1
        if idx==Len and word in Dic:break
        Dic[word]=n
        n+=1
        answer.append(Dic[word[:len(word)-1]])
        word=word[-1]
    answer.append(Dic[word])
    return answer

solution('KAKAO')
solution('TOBEORNOTTOBEORTOBEORNOT')