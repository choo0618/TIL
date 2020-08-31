List=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def Change(i,j):
    r='' if i!=0 else'0'
    while i:
        i,b=divmod(i,j)
        r+=List[b]
    return r[::-1]
def solution(n, t, m, p):
    answer = ''
    Num=''
    for i in range(t*m+1):
        Num+=Change(i,n)
    for i in range(t):
        answer+=Num[p-1]
        p+=m
    print(Num)
    print(answer)
    return answer

solution(2, 4, 2, 1)