def solution(inputString):
    answer = 0

    Dic={'(':0,'{':0,'[':0,'<':0}
    for c in inputString:
        if not c in '(){}[]<>':continue
        if c in '({[<':Dic[c]+=1;continue
        if c==')':
            if not Dic['(']:return -1
            Dic['(']-=1
        elif c=='}':
            if not Dic['{']:return -1
            Dic['{']-=1
        elif c==']':
            if not Dic['[']:return -1
            Dic['[']-=1
        elif c=='>':
            if not Dic['<']:return -1
            Dic['<']-=1
        answer+=1

    return answer