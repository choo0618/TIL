idx=[(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
def Dis(now,n):
    return abs(now[0]-n[0])+abs(now[1]-n[1])
def solution(numbers, hand):
    answer = ''
    L,R=(3,0),(3,2)
    for n in numbers:
        if n==1 or n==4 or n==7:
            answer+='L'
            L=idx[n]
        elif n==3 or n==6 or n==9:
            answer+='R'
            R=idx[n]
        else:
            l,r=Dis(L,idx[n]),Dis(R,idx[n])
            if l==r:
                if hand=='right':
                    answer+='R'
                    R=idx[n]
                else:
                    answer+='L'
                    L=idx[n]
            elif l<r:
                answer+='L'
                L=idx[n]
            else:
                answer+='R'
                R=idx[n]
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #