Dic={'#':'(-1)','*':'2','S':1,'D':2,'T':3}
def solution(dartResult):
    answer,a,b=0,0,0,
    for c in dartResult:
        if c.isdigit():
            if c=='0' and b==1:b=10;continue
            answer+=a
            a,b=b,int(c)
        elif c=='#':b*=-1
        elif c=='*':a*=2;b*=2
        else:b**=Dic[c]
    return answer+a+b

solution("1D2S0T")
solution("1D2S#10S")
solution("1T2D3D#")
solution("1S2D*3T")
