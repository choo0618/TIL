def solution(cards):
    answer=0
    Len=len(cards)

    i=1
    idx=0
    while idx!=Len:
        D=[]
        P=[]
        while idx!=Len+1:
            if i:
                if len(D)==2:
                    a,b,tmp=0,0,1
                    for n in P:
                        if n>10:n=10
                        a+=n;b+=n
                        if n==1 and tmp==1:b+=10;tmp=0
                    if D[-1]==1 or D[-1]>=7:
                        while a<17 and b<17:
                            if idx==Len:return answer
                            a+=cards[idx];b+=cards[idx]
                            idx+=1
                    elif D[-1] in [4,5,6]:
                        pass
                    elif D[-1] in [2,3]:
                        while a<12 and b<12:
                            if idx==Len:return answer
                            a+=cards[idx];b+=cards[idx]
                            idx+=1
                    PS=b
                    if PS>21:PS=a
                    break
                P.append(cards[idx])
                i=0
            else:
                D.append(cards[idx])
                i=1
            idx+=1
        a,b,tmp=0,0,1
        for n in D:
            if n>10:n=10
            a+=n;b+=n
            if n==1 and tmp==1:b+=10;tmp=0
        DS=b
        if DS>21:DS=a
        if PS==21 and DS!=21:answer+=3;continue
        elif DS==21 and PS!=21:answer-=2;continue
        elif DS==21 and PS==21:continue

        while a<17 and b<17:
            if idx==Len:return answer
            n=cards[idx]
            if n>10:n=10
            a+=n;b+=n
            if n==1 and tmp==1:b+=10;tmp=0
            idx+=1
        DS=b
        if DS>21:DS=a

        if PS>21:
            if DS>21:pass
            else:answer-=2
        elif PS<21:
            if PS==DS:pass
            elif PS>DS or DS>21:answer+=2
            else:answer-=2
        D,P=[],[]
        DS,PS=0,0

    print(answer)
    return answer

# solution([1, 4, 10, 6, 9, 1, 8, 13])
solution([12, 7, 11, 6, 2, 12])

