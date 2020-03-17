import heapq
def solution(operations):
    answer=[]
    for s in operations:
        if s[0]=='I':
            n=int(s[2:])
            answer.append(n)
        elif s[0]=='D' and answer:
            if s[2]=='1':answer.pop()
            else:answer.pop(0)
        answer.sort()
    if not answer:return [0,0]
    return [answer[-1],answer[0]]

solution(['I 7','I 5','I -5','D -1'])

heapq.n