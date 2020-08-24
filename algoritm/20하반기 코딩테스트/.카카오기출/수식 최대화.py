def Cal(a, b, c):
    if c=='+':return a+b
    elif c=='-':return a-b
    else:return a*b
def solution(expression):
    answer=[]
    Num,cal=[],['+','-','*']
    num=''
    for c in expression:
        if c in '*+-':
            Num.append(int(num))
            Num.append(c)
            num=''
        else:num+=c
    Num.append(int(num))
    Check=[0]*3
    def DFS(List,t):
        if t==3:answer.append(abs(List[0]));return
        for i in range(3):
            if Check[i]:continue
            tmp=[List[0]]
            Check[i]=1
            for j in range(2,len(List),2):
                if List[j-1]==cal[i]:tmp[-1]=Cal(tmp[-1],List[j],List[j-1])
                else:
                    tmp.append(List[j-1])
                    tmp.append(List[j])
            DFS(tmp,t+1)
            Check[i]=0
    DFS(Num,0)
    return max(answer)
solution("100-200*300-500+20")