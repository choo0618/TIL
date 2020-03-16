def Check(S):
    Stack=[]
    for c in S:
        if c=='(':Stack.append('(')
        else:
            if not Stack:return False
            Stack.pop()
    if not Stack:return True
    return False
def Answer(p):
    if p=='':return ''

    u=''
    v=''
    result=''

    cnt1=0
    cnt2=0
    idx=0

    for c in p:
        if c=='(':cnt1+=1
        else:cnt2+=1
        idx+=1
        if cnt1==cnt2:break

    u+=p[:idx]
    v+=p[idx:]
    if Check(u):
        result+=u
        result+=Answer(v)
    else:
        result+='('
        result+=Answer(v)
        result+=')'
        u=u[1:len(u)-1]
        for c in u:
            if c=='(':result+=')'
            else:result+='('

    return result

def solution(p):
    if Check(p):return p
    answer=Answer(p)
    return answer

print(solution('()))((()'))