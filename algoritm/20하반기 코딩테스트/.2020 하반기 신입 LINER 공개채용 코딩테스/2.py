from collections import deque
def solution(ball, order):
    answer=[]
    ball=deque(ball)
    while ball:
        idx=0
        while ball[0]!=order[idx] and ball[-1]!=order[idx]:
            idx+=1

        if ball[0]==order[idx]:x=ball.popleft()
        else:x=ball.pop()
        answer.append(x)

        o=order[idx+1:]
        tmp=order[:idx]
        Chk=1
        while tmp and Chk:
            Chk=0
            ttmp=[]
            for i,n in enumerate(tmp):
                if ball[0]==n or ball[-1]==n:
                    Chk=1
                    if ball[0]==n:x=ball.popleft()
                    else:x=ball.pop()
                    answer.append(x)
                else:ttmp.append(n)
            tmp=ttmp
        order=tmp+o
    print(answer)
    return answer

solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3])
solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11])