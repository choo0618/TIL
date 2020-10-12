def solution(new_id):
    answer = ''
    Len=0
    for c in new_id:
        if c in '.-_':
            if c=='.' and (not answer or answer[-1]=='.'):
                continue
            else:
                answer+=c
        elif c.isdigit() or c.isalpha():
            answer+=c.lower()
        elif c==' ':
            answer+='a'
        else:continue
        Len+=1

    if Len==0:
        answer='a'
        Len=1

    if answer[-1]=='.':
        answer=answer[:Len-1]
        Len-=1

    if Len>=16:
        answer=answer[:15]
        Len=15

    if answer[-1]=='.':
        answer=answer[:14]
        Len=14

    while Len<=2:
        answer+=answer[-1]
        Len+=1
    print(answer)
    return answer

# solution("...!@BaT#*..y.abcdefghijklm.")
# solution("z-+.^.")
solution("=.=")
solution("abcdefghijklmn.p")
