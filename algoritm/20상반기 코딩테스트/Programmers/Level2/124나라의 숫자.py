def solution(n):
    answer=''
    while n:
        n,b=divmod(n,3)
        answer+='412'[b]
        if not b:n-=1
    return answer[::-1]