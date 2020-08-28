def solution(str1, str2):
    a,b=[],[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append((str1[i]+str1[i+1]).upper())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append((str2[i]+str2[i+1]).upper())
    I=set(a)&set(b)
    i=0
    for c in I:
        i+=min(a.count(c),b.count(c))
    u=len(a)+len(b)-i
    if u==0:return 65536
    return int(i/u*65536)

solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution('FRANCE','french')