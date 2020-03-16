def solution(s):
    answer = 1
    for n in range(len(s),1,-1):
        for i in range(0,len(s)-n+1):
            front=s[i:n//2+i]
            if n%2:back=s[n//2+i+1:n+i]
            else:back=s[n//2+i:n+i]
            if front[::-1]==back:answer=n;break
        if answer!=1:break
    return answer
solution('abcdcba')